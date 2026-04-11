/**
 * Pre-renders implied sats/CC (USD cross) chart as static SVG for the homepage.
 * Run automatically before `astro build` — no client-side market_chart fetch.
 *
 * Keep High/Low labels in sync with site copy (see LABELS in this file vs translations home).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT_DIR = path.join(__dirname, '..', 'public', 'generated');

const W = 420;
const H = 156;
const PAD = { t: 22, r: 10, b: 26, l: 10 };
const IW = W - PAD.l - PAD.r;
const IH = H - PAD.t - PAD.b;
const CHART_MAX_POINTS = 850;
const DAY_TRIES = ['max', '365', '180', '90'];

const LABELS = {
  en: { high: 'Raw high', low: 'Raw low', latest: 'Latest' },
  zh: { high: 'Raw最高点', low: 'Raw最低点', latest: '最新' },
};

function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/** @typedef {[number, number]} Pt */

function sortByTime(pairs) {
  return [...pairs].sort((a, b) => a[0] - b[0]);
}

function interpolateY(points, x) {
  if (points.length === 0) return null;
  if (x <= points[0][0]) return points[0][1];
  const last = points[points.length - 1];
  if (x >= last[0]) return last[1];
  let lo = 0;
  let hi = points.length - 1;
  while (hi - lo > 1) {
    const mid = (lo + hi) >> 1;
    if (points[mid][0] <= x) lo = mid;
    else hi = mid;
  }
  const [x0, y0] = points[lo];
  const [x1, y1] = points[hi];
  if (x1 <= x0) return y0;
  return y0 + ((x - x0) / (x1 - x0)) * (y1 - y0);
}

function emaSeries(values, alpha) {
  const out = [];
  let e = values[0];
  for (const v of values) {
    e = alpha * v + (1 - alpha) * e;
    out.push(e);
  }
  return out;
}

function smoothCurveAdaptive(sats) {
  const n = sats.length;
  const a = Math.max(0.03, Math.min(0.14, 95 / n));
  const b = Math.max(0.05, Math.min(0.22, 130 / n));
  return emaSeries(emaSeries(sats, a), b);
}

function argMinMax(arr) {
  let iMin = 0;
  let iMax = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[iMin]) iMin = i;
    if (arr[i] > arr[iMax]) iMax = i;
  }
  return { iMin, iMax };
}

