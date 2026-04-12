#!/usr/bin/env node
/**
 * DNS + HTTPS checks for a custom domain ↔ GitHub Pages.
 * Default domain: hashclaw.ai (override with DOMAIN=example.com).
 * Apex A must be the four 185.199.*.153; curl -4 catches IPv4-only TLS issues.
 */
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);

const GITHUB_A = new Set([
  '185.199.108.153',
  '185.199.109.153',
  '185.199.110.153',
  '185.199.111.153',
]);

async function dig(args) {
  try {
    const { stdout } = await execFileAsync('dig', args, {
      timeout: 20_000,
      maxBuffer: 512 * 1024,
    });
    return stdout.trim();
  } catch (e) {
    return `ERROR:${e?.message || e}`;
  }
}

function parseShortA(raw) {
  return raw
    .split(/\s+/)
    .map((s) => s.trim())
    .filter((s) => /^\d+\.\d+\.\d+\.\d+$/.test(s));
}

function apexMatchesGithub(ips) {
  if (ips.length !== 4) return false;
  return ips.every((ip) => GITHUB_A.has(ip));
}

/** First zone NS from `dig +short NS` (any registrar), trailing dot stripped, for `@ns` apex queries. */
function firstZoneNsHost(nsRaw) {
  if (!nsRaw || nsRaw.startsWith('ERROR:')) return null;
  const line = nsRaw
    .split(/\n/)
    .map((s) => s.trim())
    .filter((s) => s && !s.startsWith(';'))[0];
  if (!line) return null;
  const host = line.replace(/\.$/, '').trim();
  if (!/^[a-z0-9.-]+$/i.test(host)) return null;
  return host || null;
}

/**
 * www OK if: no records, error (ignored), CNAME to github.io / apex, or A flattening to GitHub Pages IPs.
 */
function wwwDnsOk(cnameRaw, aRaw, domain) {
  const lines = [...cnameRaw.trim().split(/\n/), ...aRaw.trim().split(/\n/)]
    .map((l) => l.trim().replace(/\.$/, ''))
    .filter(Boolean);
  if (lines.length === 0) return true;
  if (lines.every((l) => l.startsWith('ERROR:'))) return true;
  const esc = domain.replace(/\./g, '\\.');
  const reApex = new RegExp(`^${esc}$`, 'i');
  return lines.some(
    (line) =>
      line.startsWith('ERROR:') ||
      /\.github\.io$/i.test(line) ||
      reApex.test(line) ||
      GITHUB_A.has(line),
  );
}

async function curlHead(url, forceIpv4) {
  const args = ['-sI', '-m', '20', '-L', '--max-redirs', '5', url];
  if (forceIpv4) args.splice(1, 0, '-4');
  try {
    const { stdout } = await execFileAsync('curl', args, {
      timeout: 25_000,
      maxBuffer: 256 * 1024,
    });
    const lines = stdout.split(/\r?\n/).filter(Boolean);
    const statusLines = lines.filter((l) => /^HTTP\//i.test(l));
    const ok200 = statusLines.some((l) => /200/.test(l));
    return { ok200, statusLines, error: null };
  } catch (e) {
    return { ok200: false, statusLines: [], error: String(e?.message || e) };
  }
}

async function main() {
  const DOMAIN = (process.env.DOMAIN || 'hashclaw.ai').replace(/[^a-z0-9.-]/gi, '');
  if (!DOMAIN || !DOMAIN.includes('.')) {
    console.error('Invalid or missing DOMAIN (expected a hostname like hashclaw.ai).');
    process.exit(1);
  }
  const wwwHost = `www.${DOMAIN}`;
  const siteUrl = `https://${DOMAIN}/`;

  const apexSys = await dig([DOMAIN, '+short', 'A']);
  const apex8888 = await dig(['@8.8.8.8', DOMAIN, '+short', 'A']);
  const aaaa8888 = await dig(['@8.8.8.8', DOMAIN, '+short', 'AAAA']);
  const wwwCname = await dig(['@8.8.8.8', wwwHost, '+short', 'CNAME']);
  const wwwA = await dig(['@8.8.8.8', wwwHost, '+short', 'A']);
  const ipsSys = parseShortA(apexSys).sort().join(',');
  const ipsPub = parseShortA(apex8888).sort().join(',');

  const httpsAny = await curlHead(siteUrl, false);
  const httpsV4 = await curlHead(siteUrl, true);

  const ns = await dig(['@8.8.8.8', DOMAIN, '+short', 'NS']);
  const nsHost = firstZoneNsHost(ns);
  let apexAuthRaw = '';
  if (nsHost) {
    apexAuthRaw = await dig(['@' + nsHost, DOMAIN, '+short', 'A']);
  }

  const apexOk = apexMatchesGithub(parseShortA(apex8888));
  const wwwOk = wwwDnsOk(wwwCname, wwwA, DOMAIN);
  /** Only flag split DNS when both resolvers returned at least one A (avoid false FAIL on local dig timeout/empty). */
  const splitDns =
    parseShortA(apex8888).length > 0 &&
    parseShortA(apexSys).length > 0 &&
    ipsSys !== ipsPub;

  const apexAuthIps = parseShortA(apexAuthRaw);
  /** Authoritative check is best-effort: skip if we cannot identify NS, or if auth query errored/empty. */
  let apexAuthOk = !nsHost;
  if (nsHost) {
    if (apexAuthRaw.startsWith('ERROR:')) apexAuthOk = apexOk;
    else if (!apexAuthRaw.trim()) apexAuthOk = apexOk;
    else apexAuthOk = apexMatchesGithub(apexAuthIps);
  }

  const summary = {
    domain: DOMAIN,
    apexDig8888Error: apex8888.startsWith('ERROR:') ? apex8888 : null,
    apexGithubOk8888: apexOk,
    apexIps8888: parseShortA(apex8888),
    apexAuthNs: nsHost,
    apexAuthRaw,
    apexAuthOk,
    apexAuthIps,
    apexAaaa8888Raw: aaaa8888,
    wwwCnameDig: wwwCname,
    wwwADig: wwwA,
    wwwPointsToPagesHost: wwwOk,
    splitDns,
    httpsOkDualStack: httpsAny.ok200,
    httpsOkIpv4Only: httpsV4.ok200,
    httpsV4StatusLines: httpsV4.statusLines,
    httpsV4Error: httpsV4.error,
    nsRaw: ns,
  };

  console.log(JSON.stringify(summary, null, 2));

  /** IPv4 HTTPS is the gate; dual-stack is advisory only. */
  const fail =
    !apexOk ||
    !apexAuthOk ||
    !wwwOk ||
    splitDns ||
    !httpsV4.ok200;
  if (fail) {
    const reasons = [];
    if (!apexOk) reasons.push(`apex A via 8.8.8.8 is not exactly the four GitHub Pages IPs (got: ${ipsPub || '(none)'})`);
    if (!apexAuthOk) reasons.push('authoritative apex A at zone NS does not match GitHub Pages');
    if (!wwwOk) reasons.push(`www DNS (${wwwHost}) is not CNAME to *.github.io / apex / flattened GitHub A`);
    if (splitDns) reasons.push(`resolver mismatch: system A (${ipsSys || 'empty'}) vs 8.8.8.8 (${ipsPub || 'empty'})`);
    if (!httpsV4.ok200) reasons.push(`IPv4 HTTPS HEAD to ${siteUrl} did not reach HTTP 200`);
    console.error('\nFAIL — checks that did not pass:\n- ' + reasons.join('\n- ') + '\n');
    console.error(
      'Docs: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain\n',
    );
    process.exit(1);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
