export function formatDate(date: Date): string {
  return date.toISOString().slice(0, 10);
}

/**
 * Rough reading time. Latin words at 220 wpm, CJK characters at 400 cpm, so a
 * mixed-language post does not read as "1 min".
 */
export function readingTime(body = ''): string {
  const cjk = (body.match(/[\u4e00-\u9fff]/g) || []).length;
  const words = (body.match(/\S+/g) || []).length;
  const latin = Math.max(0, words - cjk);
  const minutes = Math.max(1, Math.round(latin / 220 + cjk / 400));
  return `${minutes} min read`;
}

export function sortByDate<T extends { data: { date: Date } }>(posts: T[]): T[] {
  return [...posts].sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}
