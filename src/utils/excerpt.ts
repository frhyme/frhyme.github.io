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

export function extractTldr(body?: string, maxLength: number = 180): string {
  if (!body) return '';
  let text = body.replace(/^---[\s\S]*?---/, '');
  text = text.replace(/```[\s\S]*?```/g, '');
  text = text.replace(/!\[[^\]]*\]\([^\)]*\)/g, '');
  text = text.replace(/\[([^\]]+)\]\([^\)]*\)/g, '$1');
  text = text.replace(/<[^>]+>/g, '');
  text = text.replace(/^[#>-]+\s*/gm, '');
  text = text.replace(/[*_~]+/g, '');

  const paras = text
    .split(/\n\s*\n/)
    .map((p) => p.replace(/\s+/g, ' ').trim())
    .filter(Boolean);

  let selected = '';
  for (const p of paras) {
    if (p.length > 35 && !/^(intro|마무리|정리|결론|참고)\s*[-:]?/i.test(p)) {
      selected = p;
      break;
    }
  }

  if (!selected && paras.length > 0) {
    selected = paras[0];
  }

  selected = selected.replace(/^(intro|정리|요약)\s*[-:]?\s*/i, '');

  if (selected.length > maxLength) {
    return selected.slice(0, maxLength - 3) + '...';
  }
  return selected;
}

export function getReadingTime(body?: string): number {
  if (!body) return 1;
  const length = body.replace(/\s+/g, ' ').length;
  return Math.max(1, Math.round(length / 500));
}
