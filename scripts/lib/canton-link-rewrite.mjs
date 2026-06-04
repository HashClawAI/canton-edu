import path from 'node:path';
import { pathToSlug } from './canton-doc-utils.mjs';

const OFFICIAL_ORIGIN = 'https://docs.canton.network';

/** Manual overrides when official path ≠ mirrored slug or section index. */
export const PATH_ALIASES = {
  '/appdev/quickstart': 'appdev-quickstart-index',
  '/appdev/deep-dives/query-with-pqs': 'appdev-modules-m4-query-with-pqs',
  '/appdev/deep-dives/manage-daml-packages': 'appdev-modules-m5-manage-daml-packages',
  '/appdev/get-started/upgrading-from-previous-versions': 'appdev-get-started-whats-new',
  '/appdev/deep-dives/explicit-contract-disclosure': 'appdev-deep-dives-explicit-contract-disclosure',
  '/appdev/deep-dives/授权': 'appdev-deep-dives-authorization',
  '/appdev/deep-dives/命令-deduplication': 'appdev-deep-dives-command-deduplication',
  '/appdev/快速入门': 'appdev-quickstart-index',
  '/reference/json-api-asyncapi-reference': 'reference-json-api-asyncapi-reference-operations-details',
  '/global-synchronizer/product-operations/sv-pruning': 'global-synchronizer-production-operations-sv-pruning',
  '/global-synchronizer/deployment/installation': 'global-synchronizer-deployment-validator-docker-compose',
  '/global-synchronizer/理解/介绍': 'global-synchronizer-understand-introduction',
  '/global-synchronizer/生产运营/关键指标': 'global-synchronizer-production-operations-key-metrics',
  '/integrations/钱包/guidance': 'integrations-wallet-guidance',
  '/integrations/wallet/guidance': 'integrations-wallet-guidance',
  '/sdks-tools/development-tools/localnet': 'appdev-modules-m5-localnet-development',
  '/sdks-tools/reference-projects/cn-quickstart': 'appdev-quickstart-index',
  '/appdev/reference/daml-standard-library/da-action':
    'appdev-reference-daml-standard-library-da-action',
  '/appdev/reference/daml-standard-library/index': 'appdev-reference-daml-standard-library-index',
  '/global-synchronizer/extension-synchronizers/hybrid-同步器-pattern':
    'global-synchronizer-extension-synchronizers-hybrid-synchronizer-pattern',
  '/appdev/deep-dives/explicit-合约-disclosure': 'appdev-deep-dives-explicit-contract-disclosure',
};

/** Apply to path strings before slug lookup (order: longer / specific first). */
const ZH_PATH_REPLACEMENTS = [
  ['/global-同步器/生产操作/', '/global-synchronizer/production-operations/'],
  ['/global-同步器/生产-operations/', '/global-synchronizer/production-operations/'],
  ['/global-同步器/deployment/', '/global-synchronizer/deployment/'],
  ['/global-同步器/理解/', '/global-synchronizer/understand/'],
  ['/global-同步器/', '/global-synchronizer/'],
  ['/global-synchronizer/生产操作/', '/global-synchronizer/production-operations/'],
  ['/global-synchronizer/生产-operations/', '/global-synchronizer/production-operations/'],
  ['/集成/钱包-gateway/', '/integrations/wallet-gateway/'],
  ['/集成/钱包/', '/integrations/wallet/'],
  ['/集成/dapp-sdk/', '/integrations/dapp-sdk/'],
  ['/集成/overview', '/integrations/overview'],
  ['/集成/', '/integrations/'],
  ['/sdks-tools/development-tools/', '/sdks-tools/development-tools/'],
  ['/钱包-gateway/', '/wallet-gateway/'],
  ['/钱包/', '/wallet/'],
  ['/提供方', '/providers'],
  ['/参与方', '/participant'],
  ['/同步器', '/synchronizer'],
  ['/修剪', '/pruning'],
  ['/授权', '/authorization'],
  ['/合约', '/contract'],
  ['/命令', '/command'],
  ['/关键指标', '/key-metrics'],
  ['/备份', '/backups'],
  ['/流量', '/traffic'],
  ['/配置', '/configuration'],
  ['/运维', '/operations'],
  ['/理解', '/understand'],
  ['/快速入门', '/quickstart'],
  ['参与方-config', 'participant-config'],
  ['remote参与方config', 'remoteparticipantconfig'],
  ['hybrid-同步器-pattern', 'hybrid-synchronizer-pattern'],
  ['同步器-流量', 'synchronizer-traffic'],
  ['oidc-提供方', 'oidc-providers'],
  ['validator-备份', 'validator-backups'],
  ['node-备份-恢复', 'node-backup-restore'],
  ['product-operations', 'production-operations'],
];

