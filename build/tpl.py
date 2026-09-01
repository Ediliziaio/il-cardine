# -*- coding: utf-8 -*-
"""Renderer articolo — replica ESATTA del template canonico pannelli-solari-guida."""
import json, re
from urllib.parse import quote

DOMAIN = "https://www.ilcardine.it"

SILO_NAMES = {
    "ristrutturazioni": "Ristrutturazioni",
    "serramenti-infissi": "Serramenti e Infissi",
    "efficienza-energetica": "Efficienza Energetica",
    "materiali-costruzione": "Materiali da Costruzione",
    "impianti": "Impianti",
    "incentivi-bonus": "Incentivi e Bonus",
    "tecnologie-innovazione": "Tecnologie e Innovazione",
    "normative": "Normative",
}

AD_LEADERBOARD = '''  <!-- Slot pubblicitario: leaderboard -->
  <div class="container">
    <div class="ad-slot ad-leaderboard" data-ad-slot="leaderboard-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span>
      <a class="ad-creative" href="https://www.ediliziaincloud.com/" target="_blank" rel="sponsored noopener"><img src="/assets/ads/eic-leaderboard.webp" alt="EdiliziaInCloud, il gestionale con AI per l'edilizia: prova gratuita di 31 giorni" width="1456" height="136" loading="lazy" decoding="async"></a>
    </div>
    <div class="ad-slot ad-mobile mobile-only" data-ad-slot="mobile-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span>
      <a class="ad-creative" href="https://www.ediliziaincloud.com/" target="_blank" rel="sponsored noopener"><img src="/assets/ads/eic-billboard.webp" alt="EdiliziaInCloud, il gestionale con AI per l'edilizia: prova gratuita di 31 giorni" width="1200" height="498" loading="lazy" decoding="async"></a>
    </div>
  </div>'''

def ad_rect(n):
    return f'''          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-{n}" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>'''

def header(nav_current):
    nav = []
    nav.append('        <li><a href="/">Home</a></li>')
    for slug, name in SILO_NAMES.items():
        cur = ' aria-current="page"' if slug == nav_current else ''
        nav.append(f'        <li><a href="/{slug}/"{cur}>{name}</a></li>')
    nav_html = "\n".join(nav)
    return f'''  <a class="skip-link" href="#contenuto">Salta al contenuto</a>

  <!-- Topbar -->
  <div class="topbar">
    <div class="container">
      <span class="tb-date" data-tb-date>Martedì 21 luglio 2026</span>
      <nav class="tb-links" aria-label="Link utili">
        <a href="/chi-siamo/">Chi siamo</a>
        <a href="/redazione/">Redazione</a>
        <a href="/contatti/">Contatti</a>
        <a href="/pubblicita/">Pubblicità</a>
        <a href="/feed.xml">RSS</a>
      </nav>
    </div>
  </div>

  <!-- Testata -->
  <header class="masthead">
    <div class="container">
      <a class="logo" href="/" aria-label="Il Cardine — Home">
        <img src="/assets/logo.png" alt="Il Cardine — Il punto di riferimento per chi costruisce, ristruttura e riqualifica" width="300" height="61" fetchpriority="high">
      </a>
      <div class="mh-right">
        <p class="mh-tagline">Il punto di riferimento per chi costruisce, ristruttura e riqualifica.</p>
        <a class="btn" href="/#newsletter">Iscriviti gratis</a>
      </div>
    </div>
  </header>

  <!-- Navigazione principale -->
  <nav class="mainnav" aria-label="Navigazione principale" data-open="false">
    <div class="container">
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-list">
        <span class="burger" aria-hidden="true"></span> Menu
      </button>
      <ul id="nav-list">
{nav_html}
      </ul>
    </div>
  </nav>

  <!-- Ticker ultim'ora -->
  <div class="ticker" aria-label="In evidenza">
    <div class="container">
      <span class="ticker-label">In evidenza</span>
      <div class="ticker-items">
        <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">Bonus ristrutturazione 2026: confermata la doppia aliquota 50% / 36%</a>
        <a href="/normative/direttiva-case-green-cosa-cambia/">Direttiva Case Green: le nuove scadenze per gli edifici italiani</a>
        <a href="/efficienza-energetica/fotovoltaico-incentivi-2026/">Fotovoltaico 2026: detrazione 50% e comunità energetiche</a>
      </div>
    </div>
  </div>

{AD_LEADERBOARD}'''

