// Build statico: Il Cardine è un sito multipagina già pre-renderizzato.
// `vite build` includerebbe solo la index.html di root, perdendo le altre 50
// pagine e i file di root (robots/sitemap/llms/feed/404). Questo script copia
// l'intero sito in dist/ escludendo solo i file di sviluppo, così dist/ è un
// artefatto deployabile completo (Vercel/Cloudflare/OVH) e `vite preview` lo
// serve integralmente.
import { cpSync, rmSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve, relative, join } from 'node:path';

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

// Svuota il placeholder della data in topbar (data-tb-date).
// NON timbriamo la data del build: cambierebbe il contenuto di tutte le pagine
// a ogni deploy (churn) senza che il contenuto reale cambi, e Google impara a
// ignorare la freschezza dichiarata dal sito. L'HTML resta identico tra build;
// la data la scrive main.js lato client, sempre corretta.
const tbRe = /(<[^>]*data-tb-date[^>]*>)[^<]*(<\/)/;

const htmlFiles = readdirSync(out, { recursive: true })
  .map(String)
  .filter((e) => e.endsWith('.html'));
let cleaned = 0;
for (const rel of htmlFiles) {
  const p = join(out, rel);
  const html = readFileSync(p, 'utf8');
  if (tbRe.test(html)) {
    writeFileSync(p, html.replace(tbRe, '$1$2'));
    cleaned++;
  }
}

console.log(`Static build completata → dist/ (${htmlFiles.length} pagine HTML, topbar stabile su ${cleaned})`);
