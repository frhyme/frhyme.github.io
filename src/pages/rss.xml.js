import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('posts');
  const sortedPosts = posts
    .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
    .slice(0, 50);

  return rss({
    title: 'frhyme.code',
    description: 'study, code, re-study - 개발 지식 저장소',
    site: context.site,
    items: sortedPosts.map((post) => {
      let link = post.data.permalink;
      if (!link) {
        const filename = post.id.replace(/\.md$/, '');
        const slugMatch = filename.match(/^(\d{4}-\d{2}-\d{2})-(.*)$/);
        const postSlug = slugMatch ? slugMatch[2] : filename;
        const category = (post.data.category || 'others').toLowerCase().replace(/\s+/g, '-');
        link = `/${category}/${postSlug}/`;
      }

      return {
        title: post.data.title,
        pubDate: post.data.date,
        description: post.data.description || post.data.title,
        link,
      };
    }),
    customData: `<language>ko</language>`,
  });
}
