/**
 * Latest cip-discuss threads for the CIPs page.
 *
 * 1) If GROUPSIO_API_KEY is set, uses the official Groups.io API (Bearer token).
 *    Set GROUPSIO_GROUP_NAME (default: cip-discuss) or GROUPSIO_GROUP_ID.
 *    Topic links use CIP_DISCUSS_PUBLIC_BASE (default: https://lists.sync.global).
 *
 * 2) Otherwise falls back to Jina Reader on lists.sync.global/topics (no API key).
 */

const TOPICS_PAGE = 'https://lists.sync.global/g/cip-discuss/topics';
const JINA_READER = `https://r.jina.ai/${TOPICS_PAGE}`;
const GROUPS_API = 'https://groups.io/api/v1/gettopics';

export type CipDiscussTopic = { title: string; url: string };

const TOPIC_LINK =
  /\[([^\]]+)\]\((https:\/\/lists\.sync\.global\/g\/cip-discuss\/topic\/[^)\s]+)\)/g;

type GroupsIoTopicRow = {
  id?: number;
  subject?: string;
};

type GroupsIoListResponse = {
  object?: string;
  type?: string;
  data?: GroupsIoTopicRow[];
};

function topicUrlOnListSite(groupPath: string, topicId: number, publicBase: string): string {
  const base = publicBase.replace(/\/$/, '');
  return `${base}/g/${encodeURIComponent(groupPath)}/topic/${topicId}`;
}

async function fetchCipDiscussTopicsFromGroupsIo(max: number): Promise<CipDiscussTopic[] | null> {
  const key = process.env.GROUPSIO_API_KEY?.trim();
  if (!key) return null;

  const groupName = process.env.GROUPSIO_GROUP_NAME?.trim() || 'cip-discuss';
  const groupId = process.env.GROUPSIO_GROUP_ID?.trim();
  const publicBase =
    process.env.CIP_DISCUSS_PUBLIC_BASE?.trim() || 'https://lists.sync.global';
  const groupPath =
    process.env.CIP_DISCUSS_GROUP_PATH?.trim() || groupName;

  const url = new URL(GROUPS_API);
  if (groupId) {
    // gettopics historically uses `groupid` in the official curl examples.
    url.searchParams.set('groupid', groupId);
  } else {
    url.searchParams.set('group_name', groupName);
  }
  url.searchParams.set('limit', String(Math.min(100, max)));
  url.searchParams.set('sort_field', 'updated');
  url.searchParams.set('sort_dir', 'desc');

  const res = await fetch(url.toString(), {
    headers: {
      Authorization: `Bearer ${key}`,
      Accept: 'application/json',
    },
    signal: AbortSignal.timeout(25_000),
  });

  if (!res.ok) return null;

  const json = (await res.json()) as GroupsIoListResponse;
  if (json.object === 'error' || json.type === 'unauthorized_error') return null;
  if (json.object !== 'list' || !Array.isArray(json.data)) return null;

  const out: CipDiscussTopic[] = [];
  for (const row of json.data) {
    const id = row.id;
    const subject = row.subject?.trim();
    if (typeof id !== 'number' || !subject) continue;
    out.push({
      title: subject,
      url: topicUrlOnListSite(groupPath, id, publicBase),
    });
    if (out.length >= max) break;
  }
  return out;
}

async function fetchCipDiscussTopicsFromJina(max: number): Promise<CipDiscussTopic[]> {
  const res = await fetch(JINA_READER, {
    headers: { Accept: 'text/plain' },
    signal: AbortSignal.timeout(28_000),
  });
  if (!res.ok) return [];
  const text = await res.text();
  const out: CipDiscussTopic[] = [];
  const seen = new Set<string>();
  let m: RegExpExecArray | null;
  TOPIC_LINK.lastIndex = 0;
  while ((m = TOPIC_LINK.exec(text)) !== null) {
    const title = m[1].trim();
    const url = m[2].trim();
    if (!title || seen.has(url)) continue;
    if (title.startsWith('!')) continue;
    seen.add(url);
    out.push({ title, url });
    if (out.length >= max) break;
  }
  return out;
}

/** Build-time fetch for Astro static pages. */
export async function fetchCipDiscussTopics(max = 12): Promise<CipDiscussTopic[]> {
  const fromApi = await fetchCipDiscussTopicsFromGroupsIo(max).catch(() => null);
  if (fromApi !== null && fromApi.length > 0) return fromApi;
  if (fromApi !== null && fromApi.length === 0) return [];
  return fetchCipDiscussTopicsFromJina(max);
}
