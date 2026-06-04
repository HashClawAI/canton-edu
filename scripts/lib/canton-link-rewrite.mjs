import { pathToSlug } from './canton-doc-utils.mjs';

const INTERNAL_SEGMENT =
  '(?:overview|appdev|global-synchronizer|integrations|reference|api-reference)';

const MD_LINK_RE = new RegExp(
  `\\]\\((\\/(?:${INTERNAL_SEGMENT})[^)\\s]*?)\\)`,
  'g',
);

const HREF_DQ_RE = new RegExp(
  `href="(\\/(?:${INTERNAL_SEGMENT})[^"]*?)"`,
  'g',
);

const HREF_SQ_RE = new RegExp(
  `href='(\\/(?:${INTERNAL_SEGMENT})[^']*?)'`,
  'g',
);

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

export function docsPrefixForLocale(locale, base = '/') {
  const root = base === '/' ? '/' : base.endsWith('/') ? base : `${base}/`;
  return locale === 'zh' ? `${root}zh/docs/canton/` : `${root}docs/canton/`;
}

export function rewriteInternalLinks(text, { locale, base = '/', validSlugs }) {
  if (!text || !validSlugs?.size) {
    return text;
  }

  const prefix = docsPrefixForLocale(locale, base);

  const replacePath = (full) => {
    const hashIdx = full.indexOf('#');
    const queryIdx = full.indexOf('?');
    const cut = [hashIdx, queryIdx].filter((i) => i >= 0).sort((a, b) => a - b)[0];
    const pathPart = cut === undefined ? full : full.slice(0, cut);
    const suffix = cut === undefined ? '' : full.slice(cut);
    const slug = legacyPathToSlug(pathPart);
    if (!slug || !validSlugs.has(slug)) {
      return full;
    }
    return `${prefix}${slug}${suffix}`;
  };

  const rewrite = (input, regex) =>
    input.replace(regex, (match, captured) => {
      const next = replacePath(captured);
      if (next === captured) {
        return match;
      }
      return match.replace(captured, next);
    });

  let out = text;
  out = rewrite(out, MD_LINK_RE);
  out = rewrite(out, HREF_DQ_RE);
  out = rewrite(out, HREF_SQ_RE);
  return out;
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

  return redirects;
}
