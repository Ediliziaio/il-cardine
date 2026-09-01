# IL CARDINE — Documento di progetto
**Testata editoriale verticale sull'edilizia** · Dominio canonico: `https://www.ilcardine.it/` · Stack: HTML statico + Vite · Data: 21 luglio 2026

---

## 1. Mappa del sito / architettura a silos

```
ilcardine.it/
├── index.html                        → Home (hub, H1 brand)
├── ristrutturazioni/                 → Silo 1 · 4 articoli
├── serramenti-infissi/               → Silo 2 · 4 articoli
├── efficienza-energetica/            → Silo 3 · 5 articoli (pillar + 4 cluster)
├── materiali-costruzione/            → Silo 4 · 4 articoli
├── impianti/                         → Silo 5 · 4 articoli
├── incentivi-bonus/                  → Silo 6 · 4 articoli
├── tecnologie-innovazione/           → Silo 7 · 4 articoli
├── normative/                        → Silo 8 · 4 articoli
├── chi-siamo/ · redazione/ · contatti/ · pubblicita/ · privacy/ · cookie-policy/
├── sitemap/                          → Sitemap HTML utenti
├── sitemap.xml · robots.txt · llms.txt · feed.xml
```

- **49 URL totali** in sitemap.xml, tutte con canonical assoluto, `lastmod`, priorità (home 1.0 · pillar 1.0 · categorie 0.9 · articoli 0.8 · servizio 0.5).
- URL parlanti brevi coerenti con la gerarchia: `/efficienza-energetica/pannelli-solari-guida/`.
- Ogni pagina è raggiungibile in ≤ 3 click dalla home (home → categoria → articolo; correlati e "più letti" accorciano a 2).

## 2. Layout home page (magazine "a giornale")

Topbar (data + link utili) → Masthead (logo, tagline, CTA newsletter) → Mainnav sticky (8 silos) → Ticker ultim'ora → **Leaderboard 728×90** → **Hero**: apertura (pillar pannelli solari, thumb 16:9) + 4 secondari → **Ultimi articoli**: griglia 6 card + sidebar (**Half page 300×600**, "I più letti", newsletter, **Rectangle 300×250**) → **In-feed ad** → **8 sezioni silo** (section-head H2 + 4 card ciascuna) → **Footer ad** → Footer scuro a 4 colonne (mappa completa sezioni).

- H1 unico (`sr-only`, brand); H2 sui blocchi; H3 sui titoli articolo. Above the fold senza immagini raster oltre al logo: LCP = testo/thumb CSS.

## 3. Template pagina articolo (33/33 conformi)

1. Head SEO: title ≤60 ch con keyword · meta description ≤155 ch · canonical · robots `max-image-preview:large` · OG + Twitter Card · JSON-LD `@graph` = **Article + BreadcrumbList + FAQPage** (FAQ identiche al markup visibile).
2. Breadcrumb visibile Home › Silo › Titolo.
3. Kicker, **un solo H1**, standfirst, byline con autore (link `/redazione/`), data pubblicazione + "Aggiornato il", minuti lettura (E-E-A-T).
4. **Answer-box "Risposta rapida"** (40-60 parole auto-conclusive) → AEO/AI Overviews.
5. **TOC cliccabile** con ancore su ogni H2 (id descrittivi) → sitelink + jump link.
6. Corpo: H2 a domanda reale, H3 ordinati, ≥1 tabella comparativa o lista numerata, frasi estraibili, link interni contestuali.
7. **2 slot 300×250 in-article** con spazio riservato (zero CLS) + sidebar 300×600 + "I più letti" + newsletter.
8. Box FAQ finale (5 domande, `<details>`), author-box, share-row testuale (zero script terzi), 3 articoli correlati, tag, fonti.

## 4. Specifiche tecniche SEO

