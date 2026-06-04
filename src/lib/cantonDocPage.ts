import { getEntry } from 'astro:content';
import type { CollectionEntry } from 'astro:content';
import type { Locale } from '@/i18n/translations';

export type CantonDocPageEntry = CollectionEntry<'canton-doc-pages'>;

export function cantonDocPageId(locale: Locale, slug: string) {
  return `${locale}/${slug}`;
}

export async function getCantonDocPage(locale: Locale, slug: string) {
  return getEntry('canton-doc-pages', cantonDocPageId(locale, slug));
}