function pickPlotIndices(n, maxPts, iMin, iMax) {
  const s = new Set([0, n - 1, iMin, iMax]);
  const k = Math.max(1, Math.ceil(n / maxPts));
  for (let i = 0; i < n; i += k) s.add(i);
  return [...s].sort((a, b) => a - b).filter((i) => i >= 0 && i < n);
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function fetchMarketChart(coinId, days, attempt = 0) {
  const url = `https://api.coingecko.com/api/v3/coins/${coinId}/market_chart?vs_currency=usd&days=${days}`;
  const res = await fetch(url, { signal: AbortSignal.timeout(60_000) });
  if (res.status === 429 && attempt < 6) {
    await sleep(2500 * (attempt + 1));
    return fetchMarketChart(coinId, days, attempt + 1);
  }
  if (!res.ok) return null;
  const j = await res.json();
  const p = j.prices;
  if (!Array.isArray(p) || p.length < 4) return null;
  return p;
}

async function fetchAlignedCharts() {
  for (let i = 0; i < DAY_TRIES.length; i++) {
    const days = DAY_TRIES[i];
    if (i > 0) await sleep(2000);
    const [cc, btc] = await Promise.all([
      fetchMarketChart('canton-network', days),
      fetchMarketChart('bitcoin', days),
    ]);
    if (cc && btc) return { cc, btc, days };
  }
  return null;
}

function buildSatsSeries(ccPrices, btcPrices) {
  const cc = sortByTime(ccPrices);
  const btc = sortByTime(btcPrices);
  const out = [];
  for (const [t, ccUsd] of cc) {
    if (typeof ccUsd !== 'number' || ccUsd <= 0) continue;
    const btcUsd = interpolateY(btc, t);
    if (btcUsd == null || btcUsd <= 0) continue;
    out.push({ t, sats: (ccUsd / btcUsd) * 1e8 });
  }
  return out;
}

function ySvg(v, ymin, ymax) {
  const span = ymax - ymin || 1;
  const n = (v - ymin) / span;
  return PAD.t + (1 - n) * IH;
}

function pathFromTimeSeries(plot, tMin, tMax, ymin, ymax) {
  if (plot.length < 2) return { line: '', area: '' };
  const spanT = tMax - tMin || 1;
  const xOf = (t) => PAD.l + ((t - tMin) / spanT) * IW;
  const pts = plot.map((p) => [xOf(p.t), ySvg(p.y, ymin, ymax)]);
  let d = `M ${pts[0][0].toFixed(1)} ${pts[0][1].toFixed(1)}`;
  for (let i = 1; i < pts.length; i++) {
    d += ` L ${pts[i][0].toFixed(1)} ${pts[i][1].toFixed(1)}`;
  }
  const y0 = PAD.t + IH;
  const area = `${d} L ${pts[pts.length - 1][0].toFixed(1)} ${y0} L ${pts[0][0].toFixed(1)} ${y0} Z`;
  return { line: d, area };
}

function markerXml(x, y, label, valueLine, kind, labelNudgeX) {
  const tx = x + labelNudgeX;
  const anchor = tx < PAD.l + IW * 0.22 ? 'start' : tx > PAD.l + IW * 0.78 ? 'end' : 'middle';
  const dy1 = kind === 'lo' ? 12 : -10;
  const dy2 = kind === 'lo' ? 24 : -22;
  const cls = kind === 'hi' ? 'm-hi' : kind === 'lo' ? 'm-lo' : 'm-lt';
  return `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4" class="mk ${cls}" />
<text x="${tx.toFixed(1)}" y="${(y + dy1).toFixed(1)}" text-anchor="${anchor}" class="m-t">${esc(label)}</text>
<text x="${tx.toFixed(1)}" y="${(y + dy2).toFixed(1)}" text-anchor="${anchor}" class="m-s">${esc(valueLine)}</text>`;
}

async function buildSvgForLocale(locale) {
  const pack = await fetchAlignedCharts();
  if (!pack) throw new Error('build-sats-chart: no market_chart data from CoinGecko');
  const { cc: ccP, btc: btcP, days } = pack;
  const series = buildSatsSeries(ccP, btcP);
  if (series.length < 6) throw new Error('build-sats-chart: series too short');

  const localeTag = locale === 'zh' ? 'zh-CN' : 'en-US';
  const labels = LABELS[locale] || LABELS.en;
  const dfmt = { year: 'numeric', month: 'short', day: 'numeric' };

  const tMin = series[0].t;
  const tMax = series[series.length - 1].t;
  const raw = series.map((s) => s.sats);
  const { iMin, iMax } = argMinMax(raw);
  const smoothed = smoothCurveAdaptive(raw);

  let ymin = Math.min(...smoothed, ...raw);
  let ymax = Math.max(...smoothed, ...raw);
  const pad = (ymax - ymin) * 0.1 || Math.abs(ymin) * 0.002 || 1e-6;
  ymin -= pad;
  ymax += pad;

  const spanT = tMax - tMin || 1;
  const xOf = (t) => PAD.l + ((t - tMin) / spanT) * IW;

  const ix = pickPlotIndices(series.length, CHART_MAX_POINTS, iMin, iMax);
  const plot = ix.map((i) => ({ t: series[i].t, y: smoothed[i] }));
  const { line, area } = pathFromTimeSeries(plot, tMin, tMax, ymin, ymax);

  const fmtSats = (v) =>
    v.toLocaleString(localeTag, { maximumFractionDigits: 4, minimumFractionDigits: 2 });

  const iLast = series.length - 1;
  const xHi = xOf(series[iMax].t);
  const xLo = xOf(series[iMin].t);
  const yHi = ySvg(raw[iMax], ymin, ymax);
  const yLo = ySvg(raw[iMin], ymin, ymax);
  const loNudge = iMin !== iMax && Math.abs(xHi - xLo) < 42 ? 26 : 0;
  const df = (t) => new Date(t).toLocaleDateString(localeTag, dfmt);
  const latestParen = locale === 'zh' ? `（${labels.latest}）` : ` (${labels.latest})`;

  let markers = '';
  if (iMin === iMax) {
    markers = markerXml(
      xOf(series[iLast].t),
      ySvg(raw[iLast], ymin, ymax),
      labels.latest,
      `${fmtSats(raw[iLast])} · ${df(series[iLast].t)}`,
      'lt',
      -22,
    );
  } else {
    const hiLine =
      iLast === iMax
        ? `${fmtSats(raw[iMax])} · ${df(series[iMax].t)}${latestParen}`
        : `${fmtSats(raw[iMax])} · ${df(series[iMax].t)}`;
    markers = markerXml(xHi, yHi, labels.high, hiLine, 'hi', 0);
    const loLine =
      iLast === iMin
        ? `${fmtSats(raw[iMin])} · ${df(series[iMin].t)}${latestParen}`
        : `${fmtSats(raw[iMin])} · ${df(series[iMin].t)}`;
    markers += markerXml(xLo, yLo, labels.low, loLine, 'lo', loNudge);
    if (iLast !== iMax && iLast !== iMin) {
      const xLt = xOf(series[iLast].t);
      const ltNudge = Math.abs(xLt - xHi) < 48 || Math.abs(xLt - xLo) < 48 ? -28 : -12;
      markers += markerXml(
        xLt,
        ySvg(raw[iLast], ymin, ymax),
        labels.latest,
        `${fmtSats(raw[iLast])} · ${df(series[iLast].t)}`,
        'lt',
        ltNudge,
      );
    }
  }

  const t0 = new Date(tMin).toLocaleDateString(localeTag, dfmt);
  const t1 = new Date(tMax).toLocaleDateString(localeTag, dfmt);
  const axisText = `${t0} — ${t1} · ${series.length} pts · CoinGecko days=${days}`;

  const gid = `cf-${locale}`;
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img">
  <defs>
    <linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3d8bfd" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#3d8bfd" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style><![CDATA[
    .c-area { stroke: none; }
    .c-line { stroke: #3d8bfd; stroke-width: 1.75; fill: none; stroke-linecap: round; stroke-linejoin: round; }
    .mk { fill: #0c0f14; stroke-width: 2; }
    .m-hi { stroke: #4ade80; }
    .m-lo { stroke: #f87171; }
    .m-lt { stroke: #3d8bfd; }
    .m-t { font: 600 13px system-ui, -apple-system, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif; fill: #e8edf4; }
    .m-s { font: 400 11.5px system-ui, -apple-system, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif; fill: rgba(232,237,244,0.9); font-variant-numeric: tabular-nums; }
    .c-axis { font: 400 11px system-ui, -apple-system, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif; fill: #8b9cb3; font-variant-numeric: tabular-nums; }
  ]]></style>
  <path class="c-area" d="${area}" fill="url(#${gid})"/>
  <path class="c-line" d="${line}"/>
  <g>${markers}</g>
  <text x="${PAD.l}" y="${H - 6}" class="c-axis">${esc(axisText)}</text>
</svg>`;
}

async function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  for (const loc of ['en', 'zh']) {
    const svg = await buildSvgForLocale(loc);
    const out = path.join(OUT_DIR, `cc-sats-chart-${loc}.svg`);
    fs.writeFileSync(out, svg, 'utf8');
    console.log('wrote', path.relative(path.join(__dirname, '..'), out));
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
