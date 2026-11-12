#!/usr/bin/env node
/**
 * Build a Chinese long-form daily digest from zh news.items and optionally
 * publish it to Binance Square (contentType=2).
 *
 * Usage:
 *   node scripts/binance-square-daily-digest.mjs                 # dry-run latest unposted date
 *   node scripts/binance-square-daily-digest.mjs --date 2026-11-11
 *   node scripts/binance-square-daily-digest.mjs --days 2
 *   node scripts/binance-square-daily-digest.mjs --publish
 *   node scripts/binance-square-daily-digest.mjs --publish --force
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getLedgerFilePath,
  maskApiKey,
  publishArticle,
  readLedger,
  resolveApiKey,
  writeLedger,
} from './lib/binance-square.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const TRANSLATIONS = path.join(ROOT, 'src', 'i18n', 'translations.ts');
const ARTIFACT_DIR = path.join(ROOT, 'artifacts', 'binance-square');
const DIGEST_TITLE = 'Canton生态快报';

function shanghaiYmd(d = new Date()) {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Shanghai',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(d);
}

function parseArgs(argv) {
  const out = {
    date: null,
    days: 1,
    latest: true,
    publish: false,
    force: false,
    dryRun: true,
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--publish') {
      out.publish = true;
      out.dryRun = false;
    } else if (a === '--dry-run') {
      out.dryRun = true;
      out.publish = false;
    } else if (a === '--force') {
      out.force = true;
    } else if (a === '--latest') {
      out.latest = true;
      out.date = null;
    } else if (a === '--today') {
      out.latest = false;
      out.date = shanghaiYmd();
    } else if (a === '--date') {
      out.date = argv[++i];
      out.latest = false;
    } else if (a === '--days') {
      out.days = Number(argv[++i]);
    } else if (a === '--help' || a === '-h') {
      out.help = true;
    } else {
      throw new Error(`Unknown arg: ${a}`);
    }
  }
  if (out.date && !/^\d{4}-\d{2}-\d{2}$/.test(out.date)) {
    throw new Error(`Invalid --date ${out.date}; expected YYYY-MM-DD`);
  }
  if (!Number.isFinite(out.days) || out.days < 1 || out.days > 14) {
    throw new Error(`Invalid --days ${out.days}; use 1–14`);
  }
  return out;
}

function uniqueSortedDates(items) {
  return [...new Set(items.map((i) => i.date))].sort((a, b) => (a < b ? 1 : a > b ? -1 : 0));
}

function pickLatestUnpostedDate(items, ledger, force) {
  for (const d of uniqueSortedDates(items)) {
    if (force || !ledger.posts?.[d]) return d;
  }
  return null;
}

function extractZhNewsBlock(source) {
  const zhIdx = source.indexOf('\n  zh:');
  if (zhIdx === -1) throw new Error('zh locale block not found in translations.ts');
  const zhPart = source.slice(zhIdx);
  const re =
    /news:\s*\{[\s\S]*?items:\s*\[([\s\S]*?)\]\s*,\s*\n    \},\n    videos:/;
  const m = zhPart.match(re);
  if (!m) throw new Error('zh news.items array not found');
  return m[1];
}

function parseNewsItems(block) {
  const items = [];
  const objRe =
    /\{\s*date:\s*'([^']+)'\s*,\s*tag:\s*'((?:\\'|[^'])*)'\s*,\s*title:\s*'((?:\\'|[^'])*)'\s*,\s*body:\s*'((?:\\'|[^'])*)'\s*,\s*url:\s*'((?:\\'|[^'])*)'\s*,?\s*\}/g;
  let m;
  while ((m = objRe.exec(block))) {
    items.push({
      date: m[1],
      tag: unescapeTs(m[2]),
      title: unescapeTs(m[3]),
      body: unescapeTs(m[4]),
      url: unescapeTs(m[5]),
    });
  }
  return items;
}

function unescapeTs(s) {
  return s.replace(/\\'/g, "'").replace(/\\\\/g, '\\');
}

function dateRangeEnding(endYmd, days) {
  const [y, mo, d] = endYmd.split('-').map(Number);
  // Noon UTC avoids DST edge; we only need calendar arithmetic for Asia/Shanghai labels.
  const end = new Date(Date.UTC(y, mo - 1, d, 12, 0, 0));
  const set = new Set();
  for (let i = 0; i < days; i++) {
    const t = new Date(end.getTime() - i * 86400000);
    const ymd = t.toISOString().slice(0, 10);
    set.add(ymd);
  }
  return set;
}

function selectItems(all, endYmd, days) {
  const allowed = dateRangeEnding(endYmd, days);
  return all.filter((it) => allowed.has(it.date));
}

/** Strip outlet branding, source labels, and any URLs from item body copy. */
function sanitizeBody(body) {
  let s = String(body ?? '');
  s = s.replace(/^CantonNews(?:（[^）]*）|\([^)]*\))[：:]\s*/i, '');
  s = s.replace(/\bCantonNews\b/gi, '');
  s = s.replace(/CC\s*Privacy\s*Club/gi, '');
  s = s.replace(/ccprivacy\.club/gi, '');
  s = s.replace(/https?:\/\/\S+/gi, '');
  s = s.replace(/\bwww\.\S+/gi, '');
  // Bare hostnames / RPC endpoints (e.g. ostia.devnet.romeprotocol.xyz)
  s = s.replace(
    /\b(?:[a-z0-9-]+\.)+(?:com|org|net|io|xyz|app|dev|info|co|ai|fi|cc|club|network|finance|exchange)(?:\/\S*)?/gi,
    '',
  );
  s = s.replace(/(?:来源|出处|原文|链接|Source|URL)\s*[：:]\s*/gi, '');
  s = s.replace(/\(\s*[;，,]\s*/g, '(');
  s = s.replace(/\(\s*\)/g, '');
  s = s.replace(/[ \t]{2,}/g, ' ');
  s = s.replace(/\s+([，。；、）】])/g, '$1');
  s = s.replace(/\n{3,}/g, '\n\n');
  return s.trim();
}

