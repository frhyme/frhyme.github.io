export function cleanExcerpt(body?: string, maxLength: number = 140): string {
  if (!body) return '';
  const text = body
    .replace(/^---[\s\S]*?---/, '')
    .replace(/```[\s\S]*?```/g, '')
    .replace(/`[^`]+`/g, '')
    .replace(/!\[[^\]]*\]\([^\)]*\)/g, '')
    .replace(/\[([^\]]+)\]\([^\)]*\)/g, '$1')
    .replace(/<[^>]+>/g, '')
    .replace(/^[#>-]+\s*/gm, '')
    .replace(/[*_~]+/g, '')
    .replace(/\s+/g, ' ')
    .trim();

  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength - 3) + '...';
}

export function getReadingTime(body?: string): number {
  if (!body) return 1;
  const length = body.replace(/\s+/g, ' ').length;
  return Math.max(1, Math.round(length / 500));
}
