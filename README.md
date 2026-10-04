# [frhyme.code](https://frhyme.github.io)

> study, code, re-study — 개인 엔지니어링 지식 저장소

Astro 기반의 초고속 정적 기술 블로그입니다. (1,450여 개의 포스트와 실시간 정적 검색 지원)

---

## Tech Stack

- **Framework**: [Astro v7](https://astro.build/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Search Engine**: [Pagefind](https://pagefind.app/) (정적 풀텍스트 검색)
- **Code Highlighting**: [Shiki](https://shiki.matsu.io/)
- **Math & LaTeX**: [KaTeX](https://katex.org/) + `remark-math`
- **Comments**: [Disqus](https://disqus.com/)
- **Monetization & Analytics**: Google AdSense, Google Analytics 4 (GA4)
- **Deployment**: GitHub Pages (via GitHub Actions)

---

## Local Development

```bash
# 의존성 설치
npm install

# 로컬 개발 서버 실행 (http://localhost:4321)
npm run dev

# 프로덕션 빌드 & Pagefind 인덱싱
npm run build

# 빌드 결과물 미리보기
npm run preview
```
