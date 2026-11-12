/**
 * Minimal Binance Square OpenAPI client (text / long article only).
 * Key: BINANCE_SQUARE_OPENAPI_KEY or ~/.config/binance-square/openapi-key
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const BASE_URL_V1 = 'https://www.binance.com/bapi/composite/v1/public/pgc/openApi';
const CONFIG_DIR = path.join(os.homedir(), '.config', 'binance-square');
const CONFIG_FILE = path.join(CONFIG_DIR, 'openapi-key');
const LEDGER_FILE = path.join(CONFIG_DIR, 'ccprivacy-digest-ledger.json');

export function getConfigFilePath() {
  return CONFIG_FILE;
}

export function getLedgerFilePath() {
  return LEDGER_FILE;
}

export function maskApiKey(apiKey) {
  if (!apiKey) return '';
  if (apiKey.length <= 9) return `${apiKey.slice(0, 2)}...`;
  return `${apiKey.slice(0, 5)}...${apiKey.slice(-4)}`;
}

export function resolveApiKey() {
  const envKey = process.env.BINANCE_SQUARE_OPENAPI_KEY?.trim();
  if (envKey) return envKey;

  if (fs.existsSync(CONFIG_FILE)) {
    const saved = fs.readFileSync(CONFIG_FILE, 'utf8').trim();
    if (saved) return saved;
  }

  throw new Error(
    `Missing Square OpenAPI key. Set BINANCE_SQUARE_OPENAPI_KEY or save it to ${CONFIG_FILE}`,
  );
}

export function readLedger() {
  if (!fs.existsSync(LEDGER_FILE)) {
    return { posts: {} };
  }
  try {
    const raw = JSON.parse(fs.readFileSync(LEDGER_FILE, 'utf8'));
    if (!raw || typeof raw !== 'object') return { posts: {} };
    if (!raw.posts || typeof raw.posts !== 'object') return { posts: {} };
    return raw;
  } catch {
    return { posts: {} };
  }
}

export function writeLedger(ledger) {
  fs.mkdirSync(CONFIG_DIR, { recursive: true, mode: 0o700 });
  fs.writeFileSync(LEDGER_FILE, `${JSON.stringify(ledger, null, 2)}\n`, {
    mode: 0o600,
  });
  fs.chmodSync(LEDGER_FILE, 0o600);
}

export async function publishArticle(apiKey, { title, bodyTextOnly }) {
  const res = await fetch(`${BASE_URL_V1}/content/add`, {
    method: 'POST',
    headers: {
      'X-Square-OpenAPI-Key': apiKey,
      'Content-Type': 'application/json',
      clienttype: 'binanceSkill',
    },
    body: JSON.stringify({
      contentType: 2,
      title,
      bodyTextOnly,
    }),
  });

  const raw = await res.text();

  // Official skill treats 504 on /content/add as soft success.
  if (res.status === 504) {
    return { id: null, shareLink: null, publishStatus: 'success_without_post_id' };
  }

  let json;
  try {
    json = JSON.parse(raw);
  } catch {
    throw new Error(`API returned non-JSON (${res.status} ${res.statusText}): ${raw.slice(0, 200)}`);
  }

  if (json.code !== '000000') {
    throw new Error(`API error [${json.code}]: ${json.message}`);
  }

  return json.data;
}
