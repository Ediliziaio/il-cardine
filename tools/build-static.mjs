// Build statico: Il Cardine è un sito multipagina già pre-renderizzato.
// `vite build` includerebbe solo la index.html di root, perdendo le altre 50
// pagine e i file di root (robots/sitemap/llms/feed/404). Questo script copia
// l'intero sito in dist/ escludendo solo i file di sviluppo, così dist/ è un
// artefatto deployabile completo (Vercel/Cloudflare/OVH) e `vite preview` lo
// serve integralmente.
import { cpSync, rmSync, mkdirSync, readdirSync } from 'node:fs';
import { resolve, relative, sep } from 'node:path';

const root = process.cwd();
const out = resolve(root, 'dist');

// Cartelle/file di sviluppo da NON pubblicare
const EXCLUDE_TOP = new Set([
  'dist', 'node_modules', '.git', '.claude', 'tools', 'build',
  'build_articles.py', 'package.json', 'package-lock.json',
  'BUILD-SPEC.md', 'DOCUMENTO-PROGETTO.md', '.gitignore', '.DS_Store',
  'vercel.json',
]);

rmSync(out, { recursive: true, force: true });
mkdirSync(out);

// Copia voce-per-voce: Node vieta cpSync(root → root/dist). Iteriamo sui
// top-level e copiamo solo quelli pubblicabili.
for (const entry of readdirSync(root)) {
  if (EXCLUDE_TOP.has(entry)) continue;
  cpSync(resolve(root, entry), resolve(out, entry), {
    recursive: true,
    filter(src) {
      const rel = relative(root, src);
      if (rel.includes('__pycache__')) return false;
      if (rel.endsWith('.py') || rel.endsWith('.md')) return false;
      return true;
    },
  });
}

const count = (dir) => {
  let n = 0;
  for (const e of readdirSync(dir, { recursive: true })) {
    if (String(e).endsWith('.html')) n++;
  }
  return n;
};
console.log(`Static build completata → dist/ (${count(out)} pagine HTML)`);
