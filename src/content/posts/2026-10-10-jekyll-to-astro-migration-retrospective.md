---
title: "1,400개 포스트의 기술 블로그를 Jekyll에서 Astro 5로 마이그레이션한 여정"
date: 2026-10-10
category: "tech"
tags: ["astro", "jekyll", "web", "search", "pagefind", "d3", "migration"]
permalink: "/tech/jekyll-to-astro-migration-retrospective/"
description: "1,400개 이상의 마크다운 포스트가 쌓이며 빌드 지옥에 빠졌던 기술 블로그를 Astro 5, Pagefind 오프라인 검색, D3.js 지식 그래프로 전면 리빌딩한 실전 마이그레이션 여정과 성능 최적화 회고록입니다."
---

## 1. 프롤로그: 1,400개의 마크다운 문서, 그리고 멈춰버린 Jekyll

2017년부터 개발 공부와 실무 과정에서 마주친 트러블슈팅, 알고리즘, 인공지능, 시스템 아키텍처 기록을 블로그에 남겨왔습니다. 몇 편 안 되던 글은 시간이 흘러 어느덧 **1,420여 편의 마크다운(`.md`) 문서**로 불어났습니다.

하지만 아카이브가 거대해질수록, 기존에 사용하던 **Jekyll(Ruby 기반 정적 사이트 생성기)** 환경은 한계에 봉착했습니다.

```log
[Legacy Jekyll Build Log]
Configuration file: /Users/frhyme/frhyme.github.io/_config.yml
Source:            /Users/frhyme/frhyme.github.io
Destination:       /Users/frhyme/frhyme.github.io/_site
Incremental build: disabled. Enable with --incremental
Generating... 
  Rendering Feed: 1420 posts...
  Rendering Liquid Tags...
  Liquid Exception: Memory limit exceeded in tags/category.html
  ...
done in 218.423 seconds. (3분 38초 소요)
```

### 마주했던 치명적인 병목 현상들

1. **빌드 속도의 지옥 (수 분 단위의 대기 시간):**  
   오타 하나를 수정하고 `bundle exec jekyll serve`로 프리뷰를 확인하려면 아무리 증분 빌드(Incremental build)를 켜도 최소 30초, 전체 빌드는 **3분 30초에서 4분**이 걸렸습니다. 글을 쓰는 리듬이 완전히 깨지는 수준이었습니다.
2. **검색 기능의 붕괴 (클라이언트 브라우저 크래시):**  
   서버리스 정적 호스팅(GitHub Pages) 특성상 외부 유료 검색 API(Algolia 등)를 쓰지 않으려면 모든 글의 메타데이터를 담은 거대한 `search.json`을 브라우저로 내려받아 Lunr.js 등으로 검색해야 했습니다. 1,400개 글의 인덱스 파일은 압축해도 4~5MB에 달했고, 모바일 브라우저에서는 검색창을 누르는 순간 탭이 멈추거나 튕기는 현상이 발생했습니다.
3. **Ruby Liquid 템플릿의 확장 한계:**  
   현대적인 인터랙션(태그 네트워크 지식 그래프, 시리즈별 진행률 네비게이터, 다크 모드 토글 등)을 도입하려 해도 Liquid 템플릿 엔진 특유의 빈약한 컴포넌트 추상화와 느린 파싱 속도 때문에 유지보수가 불가능에 가까웠습니다.

> **"블로그를 다시 살려내자. 1,400개의 기존 URL(퍼머링크)과 SEO 점수를 100% 보존하면서, 5초 이내에 빌드되고 0.01초 만에 전체 글을 검색할 수 있는 모던 아키텍처로 전면 마이그레이션하자."**

---

## 2. 정적 프레임워크 3파전: 왜 Astro 5였는가?

기술 스택을 전환하기 위해 2026년 기준 정적 사이트 생성 생태계의 대표 후보 3가지를 벤치마크했습니다.

