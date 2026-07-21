# IL CARDINE — Specifica di build condivisa (contratto per tutti gli agenti)

Dominio canonico: `https://www.ilcardine.it/` — lingua `it-IT`.
Root progetto: `/Users/agenteai/Documents/kimi/workspace/il-cardine/`
Stack: sito statico HTML + Vite (dev server). CSS unico: `css/style.css`. JS unico defer: `js/main.js`.
Logo header: `assets/logo.png` (634×128, navy+arancio). Logo footer (su sfondo scuro): `assets/logo-white.png`. Favicon: `assets/favicon.svg`.

## Palette brand (da logo)
- Navy primario: `#16324f` (testi titoli, header, footer bg)
- Arancio accento: `#e8702a` (kicker, link hover, bottoni, label)
- Sfondo pagina: `#ffffff` / `#f6f7f9` sezioni; testo body `#1f2733`; grigio meta `#6b7686`; bordi `#e3e7ee`
- Font: Playfair Display (700/800) per testata e titoli; Source Sans 3 (400/600/700) per body. Google Fonts con preconnect + display=swap.

## Struttura URL (silos) — directory con index.html
- Home: `index.html`
- Categorie: `/<silo>/index.html`
- Articoli: `/<silo>/<slug>/index.html`
- Servizio: `chi-siamo/index.html`, `redazione/index.html`, `contatti/index.html`, `pubblicita/index.html`, `privacy/index.html`, `cookie-policy/index.html`, `sitemap/index.html` (sitemap HTML)
- File root: `robots.txt`, `sitemap.xml`, `llms.txt`, `feed.xml`

Nei link interni usare percorsi assoluti da root (`/efficienza-energetica/pannelli-solari-guida/`) così breadcrumb e canonical restano coerenti. I riferimenti a css/js/asset da pagine annidate usano percorsi assoluti (`/css/style.css`).

## Gli 8 silos
1. `ristrutturazioni/` — Ristrutturazioni
2. `serramenti-infissi/` — Serramenti e Infissi
3. `efficienza-energetica/` — Efficienza Energetica
4. `materiali-costruzione/` — Materiali da Costruzione
5. `impianti/` — Impianti
6. `incentivi-bonus/` — Incentivi e Bonus
7. `tecnologie-innovazione/` — Tecnologie e Innovazione
8. `normative/` — Normative

## Piano editoriale — 33 articoli (silo/slug · titolo H1 · keyword primaria · data)
### efficienza-energetica (5)
- `pannelli-solari-guida` · PILLAR "Pannelli solari: la guida definitiva 2026 — costi, incentivi e installazione" · pannelli solari · 21 lug 2026
- `fotovoltaico-costi-2026` · "Quanto costa un impianto fotovoltaico nel 2026: prezzi al kWp e tempi di rientro" · costo impianto fotovoltaico · 18 lug 2026
- `fotovoltaico-incentivi-2026` · "Incentivi fotovoltaico 2026: detrazione 50%, comunità energetiche e ritiro dedicato" · incentivi fotovoltaico 2026 · 15 lug 2026
- `pompe-di-calore-come-funzionano` · "Pompa di calore: come funziona, consumi reali e quando conviene" · pompa di calore come funziona · 10 lug 2026
- `cappotto-termico-esterno-guida` · "Cappotto termico esterno: materiali, costi al mq e detrazioni 2026" · cappotto termico · 6 lug 2026

### ristrutturazioni (4)
- `costo-ristrutturazione-al-mq-2026` · "Costo ristrutturazione al mq nel 2026: prezzi voce per voce" · costo ristrutturazione al mq · 19 lug 2026
- `ristrutturazione-chiavi-in-mano` · "Ristrutturazione chiavi in mano: come funziona, costi e garanzie" · ristrutturazione chiavi in mano · 12 lug 2026
- `ristrutturare-bagno-costi-tempi` · "Ristrutturare il bagno nel 2026: costi, tempi e errori da evitare" · costo ristrutturazione bagno · 8 lug 2026
- `ristrutturare-casa-permessi-cila-scia` · "Ristrutturare casa: quali permessi servono tra CILA, SCIA e titolo edilizio" · permessi ristrutturazione casa · 2 lug 2026

