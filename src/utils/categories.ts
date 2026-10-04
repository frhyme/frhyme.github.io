export type MajorCategory = 'tech' | 'english' | 'life';

export const ENGLISH_CATEGORIES = new Set([
  'english',
  'english_study_by_movie_script',
]);

export const LIFE_CATEGORIES = new Set([
  'baseball',
  'life',
  'moviediary',
  'trip',
  'trip_log',
  'tour',
  'game',
  'furniture',
  'essay',
  'trivia',
]);

export function getMajorCategory(category?: string): MajorCategory {
  const cat = (category || 'others').toLowerCase().trim();
  if (ENGLISH_CATEGORIES.has(cat)) return 'english';
  if (LIFE_CATEGORIES.has(cat)) return 'life';
  return 'tech';
}

export const MAJOR_CATEGORY_META: Record<
  MajorCategory,
  { label: string; icon: string; description: string; path: string }
> = {
  tech: {
    label: 'Tech',
    icon: '💻',
    description: 'Python, Java, AI/ML, Vim, Web, CS 이론 등 소프트웨어 개발 및 엔지니어링 기록',
    path: '/tech/',
  },
  english: {
    label: 'English',
    icon: '📚',
    description: '영화 대본(인턴, 어바웃타임 등)을 통해 정리한 실생활 영어 표현 및 단어 아카이브',
    path: '/english/',
  },
  life: {
    label: 'Life',
    icon: '☕',
    description: '야구(세이버메트릭스), 영화 리뷰, 여행, 게임, 일상 단상 등 라이프 아카이브',
    path: '/life/',
  },
};