SIDEBAR = '''        <!-- Sidebar articolo -->
        <aside class="sidebar">
          <div class="ad-slot ad-halfpage" data-ad-slot="sidebar-halfpage" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <a class="ad-creative" href="https://www.ediliziaincloud.com/" target="_blank" rel="sponsored noopener"><img src="/assets/ads/eic-rect.webp" alt="EdiliziaInCloud, il gestionale con AI per l'edilizia: prova gratuita di 31 giorni" width="600" height="500" loading="lazy" decoding="async"></a>
          </div>

          <section class="widget" aria-labelledby="piu-letti">
            <h3 class="w-title" id="piu-letti">I più letti</h3>
            <ol class="rank-list">
              <li><div><a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">Bonus ristrutturazione 2026: guida completa a detrazione 50% e 36%</a><span class="rl-cat">Incentivi e Bonus</span></div></li>
              <li><div><a href="/ristrutturazioni/costo-ristrutturazione-al-mq-2026/">Costo ristrutturazione al mq nel 2026: prezzi voce per voce</a><span class="rl-cat">Ristrutturazioni</span></div></li>
              <li><div><a href="/normative/direttiva-case-green-cosa-cambia/">Direttiva Case Green UE: cosa cambia per gli edifici italiani</a><span class="rl-cat">Normative</span></div></li>
              <li><div><a href="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/">Serramenti in PVC, alluminio o legno: il confronto completo 2026</a><span class="rl-cat">Serramenti e Infissi</span></div></li>
              <li><div><a href="/efficienza-energetica/pannelli-solari-guida/">Pannelli solari: la guida definitiva 2026 — costi, incentivi e installazione</a><span class="rl-cat">Efficienza Energetica</span></div></li>
            </ol>
          </section>

          <section class="widget newsletter" aria-labelledby="nl-art">
            <h3 class="w-title" id="nl-art">Newsletter Il Cardine</h3>
            <p>Bonus, norme e cantieri: ogni settimana nella tua email, in 5 minuti.</p>
            <form action="#" method="post">
              <label class="sr-only" for="nl-email-art">Email</label>
              <input type="email" id="nl-email-art" name="email" placeholder="La tua email" required>
              <button class="btn" type="submit">Iscriviti</button>
            </form>
            <small>Iscrivendoti accetti la nostra informativa privacy. Nessuno spam, solo edilizia.</small>
          </section>
        </aside>'''

FOOTER = '''  <!-- Slot pubblicitario: footer -->
  <div class="ad-slot ad-footer" data-ad-slot="footer-leaderboard" role="complementary" aria-label="Spazio pubblicitario">
    <span class="ad-tag">Pubblicità</span>
    <a class="ad-creative" href="https://www.ediliziaincloud.com/" target="_blank" rel="sponsored noopener"><img src="/assets/ads/eic-leaderboard.webp" alt="EdiliziaInCloud, il gestionale con AI per l'edilizia: prova gratuita di 31 giorni" width="1456" height="136" loading="lazy" decoding="async"></a>
  </div>

  <!-- FOOTER CANONICO — identico in tutte le pagine -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="f-logo" href="/" aria-label="Il Cardine — Home">
            <img src="/assets/logo-white.png" alt="Il Cardine" width="240" height="48">
          </a>
          <p class="f-desc">Il Cardine è la testata online dedicata a chi costruisce, ristruttura e riqualifica: guide pratiche, incentivi, norme e tecnologie per l'edilizia italiana, con un linguaggio tecnico ma accessibile.</p>
        </div>
        <nav aria-label="Sezioni del sito">
          <h4>Sezioni</h4>
          <ul>
            <li><a href="/ristrutturazioni/">Ristrutturazioni</a></li>
            <li><a href="/serramenti-infissi/">Serramenti e Infissi</a></li>
            <li><a href="/efficienza-energetica/">Efficienza Energetica</a></li>
            <li><a href="/materiali-costruzione/">Materiali da Costruzione</a></li>
            <li><a href="/impianti/">Impianti</a></li>
            <li><a href="/incentivi-bonus/">Incentivi e Bonus</a></li>
            <li><a href="/tecnologie-innovazione/">Tecnologie e Innovazione</a></li>
            <li><a href="/normative/">Normative</a></li>
          </ul>
        </nav>
        <nav aria-label="Testata">
          <h4>Testata</h4>
          <ul>
            <li><a href="/chi-siamo/">Chi siamo</a></li>
            <li><a href="/redazione/">Redazione</a></li>
            <li><a href="/contatti/">Contatti</a></li>
            <li><a href="/pubblicita/">Pubblicità</a></li>
            <li><a href="/feed.xml">Feed RSS</a></li>
            <li><a href="/sitemap/">Mappa del sito</a></li>
          </ul>
        </nav>
        <div>
          <h4>Newsletter</h4>
          <p class="f-desc">Bonus, scadenze e norme spiegate in 5 minuti, ogni settimana. Gratis.</p>
          <a class="btn" href="/#newsletter">Iscriviti gratis</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>2026</span> Il Cardine — Tutti i diritti riservati</span>
        <span><a href="/privacy/">Privacy</a> · <a href="/cookie-policy/">Cookie</a></span>
      </div>
    </div>
  </footer>
  <script src="/js/main.js" defer></script>'''


