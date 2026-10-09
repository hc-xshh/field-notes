import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import { TOPIC_SLUGS } from './lib/topics';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    lang: z.enum(['en', 'zh']).default('en'),
    // Which section the post belongs to; the list lives in src/lib/topics.ts.
    topic: z.enum(TOPIC_SLUGS as [string, ...string[]]).default('ai-and-engineering'),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };
