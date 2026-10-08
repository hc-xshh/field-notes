import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { sortByDate } from '../lib/posts';

export async function GET(context) {
  const posts = sortByDate(await getCollection('posts', ({ data }) => !data.draft));

  return rss({
    title: 'Field Notes',
    description:
      'Notes on building, testing and shipping AI tooling — written from China, for a global audience.',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.date,
      link: `/posts/${post.id}/`,
    })),
    customData: '<language>en</language>',
  });
}
