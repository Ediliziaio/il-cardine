# -*- coding: utf-8 -*-
"""Scaffolding condiviso per gli articoli de Il Cardine.
Replica ESATTAMENTE header, footer, sidebar e componenti del template canonico
efficienza-energetica/pannelli-solari-guida/index.html.
"""
import json
import re
from urllib.parse import quote

SITE = "https://www.ilcardine.it"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


def strip_tags(html_text):
    txt = re.sub(r"<script.*?</script>", " ", html_text, flags=re.S | re.I)
    txt = re.sub(r"<style.*?</style>", " ", txt, flags=re.S | re.I)
    txt = re.sub(r"<[^>]+>", " ", txt)
    txt = re.sub(r"&amp;", "&", txt)
    txt = re.sub(r"&[a-z]+;", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def jsonld(art, word_count):
    url = SITE + "/" + art["silo"] + "/" + art["slug"] + "/"
    faq_entities = []
    for q, a_html in art["faq"]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a_html)}
        })
    graph = [
        {
            "@type": "NewsArticle",
            "@id": url + "#article",
            "headline": art["h1"],
            "description": art["desc"],
            "inLanguage": "it-IT",
            "datePublished": art["pub"] + "T08:00:00+02:00",
            "dateModified": art["mod"] + "T08:00:00+02:00",
            "author": {
                "@type": "Person",
                "name": art["author"],
                "url": SITE + "/redazione/",
                "jobTitle": "Giornalista, redazione Il Cardine"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Il Cardine",
                "url": SITE + "/",
                "logo": {
                    "@type": "ImageObject",
                    "url": SITE + "/assets/logo.png",
                    "width": 634,
                    "height": 128
                }
            },
            "mainEntityOfPage": url,
            "image": SITE + "/assets/logo.png",
            "articleSection": art["silo_name"],
            "keywords": art["keywords"],
            "wordCount": word_count
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": art["silo_name"], "item": SITE + "/" + art["silo"] + "/"},
                {"@type": "ListItem", "position": 3, "name": art["breadcrumb_title"]}
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent="  ")


def head(art, word_count):
    url = SITE + "/" + art["silo"] + "/" + art["slug"] + "/"
    return """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%(title_tag)s</title>
  <meta name="description" content="%(desc)s">
  <link rel="canonical" href="%(url)s">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="%(author)s">
  <meta name="geo.region" content="IT">
  <meta name="geo.placename" content="Italia">
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Il Cardine">
  <meta property="og:title" content="%(og_title)s">
  <meta property="og:description" content="%(og_desc)s">
  <meta property="og:url" content="%(url)s">
  <meta property="og:locale" content="it_IT">
  <meta property="og:image" content="https://www.ilcardine.it/assets/logo.png">
  <meta property="article:published_time" content="%(pub)sT08:00:00+02:00">
  <meta property="article:modified_time" content="%(mod)sT08:00:00+02:00">
  <meta property="article:section" content="%(silo_name)s">
  <!-- Twitter -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="%(tw_title)s">
  <meta name="twitter:description" content="%(tw_desc)s">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <!-- Structured data: NewsArticle + BreadcrumbList + FAQPage (allineati al contenuto visibile) -->
  <script type="application/ld+json">
%(jsonld)s
  </script>
</head>""" % {
        "title_tag": art["title_tag"], "desc": art["desc"], "url": url,
        "author": art["author"], "og_title": art["og_title"], "og_desc": art["og_desc"],
        "pub": art["pub"], "mod": art["mod"], "silo_name": art["silo_name"],
        "tw_title": art["tw_title"], "tw_desc": art["tw_desc"],
        "jsonld": jsonld(art, word_count),
    }


NAV = [
    ("/", "Home", None),
    ("/ristrutturazioni/", "Ristrutturazioni", "ristrutturazioni"),
    ("/serramenti-infissi/", "Serramenti e Infissi", "serramenti-infissi"),
    ("/efficienza-energetica/", "Efficienza Energetica", "efficienza-energetica"),
    ("/materiali-costruzione/", "Materiali da Costruzione", "materiali-costruzione"),
    ("/impianti/", "Impianti", "impianti"),
    ("/incentivi-bonus/", "Incentivi e Bonus", "incentivi-bonus"),
    ("/tecnologie-innovazione/", "Tecnologie e Innovazione", "tecnologie-innovazione"),
    ("/normative/", "Normative", "normative"),
]


def header(silo):
    nav_items = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == silo else ""
        nav_items.append('        <li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    nav_html = "\n".join(nav_items)
    return """<body>
  <a class="skip-link" href="#contenuto">Salta al contenuto</a>

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
%s
      </ul>
    </div>
  </nav>

  <!-- Ticker ultim'ora -->
  <div class="ticker" aria-label="In evidenza">
    <div class="container">
      <span class="ticker-label">In evidenza</span>
      <div class="ticker-items">
        <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">Bonus ristrutturazione 2026: confermata la doppia aliquota 50%% / 36%%</a>
        <a href="/normative/direttiva-case-green-cosa-cambia/">Direttiva Case Green: le nuove scadenze per gli edifici italiani</a>
        <a href="/efficienza-energetica/fotovoltaico-incentivi-2026/">Fotovoltaico 2026: detrazione 50%% e comunità energetiche</a>
      </div>
    </div>
  </div>

  <!-- Slot pubblicitario: leaderboard -->
  <div class="container">
    <div class="ad-slot ad-leaderboard" data-ad-slot="leaderboard-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span>
      <span class="ad-size">Leaderboard 728×90</span>
    </div>
    <div class="ad-slot ad-mobile mobile-only" data-ad-slot="mobile-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span>
      <span class="ad-size">Mobile banner 320×100</span>
    </div>
  </div>

  <main id="contenuto">
    <article itemscope itemtype="https://schema.org/NewsArticle">""" % nav_html


SIDEBAR = """        <!-- Sidebar articolo -->
        <aside class="sidebar">
          <div class="ad-slot ad-halfpage" data-ad-slot="sidebar-halfpage" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Half page 300×600</span>
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
        </aside>"""


FOOTER = """  <!-- Slot pubblicitario: footer -->
  <div class="ad-slot ad-footer" data-ad-slot="footer-leaderboard" role="complementary" aria-label="Spazio pubblicitario">
    <span class="ad-tag">Pubblicità</span>
    <span class="ad-size">Leaderboard 728×90</span>
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
  <script src="/js/main.js" defer></script>
</body>
</html>
"""


def share_row(art):
    url = SITE + "/" + art["silo"] + "/" + art["slug"] + "/"
    eu = quote(url, safe="")
    et = quote(art["h1"], safe="")
    et_short = quote(art["breadcrumb_title"], safe="")
    return """          <!-- Condivisione -->
          <div class="share-row" aria-label="Condividi l'articolo">
            <span class="sr-label">Condividi</span>
            <a href="https://wa.me/?text=%s%%20%s" rel="noopener" target="_blank">WhatsApp</a>
            <a href="https://www.facebook.com/sharer/sharer.php?u=%s" rel="noopener" target="_blank">Facebook</a>
            <a href="https://twitter.com/intent/tweet?url=%s&amp;text=%s" rel="noopener" target="_blank">X</a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url=%s" rel="noopener" target="_blank">LinkedIn</a>
            <a href="mailto:?subject=%s&amp;body=%s">Email</a>
          </div>""" % (et, eu, eu, eu, et, eu, et_short, eu)


def toc_html(art):
    items = "\n".join('              <li><a href="#%s">%s</a></li>' % (aid, label)
                      for aid, label in art["toc"])
    return """          <!-- Indice dei contenuti -->
          <nav class="article-toc" aria-label="Indice dei contenuti">
            <span class="toc-title">Indice dei contenuti</span>
            <ol>
%s
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>""" % items


def faq_html(art):
    blocks = []
    for q, a in art["faq"]:
        blocks.append("""            <details>
              <summary>%s</summary>
              <div class="faq-a"><p>%s</p></div>
            </details>""" % (q, a))
    return """          <!-- FAQ -->
          <h2 id="faq">%s</h2>
          <div class="faq-section">
%s
          </div>""" % (art["faq_title"], "\n".join(blocks))


def related_html(art):
    cards = []
    for c in art["related"]:
        cards.append("""          <article class="card">
            <a href="%(href)s"><div class="thumb %(thumb)s ar-3-2"><span class="thumb-label">%(cat)s</span></div></a>
            <div class="card-body">
              <span class="cat-mini">%(cat)s</span>
              <h3><a href="%(href)s">%(title)s</a></h3>
              <p class="card-excerpt">%(excerpt)s</p>
              <div class="card-meta"><span>%(date)s</span><span>%(mins)s</span></div>
            </div>
          </article>""" % c)
    return """      <!-- Articoli correlati -->
      <section class="related container" aria-labelledby="correlati">
        <h2 id="correlati">Articoli correlati</h2>
        <div class="related-grid">
%s
        </div>
      </section>""" % "\n".join(cards)


def article_body_inner(art):
    """Tutto il contenuto di <div class="article-body"> (usato anche per wordCount)."""
    parts = [
        """          <figure class="thumb %s ar-16-9" role="img" aria-label="%s">
            <span class="thumb-label">%s</span>
          </figure>""" % (art["thumb"], art["thumb_aria"], art["thumb_label"]),
        """          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <div class="answer-box">
            <span class="ab-title">Risposta rapida</span>
            <p>%s</p>
          </div>""" % art["answer"],
        toc_html(art),
        art["body"],
        faq_html(art),
        """          <p class="sources"><strong>Fonti:</strong> %s</p>""" % art["sources"],
        """          <!-- Box autore (E-E-A-T) -->
          <div class="author-box">
            <div class="author-avatar" aria-hidden="true">%s</div>
            <div>
              <p class="ab-name"><a href="/redazione/">%s</a></p>
              <p class="ab-role">%s</p>
              <p class="ab-bio">%s</p>
            </div>
          </div>""" % (art["initials"], art["author"], art["role"], art["bio"]),
        share_row(art),
        """          <div class="tags" aria-label="Argomenti dell'articolo">
%s
          </div>""" % "\n".join('            <a href="%s">%s</a>' % t for t in art["tags"]),
    ]
    return "\n\n".join(parts)


def build_article(art):
    inner = article_body_inner(art)
    text = strip_tags(inner)
    word_count = len(text.split())
    char_count = len(text)

    page = "\n".join([
        head(art, word_count),
        header(art["silo"]),
        """      <!-- Intestazione articolo -->
      <header class="article-head container">
        <nav class="breadcrumbs" aria-label="Percorso di navigazione">
          <a href="/">Home</a><span class="sep" aria-hidden="true">›</span>
          <a href="/%s/">%s</a><span class="sep" aria-hidden="true">›</span>
          <span aria-current="page">%s</span>
        </nav>
        <span class="kicker">%s</span>
        <h1 itemprop="headline">%s</h1>
        <p class="standfirst" itemprop="description">%s</p>
        <div class="article-meta-bar">
          <span class="b-author">di <a href="/redazione/" itemprop="author">%s</a> — Redazione</span>
          <span>Pubblicato il <time datetime="%sT08:00:00+02:00" itemprop="datePublished">%s</time></span>
          <span>Aggiornato il <time datetime="%sT08:00:00+02:00" itemprop="dateModified">%s</time></span>
          <span>Tempo di lettura: %d min</span>
        </div>
      </header>""" % (art["silo"], art["silo_name"], art["breadcrumb_title"],
                       art["kicker"], art["h1"], art["standfirst"], art["author"],
                       art["pub"], art["pub_it"], art["mod"], art["mod_it"],
                       art["read_min"]),
        """      <div class="article-layout">
        <div class="article-body" itemprop="articleBody">""",
        inner,
        """        </div>""",
        SIDEBAR,
        """      </div>""",
        related_html(art),
        """    </article>
  </main>""",
        FOOTER,
    ])
    return page, char_count, word_count
