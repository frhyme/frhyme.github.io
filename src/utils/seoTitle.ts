/**
 * SEO Title Optimization Utility
 * Cleans repetitive legacy prefixes, category noise, and formatting
 * to maximize click-through rate (CTR) and search engine visibility.
 */
export function cleanTitle(rawTitle: string): string {
  if (!rawTitle) return '';
  let t = rawTitle.trim();

  // Strip leading legacy parenthesis patterns like:
  // 'python-lib) ', 'python-basic) ', 'Algorithm) ', 'kaggle) ', '[python] '
  t = t.replace(/^\[?[a-zA-Z0-9_\-\s]+\]?\s*[\)\:]\s*/i, '');

  // Strip duplicate nested prefixes and standardize to crisp topics
  if (/^python\s*-\s*networkx\s*-\s*/i.test(t)) {
    t = t.replace(/^python\s*-\s*networkx\s*-\s*/i, 'NetworkX: ');
  } else if (/^python\s*-\s*pandas\s*-\s*/i.test(t)) {
    t = t.replace(/^python\s*-\s*pandas\s*-\s*/i, 'Pandas: ');
  } else if (/^python\s*-\s*django\s*-\s*/i.test(t)) {
    t = t.replace(/^python\s*-\s*django\s*-\s*/i, 'Django: ');
  } else if (/^python\s*-\s*lib\s*-\s*/i.test(t)) {
    t = t.replace(/^python\s*-\s*lib\s*-\s*/i, 'Python: ');
  } else if (/^python\s*-\s*basic\s*-\s*/i.test(t)) {
    t = t.replace(/^python\s*-\s*basic\s*-\s*/i, 'Python: ');
  } else if (/^networkx\s*-\s*centrality\s*-\s*/i.test(t)) {
    t = t.replace(/^networkx\s*-\s*centrality\s*-\s*/i, 'NetworkX Centrality: ');
  } else if (/^networkx\s*-\s*community\s*detection\s*-\s*/i.test(t)) {
    t = t.replace(/^networkx\s*-\s*community\s*detection\s*-\s*/i, 'NetworkX Community: ');
  } else if (/^networkx\s*-\s*link\s*prediction\s*-\s*/i.test(t)) {
    t = t.replace(/^networkx\s*-\s*link\s*prediction\s*-\s*/i, 'NetworkX Link Prediction: ');
  } else if (/^networkx\s*-\s*/i.test(t)) {
    t = t.replace(/^networkx\s*-\s*/i, 'NetworkX: ');
  } else if (/^java\s*-\s*thread\s*-\s*/i.test(t)) {
    t = t.replace(/^java\s*-\s*thread\s*-\s*/i, 'Java Thread: ');
  } else if (/^java\s*-\s*data\s*structure\s*-\s*/i.test(t)) {
    t = t.replace(/^java\s*-\s*data\s*structure\s*-\s*/i, 'Java 자료구조: ');
  } else if (/^java\s*-\s*/i.test(t)) {
    t = t.replace(/^java\s*-\s*/i, 'Java: ');
  } else if (/^python\s*-\s*/i.test(t)) {
    t = t.replace(/^python\s*-\s*/i, 'Python: ');
  } else if (/^algorithm\s*-\s*/i.test(t)) {
    t = t.replace(/^algorithm\s*-\s*/i, 'Algorithm: ');
  } else if (/^vim\s*-\s*/i.test(t)) {
    t = t.replace(/^vim\s*-\s*/i, 'Vim: ');
  } else if (/^c\s*-\s*/i.test(t)) {
    t = t.replace(/^c\s*-\s*/i, 'C: ');
  }

  // Replace hyphens between Korean words (e.g. 'python에서-excel을-읽읍시다' -> 'python에서 excel을 읽읍시다')
  t = t.replace(/([가-힣a-zA-Z0-9])-([가-힣])/g, '$1 $2');
  t = t.replace(/([가-힣])-([가-힣a-zA-Z0-9])/g, '$1 $2');

  // Strip duplicate double parentheses like 'arrayMaxConsecutiveSum(inputArray, k))'
  t = t.replace(/\)\)+$/, ')');

  // Capitalize first letter if it starts with lower-case english
  if (/^[a-z]/.test(t)) {
    t = t.charAt(0).toUpperCase() + t.slice(1);
  }

  return t.trim();
}
