/**
 * Fetches Canton Featured Apps for the ecosystem page.
 *
 * Priority:
 * 1) CC View API when CCVIEW_API_KEY is set (richest metadata)
 * 2) CC View App Locking page via Jina Reader (no API key) + on-chain list from 5N Lighthouse
 * 3) 5N Lighthouse public API only (fallback if CC View scrape fails)
 *
 * Writes src/data/featured-apps.json — run before `astro build`.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, '..', 'src', 'data', 'featured-apps.json');
const LIGHTHOUSE = 'https://lighthouse.cantonloop.com/api';
const CCVIEW = 'https://ccview.io/api/v4/featured-apps';
const CCVIEW_LOCKING_PAGE = 'https://ccview.io/featured-app-locking/';
const JINA_READER = `https://r.jina.ai/${CCVIEW_LOCKING_PAGE}`;

/** @typedef {{ provider: string, name: string, organization?: string, description?: string, url?: string, logoUrl?: string, tags: string[], featuredSince?: string, transactions?: number, volume?: string, rewards?: string }} FeaturedApp */

function formatHint(provider) {
  const hint = provider.split('::')[0] ?? provider;
  return hint
    .replace(/[-_]+/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase())
    .trim();
}

function ccviewPartyUrl(provider) {
  return `https://ccview.io/party/${encodeURIComponent(provider)}/`;
}

