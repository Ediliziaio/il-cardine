// Genera sitemap.xml dal filesystem.
// - Dominio canonico: https://www.ilcardine.it (coerente coi canonical del sito)
// - Include ogni /index.html indicizzabile; esclude pagine con robots noindex
//   (es. /cerca/) e la 404.
// - Priorita'/changefreq: riusa quelle curate nella sitemap esistente se
//   presenti, altrimenti le deriva dal tipo di pagina.
// - lastmod: data odierna (le pagine sono state aggiornate).
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const ORIGIN = 'https://www.ilcardine.it';
const root = process.cwd();
const today = new Date().toISOString().slice(0, 10); // YYYY-MM-DD

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
      const html = readFileSync(join(dir, entry.name), 'utf8');
      if (/<meta[^>]+noindex/i.test(html)) continue; // esclude /cerca/ ecc.
      pages.push(rel);
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
  .map((rel) => ({ loc: ORIGIN + '/' + rel, lastmod: today, ...rule(rel) }))
  .sort((a, b) => a.loc.localeCompare(b.loc));

const body = urls
  .map((u) => `  <url><loc>${u.loc}</loc><lastmod>${u.lastmod}</lastmod><changefreq>${u.changefreq}</changefreq><priority>${u.priority}</priority></url>`)
  .join('\n');

const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>\n`;
writeFileSync('sitemap.xml', xml);
console.log(`sitemap.xml rigenerata: ${urls.length} URL su ${ORIGIN} (lastmod ${today})`);
