#!/usr/bin/env node
/**
 * DNS + HTTPS checks for canton.tools ↔ GitHub Pages.
 * GitHub's NotServedByPagesError follows DNS; apex A must be the four 185.199.*.153.
 * curl -4 catches IPv4-only failures when wrong A records exist but AAAA still points to GitHub.
 */
import { appendFileSync } from 'node:fs';
import { execFile } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);
const __dirname = dirname(fileURLToPath(import.meta.url));
const DEBUG_LOG =
  process.env.DEBUG_LOG_PATH ||
  join(__dirname, '../../.cursor/debug-46264c.log');

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

/** First NS hostname without trailing dot, for @ns queries */
function firstNsHost(nsRaw) {
  const line = nsRaw
    .split(/\n/)
    .map((s) => s.trim())
    .find((s) => s.includes('domaincontrol'));
  if (!line) return null;
  return line.replace(/\.$/, '').trim() || null;
}

async function curlHead(url, forceIpv4) {
  const args = ['-sI', '-m', '20', '-L', '--max-redirs', '5', url];
  if (forceIpv4) args.splice(1, 0, '-4');
  try {
    const { stdout } = await execFileAsync('curl', args, {
      timeout: 25_000,
      maxBuffer: 256 * 1024,
    });
    const lines = stdout.split(/\r\n/).filter(Boolean);
    const statusLines = lines.filter((l) => /^HTTP\//i.test(l));
    const ok200 = statusLines.some((l) => /200/.test(l));
    return { ok200, statusLines, error: null };
  } catch (e) {
    return { ok200: false, statusLines: [], error: String(e?.message || e) };
  }
}

async function main() {
  const apexSys = await dig(['canton.tools', '+short', 'A']);
  const apex8888 = await dig(['@8.8.8.8', 'canton.tools', '+short', 'A']);
  const aaaa8888 = await dig(['@8.8.8.8', 'canton.tools', '+short', 'AAAA']);
  const wwwCname = await dig(['@8.8.8.8', 'www.canton.tools', '+short', 'CNAME']);
  const ipsSys = parseShortA(apexSys).sort().join(',');
  const ipsPub = parseShortA(apex8888).sort().join(',');

  const httpsAny = await curlHead('https://canton.tools/', false);
  const httpsV4 = await curlHead('https://canton.tools/', true);

  const ns = await dig(['@8.8.8.8', 'canton.tools', '+short', 'NS']);
  const nsHost = firstNsHost(ns);
  let apexAuthRaw = '';
  if (nsHost) {
    apexAuthRaw = await dig(['@' + nsHost, 'canton.tools', '+short', 'A']);
  }

  const apexOk = apexMatchesGithub(parseShortA(apex8888));
  /** www → *.github.io (recommended) OR www → apex (GitHub documents apex+www together) */
  const wwwLine = (wwwCname.trim().split(/\n/)[0] || '').replace(/\.$/, '').trim();
  const wwwOk =
    !wwwLine ||
    wwwLine.startsWith('ERROR:') ||
    /\.github\.io$/i.test(wwwLine) ||
    /^canton\.tools$/i.test(wwwLine);
  const splitDns = ipsSys !== ipsPub;

  const apexAuthIps = parseShortA(apexAuthRaw);
  const apexAuthOk = apexMatchesGithub(apexAuthIps);

  const summary = {
    apexGithubOk8888: apexOk,
    apexIps8888: parseShortA(apex8888),
    apexAuthNs: nsHost,
    apexAuthRaw,
    apexAuthOk,
    apexAuthIps,
    apexAaaa8888Raw: aaaa8888,
    wwwCnameRaw: wwwCname,
    wwwPointsToPagesHost: wwwOk,
    splitDns,
    httpsOkDualStack: httpsAny.ok200,
    httpsOkIpv4Only: httpsV4.ok200,
    httpsV4StatusLines: httpsV4.statusLines,
    httpsV4Error: httpsV4.error,
    nsRaw: ns,
  };

  // #region agent log
  try {
    appendFileSync(
      DEBUG_LOG,
      JSON.stringify({
        sessionId: '46264c',
        runId: process.env.DEBUG_RUN_ID || 'dns-check',
        hypothesisId: 'H_AUTH',
        location: 'debug-pages-dns.mjs',
        message: 'DNS snapshot',
        data: summary,
        timestamp: Date.now(),
      }) + '\n',
    );
  } catch {
    /* log path may be missing in sandboxes */
  }
  // #endregion

  console.log(JSON.stringify(summary, null, 2));

  const fail =
    !apexOk ||
    !apexAuthOk ||
    !wwwOk ||
    splitDns ||
    !httpsV4.ok200 ||
    !httpsAny.ok200;
  if (fail) {
    console.error(
      '\nFAIL: Fix GoDaddy DNS — apex @ must be ONLY the four GitHub A records (185.199.108–111.153). Turn off domain forwarding. If apexAuthOk is false, authoritative NS still serves wrong A. See https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain\n',
    );
    process.exit(1);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