def strip_tags(html):
    txt = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", txt).strip()


def render(a):
    url = f"{DOMAIN}/{a['silo']}/{a['slug']}/"
    silo_name = SILO_NAMES[a["silo"]]
    author = a["author"]

    # ---- body sections + ads ----
    body_parts = []
    ad_after = a.get("ad_after", [2, 4])
    for i, sec in enumerate(a["sections"]):
        body_parts.append(f'          <h2 id="{sec["id"]}">{sec["title"]}</h2>')
        body_parts.append(sec["html"])
        if i in ad_after:
            body_parts.append(ad_rect(ad_after.index(i) + 1))
    body_html = "\n\n".join(body_parts)

    # ---- FAQ ----
    faq_html_parts = []
    faq_json = []
    for q, ans in a["faqs"]:
        faq_html_parts.append(f'''            <details>
              <summary>{q}</summary>
              <div class="faq-a"><p>{ans}</p></div>
            </details>''')
        faq_json.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)},
        })
    faq_html = "\n".join(faq_html_parts)

    # ---- TOC ----
    toc_items = "\n".join(
        f'              <li><a href="#{s["id"]}">{s["toc"]}</a></li>' for s in a["sections"])
    toc_items += '\n              <li><a href="#faq">Domande frequenti</a></li>'

    # ---- related cards ----
    cards = []
    for c in a["related"]:
        cards.append(f'''          <article class="card">
            <a href="{c["url"]}"><div class="thumb {c["thumb"]} ar-3-2"><span class="thumb-label">{c["label"]}</span></div></a>
            <div class="card-body">
              <span class="cat-mini">{c["label"]}</span>
              <h3><a href="{c["url"]}">{c["title"]}</a></h3>
              <p class="card-excerpt">{c["excerpt"]}</p>
              <div class="card-meta"><span>{c["date"]}</span><span>{c["mins"]} min</span></div>
            </div>
          </article>''')
    cards_html = "\n".join(cards)

    # ---- tags ----
    tags_html = "\n".join(f'            <a href="{t[0]}">{t[1]}</a>' for t in a["tags"])

    # ---- word count (body reale) ----
    all_text = " ".join([
        a["standfirst_plain"], strip_tags(a["answer"]),
        " ".join(strip_tags(s["html"]) + " " + s["title"] for s in a["sections"]),
        " ".join(q + " " + strip_tags(ans) for q, ans in a["faqs"]),
        strip_tags(a["sources"]),
    ])
    wc = len(all_text.split())

    # ---- JSON-LD ----
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": url + "#article",
                "headline": a["h1"],
                "description": a["description"],
                "inLanguage": "it-IT",
                "datePublished": a["date_iso"],
                "dateModified": a["mod_iso"],
                "author": {
                    "@type": "Person",
                    "name": author["name"],
                    "url": DOMAIN + "/redazione/",
                    "jobTitle": author["job"],
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Il Cardine",
                    "url": DOMAIN + "/",
                    "logo": {
                        "@type": "ImageObject",
                        "url": DOMAIN + "/assets/logo.png",
                        "width": 634,
                        "height": 128,
                    },
                },
                "mainEntityOfPage": url,
                "image": DOMAIN + "/assets/logo.png",
                "articleSection": silo_name,
                "keywords": a["keywords"],
                "wordCount": wc,
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
                    {"@type": "ListItem", "position": 2, "name": silo_name, "item": f"{DOMAIN}/{a['silo']}/"},
                    {"@type": "ListItem", "position": 3, "name": a["bc_short"]},
                ],
            },
            {"@type": "FAQPage", "mainEntity": faq_json},
        ],
    }
    ld_json = json.dumps(ld, ensure_ascii=False, indent=2)
    ld_json = "\n".join("  " + line for line in ld_json.splitlines())

    # ---- share urls ----
    q_url = quote(url, safe="")
    q_title = quote(a["h1"], safe="")
    q_short = quote(a["bc_short"], safe="")

    html = f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a["title_tag"]}</title>
  <meta name="description" content="{a["description"]}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="{author["name"]}">
  <meta name="geo.region" content="IT">
  <meta name="geo.placename" content="Italia">
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Il Cardine">
  <meta property="og:title" content="{a["h1"]}">
  <meta property="og:description" content="{a["og_desc"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="it_IT">
  <meta property="og:image" content="{DOMAIN}/assets/logo.png">
  <meta property="article:published_time" content="{a["date_iso"]}">
  <meta property="article:modified_time" content="{a["mod_iso"]}">
  <meta property="article:section" content="{silo_name}">
  <!-- Twitter -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{a["title_tag"]}">
  <meta name="twitter:description" content="{a["tw_desc"]}">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <!-- Structured data: Article + BreadcrumbList + FAQPage (allineati al contenuto visibile) -->
  <script type="application/ld+json">
{ld_json}
  </script>
