import { defineConfig } from 'astro/config';

// Site URL is the temporary Cloudflare Pages subdomain.
// Swap it for the real domain when one is bought.
export default defineConfig({
  site: 'https://field-notes.pages.dev',
  build: { format: 'directory' },
});
