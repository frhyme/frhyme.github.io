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