### serramenti-infissi (4)
- `serramenti-pvc-alluminio-legno-confronto` · "Serramenti in PVC, alluminio o legno: il confronto completo 2026" · serramenti pvc o alluminio · 17 lug 2026
- `finestre-triplo-vetro-conviene` · "Triplo vetro: quando conviene davvero e quanto costa in più" · triplo vetro finestre · 11 lug 2026
- `prezzi-infissi-al-mq-2026` · "Prezzi infissi al mq nel 2026: PVC, alluminio e legno a confronto" · prezzi infissi al mq · 5 lug 2026
- `top-5-produttori-serramenti-italia` · "I 5 migliori produttori di serramenti in Italia: qualità e prezzi" · migliori produttori serramenti · 28 giu 2026

### materiali-costruzione (4)
- `materiali-isolanti-confronto` · "Materiali isolanti a confronto: EPS, lana di roccia, sughero e fibra di legno" · materiali isolanti termici · 16 lug 2026
- `edilizia-legno-xlam` · "Case in legno XLAM: costi, tempi di cantiere e prestazioni antisismiche" · case in legno xlam · 9 lug 2026
- `calcestruzzo-tipologie-usi` · "Tipi di calcestruzzo: classi di resistenza, usi e prezzi al metro cubo" · tipi di calcestruzzo · 1 lug 2026
- `laterizi-blocchi-termici-guida` · "Blocchi in laterizio termici: guida a murature portanti e tramezzi" · blocchi termici laterizio · 25 giu 2026

### impianti (4)
- `riscaldamento-a-pavimento-guida` · "Riscaldamento a pavimento: pro, contro, costi e consumi reali" · riscaldamento a pavimento · 14 lug 2026
- `vmc-ventilazione-meccanica-controllata` · "VMC: cos'è, come funziona e perché installarla in ristrutturazione" · ventilazione meccanica controllata · 7 lug 2026
- `rifacimento-impianto-idraulico-costi` · "Rifacimento impianto idraulico: costi, materiali e tempi di cantiere" · costo rifacimento impianto idraulico · 30 giu 2026
- `domotica-casa-impianti-guida` · "Domotica in casa: impianti, costi e cosa prevedere in ristrutturazione" · domotica casa · 24 giu 2026

### incentivi-bonus (4)
- `bonus-ristrutturazione-2026-guida` · "Bonus ristrutturazione 2026: guida completa a detrazione 50% e 36%" · bonus ristrutturazione 2026 · 20 lug 2026
- `superbonus-2026-cosa-resta` · "Superbonus 2026: cosa resta, chi può ancora accedere e come" · superbonus 2026 · 13 lug 2026
- `conto-termico-3-guida` · "Conto Termico 3.0: incentivi GSE, importi e come fare domanda" · conto termico 3.0 · 4 lug 2026
- `ecobonus-2026-come-funziona` · "Ecobonus 2026: interventi ammessi, aliquote e adempimenti ENEA" · ecobonus 2026 · 27 giu 2026

### tecnologie-innovazione (4)
- `bim-obbligatorio-scadenze` · "BIM obbligatorio in Italia: scadenze, soglie e obblighi per imprese e studi" · BIM obbligatorio · 15 lug 2026
- `stampa-3d-edilizia` · "Stampa 3D in edilizia: case stampate, costi e stato dell'arte in Italia" · stampa 3d edilizia · 8 lug 2026
- `intelligenza-artificiale-cantiere` · "Intelligenza artificiale in cantiere: usi reali, strumenti e limiti" · intelligenza artificiale edilizia · 1 lug 2026
- `top-5-software-bim-edilizia` · "I 5 migliori software BIM per l'edilizia: funzioni e costi a confronto" · software bim · 23 giu 2026