| 비교 항목 | Next.js 15 (App Router) | Hugo (v0.140+) | Astro 5 (Content Layer) |
| :--- | :--- | :--- | :--- |
| **렌더링 엔진** | React SSR / SSG | Go HTML Template | Islands Architecture (HTML 우선) |
| **클라이언트 JS** | React 런타임 기본 번들 (수십 KB) | 0KB (순수 정적) | **0KB (필요한 섬만 온디맨드 로드)** |
| **1,400+ 빌드 속도** | 1분 30초 이상 (메모리 부담) | **0.8초** (압도적 속도) | **4~5초** (Vite + 병렬 처리) |
| **모던 컴포넌트 확장성**| 최고 (React 생태계) | 낮음 (Go 템플릿 문법 한계) | **최고 (React, Svelte, Preact 등 혼용 가능)** |
| **콘텐츠 검증/파이프라인**| `contentlayer` (유지보수 불안정) | Go struct 파싱 | **Astro Content Layer + Zod 표준 내장** |

- **Next.js 탈락 이유:** 3,000개가 넘는 페이지(포스트, 카테고리, 태그, 페이지네이션)를 SSG로 사전 렌더링할 때 React의 가상 돔 생성 및 번들링 오버헤드로 인해 빌드 시간이 지나치게 길어졌습니다. 또한 단순 블로그 글을 읽는데 불필요한 React 하이드레이션(Hydration) 자바스크립트를 다운로드해야 한다는 점이 불필요한 낭비였습니다.
- **Hugo 탈락 이유:** 빌드 속도는 세상에서 가장 빨랐지만, Go 템플릿 언어는 복잡한 UI 인터랙션(D3.js 지식 그래프 시각화, 인터랙티브 시리즈 맵)을 컴포넌트 단위로 격리하고 관리하기에 DX(개발자 경험)가 너무 열악했습니다.
- **Astro 5 선정 이유:**
  1. **Zero-JS by Default:** 기본적으로 완성된 순수 HTML과 CSS만 서빙하므로 초기 로딩 속도와 코어 웹 바이탈(Lighthouse 100점)이 보장됩니다.
  2. **Islands Architecture:** 검색창이나 지식 그래프처럼 자바스크립트가 필요한 컴포넌트만 `client:idle` 또는 `client:visible` 디렉티브로 선별적 로딩할 수 있습니다.
  3. **Content Layer & Vite:** Astro 5에 도입된 차세대 Content Layer API는 수천 개의 마크다운 문서를 메모리 캐싱 및 병렬 파싱하여 초고속으로 처리합니다.

---

## 3. 도전 1: 레거시 마크다운 1,400개 정규화와 URL 영속성

기존 Jekyll 블로그의 가장 큰 자산은 구글과 네이버 검색 엔진에 이미 색인되어 유입되고 있는 **수천 개의 기존 URL(Permalink)**이었습니다. 프레임워크가 바뀌었다고 URL 구조가 바뀌어 404가 뜨는 순간, 지난 8년간 쌓아온 오가닉 트래픽은 소멸합니다.

### 1) 퍼머링크 1:1 보존 및 하위 호환 라우팅

Astro 5의 `[...slug].astro` 동적 라우트에서 기존 Jekyll의 커스텀 퍼머링크 규칙을 완벽하게 재현했습니다.

```typescript
// src/pages/[...slug].astro (핵심 라우팅 로직)
export async function getStaticPaths() {
  const posts = await getCollection('posts');

  return posts.map((post) => {
    let routeSlug: string;
    
    // 1. 글에 직접 지정된 레거시 permalink가 있다면 최우선 적용 (/git/git18_garbage_collection/ 등)
    if (post.data.permalink) {
      routeSlug = post.data.permalink.replace(/^\/+|\/+$/g, '');
    } else {
      // 2. permalink가 없다면 파일명(YYYY-MM-DD-slug.md)에서 날짜를 파싱하여 카테고리/슬러그 매핑
      const filename = post.id.replace(/\.md$/, '');
      const slugMatch = filename.match(/^(\d{4}-\d{2}-\d{2})-(.*)$/);
      const postSlug = slugMatch ? slugMatch[2] : filename;
      const cat = (post.data.category || 'others').toLowerCase().replace(/\s+/g, '-');
      routeSlug = `${cat}/${postSlug}`;
    }

    return {
      params: { slug: routeSlug },
      props: { post },
    };
  });
}
```

### 2) Content Schema와 Zod 타입 안전성 확보

수년간 다양한 에디터에서 작성되며 프론트매터의 날짜 형식(`YYYY-MM-DD`, `YYYY-MM-DD HH:mm:ss`), 태그 포맷(`tags: [a, b]` vs `tags: a, b`), 카테고리 누락 등이 뒤섞여 있었습니다. Astro 5의 `defineCollection`을 통해 엄격한 스키마 변환 규칙을 부여했습니다.

```typescript
// src/content.config.ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string().default('Untitled'),
    date: z.coerce.date().default(() => new Date()),
    category: z.string().default('others'),
    tags: z.array(z.string()).default([]),
    permalink: z.string().optional(),
    description: z.string().optional(),
  }),
});

export const collections = { posts };
```

---

## 4. 도전 2: 서버 없는 1,400개 포스트 초고속 검색 (Pagefind)

서버(DB)를 두지 않는 정적 호스팅 환경에서 1,400편의 장문 아티클을 어떻게 0.01초 만에 검색할 수 있을까요? 해답은 Rust로 작성된 정적 검색 라이브러리 **Pagefind**였습니다.

```
[Pagefind 아키텍처 다이어그램]

  [Astro 5 Build Output (HTML)]
               │
               ▼  (Pagefind CLI: 1.8초 소요)
  ┌────────────────────────────────────────────────────────┐
  │  정적 인덱스 청크 생성 (WASM 바이너리 + 분할 인덱스)     │
  │  - dist/_pagefind/pagefind.js (15KB)                   │
  │  - dist/_pagefind/wasm.ko.pagefind (압축 WASM)         │
  │  - dist/_pagefind/fragment_*.pf_fragment (온디맨드 분할)│
  └────────────────────────────────────────────────────────┘
               │
               ▼  (브라우저 검색 요청 시)
  [클라이언트]: 필요한 단어 청크만 브라우저가 온디맨드 Fetch 
               ➜ WASM 인메모리 고속 검색 
               ➜ 0.01초 만에 하이라이트 결과 렌더링!
```

### Pagefind 도입 결과

1. **색인 빌드 시간:** 1,420여 개 전체 페이지의 본문을 파싱하고 역색인(Inverted Index)을 만드는 데 **단 1.8초**밖에 걸리지 않았습니다.
2. **네트워크 대역폭 절약:** 4~5MB의 단일 JSON을 내려받는 대신, 사용자가 검색한 키워드가 속한 10~20KB의 파편(Fragment) 파일만 레이지 로딩합니다.
3. **CJK (한국어) 지원:** 한글 형태소와 단어 토큰을 정확히 파싱하여 한글 기술 용어(`가비지 컬렉션`, `동적 계획법`, `도커 컴포즈`)도 누락 없이 즉각 탐색됩니다.

---

## 5. 도전 3: D3.js 기반 태그 동시 출현(Co-occurrence) 지식 그래프

단순한 목록형 카테고리와 태그 클라우드는 1,400개의 방대한 지식 체계를 조망하기에 역부족이었습니다. 각 글에 붙은 태그들이 서로 어떻게 얽혀있는지를 보여주는 **인터랙티브 지식 그래프(Knowledge Graph)**를 직접 구현했습니다.

### 1) 동시 출현(Co-occurrence) 네트워크 알고리즘

두 태그 $A$와 $B$가 같은 마크다운 문서에 동시에 태깅된 횟수를 엣지(Edge)의 가중치로 계산했습니다.

```typescript
// 태그 동시 출현 가중치 계산
const edgeMap = new Map<string, number>();

posts.forEach((post) => {
  const tags = post.data.tags;
  for (let i = 0; i < tags.length; i++) {
    for (let j = i + 1; j < tags.length; j++) {
      const [source, target] = [tags[i], tags[j]].sort();
      const key = `${source}---${target}`;
      edgeMap.set(key, (edgeMap.get(key) || 0) + 1);
    }
  }
});
```