function sanitizeTitle(title) {
  return sanitizeBody(title);
}

function buildDigest(items) {
  const lines = [];

  for (const it of items) {
    const title = sanitizeTitle(it.title);
    const body = sanitizeBody(it.body);
    if (!title && !body) continue;
    lines.push(`【${it.tag}】${title}`);
    if (it.date) lines.push(it.date);
    if (body) lines.push(body);
    lines.push('');
  }

  return {
    title: DIGEST_TITLE,
    bodyTextOnly: lines.join('\n').trim() + '\n',
  };
}

function writeArtifact(endYmd, payload) {
  fs.mkdirSync(ARTIFACT_DIR, { recursive: true });
  const file = path.join(ARTIFACT_DIR, `${endYmd}.json`);
  fs.writeFileSync(file, `${JSON.stringify(payload, null, 2)}\n`);
  return file;
}

function printHelp() {
  console.log(`Usage: node scripts/binance-square-daily-digest.mjs [options]

Options:
  --latest            Use newest ZH news date not yet in ledger (default).
  --today             Use Asia/Shanghai today.
  --date YYYY-MM-DD   Digest end date (explicit).
  --days N            Include items from the last N days ending on the chosen date (1–14). Default: 1.
  --dry-run           Print title/body only (default).
  --publish           Publish long article to Binance Square.
  --force             With --latest, ignore ledger; with --publish, allow same-day re-post.
  -h, --help          Show help.

Auth:
  BINANCE_SQUARE_OPENAPI_KEY or ~/.config/binance-square/openapi-key

Ledger (idempotency):
  ${getLedgerFilePath()}
`);
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    printHelp();
    return;
  }

  const source = fs.readFileSync(TRANSLATIONS, 'utf8');
  const block = extractZhNewsBlock(source);
  const all = parseNewsItems(block);
  if (all.length === 0) {
    throw new Error('Parsed 0 zh news items — check translations.ts shape');
  }

  const ledger = readLedger();
  let endYmd = args.date;
  if (args.latest || !endYmd) {
    endYmd = pickLatestUnpostedDate(all, ledger, args.force);
    if (!endYmd) {
      console.log(
        JSON.stringify(
          {
            ok: true,
            skipped: true,
            reason: 'all_dates_already_posted',
            newest: uniqueSortedDates(all)[0] ?? null,
          },
          null,
          2,
        ),
      );
      return;
    }
  }

  const items = selectItems(all, endYmd, args.days);
  if (items.length === 0) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          skipped: true,
          reason: 'no_news_items_in_range',
          date: endYmd,
          days: args.days,
        },
        null,
        2,
      ),
    );
    return;
  }

  const digest = buildDigest(items);
  const ledgerKey = args.days === 1 ? endYmd : `${endYmd}_d${args.days}`;
  const prior = ledger.posts?.[ledgerKey];

  if (args.publish && prior && !args.force) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          skipped: true,
          reason: 'already_posted',
          date: endYmd,
          prior,
          hint: 'Pass --force to re-publish',
        },
        null,
        2,
      ),
    );
    return;
  }

  const artifact = writeArtifact(endYmd, {
    date: endYmd,
    days: args.days,
    itemCount: items.length,
    urls: items.map((i) => i.url),
    title: digest.title,
    bodyTextOnly: digest.bodyTextOnly,
    mode: args.publish ? 'publish' : 'dry-run',
    createdAt: new Date().toISOString(),
  });

  console.log(`Items: ${items.length}`);
  console.log(`Title: ${digest.title}`);
  console.log(`Body chars: ${digest.bodyTextOnly.length}`);
  console.log(`Artifact: ${artifact}`);

  if (!args.publish) {
    console.log('\n----- TITLE -----\n' + digest.title);
    console.log('\n----- BODY -----\n' + digest.bodyTextOnly);
    console.log(
      JSON.stringify(
        { ok: true, dryRun: true, date: endYmd, itemCount: items.length },
        null,
        2,
      ),
    );
    return;
  }

  const apiKey = resolveApiKey();
  console.log(`Publishing with key ${maskApiKey(apiKey)} …`);
  const result = await publishArticle(apiKey, digest);

  ledger.posts[ledgerKey] = {
    date: endYmd,
    days: args.days,
    itemCount: items.length,
    urls: items.map((i) => i.url),
    title: digest.title,
    id: result?.id ?? null,
    shareLink: result?.shareLink ?? null,
    publishStatus: result?.publishStatus ?? 'ok',
    postedAt: new Date().toISOString(),
  };
  writeLedger(ledger);

  console.log(
    JSON.stringify(
      {
        ok: true,
        published: true,
        date: endYmd,
        id: result?.id ?? null,
        shareLink: result?.shareLink ?? null,
        ledger: getLedgerFilePath(),
      },
      null,
      2,
    ),
  );
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
