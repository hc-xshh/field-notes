/**
 * The five sections of the site. One post belongs to exactly one section, and the
 * section is what the reader picks when they decide whether to come back: the feed
 * and the newsletter are split along the same line.
 *
 * `main` marks the line the newsletter carries. Everything is on the site; only the
 * main line is pushed by email, because a reader who signed up for AI tooling notes
 * should not be surprised by a freight-rate chart.
 */
export type TopicSlug =
  | 'ai-and-engineering'
  | 'supply-chain'
  | 'life-in-china'
  | 'data-and-the-world'
  | 'chinese-abroad';

export type Topic = {
  slug: TopicSlug;
  name: string;
  lang: 'en' | 'zh';
  tagline: string;
  main?: boolean;
};

export const TOPICS: Topic[] = [
  {
    slug: 'ai-and-engineering',
    name: 'AI and engineering',
    lang: 'en',
    main: true,
    tagline:
      'Evaluations, task books and pipelines — plus the numbers worth keeping, from model prices to page weight.',
  },
  {
    slug: 'supply-chain',
    name: 'Supply chain',
    lang: 'en',
    tagline: 'What things cost to make and move: factory quotes, sourcing, freight rates, month by month.',
  },
  {
    slug: 'life-in-china',
    name: 'Life in China',
    lang: 'en',
    tagline: 'Everyday life here, sorted into what has been measured and what is only habit.',
  },
  {
    slug: 'data-and-the-world',
    name: 'Data and the world',
    lang: 'en',
    tagline: 'Open datasets, charted — global flows, and what they look like up close in one place.',
  },
  {
    slug: 'chinese-abroad',
    name: '海外华人',
    lang: 'zh',
    tagline: '中文栏目：生活成本、跨境比价、出入境流程，按年更新。',
  },
];

export const MAIN_TOPIC = TOPICS.find((topic) => topic.main) as Topic;

export const TOPIC_SLUGS = TOPICS.map((topic) => topic.slug);

export function getTopic(slug: string): Topic | undefined {
  return TOPICS.find((topic) => topic.slug === slug);
}

/** Section label for a slug, falling back to the slug itself if it ever drifts. */
export function topicName(slug: string): string {
  return getTopic(slug)?.name ?? slug;
}