| Area | Implementazione |
|---|---|
| Indicizzazione | sitemap.xml (49 URL) · robots.txt (Allow all, blocca solo /cerca) · canonical ovunque · feed RSS |
| Crawler AI (GEO) | robots.txt consente esplicitamente GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, Applebot-Extended, meta-externalagent · **llms.txt** con sintesi e link ai pillar |
| Structured data | Organization + WebSite (SearchAction) in home · CollectionPage + BreadcrumbList nelle categorie · Article + BreadcrumbList + FAQPage in ogni articolo |
| Tag | title/meta unici e in soglia (verificati a script) · 1 solo H1 per pagina (verificato) · gerarchia H2/H3 ordinata |
| Performance | 1 CSS (24 KB) + 1 JS defer (2,3 KB) · zero framework/librerie · zero immagini raster nei contenuti (thumb CSS con aspect-ratio → CLS ≈ 0) · font con preconnect + display=swap · slot ads a dimensioni riservate |
| Mobile | mobile-first, breakpoint 720/1080 px, menu hamburger, touch target ≥44 px, ad mobile 320×100 dedicato, nessun popup |

## 5. Piano editoriale (33 articoli ≥ 4.000 caratteri — misurati 8.700-16.000)

Keyword primaria per articolo: vedi `BUILD-SPEC.md` §Piano editoriale (tabella completa silo/slug/titolo/keyword/data). Autori redazione: Marco Ferreri (energia/tech), Giulia Santoro (fisco), Luca Bianchi (involucro), Elena Riva (materiali/mercato), Paolo Gatti (impianti), Sara Colombo (normative).

## 6. Strategia sitelink — cluster "Pannelli solari"

- **Pillar**: `/efficienza-energetica/pannelli-solari-guida/` (16.030 caratteri, TOC con 9 sezioni ancorabili: cosa-sono, come-funzionano, tipologie, costi, incentivi, installazione, manutenzione, conviene, FAQ → ogni sezione è un potenziale sitelink).
- **Cluster figli** (tutti linkano il pillar con anchor descrittive e sono linkati dal pillar): `fotovoltaico-costi-2026` · `fotovoltaico-incentivi-2026` · `pompe-di-calore-come-funzionano` · `cappotto-termico-esterno-guida`.
- URL/title/H2 distintivi per sotto-argomento + BreadcrumbList su ogni pagina → Google può proporre link indentati sotto il risultato del pillar.
- Stesso schema pillar→cluster replicato in scala minore negli altri 7 silos (hub di silo + fratelli interconnessi).

## 7. Spazi pubblicitari predisposti (AdSense/Ad Manager ready)

Leaderboard 728×90 (header/in-feed/footer) · Half page 300×600 e Rectangle 300×250 (sidebar) · 2× Rectangle in-article · Mobile 320×100. Tutti con etichetta "Pubblicità", dimensioni riservate in CSS (no CLS), markup `data-ad-slot` pronto per il riempimento. Media kit in `/pubblicita/`.

## 8. Aggiornamento 21 lug 2026 (sera) — immagini, ampliamento, extra

- **33 immagini hero reali** (AI, 1200×675 WebP <200 KB, alt descrittivi con keyword): hero `fetchpriority="high"` in ogni articolo, card home/categorie/correlati convertite a `<img loading="lazy">`; og:image/twitter:image/JSON-LD image aggiornati.
- **Tutti i 33 articoli ampliati**: minimo 13.900 caratteri (pillar 19.275); nuove sezioni "Errori da evitare", "Caso pratico" con numeri, "Checklist", FAQ extra (allineate al JSON-LD), dateModified 2026-07-21, wordCount reale.
- **Nuove funzionalità**: `/cerca/` (ricerca client-side noindex + `assets/search-index.json`), `news-sitemap.xml` (Google News, dichiarata in robots.txt), `404.html`, cookie banner leggero (localStorage, zero CLS, CSS/JS append), `manifest.webmanifest` + `theme-color` + icone 192/512 su tutte le pagine.
- `sitemap.xml` rigenerata con dateModified; script di build/manutenzione in `tools/`.

## Stato verifiche (21 lug 2026)

✅ 49 pagine · 0 link interni rotti · H1=1 ovunque · title ≤62 ch · meta ≤156 ch · articoli ≥13.900 ch · JSON-LD valido · FAQ visibili = FAQ JSON-LD · 33/33 immagini hero presenti e referenziate · smoke test dev server: 200 su home, articoli, categorie, ricerca, 404, sitemap, robots, llms, feed.