### normative (4)
- `direttiva-case-green-cosa-cambia` · "Direttiva Case Green UE: cosa cambia per gli edifici italiani" · direttiva case green · 19 lug 2026
- `sicurezza-cantiere-dlgs-81` · "Sicurezza in cantiere: D.Lgs 81/08, obblighi e novità 2026" · sicurezza in cantiere norme · 11 lug 2026
- `ntc-norme-tecniche-costruzioni` · "NTC: le Norme Tecniche per le Costruzioni spiegate in pratica" · norme tecniche costruzioni · 3 lug 2026
- `certificazione-ape-guida` · "Certificazione APE: quando è obbligatoria, costi e classi energetiche" · certificazione APE · 26 giu 2026

## Internal linking obbligatorio
- Il pillar `efficienza-energetica/pannelli-solari-guida/` linka i 4 figli del silo; ogni figlio linka il pillar (anchor "guida ai pannelli solari" o simile) + almeno 2 fratelli.
- Ogni articolo: 3-5 link interni contestuali nel corpo (stesso silo + bonus/normative pertinenti) + box "Articoli correlati" (3 card, stesso silo prima).
- Ogni articolo di taglio pratico linka almeno un articolo di `incentivi-bonus/` pertinente.

## Template articolo (obbligatorio, identico per tutti) — vedi l'esemplare
L'esemplare canonico è `efficienza-energetica/pannelli-solari-guida/index.html`. Ogni articolo DEVE replicarne struttura e classi CSS:
1. `<head>`: title ≤60 char con keyword; meta description ≤155 char; canonical assoluto; robots `index,follow,max-image-preview:large`; OG+Twitter card; JSON-LD `@graph` con NewsArticle (author Person redazione, publisher Organization con logo, datePublished, dateModified, mainEntityOfPage, image, wordCount), BreadcrumbList (Home > Silo > Titolo), FAQPage (allineata alle FAQ visibili).
2. Breadcrumb visibile con aria-label.
3. Kicker categoria, un solo H1, standfirst, byline (autore con link `/redazione/`, data pubblicazione + "Aggiornato il", minuti lettura).
4. Box "Risposta rapida" (`answer-box`, 40-60 parole auto-conclusive, risponde alla domanda della keyword).
5. TOC cliccabile (`article-toc`) con ancore a ogni H2 (id descrittivi, es. `#costi`, `#incentivi`).
6. Corpo: H2 formulati come domande reali dove naturale; H3 ordinati; almeno una tabella o lista puntata; frasi estraibili; link interni contestuali.
7. Slot pubblicitari in-article (`.ad-slot.ad-rect` riservato 300×250) tra i paragrafi, senza CLS.
8. Box FAQ in fondo (`faq-section`) con 4-5 domande in `<details>` o div strutturati, identiche al JSON-LD FAQPage.
9. Byline E-E-A-T finale + box autore; share buttons leggeri (link share URL, niente script esterni).
10. "Articoli correlati": 3 card.
11. Header/footer IDENTICI all'esemplare (stessa markup, adattare solo `aria-current` e breadcrumb).
12. Sidebar articolo con ad 300×600 + "I più letti" (stessa lista dell'esemplare).

## Requisiti contenuto per articolo
- Minimo 4.000 caratteri di testo contenuto (esclusi tag HTML): target prudente 5.000-7.000 caratteri.
- Italiano giornalistico, tecnico ma accessibile; dati plausibili 2026, tono autorevole; niente testo placeholder.
- Keyword primaria in: title, H1, primo paragrafo, URL, almeno un H2, FAQ.
- Niente immagini raster: usa i thumb CSS `.thumb t-<silo>` con `.thumb-label` (gradienti definiti nel CSS: t-ristrutturazioni, t-serramenti, t-energia, t-materiali, t-impianti, t-bonus, t-tech, t-normative).

## Vincoli performance
- Un solo CSS, un solo JS defer; niente librerie esterne; immagini solo logo (header fetchpriority alto); tutto il resto CSS. Slot ads con dimensioni riservate.