function normalizeName(name) {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

function pickWebsite(socials) {
  if (!Array.isArray(socials)) return undefined;
  const url = socials.find((s) => typeof s === 'string' && /^https?:\/\//i.test(s));
  return url;
}

function groupKey(tags) {
  const primary = tags[0]?.trim();
  return primary ? primary.toLowerCase().replace(/\s+/g, '-').replace(/&/g, 'and') : 'other';
}

function groupLabel(key, locale) {
  const en = {
    wallets: 'Wallets',
    identity: 'Identity',
    'infra-and-dev-tools': 'Infra & Dev Tools',
    rwa: 'RWA',
    liquidity: 'Liquidity',
    payments: 'Payments',
    lending: 'Lending',
    amm: 'AMM',
    defi: 'DeFi',
    'social-and-community': 'Social & Community',
    'api-and-analytics': 'API & Analytics',
    financing: 'Financing',
    'non-issuer': 'Non-Issuer',
    'asset-issuer': 'Asset Issuer',
    other: 'Featured Apps',
  };
  const zh = {
    wallets: '钱包',
    identity: '身份',
    'infra-and-dev-tools': '基础设施与开发工具',
    rwa: 'RWA',
    liquidity: '流动性',
    payments: '支付',
    lending: '借贷',
    amm: 'AMM',
    defi: 'DeFi',
    'social-and-community': '社交与社区',
    'api-and-analytics': 'API 与分析',
    financing: '融资',
    'non-issuer': '非发行方应用',
    'asset-issuer': '资产发行方',
    other: '精选应用',
  };
  const map = locale === 'zh' ? zh : en;
  return map[key] ?? tagsTitleCase(key);
}

function tagsTitleCase(key) {
  return key
    .split('-')
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');
}

/** @param {FeaturedApp[]} apps */
function buildGroups(apps) {
  /** @type {Map<string, FeaturedApp[]>} */
  const byGroup = new Map();
  for (const app of apps) {
    const key = groupKey(app.tags);
    if (!byGroup.has(key)) byGroup.set(key, []);
    byGroup.get(key).push(app);
  }
  const order = [
    'wallets',
    'defi',
    'amm',
    'payments',
    'lending',
    'liquidity',
    'rwa',
    'infra-and-dev-tools',
    'api-and-analytics',
    'identity',
    'social-and-community',
    'financing',
    'non-issuer',
    'asset-issuer',
    'other',
  ];
  const keys = [...new Set([...order, ...byGroup.keys()])].filter((k) => byGroup.has(k));
  return keys.map((key) => ({
    id: key,
    labelEn: groupLabel(key, 'en'),
    labelZh: groupLabel(key, 'zh'),
    apps: byGroup
      .get(key)
      .slice()
      .sort((a, b) => a.name.localeCompare(b.name, 'en')),
  }));
}

const ROLE_PREFIX = /^(App provider|Asset issuer)\b/i;

/** @param {string} chunk */
function parseRoleChunk(chunk) {
  const line = chunk.split('\n')[0].trim();
  const prefix = line.match(ROLE_PREFIX);
  if (!prefix) return null;

  const role = prefix[1];
  let rest = line.slice(prefix[0].length).replace(/^·\s*/, '').trim();
  if (!rest) return { role };

  rest = rest.replace(/—Featured.*$/i, '').replace(/—Pending.*$/i, '').trim();

  const lockMatch = rest.match(
    /^(.+?)\s+(\d[\d.,]*(?:K|M)?(?:\s*\/\s*\d[\d.,]*(?:K|M)?)?)\s*CC(?:\s+[-+]?[\d.,]+[KMB]?\s*CC)?$/i,
  );
  if (lockMatch) {
    return {
      role,
      category: lockMatch[1].trim(),
      lockSummary: `${lockMatch[2]} CC`.replace(/\s+/g, ' '),
    };
  }
  if (/^\d[\d.,]*(?:K|M)?(?:\s*\/\s*\d[\d.,]*(?:K|M)?)?\s*CC$/i.test(rest)) {
    return { role, lockSummary: rest.replace(/\s+/g, ' ') };
  }
  return { role, category: rest };
}

function cleanCategory(raw) {
  if (!raw) return undefined;
  return raw
    .replace(/\s+\d[\d.,]*(?:K|M)?(?:\s*\/\s*\d[\d.,]*(?:K|M)?)?\s*CC.*$/i, '')
    .replace(/—Featured.*$/i, '')
    .replace(/—Pending.*$/i, '')
    .trim();
}

function cleanAppName(name) {
  return name.replace(/^\d+\s+(?:day|days|month|months)\s+/i, '').trim();
}

/**
 * Parse CC View App Locking markdown (via Jina Reader).
 * @param {string} markdown
 */
export function parseCcviewLockingMarkdown(markdown) {
  const content = markdown.includes('Markdown Content:')
    ? markdown.split('Markdown Content:')[1].trim()
    : markdown.trim();
  const chunks = content.split(/\n{2,}/).map((c) => c.trim()).filter(Boolean);

  /** @type {Array<{ name: string, role?: string, category?: string, status?: string, lockSummary?: string }>} */
  const apps = [];
  let pendingName = '';

  for (const chunk of chunks) {
    if (/^(Title:|URL Source:|#)/.test(chunk)) continue;
    if (/^Cookie Notice|^RejectAccept|^Explore$|^Sign In$/i.test(chunk)) continue;

    const roleParsed = parseRoleChunk(chunk);
    if (roleParsed) {
      const name = pendingName || chunk.split('\n')[0].trim();
      pendingName = '';
      const status = /\bFeatured\b/i.test(chunk)
        ? 'Featured'
        : /\bPending\b/i.test(chunk)
          ? 'Pending'
          : undefined;
      if (name && !ROLE_PREFIX.test(name)) {
        apps.push({
          name: cleanAppName(name.replace(/\n/g, ' ').trim()),
          role: roleParsed.role,
          category: cleanCategory(roleParsed.category),
          status,
          lockSummary: roleParsed.lockSummary,
        });
      }
      pendingName = '';
      continue;
    }

    if (
      /^shared ·/i.test(chunk) ||
      /^[-+]?[\d.,]+[KMB]?\s+net/i.test(chunk) ||
      /^awaiting vote/i.test(chunk) ||
      /^no deposit yet/i.test(chunk) ||
      /^—$/.test(chunk) ||
      /^\d+\s+(?:day|days|month|months)$/i.test(chunk)
    ) {
      pendingName = '';
      continue;
    }

    if (/^(Featured|Pending)$/i.test(chunk)) {
      continue;
    }

    pendingName = pendingName ? `${pendingName} ${chunk}` : chunk;
  }

  return apps.map((app) => ({
    ...app,
    name: cleanAppName(app.name),
    category: cleanCategory(app.category),
  }));
}

/** @returns {Promise<Map<string, { name: string, role?: string, category?: string, status?: string, lockSummary?: string }>>} */
async function fetchCcviewLockingIndex() {
  const res = await fetch(JINA_READER, {
    headers: { Accept: 'text/plain' },
  });
  if (!res.ok) {
    throw new Error(`Jina reader for CC View locking ${res.status}`);
  }
  const markdown = await res.text();
  const parsed = parseCcviewLockingMarkdown(markdown);
  /** @type {Map<string, typeof parsed[0]>} */
  const byName = new Map();
  for (const row of parsed) {
    byName.set(normalizeName(row.name), row);
  }
  return byName;
}

/** @returns {Promise<{ onChain: Map<string, string>, lockByParty: Map<string, object>, lockByName: Map<string, object> }>} */
async function fetchLighthouseIndex() {
  const [faRes, lockRes] = await Promise.all([
    fetch(`${LIGHTHOUSE}/featured-apps`),
    fetch(`${LIGHTHOUSE}/featured-app-locking`),
  ]);
  if (!faRes.ok) throw new Error(`Lighthouse featured-apps ${faRes.status}`);
  if (!lockRes.ok) throw new Error(`Lighthouse featured-app-locking ${lockRes.status}`);

  const faJson = await faRes.json();
  const lockJson = await lockRes.json();

  /** @type {Map<string, string>} */
  const onChain = new Map();
  for (const row of faJson.apps ?? []) {
    const provider = row.payload?.provider;
    if (provider) onChain.set(provider, row.created_at ?? '');
  }

  /** @type {Map<string, object>} */
  const lockByParty = new Map();
  /** @type {Map<string, object>} */
  const lockByName = new Map();
  for (const row of lockJson.apps ?? []) {
    if (row.source_status !== '3-Approved' || !row.featured_app_party_id) continue;
    lockByParty.set(row.featured_app_party_id, row);
    if (row.app_name) {
      lockByName.set(normalizeName(row.app_name), row);
    }
  }

  return { onChain, lockByParty, lockByName };
}

function findCcviewMeta(ccviewIndex, lhMeta, provider) {
  /** @type {string[]} */
  const candidates = [lhMeta?.app_name, lhMeta?.institution, formatHint(provider)].filter(Boolean);
  for (const c of candidates) {
    const hit = ccviewIndex.get(normalizeName(c));
    if (hit) return hit;
  }

  const appNorm = lhMeta?.app_name ? normalizeName(lhMeta.app_name) : '';
  const instNorm = lhMeta?.institution ? normalizeName(lhMeta.institution) : '';
  for (const [key, meta] of ccviewIndex) {
    const metaNorm = normalizeName(meta.name);
    if (appNorm && (key === appNorm || key.includes(appNorm) || appNorm.includes(key))) return meta;
    if (instNorm && (key.includes(instNorm) || instNorm.includes(key))) return meta;
    if (metaNorm && appNorm && (metaNorm.includes(appNorm) || appNorm.includes(metaNorm))) return meta;
  }
  return undefined;
}

function buildDescription(ccviewMeta, lhMeta) {
  const parts = [];
  const role = ccviewMeta?.role ?? (lhMeta?.app_type === 'Asset Issuer' ? 'Asset issuer' : lhMeta ? 'App provider' : undefined);
  if (role) parts.push(role);
  if (ccviewMeta?.category) parts.push(ccviewMeta.category);
  else if (lhMeta?.app_type) parts.push(lhMeta.app_type);
  if (ccviewMeta?.lockSummary) parts.push(ccviewMeta.lockSummary);
  if (ccviewMeta?.status) parts.push(ccviewMeta.status);
  return parts.length ? parts.join(' · ') : undefined;
}

function buildTags(ccviewMeta, lhMeta) {
  if (ccviewMeta?.category) return [ccviewMeta.category];
  if (lhMeta?.app_type) return [lhMeta.app_type];
  return ['Featured App'];
}

/** @returns {Promise<{ apps: FeaturedApp[], source: string }>} */
async function fetchFromCcviewLockingPage() {
  const [ccviewIndex, lh] = await Promise.all([fetchCcviewLockingIndex(), fetchLighthouseIndex()]);
  /** @type {FeaturedApp[]} */
  const apps = [];

  for (const [provider, featuredSince] of lh.onChain) {
    const lhMeta = lh.lockByParty.get(provider);
    const ccviewMeta = findCcviewMeta(ccviewIndex, lhMeta, provider);

    const name =
      ccviewMeta?.name ??
      lhMeta?.app_name ??
      lhMeta?.institution ??
      formatHint(provider);

    apps.push({
      provider,
      name,
      organization: lhMeta?.institution ?? undefined,
      description: buildDescription(ccviewMeta, lhMeta),
      url: ccviewPartyUrl(provider),
      tags: buildTags(ccviewMeta, lhMeta),
      featuredSince: featuredSince || undefined,
    });
  }

  apps.sort((a, b) => a.name.localeCompare(b.name, 'en'));
  return { apps, source: 'ccview-locking' };
}

/** @returns {Promise<{ apps: FeaturedApp[], source: string }>} */
async function fetchFromCcview(apiKey) {
  /** @type {FeaturedApp[]} */
  const apps = [];
  let offset = 0;
  const limit = 100;
  let total = Infinity;

  while (offset < total) {
    const url = new URL(CCVIEW);
    url.searchParams.set('limit', String(limit));
    url.searchParams.set('offset', String(offset));
    url.searchParams.set('sort_field', 'organization');
    url.searchParams.set('sort_order', 'asc');

    const res = await fetch(url, { headers: { 'X-API-Key': apiKey } });
    if (!res.ok) {
      const body = await res.text();
      throw new Error(`CC View featured-apps ${res.status}: ${body.slice(0, 200)}`);
    }
    const json = await res.json();
    total = json.paging?.total ?? json.data?.length ?? 0;

    for (const row of json.data ?? []) {
      const provider = row.provider;
      const tags = Array.isArray(row.tags) && row.tags.length ? row.tags : ['Featured App'];
      apps.push({
        provider,
        name: row.app_name || row.organization || formatHint(provider),
        organization: row.organization ?? undefined,
        description: row.description ?? undefined,
        url: pickWebsite(row.socials) ?? ccviewPartyUrl(provider),
        logoUrl: row.logo_url ?? undefined,
        tags,
        featuredSince: row.created_at ?? undefined,
        transactions: row.transactions ?? undefined,
        volume: row.volume ?? undefined,
        rewards: row.app_rewards_total ?? undefined,
      });
    }

    if (!json.data?.length || offset + limit >= total) break;
    offset += limit;
  }

  return { apps, source: 'ccview' };
}

/** @returns {Promise<{ apps: FeaturedApp[], source: string }>} */
async function fetchFromLighthouseOnly() {
  const lh = await fetchLighthouseIndex();
  /** @type {FeaturedApp[]} */
  const apps = [];

  for (const [provider, featuredSince] of lh.onChain) {
    const lhMeta = lh.lockByParty.get(provider);
    const appType = lhMeta?.app_type;
    const tags = appType ? [appType] : ['Featured App'];
    apps.push({
      provider,
      name: lhMeta?.app_name || lhMeta?.institution || formatHint(provider),
      organization: lhMeta?.institution ?? undefined,
      description: lhMeta?.notes?.trim() || undefined,
      url: ccviewPartyUrl(provider),
      tags,
      featuredSince: featuredSince || undefined,
    });
  }

  apps.sort((a, b) => a.name.localeCompare(b.name, 'en'));
  return { apps, source: 'lighthouse' };
}

async function main() {
  const ccviewKey = process.env.CCVIEW_API_KEY?.trim();
  let result;
  if (ccviewKey) {
    result = await fetchFromCcview(ccviewKey);
  } else {
    try {
      result = await fetchFromCcviewLockingPage();
    } catch (err) {
      console.warn(`CC View locking scrape failed (${err.message}); falling back to Lighthouse only.`);
      result = await fetchFromLighthouseOnly();
    }
  }

  const { apps, source } = result;
  if (!apps.length) {
    throw new Error('No featured apps returned — refusing to overwrite data file.');
  }

  const payload = {
    fetchedAt: new Date().toISOString(),
    source,
    total: apps.length,
    groups: buildGroups(apps),
    apps,
  };

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, `${JSON.stringify(payload, null, 2)}\n`, 'utf8');
  console.log(`Wrote ${apps.length} featured apps (${source}) → ${path.relative(process.cwd(), OUT)}`);
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  main().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}
