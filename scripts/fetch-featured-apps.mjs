/**
 * Fetches Canton Featured Apps for the ecosystem page.
 *
 * Priority:
 * 1) CC View API when CCVIEW_API_KEY is set (richest metadata)
 * 2) 5N Lighthouse public API (on-chain list + CIP-0116 locking metadata)
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

/** @typedef {{ provider: string, name: string, organization?: string, description?: string, url?: string, logoUrl?: string, tags: string[], featuredSince?: string, transactions?: number, volume?: string, rewards?: string }} FeaturedApp */

function formatHint(provider) {
  const hint = provider.split('::')[0] ?? provider;
  return hint
    .replace(/[-_]+/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase())
    .trim();
}

function lighthousePartyUrl(provider) {
  return `https://lighthouse.cantonloop.com/parties/${encodeURIComponent(provider)}`;
}

function pickWebsite(socials) {
  if (!Array.isArray(socials)) return undefined;
  const url = socials.find((s) => typeof s === 'string' && /^https?:\/\//i.test(s));
  return url;
}

function groupKey(tags) {
  const primary = tags[0]?.trim();
  return primary ? primary.toLowerCase().replace(/\s+/g, '-') : 'other';
}

function groupLabel(key, locale) {
  const en = {
    'non-issuer': 'Non-Issuer',
    'asset-issuer': 'Asset Issuer',
    other: 'Featured Apps',
  };
  const zh = {
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
  const order = ['non-issuer', 'asset-issuer', 'other'];
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
        url: pickWebsite(row.socials) ?? lighthousePartyUrl(provider),
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
async function fetchFromLighthouse() {
  const [faRes, lockRes] = await Promise.all([
    fetch(`${LIGHTHOUSE}/featured-apps`),
    fetch(`${LIGHTHOUSE}/featured-app-locking`),
  ]);

  if (!faRes.ok) throw new Error(`Lighthouse featured-apps ${faRes.status}`);
  if (!lockRes.ok) throw new Error(`Lighthouse featured-app-locking ${lockRes.status}`);

  const faJson = await faRes.json();
  const lockJson = await lockRes.json();

  /** @type {Map<string, object>} */
  const lockByParty = new Map();
  for (const row of lockJson.apps ?? []) {
    if (row.source_status !== '3-Approved' || !row.featured_app_party_id) continue;
    lockByParty.set(row.featured_app_party_id, row);
  }

  /** @type {FeaturedApp[]} */
  const apps = [];
  for (const row of faJson.apps ?? []) {
    const provider = row.payload?.provider;
    if (!provider) continue;
    const meta = lockByParty.get(provider);
    const appType = meta?.app_type;
    const tags = appType ? [appType] : ['Featured App'];
    apps.push({
      provider,
      name: meta?.app_name || meta?.institution || formatHint(provider),
      organization: meta?.institution ?? undefined,
      description: meta?.notes?.trim() || undefined,
      url: lighthousePartyUrl(provider),
      tags,
      featuredSince: row.created_at ?? undefined,
    });
  }

  apps.sort((a, b) => a.name.localeCompare(b.name, 'en'));
  return { apps, source: 'lighthouse' };
}

async function main() {
  const ccviewKey = process.env.CCVIEW_API_KEY?.trim();
  const { apps, source } = ccviewKey
    ? await fetchFromCcview(ccviewKey)
    : await fetchFromLighthouse();

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

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
