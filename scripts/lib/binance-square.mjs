/**
 * Minimal Binance Square OpenAPI client (short text + long article).
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
    return { items: {}, posts: {} };
  }
  try {
    const raw = JSON.parse(fs.readFileSync(LEDGER_FILE, 'utf8'));
    if (!raw || typeof raw !== 'object') return { items: {}, posts: {} };
    return {
      items: raw.items && typeof raw.items === 'object' ? raw.items : {},
      posts: raw.posts && typeof raw.posts === 'object' ? raw.posts : {},
    };
  } catch {
    return { items: {}, posts: {} };
  }
}

export function writeLedger(ledger) {
  fs.mkdirSync(CONFIG_DIR, { recursive: true, mode: 0o700 });
  const out = {
    items: ledger.items ?? {},
    posts: ledger.posts ?? {},
  };
  fs.writeFileSync(LEDGER_FILE, `${JSON.stringify(out, null, 2)}\n`, {
    mode: 0o600,
  });
  fs.chmodSync(LEDGER_FILE, 0o600);
}

async function contentAdd(apiKey, body) {
  const res = await fetch(`${BASE_URL_V1}/content/add`, {
    method: 'POST',
    headers: {
      'X-Square-OpenAPI-Key': apiKey,
      'Content-Type': 'application/json',
      clienttype: 'binanceSkill',
    },
    body: JSON.stringify(body),
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

/** Short Square post (contentType=1). */
export async function publishShortPost(apiKey, { bodyTextOnly }) {
  return contentAdd(apiKey, {
    contentType: 1,
    bodyTextOnly,
  });
}

/** Long article (contentType=2). Kept for ad-hoc use. */
export async function publishArticle(apiKey, { title, bodyTextOnly }) {
  return contentAdd(apiKey, {
    contentType: 2,
    title,
    bodyTextOnly,
  });
}

export function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