const ROOT_MD = /\]\((\/[^)\s]+)\)/g;
const ROOT_HREF_DQ = /href="(\/[^"]+)"/g;
const ROOT_HREF_SQ = /href='(\/[^']+)'/g;
const REL_MD = /\]\(((\.\.?\/)[^)\s#]+[^)\s]*)\)/g;
const REL_HREF_DQ = /href="((?:\.\.?\/)[^"]+)"/g;
const REL_HREF_SQ = /href='((?:\.\.?\/)[^']+)'/g;
const BARE_PREFIX =
  '(?:appdev|overview|global-synchronizer|integrations|reference|sdks-tools|wallet-gateway|api-reference)';
const BARE_MD = new RegExp(`\\]\\((${BARE_PREFIX}\\/[^)\\s]+)\\)`, 'g');
const BARE_HREF_DQ = new RegExp(`href="(${BARE_PREFIX}\\/[^"]+)"`, 'g');
const BARE_HREF_SQ = new RegExp(`href='(${BARE_PREFIX}\\/[^']+)'`, 'g');

export function normalizePathString(p) {
  let out = p;
  for (const [from, to] of ZH_PATH_REPLACEMENTS) {
    if (out.includes(from)) {
      out = out.split(from).join(to);
    }
  }
  return out;
}

export function legacyPathToSlug(hrefPath) {
  const pathOnly = hrefPath.split('#')[0].split('?')[0];
  if (!pathOnly.startsWith('/')) {
    return null;
  }
  const mdPath = pathOnly.endsWith('.md') ? pathOnly : `${pathOnly}.md`;
  return pathToSlug(mdPath);
}

export function buildValidSlugSet(items) {
  return new Set(items.filter((item) => item.locale === 'en').map((item) => item.slug));
}

export function buildLegacyPathMap(items) {
  const map = new Map();
  for (const item of items) {
    if (item.locale !== 'en') continue;
    try {
      const legacy = new URL(item.sourceUrl).pathname.replace(/\.md$/i, '');
      map.set(legacy, item.slug);
    } catch {
      /* skip */
    }
  }
  return map;
}

export function buildSlugToSourceUrl(items) {
  const map = new Map();
  for (const item of items) {
    if (item.locale !== 'en') continue;
    map.set(item.slug, item.sourceUrl);
  }
  return map;
}

export function docsPrefixForLocale(locale, base = '/') {
  const root = base === '/' ? '/' : base.endsWith('/') ? base : `${base}/`;
  return locale === 'zh' ? `${root}zh/docs/canton/` : `${root}docs/canton/`;
}

function splitPathAndSuffix(href) {
  const hashIdx = href.indexOf('#');
  const queryIdx = href.indexOf('?');
  const cut = [hashIdx, queryIdx].filter((i) => i >= 0).sort((a, b) => a - b)[0];
  if (cut === undefined) {
    return { pathPart: href, suffix: '' };
  }
  return { pathPart: href.slice(0, cut), suffix: href.slice(cut) };
}

export function resolveOfficialPath(officialPath, { validSlugs, legacyPathMap }) {
  const normalized = normalizePathString(officialPath);
  const { pathPart, suffix } = splitPathAndSuffix(normalized);

  if (PATH_ALIASES[pathPart]) {
    const slug = PATH_ALIASES[pathPart];
    return { type: 'internal', slug, suffix };
  }

  if (legacyPathMap.has(pathPart)) {
    return { type: 'internal', slug: legacyPathMap.get(pathPart), suffix };
  }

  const computed = legacyPathToSlug(pathPart);
  if (computed && validSlugs.has(computed)) {
    return { type: 'internal', slug: computed, suffix };
  }

  return { type: 'external', url: `${OFFICIAL_ORIGIN}${pathPart}${suffix}`, suffix };
}