</head>
<body>
{header(a["silo"])}

  <main id="contenuto">
    <article itemscope itemtype="https://schema.org/Article">
      <!-- Intestazione articolo -->
      <header class="article-head container">
        <nav class="breadcrumbs" aria-label="Percorso di navigazione">
          <a href="/">Home</a><span class="sep" aria-hidden="true">›</span>
          <a href="/{a['silo']}/">{silo_name}</a><span class="sep" aria-hidden="true">›</span>
          <span aria-current="page">{a["bc_short"]}</span>
        </nav>
        <span class="kicker">{a["kicker"]}</span>
        <h1 itemprop="headline">{a["h1"]}</h1>
        <p class="standfirst" itemprop="description">{a["standfirst"]}</p>
        <div class="article-meta-bar">
          <span class="b-author">di <a href="/redazione/" itemprop="author">{author["name"]}</a> — Redazione</span>
          <span>Pubblicato il <time datetime="{a["date_iso"]}" itemprop="datePublished">{a["date_h"]}</time></span>
          <span>Aggiornato il <time datetime="{a["mod_iso"]}" itemprop="dateModified">{a["mod_h"]}</time></span>
          <span>Tempo di lettura: {a["mins"]} min</span>
        </div>
      </header>

      <div class="article-layout">
        <div class="article-body" itemprop="articleBody">

          <figure class="thumb {a["thumb"]} ar-16-9" role="img" aria-label="{a["thumb_aria"]}">
            <span class="thumb-label">{a["thumb_label"]}</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <div class="answer-box">
            <span class="ab-title">Risposta rapida</span>
            <p>{a["answer"]}</p>
          </div>

          <!-- Indice dei contenuti -->
          <nav class="article-toc" aria-label="Indice dei contenuti">
            <span class="toc-title">Indice dei contenuti</span>
            <ol>
{toc_items}
            </ol>
          </nav>

{body_html}

          <!-- FAQ -->
          <h2 id="faq">Domande frequenti su {a["faq_topic"]}</h2>
          <div class="faq-section">
{faq_html}
          </div>

          <p class="sources"><strong>Fonti:</strong> {a["sources"]}</p>

          <!-- Box autore (E-E-A-T) -->
          <div class="author-box">
            <div class="author-avatar" aria-hidden="true">{author["initials"]}</div>
            <div>
              <p class="ab-name"><a href="/redazione/">{author["name"]}</a></p>
              <p class="ab-role">{author["role"]}</p>
              <p class="ab-bio">{author["bio"]}</p>
            </div>
          </div>

          <!-- Condivisione -->
          <div class="share-row" aria-label="Condividi l'articolo">
            <span class="sr-label">Condividi</span>
            <a href="https://wa.me/?text={q_title}%20{q_url}" rel="noopener" target="_blank">WhatsApp</a>
            <a href="https://www.facebook.com/sharer/sharer.php?u={q_url}" rel="noopener" target="_blank">Facebook</a>
            <a href="https://twitter.com/intent/tweet?url={q_url}&amp;text={q_title}" rel="noopener" target="_blank">X</a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url={q_url}" rel="noopener" target="_blank">LinkedIn</a>
            <a href="mailto:?subject={q_short}&body={q_url}">Email</a>
          </div>

          <div class="tags" aria-label="Argomenti dell'articolo">
{tags_html}
          </div>

        </div>

{SIDEBAR}
      </div>

      <!-- Articoli correlati -->
      <section class="related container" aria-labelledby="correlati">
        <h2 id="correlati">Articoli correlati</h2>
        <div class="related-grid">
{cards_html}
        </div>
      </section>
    </article>
  </main>

{FOOTER}
</body>
</html>
'''
    return html, wc
