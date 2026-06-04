import docsData from '@/content/canton-docs/index.json';
import type { Locale } from '@/i18n/translations';

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

export function getCantonDocCategories(locale: Locale): string[] {
  return [...new Set(getCantonDocs(locale).map((item) => item.category))];
}