export function hrefToTarget(href, ctx) {
  const { locale, base, validSlugs, legacyPathMap } = ctx;

  if (
    !href ||
    href.startsWith('#') ||
    href.startsWith('mailto:') ||
    href.startsWith('tel:') ||
    href.startsWith('http://') ||
    href.startsWith('https://')
  ) {
    return href;
  }

  const prefix = docsPrefixForLocale(locale, base);

  if (href.startsWith('/docs/canton/') || href.startsWith('/zh/docs/canton/')) {
    return href;
  }

  if (href.startsWith('./') || href.startsWith('../')) {
    return resolveRelativeHref(href, ctx);
  }

  const abs = href.startsWith('/') ? href : `/${href}`;
  const resolved = resolveOfficialPath(abs, { validSlugs, legacyPathMap });
  if (resolved.type === 'internal') {
    return `${prefix}${resolved.slug}${resolved.suffix}`;
  }
  return resolved.url;
}

export function resolveRelativeHref(relHref, ctx) {
  const { fromSlug, slugToSourceUrl, validSlugs, legacyPathMap } = ctx;
  const sourceUrl = slugToSourceUrl?.get(fromSlug);
  if (!sourceUrl) {
    return relHref;
  }

  let officialPath;
  try {
    const u = new URL(sourceUrl);
    const dir = path.posix.dirname(u.pathname);
    officialPath = path.posix.normalize(path.posix.join(dir, relHref));
  } catch {
    return relHref;
  }

  const withoutMd = officialPath.replace(/\.md$/i, '');
  const resolved = resolveOfficialPath(withoutMd, { validSlugs, legacyPathMap });
  const prefix = docsPrefixForLocale(ctx.locale, ctx.base);

  if (resolved.type === 'internal') {
    return `${prefix}${resolved.slug}${resolved.suffix}`;
  }
  return resolved.url;
}

function rewriteCapture(text, regex, ctx) {
  return text.replace(regex, (match, captured) => {
    const next = hrefToTarget(captured, ctx);
    if (next === captured) {
      return match;
    }
    return match.replace(captured, next);
  });
}

/**
 * Rewrite all internal, relative, and official-site links in markdown/HTML.
 * @param {string} text
 * @param {{ locale: string, base?: string, validSlugs: Set<string>, legacyPathMap: Map<string,string>, slugToSourceUrl?: Map<string,string>, fromSlug?: string }} ctx
 */
export function rewriteAllLinks(text, ctx) {
  if (!text) {
    return text;
  }

  const fullCtx = {
    locale: ctx.locale,
    base: ctx.base ?? '/',
    validSlugs: ctx.validSlugs,
    legacyPathMap: ctx.legacyPathMap,
    slugToSourceUrl: ctx.slugToSourceUrl,
    fromSlug: ctx.fromSlug,
  };

  let out = text;
  out = rewriteCapture(out, ROOT_MD, fullCtx);
  out = rewriteCapture(out, ROOT_HREF_DQ, fullCtx);
  out = rewriteCapture(out, ROOT_HREF_SQ, fullCtx);
  out = rewriteCapture(out, REL_MD, fullCtx);
  out = rewriteCapture(out, REL_HREF_DQ, fullCtx);
  out = rewriteCapture(out, REL_HREF_SQ, fullCtx);
  out = rewriteCapture(out, BARE_MD, fullCtx);
  out = rewriteCapture(out, BARE_HREF_DQ, fullCtx);
  out = rewriteCapture(out, BARE_HREF_SQ, fullCtx);
  return out;
}

/** @deprecated use rewriteAllLinks */
export function rewriteInternalLinks(text, ctx) {
  return rewriteAllLinks(text, ctx);
}

function withBase(base, pathname) {
  if (!base || base === '/') {
    return pathname;
  }
  const trimmed = base.endsWith('/') ? base.slice(0, -1) : base;
  return `${trimmed}${pathname}`;
}

export function buildLegacyRedirects(items, base = '/') {
  const redirects = {};

  for (const item of items) {
    if (item.locale !== 'en') {
      continue;
    }
    let legacy;
    try {
      legacy = new URL(item.sourceUrl).pathname.replace(/\.md$/i, '');
    } catch {
      continue;
    }
    if (!legacy || legacy === '/') {
      continue;
    }
    const target = withBase(base, `/docs/canton/${item.slug}`);
    const source = withBase(base, legacy);
    if (source !== target) {
      redirects[source] = target;
    }
  }

  for (const [legacyPath, slug] of Object.entries(PATH_ALIASES)) {
    const target = withBase(base, `/docs/canton/${slug}`);
    const source = withBase(base, legacyPath);
    if (source !== target) {
      redirects[source] = target;
    }
  }

  return redirects;
}
