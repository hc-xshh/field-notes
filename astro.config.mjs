import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import rehypeSlug from 'rehype-slug';

// Site URL is the temporary Cloudflare Pages subdomain.
// Swap it for the real domain when one is bought.

// Wrap every markdown table in a horizontally scrollable container.
// Without this, a wide table (5-6 columns of numbers) pushes the whole page
// sideways on a phone: the table cannot shrink below its min-content width,
// so the document ends up wider than the viewport.
function rehypeTableWrap() {
  return (tree) => {
    const walk = (node) => {
      if (!node || !Array.isArray(node.children)) return;
      node.children = node.children.map((child) => {
        if (child && child.type === 'element' && child.tagName === 'table') {
          return {
            type: 'element',
            tagName: 'div',
            properties: { className: ['table-wrap'] },
            children: [child],
          };
        }
        walk(child);
        return child;
      });
    };
    walk(tree);
  };
}

export default defineConfig({
  site: 'https://field-notes-6cd.pages.dev',
  build: { format: 'directory' },
  // rehype-slug gives every heading an id derived the same way Astro derives
  // the slugs it reports in render()'s `headings`, so the table of contents
  // links to anchors that actually exist. Writing our own slugger is how those
  // links silently rot.
  markdown: { rehypePlugins: [rehypeTableWrap, rehypeSlug] },
  integrations: [sitemap()],
});
