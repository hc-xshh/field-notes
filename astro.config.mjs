import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Site URL is the temporary Cloudflare Pages subdomain.
// Swap it for the real domain when one is bought.
export default defineConfig({
  site: 'https://field-notes-6cd.pages.dev',
  build: { format: 'directory' },
  integrations: [sitemap()],
});
