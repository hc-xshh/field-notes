import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { sortByDate } from '../lib/posts';
import { MAIN_TOPIC } from '../lib/topics';

/**
 * The main line only: the section the newsletter also carries. The full feed of all
 * five sections stays at /rss.xml so that link keeps meaning what it always meant.
 */
export async function GET(context) {
  const posts = sortByDate(
    await getCollection('posts', ({ data }) => !data.draft && data.topic === MAIN_TOPIC.slug),
  );

  return rss({
    title: `Field Notes — ${MAIN_TOPIC.name}`,
    description: `The main line of Field Notes: ${MAIN_TOPIC.tagline} The other four sections are on the site and in the full feed.`,
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
