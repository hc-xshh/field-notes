import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import { TOPIC_SLUGS } from './lib/topics';
import { TAG_SLUGS } from './lib/tags';

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
    // Cross-section keywords; the list lives in src/lib/tags.ts. Enum, not free
    // text, so a typo fails the build instead of quietly creating a dead tag page.
    tags: z.array(z.enum(TAG_SLUGS as [string, ...string[]])).default([]),
    // A living page: the numbers move, so the page is re-checked on a cadence.
    // `data_checked` is when the figures were last read from the source, which is
    // what the page shows the reader; `updated` stays for ordinary edits.
    refresh: z.enum(['weekly', 'monthly', 'quarterly', 'annual', 'on-change']).optional(),
    data_checked: z.coerce.date().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };
