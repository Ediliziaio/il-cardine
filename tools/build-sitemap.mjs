// Genera sitemap.xml dal filesystem.
// - Dominio canonico: https://www.ilcardine.it (coerente coi canonical del sito)
// - Include ogni /index.html indicizzabile; esclude pagine con robots noindex
//   (es. /cerca/) e la 404.
// - Priorita'/changefreq derivate dal tipo di pagina.
// - lastmod: data reale per pagina (vedi lastmodFor), mai "oggi" a tappeto.
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';

const ORIGIN = 'https://www.ilcardine.it';
const root = process.cwd();

// lastmod REALE per pagina. Mai "oggi" su tutte le URL: un lastmod che si
// sposta a ogni build e' fake freshness, Google impara a ignorare la sitemap
// e riduce la scansione. Fonte di verita', in ordine:
//   1) dateModified del JSON-LD (la data editoriale dichiarata nella pagina)
//   2) data dell'ultimo commit che ha toccato il file (contenuto vero)
function lastmodFor(file, html) {
  const m = html.match(/"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})/);
  if (m) return m[1];
  try {
    const out = execFileSync('git', ['log', '-1', '--format=%cs', '--', file], {
      encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    if (out) return out;
  } catch { /* file non tracciato o git assente */ }
  return new Date().toISOString().slice(0, 10);
}

// Scansione ricorsiva degli index.html
const DEV = new Set(['dist', 'node_modules', '.git', '.claude', 'build', 'tools', 'assets', 'css', 'js']);
const pages = [];
(function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (DEV.has(entry.name)) continue;
      walk(join(dir, entry.name));
    } else if (entry.name === 'index.html') {
      const rel = dir === root ? '' : dir.slice(root.length + 1).replaceAll('\\', '/') + '/';
      const file = join(dir, entry.name);
      const html = readFileSync(file, 'utf8');
      if (/<meta[^>]+noindex/i.test(html)) continue; // esclude /cerca/ ecc.
      pages.push({ rel, lastmod: lastmodFor(rel + 'index.html', html) });
    }
  }
})(root);

// Regole per tipo di pagina (riproducono le priorita' curate del sito)
const SERVICE = new Set(['chi-siamo/', 'contatti/', 'redazione/', 'pubblicita/', 'privacy/', 'cookie-policy/', 'sitemap/']);
const SILOS = new Set(['ristrutturazioni/', 'serramenti-infissi/', 'efficienza-energetica/', 'materiali-costruzione/', 'impianti/', 'incentivi-bonus/', 'tecnologie-innovazione/', 'normative/']);
const PILLARS = new Set(['efficienza-energetica/pannelli-solari-guida/']); // pillar principale
function rule(rel) {
  if (rel === '') return { priority: '1.0', changefreq: 'daily' };       // home
  if (PILLARS.has(rel)) return { priority: '1.0', changefreq: 'weekly' }; // pillar
  if (SERVICE.has(rel)) return { priority: '0.5', changefreq: 'monthly' };
  if (SILOS.has(rel)) return { priority: '0.9', changefreq: 'daily' };   // hub categoria
  return { priority: '0.8', changefreq: 'weekly' };                      // articolo
}

// Costruzione XML (ordine alfabetico stabile per loc)
const urls = pages
  .map(({ rel, lastmod }) => ({ loc: ORIGIN + '/' + rel, lastmod, ...rule(rel) }))
  .sort((a, b) => a.loc.localeCompare(b.loc));

const body = urls
  .map((u) => `  <url><loc>${u.loc}</loc><lastmod>${u.lastmod}</lastmod><changefreq>${u.changefreq}</changefreq><priority>${u.priority}</priority></url>`)
  .join('\n');

const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>\n`;
writeFileSync('sitemap.xml', xml);
const dates = [...new Set(urls.map((u) => u.lastmod))].sort();
console.log(`sitemap.xml rigenerata: ${urls.length} URL su ${ORIGIN} (lastmod reali: ${dates.join(', ')})`);
