import raw from '@/data/featured-apps.json';

export type FeaturedApp = {
  provider: string;
  name: string;
  organization?: string;
  description?: string;
  url?: string;
  logoUrl?: string;
  tags: string[];
  featuredSince?: string;
  transactions?: number;
  volume?: string;
  rewards?: string;
};

export type FeaturedAppGroup = {
  id: string;
  labelEn: string;
  labelZh: string;
  apps: FeaturedApp[];
};

export type FeaturedAppsData = {
  fetchedAt: string;
  source: 'lighthouse' | 'ccview';
  total: number;
  groups: FeaturedAppGroup[];
  apps: FeaturedApp[];
};

export const featuredApps = raw as FeaturedAppsData;

export function groupLabel(group: FeaturedAppGroup, locale: 'en' | 'zh'): string {
  return locale === 'zh' ? group.labelZh : group.labelEn;
}

export function formatFeaturedSince(iso: string | undefined, locale: 'en' | 'zh'): string | undefined {
  if (!iso) return undefined;
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return undefined;
  return date.toLocaleDateString(locale === 'zh' ? 'zh-CN' : 'en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    timeZone: 'UTC',
  });
}
