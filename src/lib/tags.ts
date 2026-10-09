/**
 * Cross-cutting tags. A section answers "what kind of thing is this" (one post, one
 * section); a tag answers "what else is like this" across sections — the price posts,
 * the dataset posts, the posts where the whole job was cross-checking two sources.
 *
 * Keep the list short on purpose: a tag with one post behind it is a dead end for the
 * reader and a thin page for search. Add a tag when a third post needs it, not before.
 */
export type Tag = {
  slug: string;
  name: string;
  blurb: string;
};

export const TAGS: Tag[] = [
  {
    slug: 'sources-and-method',
    name: 'Sources and method',
    blurb:
      'Posts where the work is the cross-check: two customs records, two freight indices, two definitions of the same word — and what putting them side by side showed.',
  },
  {
    slug: 'prices',
    name: 'Prices',
    blurb:
      'What things cost and to whom: model prices per task, groceries by channel, a monthly city budget, container rates by route.',
  },
  {
    slug: 'open-data',
    name: 'Open data',
    blurb:
      'Built on datasets anyone can pull: customs records, parcel counts, urbanisation, platform hot lists, model releases.',
  },
  {
    slug: 'ai-evaluation',
    name: 'AI evaluation',
    blurb:
      'How AI work gets measured: building an eval set and watching it rot, error rates in support bots, cost per task rather than per token.',
  },
  {
    slug: 'trade-and-logistics',
    name: 'Trade and logistics',
    blurb:
      'Goods on the move: who pays under each Incoterm, what a factory quote leaves out, what a container costs, how live-commerce money settles.',
  },
  {
    slug: 'everyday-china',
    name: 'Everyday China',
    blurb:
      'The habits and costs of daily life here, sorted into what has been measured and what is only habit.',
  },
  {
    slug: 'rails-and-infrastructure',
    name: 'Rails and infrastructure',
    blurb:
      'The plumbing behind the behaviour — payments, parcels, platforms — and why the defaults look different here.',
  },
  {
    slug: 'reference-pages',
    name: 'Reference pages',
    blurb: 'Short pages meant to be kept: tables, indices and checklists you come back to.',
  },
  {
    slug: 'site-notes',
    name: 'Site notes',
    blurb: 'How this site is made, what it ships, and what it refuses to do.',
  },
];

export const TAG_SLUGS = TAGS.map((tag) => tag.slug);

export function getTag(slug: string): Tag | undefined {
  return TAGS.find((tag) => tag.slug === slug);
}

export function tagName(slug: string): string {
  return getTag(slug)?.name ?? slug;
}
