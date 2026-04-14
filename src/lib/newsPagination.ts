import type { Locale } from '@/i18n/translations';

/** Items per news list page (EN and ZH lists stay the same length). */
export const NEWS_ITEMS_PER_PAGE = 10;

export function newsPageCount(itemLength: number): number {
  return Math.max(1, Math.ceil(itemLength / NEWS_ITEMS_PER_PAGE));
}

export function newsItemsForPage<T>(items: readonly T[], page: number): T[] {
  const p = Math.max(1, page);
  const start = (p - 1) * NEWS_ITEMS_PER_PAGE;
  return items.slice(start, start + NEWS_ITEMS_PER_PAGE) as T[];
}

/** Canonical list URL for a page (1 = index path without /2). */
export function newsListHref(locale: Locale, page: number, baseUrl: string): string {
  const base = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
  const path = locale === 'zh' ? `${base}zh/news` : `${base}news`;
  return page <= 1 ? path : `${path}/${page}`;
}