### 2) D3 Force Simulation & 미니멀 UI

계산된 노드(태그)와 링크(동시 등장 빈도) 데이터를 D3의 `forceSimulation` 물리 엔진에 전달하여, 연관성이 높은 기술(예: `python` - `pandas` - `numpy` - `networkx`)들이 자연스럽게 성단(Cluster)을 이루도록 시각화했습니다.

- 다크 모드에 최적화된 Linear/Vercel 스타일의 미니멀 단색 팔레트 적용
- 특정 노드에 마우스를 올리면 연결된 지식 경로만 하이라이트되고 연결되지 않은 노드는 부드럽게 감쇠(Dimming)
- 노드 클릭 시 해당 태그의 전용 아카이브 페이지로 즉시 이동

---

## 6. 도전 4: 학습 트랙을 이어주는 지식 허브 & 시리즈 큐레이션

블로그에 방문한 독자가 하나의 에러 해결 글만 보고 이탈하는 것을 막기 위해, 연관 콘텐츠를 체계적으로 안내하는 구조를 신설했습니다.

1. **시리즈 커리큘럼 (`/series/[id]/`):**  
   파이썬 알고리즘, NetworkX 그래프 이론, 모던 자바, 시스템 아키텍처 등 다회차로 연재된 글들을 1편부터 완독할 수 있는 전용 실러버스(Syllabus) 페이지와 이전/다음 글 네비게이터를 구현했습니다.
2. **역색인(Inverted Index) 기반 연관 글 추천:**  
   전체 글 순회 방식($O(N^2)$) 대신 빌드 타임에 태그/카테고리 역색인을 생성하여, $O(1)$에 가까운 속도로 자카드 유사도(Jaccard Similarity)를 계산하고 시리즈 소속 글에는 가중치(+5점)를 부여해 최적의 추천 아티클을 매칭합니다.
3. **구조화 데이터(JSON-LD):**  
   Google 검색 결과에서 사이트 계층 구조가 깔끔하게 노출되도록 모든 글에 `BreadcrumbList`와 `TechArticle` 스키마 마크업을 자동 주입했습니다.

---

## 7. 마이그레이션 성과 및 지표 요약

| 지표 | 이전 (Jekyll) | 마이그레이션 후 (Astro 5) | 개선율 |
| :--- | :--- | :--- | :--- |
| **전체 정적 빌드 시간** | 218초 (3분 38초) | **5.1초** (3,122개 HTML 생성) | **43배 (4,270%) 단축** |
| **로컬 HMR (수정 반영)** | 35~50초 | **0.12초 (120ms)** | **즉시 반영 (체감 300배)** |
| **전체 글 검색 속도** | 1.8초 이상 (메모리 렉) | **0.01초 (WASM 인메모리)** | **180배 단축** |
| **Lighthouse Performance** | 72점 (수 MB JS 부하) | **100점 만점 (Zero-JS)** | 완벽 최적화 |
| **구글 색인 보존율** | - | **100% (404 오류 0건)** | 유기적 트래픽 유지 |

---

## 8. 에필로그: 10년을 지속 가능한 지식 저장소를 향해

정적 블로그 마이그레이션은 단순히 최신 프레임워크를 경험해보는 토이 프로젝트가 아니었습니다. **지난 8년간 쌓아온 1,400여 개의 소중한 기록들을 어떻게 하면 다음 10년 동안 가치 있고 빠르게 서빙할 수 있을까?**에 대한 진지한 엔지니어링 과제였습니다.

Astro 5의 Islands Architecture, Pagefind의 WebAssembly 검색, 그리고 D3.js 기반의 지식 시각화가 결합되면서, 이 블로그는 단순한 텍스트 저장소를 넘어 유기적으로 연결된 **개인 지식 베이스(Personal Knowledge Base)**로 다시 태어났습니다.

대규모 마크다운 아카이브의 빌드 속도나 검색 성능 문제로 고민하고 계신 엔지니어 분들께 Astro 5와 Pagefind 조합을 강력히 추천합니다.
