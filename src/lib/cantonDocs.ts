import docsData from '@/content/canton-docs/index.json';
import type { Locale } from '@/i18n/translations';
import { t } from '@/i18n/translations';

const CATEGORY_ORDER = [
  'overview',
  'appdev',
  'global-synchronizer',
  'integrations',
  'reference',
  'api-reference',
] as const;

export interface CantonDocItem {
  slug: string;
  locale: Locale;
  title: string;
  sourceTitle: string;
  summary: string;
  category: string;
  tags: string[];
  sourceUrl: string;
  localPath: string;
}

export const cantonDocsGeneratedAt = docsData.generatedAt;
export const cantonDocsSourceIndexUrl = docsData.sourceIndexUrl;

export function getCantonDocs(locale: Locale): CantonDocItem[] {
  return docsData.items
    .filter((item): item is CantonDocItem => item.locale === locale)
    .sort((a, b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title));
}

export function getCantonDoc(locale: Locale, slug: string): CantonDocItem | undefined {
  return getCantonDocs(locale).find((item) => item.slug === slug);
}

export function getCantonDocCategoryLabel(locale: Locale, category: string): string {
  const labels = t(locale).docs.categories as Record<string, string | undefined>;
  return labels[category] ?? category.replace(/-/g, ' ');
}

export function getCantonDocCategories(locale: Locale): string[] {
  const present = new Set(getCantonDocs(locale).map((item) => item.category));
  const ordered = CATEGORY_ORDER.filter((c) => present.has(c));
  for (const c of present) {
    if (!ordered.includes(c)) ordered.push(c);
  }
  return ordered;
}
