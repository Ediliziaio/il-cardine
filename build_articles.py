# -*- coding: utf-8 -*-
"""Generatore articoli Il Cardine — serramenti-infissi + materiali-costruzione.
Replica ESATTAMENTE il template canonico efficienza-energetica/pannelli-solari-guida."""
import re, os
import unicodedata
from urllib.parse import quote

ROOT = "/Users/agenteai/Documents/kimi/workspace/il-cardine"
SITE = "https://www.ilcardine.it"
LOGO = "https://www.ilcardine.it/assets/logo.png"

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

def nav_html(active):
    items = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active else ""
        items.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(items)

def header_block(active):
    return f'''  <a class="skip-link" href="#contenuto">Salta al contenuto</a>

  <!-- Topbar -->
  <div class="topbar">
    <div class="container">
      <span class="tb-date" data-tb-date></span>
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
{nav_html(active)}
      </ul>
    </div>
  </nav>

  <!-- Ticker: in evidenza -->
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
'''

FOOTER = '''  <!-- Slot pubblicitario: footer -->
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
      <div class="footer-legal">
        <p>Editore: <strong>Domus Group S.r.l.</strong> · Sede legale: Via Aurelio Saffi 29, 20123 Milano · P.IVA 13132010961 · Capitale sociale 20.000,00 € · PEC: <a href="mailto:domusgroupsrl@legalmail.it">domusgroupsrl@legalmail.it</a></p>
      </div>
    </div>
  </footer>
  <script src="/js/main.js" defer></script>
</body>
</html>
'''

SIDEBAR = '''        <!-- Sidebar articolo -->
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
        </aside>
'''

AD_RECT = '''          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-{n}" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>
'''

def strip_html(s):
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&\w+;", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")

def json_ld(a, word_count):
    faq_items = []
    for q, ans in a["faqs"]:
        faq_items.append('''          {
            "@type": "Question",
            "name": "%s",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "%s"
            }
          }''' % (esc(q), esc(strip_html(ans))))
    faqs = ",\n".join(faq_items)
    return f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "@id": "{a['url']}#article",
        "headline": "{esc(a['h1'])}",
        "description": "{esc(a['desc'])}",
        "inLanguage": "it-IT",
        "datePublished": "{a['date_iso']}",
        "dateModified": "{a['date_iso']}",
        "author": {{
          "@type": "Person",
          "@id": "https://www.ilcardine.it/redazione/#{author_slug}",
          "name": "{a['author']}",
          "url": "https://www.ilcardine.it/redazione/#{author_slug}",
          "jobTitle": "Giornalista, redazione Il Cardine"
        }},
        "publisher": {{
          "@type": "Organization",
          "@id": "https://www.ilcardine.it/#organization",
          "name": "Il Cardine",
          "legalName": "Domus Group S.r.l.",
          "url": "https://www.ilcardine.it/",
          "logo": {{
            "@type": "ImageObject",
            "url": "{LOGO}",
            "width": 634,
            "height": 128
          }},
          "vatID": "IT13132010961"
        }},
        "mainEntityOfPage": "{a['url']}",
        "image": "{LOGO}",
        "articleSection": "{a['silo_name']}",
        "keywords": "{esc(a['keywords'])}",
        "wordCount": {word_count}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.ilcardine.it/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{a['silo_name']}", "item": "https://www.ilcardine.it/{a['silo']}/" }},
          {{ "@type": "ListItem", "position": 3, "name": "{esc(a['breadcrumb_title'])}" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
{faqs}
        ]
      }}
    ]
  }}
  </script>'''

def related_html(cards):
    out = []
    for c in cards:
        out.append(f'''          <article class="card">
            <a href="{c['url']}"><div class="thumb {c['thumb']} ar-3-2"><span class="thumb-label">{c['label']}</span></div></a>
            <div class="card-body">
              <span class="cat-mini">{c['cat']}</span>
              <h3><a href="{c['url']}">{c['title']}</a></h3>
              <p class="card-excerpt">{c['excerpt']}</p>
              <div class="card-meta"><span>{c['date']}</span><span>{c['mins']}</span></div>
            </div>
          </article>''')
    return "\n".join(out)

def faq_html(faqs):
    out = []
    for q, ans in faqs:
        out.append(f'''            <details>
              <summary>{q}</summary>
              <div class="faq-a"><p>{ans}</p></div>
            </details>''')
    return "\n".join(out)

def share_html(a):
    u = quote(a["url"], safe="")
    t = quote(a["h1"])
    st = quote(a["breadcrumb_title"])
    return f'''          <div class="share-row" aria-label="Condividi l'articolo">
            <span class="sr-label">Condividi</span>
            <a href="https://wa.me/?text={t}%20{u}" rel="noopener" target="_blank">WhatsApp</a>
            <a href="https://www.facebook.com/sharer/sharer.php?u={u}" rel="noopener" target="_blank">Facebook</a>
            <a href="https://twitter.com/intent/tweet?url={u}&amp;text={t}" rel="noopener" target="_blank">X</a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url={u}" rel="noopener" target="_blank">LinkedIn</a>
            <a href="mailto:?subject={st}&body={u}">Email</a>
          </div>'''

def author_slug_of(name):
    """Slug dell'autore: aggancia la firma all'entita' Person di /redazione/."""
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return s.lower().replace(" ", "-")


def build(a):
    body_text = strip_html(a["answer"] + " " + a["body"] + " " + " ".join(q + " " + strip_html(ans) for q, ans in a["faqs"]))
    word_count = len(body_text.split())
    author_slug = author_slug_of(a["author"])
    toc_items = "\n".join(f'              <li><a href="#{i}">{lbl}</a></li>' for i, lbl in a["toc"])
    tags = "\n".join(f'            <a href="{h}">{lbl}</a>' for h, lbl in a["tags"])
    page = f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a['title_tag']}</title>
  <meta name="description" content="{a['desc']}">
  <link rel="canonical" href="{a['url']}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="{a['author']}">
  <meta name="geo.region" content="IT">
  <meta name="geo.placename" content="Italia">
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Il Cardine">
  <meta property="og:title" content="{a['h1']}">
  <meta property="og:description" content="{a['og_desc']}">
  <meta property="og:url" content="{a['url']}">
  <meta property="og:locale" content="it_IT">
  <meta property="og:image" content="{LOGO}">
  <meta property="article:published_time" content="{a['date_iso']}">
  <meta property="article:modified_time" content="{a['date_iso']}">
  <meta property="article:section" content="{a['silo_name']}">
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{a['title_tag']}">
  <meta name="twitter:description" content="{a['tw_desc']}">
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <!-- Structured data: Article + BreadcrumbList + FAQPage (allineati al contenuto visibile) -->
{json_ld(a, word_count)}
</head>
<body>
{header_block(a['silo'])}
  <main id="contenuto">
    <article itemscope itemtype="https://schema.org/Article">
      <!-- Intestazione articolo -->
      <header class="article-head container">
        <nav class="breadcrumbs" aria-label="Percorso di navigazione">
          <a href="/">Home</a><span class="sep" aria-hidden="true">›</span>
          <a href="/{a['silo']}/">{a['silo_name']}</a><span class="sep" aria-hidden="true">›</span>
          <span aria-current="page">{a['breadcrumb_title']}</span>
        </nav>
        <span class="kicker">{a['kicker']}</span>
        <h1 itemprop="headline">{a['h1']}</h1>
        <p class="standfirst" itemprop="description">{a['standfirst']}</p>
        <div class="article-meta-bar">
          <span class="b-author">di <a href="/redazione/" itemprop="author">{a['author']}</a> — Redazione</span>
          <span>Pubblicato il <time datetime="{a['date_iso']}" itemprop="datePublished">{a['date_it']}</time></span>
          <span>Aggiornato il <time datetime="{a['date_iso']}" itemprop="dateModified">{a['date_it']}</time></span>
          <span>Tempo di lettura: {a['minutes']} min</span>
        </div>
      </header>

      <div class="article-layout">
        <div class="article-body" itemprop="articleBody">

          <figure class="thumb {a['thumb']} ar-16-9" role="img" aria-label="Copertura editoriale: {a['aria_cover']}">
            <span class="thumb-label">{a['thumb_label']}</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <div class="answer-box">
            <span class="ab-title">Risposta rapida</span>
            <p>{a['answer']}</p>
          </div>

          <!-- Indice dei contenuti -->
          <nav class="article-toc" aria-label="Indice dei contenuti">
            <span class="toc-title">Indice dei contenuti</span>
            <ol>
{toc_items}
            </ol>
          </nav>

{a['body']}

          <!-- FAQ -->
          <h2 id="faq">{a['faq_title']}</h2>
          <div class="faq-section">
{faq_html(a['faqs'])}
          </div>

          <p class="sources">{a['sources']}</p>

          <!-- Box autore (E-E-A-T) -->
          <div class="author-box">
            <div class="author-avatar" aria-hidden="true">{a['initials']}</div>
            <div>
              <p class="ab-name"><a href="/redazione/">{a['author']}</a></p>
              <p class="ab-role">{a['role']}</p>
              <p class="ab-bio">{a['bio']}</p>
            </div>
          </div>

          <!-- Condivisione -->
{share_html(a)}

          <div class="tags" aria-label="Argomenti dell'articolo">
{tags}
          </div>

        </div>

{SIDEBAR}      </div>

      <!-- Articoli correlati -->
      <section class="related container" aria-labelledby="correlati">
        <h2 id="correlati">Articoli correlati</h2>
        <div class="related-grid">
{related_html(a['related'])}
        </div>
      </section>
    </article>
  </main>

{FOOTER}'''
    path = os.path.join(ROOT, a["silo"], a["slug"], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    return path, len(body_text), word_count


# ============================ SERRAMENTI-INFISSI ============================
ARTICLES = []

ARTICLES.append(dict(
    silo="serramenti-infissi", silo_name="Serramenti e Infissi", thumb="t-serramenti",
    slug="serramenti-pvc-alluminio-legno-confronto",
    url="https://www.ilcardine.it/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/",
    title_tag="Serramenti PVC o alluminio o legno: confronto 2026",
    desc="Serramenti in PVC o alluminio o legno: trasmittanze, prezzi al mq, durata e manutenzione a confronto per scegliere gli infissi giusti nel 2026.",
    keywords="serramenti pvc o alluminio, serramenti legno, confronto infissi, trasmittanza infissi, prezzi serramenti 2026",
    og_desc="PVC, alluminio o legno? Trasmittanze, costi, durata e manutenzione dei serramenti a confronto, con dati aggiornati al 2026.",
    tw_desc="Serramenti in PVC, alluminio o legno: il confronto completo 2026 su isolamento, prezzi e durata.",
    h1="Serramenti in PVC, alluminio o legno: il confronto completo 2026",
    standfirst="Trasmittanza, prezzi al mq, durata, manutenzione e vincoli estetici: la comparazione definitiva tra i tre materiali dei serramenti, con i numeri aggiornati al 2026 per orientare la scelta senza affidarla al caso.",
    kicker="Serramenti e Infissi · Confronto 2026",
    breadcrumb_title="Serramenti in PVC, alluminio o legno: il confronto 2026",
    author="Luca Bianchi", initials="LB",
    role="Redazione Il Cardine · Serramenti e involucro edilizio",
    bio="Giornalista tecnico, segue da oltre dodici anni serramenti, involucro edilizio e riqualificazione energetica. Per Il Cardine cura le guide su infissi, vetrocamere e prestazioni dell'involucro opaco e trasparente.",
    date_iso="2026-07-17T08:00:00+02:00", date_it="17 luglio 2026", minutes=10,
    aria_cover="serramenti in PVC, alluminio e legno a confronto",
    thumb_label="Serramenti e Infissi · Confronto 2026",
    answer="Non esiste un vincitore assoluto: i <strong>serramenti in PVC</strong> offrono il miglior rapporto tra isolamento e prezzo (300–550 €/mq posati), l'<strong>alluminio a taglio termico</strong> vince su grandi vetrate e durata, il <strong>legno</strong> resta insostituibile nei centri storici e per il comfort tattile. A parità di vetro e posa, le differenze di trasmittanza sono minime: contano progetto e installazione.",
    toc=[
        ("differenze", "PVC, alluminio o legno: quali sono le vere differenze?"),
        ("prestazioni", "Quale materiale isola meglio? Le trasmittanze a confronto"),
        ("durata-manutenzione", "Durata e manutenzione: quanto vivono i tre materiali?"),
        ("costi", "Quanto costano i serramenti in PVC, alluminio e legno?"),
        ("estetica-vincoli", "Estetica, vincoli e design: cosa cambia tra i tre materiali"),
        ("quale-scegliere", "Meglio serramenti in PVC o alluminio? La scelta per contesto"),
        ("incentivi", "Quali detrazioni si applicano ai serramenti nel 2026?"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="differenze">PVC, alluminio o legno: quali sono le vere differenze?</h2>
          <p>Chi deve sostituire gli infissi si trova davanti allo stesso bivio da almeno trent'anni: <strong>serramenti in PVC o alluminio</strong>, con il legno a fare da terza via tradizionale. Nel mercato italiano delle sostituzioni il PVC copre oggi poco più della metà delle vendite, l'alluminio a taglio termico circa un terzo e il legno — puro o in abbinamento — la quota restante. Ma le quote di mercato non rispondono alla domanda giusta, che è un'altra: quale materiale è adatto al mio edificio, al mio clima e al mio budget?</p>
          <p>La differenza fondamentale è costruttiva. Il <strong>PVC</strong> è un profilo in materiale plastico a camere multiple con rinforzi interni in acciaio zincato: isola bene per natura del materiale, costa poco e non richiede manutenzione straordinaria. L'<strong>alluminio a taglio termico</strong> è un profilo metallico interrotto da una barretta in materiale isolante che blocca il ponte termico: è rigidissimo, permette ante sottili e grandi luci, ed è praticamente eterno. Il <strong>legno lamellare</strong> è il materiale naturale per eccellenza: ottimo isolante, caldo al tatto, unico ammesso senza discussioni nei centri storici, ma vivo e bisognoso di cure.</p>
          <p>Il punto tecnico che sfugge a molti preventivi è che la prestazione finale dipende dal <strong>sistema</strong>, non dal solo telaio: vetro, guarnizioni, ferramenta e soprattutto posa in opera incidono quanto il materiale del profilo. Un infisso in PVC posato male perde contro un alluminio posato in modo qualificato, e viceversa.</p>

          <h2 id="prestazioni">Quale materiale isola meglio? Le trasmittanze a confronto</h2>
          <p>La prestazione termica di un serramento si misura con la <strong>trasmittanza termica Uw</strong>, espressa in W/mqK: più basso è il valore, meno calore attraversa la finestra. Per accedere alle detrazioni 2026 i limiti variano per zona climatica, indicativamente da 1,0–1,2 W/mqK nelle zone più fredde (E ed F) fino a 2,4–2,6 nelle zone miti. Tutti e tre i materiali, se ben progettati, rientrano nei limiti: la forbice è nei dettagli.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Confronto tecnico tra i materiali dei serramenti (valori tipici 2026, infisso 2 ante con doppio vetro)</caption>
            <thead>
              <tr><th>Materiale</th><th>Trasmittanza Uw tipica</th><th>Inerzia termica</th><th>Durata attesa</th><th>Manutenzione</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>PVC</strong></td><td>0,9–1,3 W/mqK</td><td>Media</td><td>30–40 anni</td><td>Quasi nulla</td></tr>
              <tr><td><strong>Alluminio a taglio termico</strong></td><td>1,1–1,6 W/mqK</td><td>Bassa</td><td>40–50 anni</td><td>Nulla</td></tr>
              <tr><td><strong>Legno lamellare</strong></td><td>1,0–1,4 W/mqK</td><td>Alta</td><td>30–50 anni (con manutenzione)</td><td>Rifinitura ogni 6–10 anni</td></tr>
              <tr><td><strong>Legno-alluminio</strong></td><td>0,8–1,2 W/mqK</td><td>Alta</td><td>40–60 anni</td><td>Minima (solo interno)</td></tr>
            </tbody>
          </table>
          </div>
          <p>Il <strong>PVC</strong> parte avvantaggiato perché il materiale stesso è isolante: un buon profilo a 6–7 camere da 76–82 mm raggiunge Uw di 0,9–1,1 W/mqK con un semplice doppio vetro basso emissivo. L'<strong>alluminio</strong>, conduttore per natura, raggiunge valori simili solo con profili a taglio termico evoluto (barrette da 34–44 mm) e vetro di qualità; con il <a href="/serramenti-infissi/finestre-triplo-vetro-conviene/">triplo vetro</a> entrambi scendono sotto 1,0 W/mqK. Il <strong>legno</strong> si colloca in mezzo e aggiunge un'inerzia termica superiore, utile d'estate contro il surriscaldamento.</p>
          <p>Sul fronte acustico la differenza la fa quasi esclusivamente il <strong>vetro</strong>: un pacchetto asimmetrico con lastra stratificata da 44.1 o 44.2 abbattimento acustico Rw di 38–42 dB si monta su qualunque telaio. Chi abita su una strada trafficata deve quindi investire sul vetro, non sul materiale del profilo.</p>

          <h2 id="durata-manutenzione">Durata e manutenzione: quanto vivono i tre materiali?</h2>
          <p>Il ciclo di vita reale dei serramenti è più lungo di quanto suggerisca il marketing della sostituzione. Un profilo in PVC di fascia medio-alta supera i <strong>30–40 anni</strong> senza interventi strutturali: le uniche attenzioni sono la pulizia, la lubrificazione della ferramenta ogni 2–3 anni e la sostituzione delle guarnizioni dopo 15–20 anni. Il nemico del PVC è il sole: i profili bianchi di bassa gamma possono ingiallire e i profili scuri scaldano, per questo sulle esposizioni sud conviene scegliere profili con film acrilico o anima in alluminio.</p>
          <p>L'<strong>alluminio</strong> è il più longevo: verniciato a polveri o anodizzato resiste 40–50 anni senza degrado, non teme raggi UV né salsedine se la lega e il trattamento sono corretti, e proprio per questo domina negli edifici costieri e nelle facciate continue. Il <strong>legno</strong>, infine, può durare mezzo secolo — le finestre delle case storiche lo dimostrano — ma a condizione di rispettare il ciclo di manutenzione: controllo della finitura ogni 4–5 anni e riverniciatura o trattamento a olio ogni 6–10 anni, a seconda dell'esposizione. La variante <strong>legno-alluminio</strong> elimina il problema: legno dentro, guscio in alluminio fuori, manutenzione esterna pari a zero.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="costi">Quanto costano i serramenti in PVC, alluminio e legno?</h2>
          <p>Nel 2026 i prezzi al metro quadro, posa e IVA escluse, si collocano indicativamente in queste fasce: <strong>PVC 280–480 €/mq</strong>, <strong>alluminio a taglio termico 450–750 €/mq</strong>, <strong>legno lamellare 500–850 €/mq</strong>, <strong>legno-alluminio 650–1.000 €/mq</strong>. Una finestra a due ante da 120×140 cm in PVC di buona fascia costa posata 550–800 euro; la stessa in alluminio a taglio termico 800–1.200 euro, in legno 900–1.400 euro. Tutti i dettagli voce per voce — vetro, ferramenta, controtelaio, posa — sono nell'articolo sui <a href="/serramenti-infissi/prezzi-infissi-al-mq-2026/">prezzi degli infissi al mq nel 2026</a>.</p>
          <p>Tre fattori spostano il preventivo più del materiale: il <strong>tipo di apertura</strong> (un alzante scorrevole in alluminio può raddoppiare il prezzo al mq), il <strong>vetro</strong> (il triplo aggiunge 30–60 €/mq, lo stratificato acustico 25–50 €/mq) e la <strong>posa</strong>, che vale il 15–25% del totale e non va mai limata: è la voce che decide tenuta all'aria, assenza di ponti termici e durata dei fissaggi.</p>
          <blockquote>«Il materiale del telaio spiega forse un terzo della prestazione finale di una finestra. Il resto lo fanno vetro, posa in opera e la qualità del nodo tra infisso e muratura: è lì che si vincono o si perdono i gradi in inverno.»</blockquote>

          <h2 id="estetica-vincoli">Estetica, vincoli e design: cosa cambia tra i tre materiali</h2>
          <p>Nei <strong>centri storici</strong> e nelle zone sottoposte a vincolo paesaggistico la scelta spesso non è libera: le Soprintendenze richiedono quasi sempre il legno, con profili a filo muro, traversi ridotti e colori a campione. In questi casi il confronto si sposta sul tipo di legno (abete lamellare, larice, rovere, okumé) e sul sistema di apertura, più che sul materiale.</p>
          <p>Sul fronte del <strong>design contemporaneo</strong>, l'alluminio vince per profili sottili: i sistemi minimal con nodo centrale da 20–35 mm e telaio a scomparsa nella muratura permettono vetrate a tutta parete impensabili in PVC, i cui profili devono restare più generosi per contenere i rinforzi in acciaio. Il PVC replica però ormai bene le finiture: i film effetto legno, i colori massellati e le versioni bicolore (bianco dentro, scuro fuori) coprono la quasi totalità delle esigenze residenziali.</p>
          <p>Chi ristruttura con il <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico esterno</a> ha un'occasione unica: spostare gli infissi in spalla al muro, nel piano dell'isolante, eliminando il ponte termico del controtelaio. In quel caso il materiale del profilo conta ancora meno e la posa conta tutto.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="quale-scegliere">Meglio serramenti in PVC o alluminio? La scelta in base al contesto</h2>
          <p>Riassumendo per scenari d'uso, la scelta razionale tra serramenti in PVC o alluminio (o legno) segue queste indicazioni:</p>
          <ol>
            <li><strong>Appartamento in condominio, budget contenuto, esposizione urbana</strong>: PVC di fascia medio-alta. È la scelta più efficiente in rapporto costo/prestazione e non richiede manutenzione.</li>
            <li><strong>Villetta con grandi aperture scorrevoli, zone costiere, estetica minimal</strong>: alluminio a taglio termico. Rigidità e profili sottili fanno la differenza sulle grandi luci.</li>
            <li><strong>Centro storico, casa di pregio, edificio vincolato</strong>: legno lamellare o legno-alluminio. Spesso è l'unica strada percorribile, e comunque la più coerente con il contesto.</li>
            <li><strong>Riqualificazione energetica profonda, climi freddi, casa passiva</strong>: qualsiasi materiale, ma con triplo vetro, Uw ≤ 0,9 W/mqK e posa certificata. La verifica strutturale dei fissaggi segue le indicazioni delle <a href="/normative/ntc-norme-tecniche-costruzioni/">Norme Tecniche per le Costruzioni</a> per l'ancoraggio ai supporti murari.</li>
            <li><strong>Seconda casa al mare o in montagna</strong>: alluminio al mare (salsedine), PVC o legno-alluminio in montagna (escursioni termiche e comfort).</li>
          </ol>
          <p>La regola pratica finale: farsi fare <strong>tre preventivi sullo stesso capitolato</strong> — stesso vetro, stessa ferramenta, stessa posa — e confrontare i materiali a parità di prestazioni dichiarate. Chi produce e installa con qualità si riconosce anche dalla rete: i <a href="/serramenti-infissi/top-5-produttori-serramenti-italia/">migliori produttori di serramenti in Italia</a> lavorano solo con posatori formati sui propri sistemi.</p>

          <h2 id="incentivi">Quali detrazioni si applicano ai serramenti nel 2026?</h2>
          <p>La sostituzione dei serramenti rientra tra gli interventi trainanti della riqualificazione energetica: nel 2026 si applica l'<a href="/incentivi-bonus/ecobonus-2026-come-funziona/">ecobonus con detrazione del 50%</a> per l'abitazione principale (36% per le altre unità), con un massimale specifico di <strong>60.000 euro</strong> per gli infissi, distinto da quello generale. Le condizioni tecniche sono precise: trasmittanza Uw entro i limiti della propria zona climatica, miglioramento rispetto all'esistente, e fatture con bonifico parlante.</p>
          <p>Due adempimenti fanno la differenza tra una detrazione incassata e una persa: la <strong>trasmissione telematica all'ENEA</strong> entro 90 giorni dalla fine dei lavori e la conservazione delle schede tecniche dei serramenti con i valori Uw certificati secondo la UNI EN 14351-1. Chi abbina infissi e cappotto nello stesso cantiere può valutare il percorso del <a href="/incentivi-bonus/superbonus-2026-cosa-resta/">Superbonus residuale</a>, dove ancora applicabile, o il <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">bonus ristrutturazione 2026</a> se l'intervento non migliora la prestazione energetica ma rientra nella manutenzione straordinaria.</p>
''',
    faq_title="Domande frequenti sui serramenti in PVC, alluminio e legno",
    faqs=[
        ("Meglio serramenti in PVC o alluminio?",
         "Dipende dal contesto: il <strong>PVC</strong> conviene per rapporto qualità-prezzo e isolamento (280–480 €/mq, Uw fino a 0,9), l'<strong>alluminio a taglio termico</strong> per grandi vetrate, profili sottili e durata (450–750 €/mq). A parità di vetro e posa la differenza termica è minima: decidono estetica, dimensioni delle ante e budget."),
        ("Quanto durano i serramenti in PVC?",
         "Un serramento in PVC di fascia medio-alta dura <strong>30–40 anni</strong> senza manutenzione straordinaria. Servono solo pulizia periodica, lubrificazione della ferramenta ogni 2–3 anni e sostituzione delle guarnizioni dopo 15–20 anni. I profili chiari con film protettivo resistono meglio all'esposizione sud."),
        ("I serramenti in legno richiedono molta manutenzione?",
         "Il legno lamellare richiede un controllo della finitura ogni 4–5 anni e una <strong>riverniciatura o trattamento ogni 6–10 anni</strong>, a seconda dell'esposizione. La variante legno-alluminio elimina la manutenzione esterna mantenendo il calore del legno all'interno, a fronte di un costo superiore del 20–30%."),
        ("Quanto costa cambiare tutti gli infissi di un appartamento?",
         "Per un appartamento di 90–100 mq con 6–8 finestre, nel 2026 la spesa posata è indicativamente di <strong>5.000–8.000 euro in PVC</strong>, 8.000–12.000 euro in alluminio a taglio termico e 9.000–14.000 euro in legno. Con la detrazione del 50% la spesa netta si dimezza nel recupero decennale."),
        ("I nuovi serramenti rientrano nell'ecobonus 2026?",
         "Sì: la sostituzione degli infissi è agevolata con la <strong>detrazione del 50%</strong> (36% per le seconde case) su un massimale di 60.000 euro, a condizione di rispettare i limiti di trasmittanza Uw della zona climatica, pagare con bonifico parlante e trasmettere la pratica ENEA entro 90 giorni dalla fine lavori."),
    ],
    sources="<strong>Fonti:</strong> UNI EN 14351-1 (marcatura CE finestre); D.M. Requisiti Minimi e decreti FER per i limiti di trasmittanza; ENEA — portale detrazioni; ANFIT — dati di mercato serramenti; listini di settore 2026. I prezzi sono medie indicative: richiedere sempre più preventivi a parità di capitolato. Contenuto a scopo informativo.",
    tags=[
        ("/serramenti-infissi/", "Serramenti"),
        ("/serramenti-infissi/", "PVC o alluminio"),
        ("/incentivi-bonus/", "Ecobonus 2026"),
        ("/efficienza-energetica/", "Involucro edilizio"),
    ],
    related=[
        dict(url="/serramenti-infissi/finestre-triplo-vetro-conviene/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Triplo vetro: quando conviene davvero e quanto costa in più",
             excerpt="Trasmittanze, comfort e sovrapprezzo reale: i casi in cui il triplo vetro si ripaga e quelli in cui è sprecato.", date="11 lug 2026", mins="8 min"),
        dict(url="/serramenti-infissi/prezzi-infissi-al-mq-2026/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Prezzi infissi al mq nel 2026: PVC, alluminio e legno a confronto",
             excerpt="Tutte le voci di costo, dalla ferramenta alla posa, con i prezzi medi aggiornati al 2026.", date="5 lug 2026", mins="9 min"),
        dict(url="/serramenti-infissi/top-5-produttori-serramenti-italia/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="I 5 migliori produttori di serramenti in Italia: qualità e prezzi",
             excerpt="Chi produce gli infissi migliori, come li abbiamo valutati e quanto costano.", date="28 giu 2026", mins="8 min"),
    ],
))


ARTICLES.append(dict(
    silo="serramenti-infissi", silo_name="Serramenti e Infissi", thumb="t-serramenti",
    slug="finestre-triplo-vetro-conviene",
    url="https://www.ilcardine.it/serramenti-infissi/finestre-triplo-vetro-conviene/",
    title_tag="Triplo vetro finestre: quando conviene e quanto costa",
    desc="Triplo vetro per le finestre: trasmittanza, comfort, sovrapprezzo rispetto al doppio vetro e i casi in cui conviene davvero installarlo nel 2026.",
    keywords="triplo vetro finestre, triplo vetro conviene, costo triplo vetro, doppio o triplo vetro, trasmittanza vetrocamera",
    og_desc="Triplo vetro: trasmittanze, comfort termico e sovrapprezzo reale rispetto al doppio vetro. I casi in cui conviene e quelli in cui è sprecato.",
    tw_desc="Triplo vetro per le finestre: quando conviene davvero e quanto costa in più nel 2026.",
    h1="Triplo vetro: quando conviene davvero e quanto costa in più",
    standfirst="Tre lastre invece di due, trasmittanza quasi dimezzata e un sovrapprezzo del 10–15% sul serramento: il triplo vetro è lo standard del Nord Europa, ma in Italia non sempre si ripaga. Ecco come capire se per la propria casa è un investimento o uno spreco.",
    kicker="Serramenti e Infissi · Approfondimento tecnico",
    breadcrumb_title="Triplo vetro: quando conviene e quanto costa in più",
    author="Luca Bianchi", initials="LB",
    role="Redazione Il Cardine · Serramenti e involucro edilizio",
    bio="Giornalista tecnico, segue da oltre dodici anni serramenti, involucro edilizio e riqualificazione energetica. Per Il Cardine cura le guide su infissi, vetrocamere e prestazioni dell'involucro opaco e trasparente.",
    date_iso="2026-07-11T08:00:00+02:00", date_it="11 luglio 2026", minutes=8,
    aria_cover="finestre con triplo vetro e vetrocamera",
    thumb_label="Serramenti e Infissi · Vetrocamera",
    answer="Il <strong>triplo vetro</strong> conviene nelle zone climatiche E ed F, sugli edifici con riscaldamento a basse temperature, nelle riqualificazioni profonde e dove servono trasmittanze Uw sotto 1,0 W/mqK. Costa il 10–15% in più del doppio vetro (30–60 €/mq): nel Centro-Sud e sulle seconde case il doppio vetro di qualità resta la scelta più equilibrata.",
    toc=[
        ("cos-e", "Cos'è il triplo vetro e come è fatto"),
        ("prestazioni", "Quanto isola davvero? I numeri a confronto"),
        ("quando-conviene", "Quando il triplo vetro conviene davvero?"),
        ("quando-no", "Quando invece il doppio vetro basta"),
        ("costi", "Quanto costa in più il triplo vetro?"),
        ("abbinamenti", "Triplo vetro, telaio e posa: il sistema completo"),
        ("incentivi", "Detrazioni 2026 per le finestre con triplo vetro"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="cos-e">Cos'è il triplo vetro e come è fatto</h2>
          <p>Il <strong>triplo vetro</strong> per le finestre è una vetrocamera composta da tre lastre separate da due intercapedini riempite di gas — in genere argon, nei modelli premium kripton — con almeno due rivestimenti basso emissivi che riflettono il calore verso l'interno. Rispetto al doppio vetro aggiunge una lastra, un'intercapedine e una superficie trattata: è questa combinazione, non il solo numero di lastre, a quasi dimezzare la dispersione termica.</p>
          <p>La composizione tipica 2026 è un 4-16-4-16-4 (tre lastre da 4 mm con intercapedini da 16 mm), per uno spessore totale di 44 mm contro i 24–28 mm del doppio vetro standard. Nei modelli acustici una delle lastre esterne diventa <strong>stratificata</strong> (due vetri uniti da una pellicola fonoassorbente), e nei modelli di sicurezza antieffrazione si aggiungono lastre temperabili o stratificati P2A/P4A. Il risultato è una lastra «intelligente» che lavora su tre fronti: dispersione termica, rumore e sicurezza.</p>
          <p>Va sfatato un equivoco frequente: il triplo vetro non è un'invenzione recente. È lo standard residenziale in Germania, Austria e Scandinavia da oltre vent'anni; in Italia si è diffuso con il Superbonus, quando i limiti di trasmittanza spinti lo hanno reso quasi obbligato nelle zone fredde. Oggi, archiviati gli incentivi straordinari, la domanda giusta è tornata quella economica: <strong>dove si ripaga e dove no</strong>.</p>

          <h2 id="prestazioni">Quanto isola davvero? I numeri a confronto</h2>
          <p>La prestazione della sola vetrata si misura con la <strong>trasmittanza Ug</strong> (g sta per glazing): più è bassa, meno calore attraversa il vetro. Il salto dal doppio al triplo vetro è marcato, e si somma a due effetti secondari che il dato di laboratorio non coglie: la temperatura superficiale interna più alta, che elimina la sensazione di «parete fredda» vicino alla finestra, e la riduzione della condensa sul vetro.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Vetrocamere a confronto: valori tipici di mercato 2026</caption>
            <thead>
              <tr><th>Tipologia</th><th>Trasmittanza Ug</th><th>Temperatura superficiale interna*</th><th>Trasmissione luminosa</th><th>Sovrapprezzo indicativo</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Doppio vetro basso emissivo</strong></td><td>1,0–1,1 W/mqK</td><td>13–14 °C</td><td>78–80%</td><td>—</td></tr>
              <tr><td><strong>Doppio vetro + argon premium</strong></td><td>0,9–1,0 W/mqK</td><td>14–15 °C</td><td>78–80%</td><td>+15–25 €/mq</td></tr>
              <tr><td><strong>Triplo vetro standard</strong></td><td>0,6–0,7 W/mqK</td><td>16–17 °C</td><td>70–74%</td><td>+30–60 €/mq</td></tr>
              <tr><td><strong>Triplo vetro acustico/sicurezza</strong></td><td>0,5–0,6 W/mqK</td><td>16–17 °C</td><td>68–72%</td><td>+60–110 €/mq</td></tr>
            </tbody>
          </table>
          </div>
          <p><em>*Con 20 °C interni e 0 °C esterni. La temperatura superficiale alta è ciò che elimina l'effetto «finestra fredda» e la condensa.</em></p>
          <p>Due contropartite vanno conosciute. La <strong>luce</strong>: ogni lastra in più toglie 4–6 punti di trasmissione luminosa, un fattore da valutare su finestre piccole o esposte a nord. Il <strong>guadagno solare</strong>: il fattore g scende da 0,60–0,63 a 0,50–0,55, il che in inverno riduce gli apporti gratuiti del sole ma d'estate aiuta contro il surriscaldamento — a patto di gestire l'ombreggiamento, perché il triplo vetro non sostituisce le schermature.</p>

          <h2 id="quando-conviene">Quando il triplo vetro conviene davvero?</h2>
          <p>Il triplo vetro è un investimento sensato quando almeno due di queste condizioni si verificano contemporaneamente:</p>
          <ul>
            <li><strong>Zona climatica E o F</strong> (Alpi, Appennino centro-settentrionale, pianura padana interna): inverni lunghi e rigidi fanno lavorare il riscaldamento per 5–6 mesi, e ogni watt disperso dalla finestra pesa.</li>
            <li><strong>Riscaldamento a bassa temperatura</strong> (pavimento radiante, pompa di calore): l'involucro deve trattenere il calore perché il sistema lavora in modulazione continua; la finestra è il punto debole da presidiare.</li>
            <li><strong>Riqualificazione profonda</strong>: se si installa il <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico esterno</a> portando le pareti sotto 0,20 W/mqK, lasciare finestre a 1,3–1,4 significa concentrare lì tutte le dispersioni, con condensa e muffa assicurate sul nodo di posa.</li>
            <li><strong>Obiettivo casa passiva o classe A</strong>: la certificazione CasaClima o Passivhaus richiede di regola Uw ≤ 0,8–1,0 W/mqK, raggiungibile solo con il triplo vetro.</li>
            <li><strong>Grandi vetrate a nord</strong>: superfici ampie senza apporti solari, dove la dispersione è massima e il comfort superficiale conta di più.</li>
          </ul>
          <p>In questi casi il sovrapprezzo si ripaga in genere in <strong>6–12 anni</strong> con il risparmio sul riscaldamento, e immediatamente in termini di comfort: chi è passato al triplo vetro descrive quasi sempre la stessa esperienza — si può stare accanto alla finestra anche con la neve fuori, senza correnti fredde percepite.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="quando-no">Quando invece il doppio vetro basta</h2>
          <p>La scelta simmetrica è altrettanto importante: nel <strong>Centro-Sud e sulle coste</strong> (zone climatiche A–C), dove il riscaldamento lavora 2–3 mesi l'anno e il problema vero è il caldo estivo, il triplo vetro si ripaga raramente. Un doppio vetro basso emissivo di qualità con Ug di 1,0–1,1 W/mqK, abbinato a schermature solari esterne, offre il miglior equilibrio costo-beneficio.</p>
          <p>Stesso discorso per le <strong>seconde case usate poco</strong> in inverno, per gli ambienti non riscaldati di continuo e per le sostituzioni parziali: se si cambia una sola finestra in una casa con pareti disperdenti e caldaia vecchia, il triplo vetro è un cerotto su una gamba rotta. Prima si ragiona sull'insieme dell'involucro — con una diagnosi energetica seria — e poi si decide il livello di prestazione del singolo componente. Per orientarsi tra materiali e prestazioni del telaio si veda il nostro <a href="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/">confronto tra serramenti in PVC, alluminio e legno</a>.</p>

          <h2 id="costi">Quanto costa in più il triplo vetro?</h2>
          <p>Nel 2026 il sovrapprezzo del triplo rispetto al doppio vetro, a parità di telaio, si aggira tra <strong>30 e 60 euro al mq</strong> di vetrata per le versioni standard, e tra 60 e 110 €/mq per le versioni acustiche o di sicurezza. Su una finestra a due ante da 120×140 cm (circa 1,4 mq di vetro) significa 50–90 euro in più; su un appartamento con 10–12 mq di finestre, 350–700 euro complessivi: il 10–15% del valore dei serramenti.</p>
          <p>Attenzione a due voci nascoste. La prima è la <strong>ferramenta</strong>: un'anta con triplo vetro pesa il 30–40% in più (fino a 25–30 kg al mq) e richiede cerniere e meccanismi rinforzati, che i preventivi seri includono di default. La seconda è il <strong>telaio</strong>: la vetrocamera da 44 mm richiede profili con sede vetro adeguata, il che in PVC orienta verso serie da 76–82 mm e in alluminio verso tagli termici evoluti. I dettagli sui prezzi completi, voce per voce, sono nell'articolo sui <a href="/serramenti-infissi/prezzi-infissi-al-mq-2026/">prezzi degli infissi al mq nel 2026</a>.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="abbinamenti">Triplo vetro, telaio e posa: il sistema completo</h2>
          <p>Il triplo vetro dà il meglio solo dentro un sistema coerente. La regola tecnica è che la trasmittanza del telaio (Uf) non dovrebbe essere peggiore di quella del vetro (Ug), altrimenti il profilo diventa la via di fuga del calore: con Ug 0,6 serve un telaio con Uf ≤ 1,0–1,1 W/mqK, quindi PVC a 6–7 camere, legno da 78–92 mm o alluminio a taglio termico spinto.</p>
          <p>Il secondo pilastro è la <strong>posa in opera</strong>: il giunto tra telaio e muratura va sigillato con il sistema a tre livelli (tenuta all'aria interna, isolamento intermedio, tenuta all'acqua esterna), possibilmente posando l'infisso in spalla al muro nel piano dell'isolante. Una finestra da 0,8 W/mqK posata male rende come una da 1,4 posata bene: è il motivo per cui i <a href="/serramenti-infissi/top-5-produttori-serramenti-italia/">produttori più seri</a> certificano la propria rete di posatori.</p>
          <blockquote>«Il triplo vetro non è un prodotto, è una scelta di sistema: vetro, telaio, ferramenta e posa devono essere pensati insieme. Comprare il vetro migliore e montarlo sul profilo più economico è come mettere gomme da neve su un'auto senza freni.»</blockquote>

          <h2 id="incentivi">Detrazioni 2026 per le finestre con triplo vetro</h2>
          <p>Le finestre con triplo vetro rientrano a pieno titolo nell'<a href="/incentivi-bonus/ecobonus-2026-come-funziona/">ecobonus 2026</a>: detrazione del 50% per l'abitazione principale e del 36% per le altre unità, massimale di 60.000 euro, a condizione di rispettare i limiti di trasmittanza Uw della zona climatica. Nelle zone E ed F il triplo vetro è spesso l'unico modo per rientrare nei limiti con finestre di grande formato; nelle zone centrali e meridionali un buon doppio vetro è sufficiente, e il triplo resta una scelta di comfort più che di conformità.</p>
          <p>Restano validi gli adempimenti consueti: bonifico parlante, schede tecniche con Uw certificato secondo UNI EN 14351-1 e <strong>trasmissione ENEA entro 90 giorni</strong> dalla fine dei lavori. Chi combina serramenti e cappotto nello stesso intervento può valutare con il tecnico il percorso agevolativo più favorevole, tenendo separati i computi delle spese.</p>
''',
    faq_title="Domande frequenti sul triplo vetro",
    faqs=[
        ("Il triplo vetro per le finestre conviene sempre?",
         "No. Il <strong>triplo vetro</strong> conviene nelle zone climatiche E ed F, con riscaldamento a bassa temperatura, nelle riqualificazioni profonde e per obiettivi di classe A o casa passiva. Nel Centro-Sud e nelle seconde case un doppio vetro basso emissivo di qualità offre un rapporto costo-beneficio migliore."),
        ("Quanto costa in più il triplo vetro rispetto al doppio?",
         "Nel 2026 il sovrapprezzo è di <strong>30–60 euro al mq</strong> di vetrata per le versioni standard e di 60–110 €/mq per quelle acustiche o di sicurezza. Su un appartamento tipo incide per 350–700 euro complessivi, pari al 10–15% del costo dei serramenti."),
        ("Il triplo vetro fa entrare meno luce in casa?",
         "Sì, in misura contenuta: la trasmissione luminosa scende da 78–80% del doppio vetro a <strong>70–74%</strong> del triplo. La differenza è appena percepibile su finestre normali, ma va valutata su aperture piccole o esposte a nord, dove ogni punto di luce naturale conta."),
        ("Il triplo vetro riduce anche il rumore?",
         "Non automaticamente: tre lastre uguali possono persino peggiorare alcune frequenze. Per l'acustica serve una <strong>vetrocamera asimmetrica con lastra stratificata</strong> (es. 44.1 stratificato), che raggiunge 38–42 dB di abbattimento. La dicitura da cercare in preventivo è «triplo vetro fonoassorbente»."),
        ("Serve un telaio speciale per il triplo vetro?",
         "Sì: la vetrocamera da 40–44 mm e il peso superiore del 30–40% richiedono <strong>profili con sede vetro adeguata e ferramenta rinforzata</strong>. In PVC servono serie da 76–82 mm, in alluminio tagli termici evoluti, in legno sezioni da 78 mm in su."),
    ],
    sources="<strong>Fonti:</strong> UNI EN 673 e UNI EN 14351-1 (prestazioni del vetro e marcatura CE); linee guida CasaClima sulla posa; ENEA — portale detrazioni; listini vetrai e serramentisti 2026. Valori Ug e temperature superficiali indicativi: variano per composizione e gas di riempimento. Contenuto a scopo informativo.",
    tags=[
        ("/serramenti-infissi/", "Triplo vetro"),
        ("/serramenti-infissi/", "Vetrocamera"),
        ("/incentivi-bonus/", "Ecobonus 2026"),
        ("/efficienza-energetica/", "Efficienza energetica"),
    ],
    related=[
        dict(url="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Serramenti in PVC, alluminio o legno: il confronto completo 2026",
             excerpt="Trasmittanze, prezzi e durata dei tre materiali a confronto, per scegliere il telaio giusto.", date="17 lug 2026", mins="10 min"),
        dict(url="/serramenti-infissi/prezzi-infissi-al-mq-2026/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Prezzi infissi al mq nel 2026: PVC, alluminio e legno a confronto",
             excerpt="Tutte le voci di costo, dalla ferramenta alla posa, con i prezzi medi aggiornati al 2026.", date="5 lug 2026", mins="9 min"),
        dict(url="/serramenti-infissi/top-5-produttori-serramenti-italia/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="I 5 migliori produttori di serramenti in Italia: qualità e prezzi",
             excerpt="Chi produce gli infissi migliori, come li abbiamo valutati e quanto costano.", date="28 giu 2026", mins="8 min"),
    ],
))


ARTICLES.append(dict(
    silo="serramenti-infissi", silo_name="Serramenti e Infissi", thumb="t-serramenti",
    slug="prezzi-infissi-al-mq-2026",
    url="https://www.ilcardine.it/serramenti-infissi/prezzi-infissi-al-mq-2026/",
    title_tag="Prezzi infissi al mq 2026: PVC, alluminio e legno",
    desc="Prezzi degli infissi al mq nel 2026: le fasce per PVC, alluminio e legno, le voci che compongono il preventivo e come risparmiare senza errori.",
    keywords="prezzi infissi al mq, costo infissi 2026, prezzo finestre pvc al mq, preventivo infissi, costo sostituzione finestre",
    og_desc="Quanto costano gli infissi al mq nel 2026: fasce di prezzo per PVC, alluminio e legno, voci di preventivo e errori da evitare.",
    tw_desc="Prezzi infissi al mq nel 2026: PVC, alluminio e legno a confronto, voce per voce.",
    h1="Prezzi infissi al mq nel 2026: PVC, alluminio e legno a confronto",
    standfirst="Da 280 a oltre 1.000 euro al metro quadro: la forbice dei prezzi degli infissi nel 2026 è ampia e capire cosa la determina è il primo passo per leggere un preventivo. Ecco le fasce reali per materiale, le voci che compongono il costo e dove ha senso investire.",
    kicker="Serramenti e Infissi · Prezzi 2026",
    breadcrumb_title="Prezzi infissi al mq nel 2026",
    author="Luca Bianchi", initials="LB",
    role="Redazione Il Cardine · Serramenti e involucro edilizio",
    bio="Giornalista tecnico, segue da oltre dodici anni serramenti, involucro edilizio e riqualificazione energetica. Per Il Cardine cura le guide su infissi, vetrocamere e prestazioni dell'involucro opaco e trasparente.",
    date_iso="2026-07-05T08:00:00+02:00", date_it="5 luglio 2026", minutes=9,
    aria_cover="prezzi degli infissi al metro quadro nel 2026",
    thumb_label="Serramenti e Infissi · Prezzi 2026",
    answer="Nel 2026 i <strong>prezzi degli infissi al mq</strong>, posa esclusa, sono indicativamente: PVC 280–480 €/mq, alluminio a taglio termico 450–750 €/mq, legno lamellare 500–850 €/mq, legno-alluminio 650–1.000 €/mq. La posa qualificata aggiunge il 15–25%. Una finestra a due ante in PVC posata costa 550–800 euro.",
    toc=[
        ("prezzi-medi", "Quanto costano gli infissi al mq nel 2026?"),
        ("voci-di-costo", "Cosa comprende il prezzo: le voci che fanno la differenza"),
        ("posa-in-opera", "Quanto incide la posa in opera sul costo finale?"),
        ("preventivo", "Come leggere un preventivo senza farsi ingannare"),
        ("esempi", "Tre esempi reali di preventivo"),
        ("risparmiare", "Come risparmiare senza rinunciare alla qualità"),
        ("detrazioni", "Detrazioni 2026: quanto si recupera"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="prezzi-medi">Quanto costano gli infissi al mq nel 2026?</h2>
          <p>I <strong>prezzi degli infissi al mq</strong> nel 2026 fotografano un mercato stabilizzato dopo gli anni turbolenti del Superbonus: i listini sono cresciuti dell'8–12% rispetto al 2022, trainati da materie prime e posa, ma la domanda più ordinata ha riportato i preventivi su tempi e margini normali. La tabella seguente riassume le fasce medie di mercato per una finestra a due ante con doppio vetro basso emissivo, fornitura senza posa.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Prezzi medi degli infissi al mq (Italia, 2026; fornitura, doppio vetro BE incluso, posa e IVA escluse)</caption>
            <thead>
              <tr><th>Materiale</th><th>Fascia economica</th><th>Fascia media</th><th>Fascia alta / design</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>PVC</strong></td><td>220–280 €/mq</td><td>280–480 €/mq</td><td>480–650 €/mq</td></tr>
              <tr><td><strong>Alluminio a taglio termico</strong></td><td>380–450 €/mq</td><td>450–750 €/mq</td><td>750–1.100 €/mq</td></tr>
              <tr><td><strong>Legno lamellare</strong></td><td>420–500 €/mq</td><td>500–850 €/mq</td><td>850–1.200 €/mq</td></tr>
              <tr><td><strong>Legno-alluminio</strong></td><td>600–700 €/mq</td><td>650–1.000 €/mq</td><td>1.000–1.400 €/mq</td></tr>
            </tbody>
          </table>
          </div>
          <p>Per tradurre in pratica: una <strong>finestra a due ante da 120×140 cm</strong> (1,68 mq) in PVC di fascia media costa 470–800 euro fornita, 550–950 posata; una <strong>portafinestra da 140×240 cm</strong> (3,36 mq) in alluminio a taglio termico 1.500–2.500 euro fornita; un <strong>alzante scorrevole da 300×240 cm</strong> in alluminio 4.000–7.000 euro, perché sui grandi scorrevoli il prezzo al mq sale invece di scendere. Per il confronto tecnico tra i materiali si veda la nostra guida <a href="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/">serramenti in PVC, alluminio o legno a confronto</a>.</p>
          <p>Le variabili geografiche contano: nei grandi centri del Nord i prezzi posati sono in media il 10–15% sopra la media nazionale, mentre al Sud la fornitura costa uguale ma la posa meno. Le differenze tra provincia e città si assottigliano per i grandi marchi nazionali, che lavorano a listini quasi uniformi attraverso la rete di rivenditori.</p>

          <h2 id="voci-di-costo">Cosa comprende il prezzo: le voci che fanno la differenza</h2>
          <p>Un preventivo di infissi si compone di cinque voci principali, e capirne il peso è il modo migliore per confrontare offerte apparentemente distanti:</p>
          <ul>
            <li><strong>Profilo e telaio (35–45% del costo)</strong>: la serie del profilo determina prestazioni e prezzo. In PVC si passa dai 220–280 €/mq delle serie da 60–70 mm ai 400 €/mq e oltre delle serie da 82–90 mm a 7 camere; in alluminio la differenza la fanno la profondità del taglio termico e lo spessore delle pareti.</li>
            <li><strong>Vetro (15–25%)</strong>: il doppio vetro basso emissivo con argon è ormai standard e incluso; il <a href="/serramenti-infissi/finestre-triplo-vetro-conviene/">triplo vetro</a> aggiunge 30–60 €/mq, lo stratificato acustico 25–50 €/mq, l'antieffrazione P2A 40–70 €/mq.</li>
            <li><strong>Ferramenta (10–15%)</strong>: cerniere a scomparsa, anta-ribalta microventilata, chiusure multipunto antieffrazione RC2: ogni upgrade vale 30–80 euro ad anta, e sui tripli vetri la ferramenta rinforzata non è un'opzione ma una necessità.</li>
            <li><strong>Finiture e accessori (10–20%)</strong>: colori RAL standard sono spesso inclusi; effetto legno, bicolore, verniciature speciali aggiungono 30–80 €/mq. Zanzariere, cassonetti coibentati, scuri e persiane sono voci separate che possono raddoppiare il conto.</li>
            <li><strong>Posa in opera (15–25%)</strong>: la trattiamo nel dettaglio nel paragrafo seguente, perché è la voce più sottovalutata e la più decisiva.</li>
          </ul>

          <h2 id="posa-in-opera">Quanto incide la posa in opera sul costo finale?</h2>
          <p>La posa rappresenta il 15–25% del costo complessivo: indicativamente <strong>80–150 euro al mq</strong> per una posa standard su vano regolare, 150–250 €/mq per la posa qualificata con sigillatura a tre livelli (nastri autoespandenti, membrane, isolamento del giunto). Su una finestra da 120×140 significa 130–420 euro: la forbice è larga e spiega gran parte delle differenze tra preventivi.</p>
          <p>La posa «vecchia maniera» — schiuma poliuretanica e silicone — costa meno ma vanifica le prestazioni: spifferi, condensa sul nodo, muffa sul davanzale interno entro pochi inverni. La posa certificata secondo la UNI 11673-1, con progettazione del nodo e materiali specifici, costa di più ma rende misurabili le prestazioni dichiarate. Chi installa con il <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico</a> dovrebbe sempre prevedere la posa in spalla, spostando l'infisso nel piano dell'isolante.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="preventivo">Come leggere un preventivo senza farsi ingannare</h2>
          <p>Tre segnali distinguono un preventivo serio da uno da cestinare. Primo: la <strong>specifica completa</strong> — serie del profilo, composizione della vetrocamera, valori Uw e Ug dichiarati, marca della ferramenta, classe di resistenza antieffrazione. Un preventivo che dice solo «finestra in PVC bianco» non è confrontabile con nulla. Secondo: la <strong>posa descritta per iscritto</strong>, con materiali e metodo. Terzo: la <strong>scomposizione tra fornitura e servizi</strong>, che permette di capire dove si concentra il margine.</p>
          <p>I prezzi «a corpo» per finestra, senza misure né specifiche, sono la prima causa di contenzioso: al sopralluogo emergono «imprevisti» — vani fuori squadra, davanzali da rifare, cassonetti da coibentare — che fanno lievitare il conto del 20–30%. La regola resta quella di sempre: tre preventivi sullo stesso capitolato, sopralluogo prima del prezzo finale, pagamenti scaglionati a stati di avanzamento.</p>

          <h2 id="esempi">Tre esempi reali di preventivo</h2>
          <div class="table-wrap">
          <table>
            <caption>Tabella 2 — Simulazioni di spesa complessiva (posa qualificata e IVA 10% incluse, 2026)</caption>
            <thead>
              <tr><th>Scenario</th><th>Composizione</th><th>Materiale</th><th>Spesa indicativa</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Bilocale 55 mq</strong></td><td>3 finestre 2 ante + 1 portafinestra</td><td>PVC fascia media</td><td>3.200–4.300 €</td></tr>
              <tr><td><strong>Trilocale 95 mq</strong></td><td>5 finestre + 2 portefinestre</td><td>PVC fascia alta o alluminio base</td><td>6.500–9.500 €</td></tr>
              <tr><td><strong>Villetta 140 mq</strong></td><td>8 finestre + 3 portefinestre + 1 alzante</td><td>Alluminio taglio termico, triplo vetro</td><td>18.000–26.000 €</td></tr>
            </tbody>
          </table>
          </div>
          <p>Con la detrazione del 50% questi importi si dimezzano nel recupero decennale: il trilocale di esempio scende a 3.250–4.750 euro netti, meno di una sostituzione «economica» senza incentivi di dieci anni fa, a fronte di prestazioni doppie.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="risparmiare">Come risparmiare senza rinunciare alla qualità</h2>
          <ol>
            <li><strong>Standardizzare misure e colori</strong>: finestre di dimensioni simili e finiture standard (bianco, grigio RAL di serie) tagliano i costi di produzione del 5–10%.</li>
            <li><strong>Concentrare il budget sul vetro e sulla posa</strong>, non sulle finiture: sono le voci che determinano comfort e bollette per i prossimi 30 anni.</li>
            <li><strong>Valutare il PVC di fascia alta prima di passare all'alluminio</strong>: a parità di prestazioni termiche costa il 25–35% in meno; l'alluminio si giustifica per grandi luci, design o contesti specifici.</li>
            <li><strong>Ordinare in bassa stagione</strong>: tra novembre e febbraio molti serramentisti applicano sconti del 5–15% e garantiscono tempi più rapidi.</li>
            <li><strong>Affidarsi a produttori con rete certificata</strong>: i <a href="/serramenti-infissi/top-5-produttori-serramenti-italia/">migliori produttori di serramenti in Italia</a> offrono garanzie estese che valgono più di uno sconto sul lungo periodo.</li>
          </ol>

          <h2 id="detrazioni">Detrazioni 2026: quanto si recupera</h2>
          <p>La sostituzione degli infissi è tra gli interventi coperti dall'<a href="/incentivi-bonus/ecobonus-2026-come-funziona/">ecobonus 2026</a>: detrazione del <strong>50%</strong> sulla prima casa (36% sulle altre unità) con massimale di 60.000 euro, recuperata in 10 rate annuali. Condizioni: rispetto dei limiti di trasmittanza della zona climatica, bonifico parlante e pratica ENEA entro 90 giorni. L'IVA agevolata al 10% si applica alla fornitura con posa in edilizia residenziale.</p>
          <p>Il calcolo finale cambia la prospettiva dei prezzi: una finestra in PVC da 800 euro posata costa al proprietario 400 euro netti distribuiti in dieci anni, cioè 40 euro l'anno per un componente che dura 30–40 anni e taglia le dispersioni del foro finestra del 60–70%. Pochi interventi edilizi hanno un rapporto altrettanto favorevole tra spesa netta, durata e risparmio energetico.</p>
''',
    faq_title="Domande frequenti sui prezzi degli infissi al mq",
    faqs=[
        ("Quanto costa al mq un infisso in PVC nel 2026?",
         "Nel 2026 un infisso in <strong>PVC costa 280–480 €/mq</strong> in fascia media, fornitura con doppio vetro basso emissivo inclusa e posa esclusa. Le serie economiche partono da 220 €/mq, le serie premium a 7 camere arrivano a 650 €/mq. La posa qualificata aggiunge 80–150 €/mq."),
        ("Perché i prezzi degli infissi al mq variano così tanto?",
         "La forbice dipende da cinque fattori: <strong>serie del profilo, tipo di vetro, ferramenta, finiture e posa</strong>. A questi si aggiungono il tipo di apertura (gli scorrevoli costano più al mq dei battenti) e le dimensioni: sulle finestre piccole il prezzo al mq sale perché i costi fissi si spalmano su meno superficie."),
        ("La posa in opera è compresa nei prezzi al mq?",
         "Di regola no: i listini si riferiscono alla fornitura. La <strong>posa aggiunge il 15–25%</strong> del costo (80–250 €/mq a seconda del livello) e va sempre richiesta per iscritto con descrizione del metodo. Diffidare dei prezzi «chiavi in mano» troppo bassi: spesso nascondono una posa sommaria."),
        ("Quanto costa cambiare le finestre di un trilocale nel 2026?",
         "Per un trilocale di 90–100 mq con 7 vani finestra la spesa posata è indicativamente di <strong>6.500–9.500 euro</strong> in PVC di fascia medio-alta o alluminio base, IVA 10% inclusa. Con la detrazione del 50% il costo netto scende a 3.250–4.750 euro recuperati in 10 anni."),
        ("Gli infissi comprati nel 2026 godono ancora delle detrazioni?",
         "Sì: l'ecobonus 2026 prevede la <strong>detrazione del 50%</strong> sulla prima casa (36% sulle seconde case) con massimale di 60.000 euro, a condizione di rispettare i limiti di trasmittanza Uw, pagare con bonifico parlante e trasmettere la pratica ENEA entro 90 giorni dalla fine lavori."),
    ],
    sources="<strong>Fonti:</strong> listini di produttori e rivenditori rilevati a giugno-luglio 2026; ANFIT; UNI 11673-1 (posa in opera dei serramenti); ENEA — portale detrazioni. I prezzi sono medie indicative nazionali: per il proprio caso richiedere sempre tre preventivi a parità di capitolato. Contenuto a scopo informativo.",
    tags=[
        ("/serramenti-infissi/", "Prezzi infissi"),
        ("/serramenti-infissi/", "PVC"),
        ("/serramenti-infissi/", "Alluminio"),
        ("/incentivi-bonus/", "Detrazioni 2026"),
    ],
    related=[
        dict(url="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Serramenti in PVC, alluminio o legno: il confronto completo 2026",
             excerpt="Trasmittanze, prezzi e durata dei tre materiali a confronto, per scegliere il telaio giusto.", date="17 lug 2026", mins="10 min"),
        dict(url="/serramenti-infissi/finestre-triplo-vetro-conviene/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Triplo vetro: quando conviene davvero e quanto costa in più",
             excerpt="Trasmittanze, comfort e sovrapprezzo reale: i casi in cui il triplo vetro si ripaga.", date="11 lug 2026", mins="8 min"),
        dict(url="/serramenti-infissi/top-5-produttori-serramenti-italia/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="I 5 migliori produttori di serramenti in Italia: qualità e prezzi",
             excerpt="Chi produce gli infissi migliori, come li abbiamo valutati e quanto costano.", date="28 giu 2026", mins="8 min"),
    ],
))


ARTICLES.append(dict(
    silo="serramenti-infissi", silo_name="Serramenti e Infissi", thumb="t-serramenti",
    slug="top-5-produttori-serramenti-italia",
    url="https://www.ilcardine.it/serramenti-infissi/top-5-produttori-serramenti-italia/",
    title_tag="Migliori produttori serramenti: la top 5 in Italia",
    desc="I migliori produttori di serramenti in Italia nel 2026: la top 5 per qualità, prestazioni e prezzo, con i criteri per scegliere il marchio giusto.",
    keywords="migliori produttori serramenti, marche infissi migliori, produttori finestre italia, serramenti di qualità, top marchi infissi",
    og_desc="La top 5 dei produttori di serramenti attivi in Italia: qualità, fasce di prezzo, reti di installazione e garanzie a confronto.",
    tw_desc="I 5 migliori produttori di serramenti in Italia: qualità e prezzi a confronto.",
    h1="I 5 migliori produttori di serramenti in Italia: qualità e prezzi",
    standfirst="Dietro una finestra che dura trent'anni c'è quasi sempre un marchio che progetta il sistema, certifica la posa e garantisce i ricambi. Abbiamo selezionato i cinque produttori di serramenti più solidi sul mercato italiano del 2026, valutando profili, reti di vendita, garanzie e rapporto qualità-prezzo.",
    kicker="Serramenti e Infissi · La classifica",
    breadcrumb_title="I 5 migliori produttori di serramenti in Italia",
    author="Elena Riva", initials="ER",
    role="Redazione Il Cardine · Materiali e sistemi costruttivi",
    bio="Giornalista tecnica, si occupa di materiali da costruzione, sistemi di facciata e mercato dei produttori. Per Il Cardine cura le classifiche di settore e le guide all'acquisto per cantieri e privati.",
    date_iso="2026-06-28T08:00:00+02:00", date_it="28 giugno 2026", minutes=8,
    aria_cover="i migliori produttori di serramenti in Italia",
    thumb_label="Serramenti e Infissi · Classifica",
    answer="Tra i <strong>migliori produttori di serramenti</strong> presenti in Italia spiccano nel 2026 Finstral, Internorm, Schüco, Oknoplast e Ponzio: coprono PVC, alluminio e sistemi misti, con prezzi da 300 a oltre 900 €/mq. La scelta dipende da materiale, budget e presenza locale di un installatore certificato dal marchio.",
    toc=[
        ("criteri", "Come abbiamo valutato i produttori"),
        ("classifica", "I 5 migliori produttori di serramenti: la classifica"),
        ("prezzi", "Quanto costano: le fasce di prezzo per marchio"),
        ("garanzie", "Garanzie, certificazioni e ricambi: cosa pretendere"),
        ("installatore", "Perché l'installatore conta quanto il marchio"),
        ("come-scegliere", "Come scegliere il produttore giusto per il proprio progetto"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="criteri">Come abbiamo valutato i produttori</h2>
          <p>Definire i <strong>migliori produttori di serramenti</strong> non significa stilare una classifica di gradimento, ma verificare cinque requisiti oggettivi: la qualità ingegneristica dei profili (progettati o solo assemblati), le prestazioni certificate secondo la UNI EN 14351-1, la capillarità e la formazione della rete di vendita e posa, le garanzie offerte su profili, ferramenta e vetro, e infine il rapporto tra prezzo e prestazioni. Solo i marchi che superano la soglia su tutti e cinque i fronti entrano nella nostra selezione.</p>
          <p>Un premessa necessaria: il mercato italiano dei serramenti vale oltre 4 miliardi di euro e conta migliaia di produttori, dai grandi gruppi internazionali alle eccellenze regionali. Questa top 5 non esaurisce la qualità disponibile — marchi come Navello, Fakro, Internorm o i migliori serramentisti locali fanno ottimi prodotti — ma fotografa i player con la combinazione più solida di prodotto, rete e assistenza sul territorio nazionale nel 2026.</p>

          <h2 id="classifica">I 5 migliori produttori di serramenti: la classifica</h2>
          <ol>
            <li><strong>Finstral (Bolzano) — il riferimento del PVC di fascia alta.</strong> Gruppo altoatesino con produzione integrata, dai profili alle vetrocamere, Finstral è il marchio che più ha spinto l'evoluzione del PVC in Italia: sistemi a 7 camere, anime rinforzate, finiture acriliche e una rete di oltre 1.000 rivenditori formati in azienda. Copre anche alluminio, legno-alluminio e i grandi scorrevoli. Punto di forza: la posa certificata dai propri centri. Fascia di prezzo: medio-alta (350–650 €/mq).</li>
            <li><strong>Internorm (Austria, forte presenza in Italia) — lo standard della casa passiva.</strong> Leader europeo della finestra ad alta efficienza, Internorm ha portato in Italia il triplo vetro di serie e i sistemi in PVC, PVC-alluminio e legno-alluminio certificabili Passivhaus, con Uw fino a 0,6 W/mqK. La rete di partner commerciali copre tutto il Nord e gran parte del Centro. Punto di forza: prestazioni e innovazione (finestre integrate con domotica e fotovoltaico). Fascia: alta (500–900 €/mq).</li>
            <li><strong>Schüco (Germania) — l'ingegneria dell'alluminio.</strong> Per progettisti e imprese Schüco è sinonimo di sistemi in alluminio: facciate continue, alzanti scorrevoli a tutta parete, profili minimal con nodi centrali ridottissimi e le serie AWS/ADS per il residenziale di pregio. Produce anche sistemi in PVC di fascia alta. Il marchio lavora attraverso serramentisti certificati che fabbricano su licenza. Punto di forza: grandi aperture e design architettonico. Fascia: medio-alta/alta (450–1.000 €/mq).</li>
            <li><strong>Oknoplast (Polonia, stabilimenti anche per il mercato italiano) — il miglior rapporto qualità-prezzo nel PVC.</strong> Tra i primi produttori europei di finestre in PVC, Oknoplast ha costruito la sua posizione su profili rinforzati in acciaio di serie, estetica curata (profilo squadrato, saldature quasi invisibili) e prezzi aggressivi. Rete di rivenditori molto capillare anche al Sud. Punto di forza: qualità percepita superiore al prezzo. Fascia: media (280–500 €/mq).</li>
            <li><strong>Ponzio (Piacenza) — l'alluminio italiano con l'anima green.</strong> Storica azienda emiliana specializzata in sistemi in alluminio, Ponzio combina profili a taglio termico evoluto, leghe con alta quota di alluminio riciclato e una filiera corta tutta italiana. Forte nelle scorrevoli e nelle soluzioni per la ristrutturazione, con verniciature certificate Qualicoat. Punto di forza: sostenibilità di filiera e assistenza tecnica al serramentista. Fascia: media-alta (420–800 €/mq).</li>
          </ol>

          <h2 id="prezzi">Quanto costano: le fasce di prezzo per marchio</h2>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — I 5 produttori a confronto (fasce indicative 2026, fornitura, posa esclusa)</caption>
            <thead>
              <tr><th>Produttore</th><th>Materiali principali</th><th>Fascia di prezzo</th><th>Ideale per</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Finstral</strong></td><td>PVC, alluminio, legno-alluminio</td><td>350–650 €/mq</td><td>Residenziale di qualità, riqualificazioni</td></tr>
              <tr><td><strong>Internorm</strong></td><td>PVC-alluminio, legno-alluminio</td><td>500–900 €/mq</td><td>Casa passiva, classe A, climi freddi</td></tr>
              <tr><td><strong>Schüco</strong></td><td>Alluminio, PVC fascia alta</td><td>450–1.000 €/mq</td><td>Grandi vetrate, design, facciate</td></tr>
              <tr><td><strong>Oknoplast</strong></td><td>PVC</td><td>280–500 €/mq</td><td>Sostituzioni con budget controllato</td></tr>
              <tr><td><strong>Ponzio</strong></td><td>Alluminio a taglio termico</td><td>420–800 €/mq</td><td>Ristrutturazioni, scorrevoli, edilizia sostenibile</td></tr>
            </tbody>
          </table>
          </div>
          <p>Per leggere queste cifre nel contesto completo — voci di preventivo, posa, esempi per tipologia di abitazione — rimandiamo all'articolo sui <a href="/serramenti-infissi/prezzi-infissi-al-mq-2026/">prezzi degli infissi al mq nel 2026</a>. Chi è indeciso sul materiale trova invece il quadro tecnico completo nel <a href="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/">confronto tra serramenti in PVC, alluminio e legno</a>.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="garanzie">Garanzie, certificazioni e ricambi: cosa pretendere</h2>
          <p>Oltre alla garanzia legale di conformità (2 anni), i produttori seri offrono garanzie estese scritte: <strong>10 anni sui profili</strong> in PVC e alluminio (verniciatura inclusa per i marchi migliori), 5–10 anni sulla ferramenta, 5 anni sulla vetrocamera contro difetti di fabbricazione e appannamento interno. Internorm e Finstral arrivano a 10 anni di assistenza completa attraverso la rete.</p>
          <p>Sul fronte documentale, pretendere sempre tre cose: la <strong>dichiarazione di prestazione (DoP)</strong> secondo UNI EN 14351-1 con i valori Uw misurati sul telaio finito, i <strong>certificati di resistenza antieffrazione</strong> (classi RC1N/RC2 dove richieste) e la disponibilità dei ricambi a magazzino per almeno 10 anni — la voce che distingue un sistema industriale da un prodotto assemblato. Le prestazioni dichiarate devono poi essere coerenti con i limiti richiesti dall'<a href="/incentivi-bonus/ecobonus-2026-come-funziona/">ecobonus 2026</a> per la propria zona climatica.</p>

          <h2 id="installatore">Perché l'installatore conta quanto il marchio</h2>
          <p>Tutti i produttori di questa classifica condividono una filosofia: il serramento arriva in cantiere attraverso una <strong>rete selezionata e formata</strong>. Non è un dettaglio commerciale ma tecnico: la stessa finestra Finstral posata da un centro certificato o da un posatore improvvisato offre prestazioni diverse del 30–50% su tenuta all'aria e ponti termici. Prima di firmare, verificare sul sito del produttore che il rivenditore sia in rete, e chiedere il riferimento della posa secondo UNI 11673-1.</p>
          <blockquote>«Comprare un marchio top e far posare le finestre al prezzo più basso trovato in zona è il modo più rapido per trasformare un ottimo prodotto in una finestra mediocre. Il sistema finestra finisce al giunto di posa, non alla battuta dell'anta.»</blockquote>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="come-scegliere">Come scegliere il produttore giusto per il proprio progetto</h2>
          <p>La scelta finale si riduce a un incrocio tra progetto e territorio. Per una <strong>riqualificazione energetica profonda</strong> con <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico</a> e obiettivo classe A, i sistemi Internorm e Finstral con <a href="/serramenti-infissi/finestre-triplo-vetro-conviene/">triplo vetro</a> sono la strada più lineare. Per <strong>grandi aperture e design contemporaneo</strong>, Schüco e Ponzio offrono i sistemi scorrevoli più maturi. Per <strong>sostituzioni standard con budget controllato</strong>, Oknoplast e le serie intermedie di Finstral coprono il miglior rapporto qualità-prezzo.</p>
          <p>In ogni caso la sequenza corretta resta immutata: diagnosi delle esigenze, sopralluogo, tre preventivi a parità di capitolato, verifica della rete di posa, contratto con specifiche e tempi scritti. Il marchio è la prima scrematura, non l'ultima parola.</p>
''',
    faq_title="Domande frequenti sui produttori di serramenti",
    faqs=[
        ("Quali sono i migliori produttori di serramenti in Italia?",
         "Tra i <strong>migliori produttori di serramenti</strong> presenti in Italia nel 2026 figurano Finstral (PVC e sistemi misti di fascia alta), Internorm (efficienza e casa passiva), Schüco (alluminio e grandi vetrate), Oknoplast (PVC con ottimo rapporto qualità-prezzo) e Ponzio (alluminio italiano sostenibile). La scelta dipende da materiale, budget e rete locale di installatori."),
        ("Quanto costano gli infissi dei marchi top di gamma?",
         "I marchi di fascia alta hanno prezzi indicativi di <strong>450–900 €/mq</strong> per la fornitura (Internorm e Schüco oltre, Oknoplast e le serie intermedie Finstral sotto), posa esclusa. Il sovrapprezzo rispetto ai prodotti di fascia bassa si ripaga in durata, garanzie estese e prestazioni certificate."),
        ("Meglio un produttore italiano o internazionale per gli infissi?",
         "Non è il passaporto a fare la differenza ma il <strong>sistema</strong>: progettazione dei profili, controlli di produzione, rete di posa e ricambi. Marchi internazionali come Finstral e Internorm producono in Italia o per il mercato italiano; marchi italiani come Ponzio competono alla pari su filiera e assistenza tecnica."),
        ("Che garanzie deve offrire un buon produttore di serramenti?",
         "Oltre alla garanzia legale di 2 anni, un produttore serio offre per iscritto <strong>10 anni sui profili, 5–10 anni sulla ferramenta e 5 anni sulla vetrocamera</strong>, la dichiarazione di prestazione secondo UNI EN 14351-1 e la disponibilità dei ricambi per almeno 10 anni."),
        ("Come verifico che un rivenditore sia autorizzato dal marchio?",
         "Ogni produttore della top 5 pubblica sul proprio sito la <strong>mappa dei rivenditori e posatori certificati</strong>: basta inserire il CAP. Diffidare di chi vende «il marchio» senza risultare in rete: la garanzia estesa e l'assistenza del produttore si attivano solo attraverso i canali ufficiali."),
    ],
    sources="<strong>Fonti:</strong> siti e documentazione tecnica dei produttori citati; ANFIT; UNI EN 14351-1 e UNI 11673-1; listini rilevati presso rivenditori a giugno 2026. La classifica riflette criteri editoriali indipendenti: Il Cardine non riceve compensi dai marchi citati. Contenuto a scopo informativo.",
    tags=[
        ("/serramenti-infissi/", "Produttori serramenti"),
        ("/serramenti-infissi/", "Marche infissi"),
        ("/serramenti-infissi/", "Classifica"),
        ("/incentivi-bonus/", "Ecobonus 2026"),
    ],
    related=[
        dict(url="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Serramenti in PVC, alluminio o legno: il confronto completo 2026",
             excerpt="Trasmittanze, prezzi e durata dei tre materiali a confronto, per scegliere il telaio giusto.", date="17 lug 2026", mins="10 min"),
        dict(url="/serramenti-infissi/finestre-triplo-vetro-conviene/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Triplo vetro: quando conviene davvero e quanto costa in più",
             excerpt="Trasmittanze, comfort e sovrapprezzo reale: i casi in cui il triplo vetro si ripaga.", date="11 lug 2026", mins="8 min"),
        dict(url="/serramenti-infissi/prezzi-infissi-al-mq-2026/", thumb="t-serramenti", label="Serramenti e Infissi", cat="Serramenti e Infissi",
             title="Prezzi infissi al mq nel 2026: PVC, alluminio e legno a confronto",
             excerpt="Tutte le voci di costo, dalla ferramenta alla posa, con i prezzi medi aggiornati al 2026.", date="5 lug 2026", mins="9 min"),
    ],
))


# ============================ MATERIALI-COSTRUZIONE ============================
ARTICLES.append(dict(
    silo="materiali-costruzione", silo_name="Materiali da Costruzione", thumb="t-materiali",
    slug="materiali-isolanti-confronto",
    url="https://www.ilcardine.it/materiali-costruzione/materiali-isolanti-confronto/",
    title_tag="Materiali isolanti termici a confronto: la guida 2026",
    desc="Materiali isolanti termici a confronto: EPS, lana di roccia, sughero e fibra di legno. Conducibilità, sfasamento, prezzi al mq e usi consigliati.",
    keywords="materiali isolanti termici, isolante per cappotto, eps o lana di roccia, sughero isolante, fibra di legno",
    og_desc="EPS, lana di roccia, sughero e fibra di legno a confronto: conducibilità, sfasamento estivo, prezzi e il miglior uso per ciascun materiale.",
    tw_desc="Materiali isolanti termici a confronto: EPS, lana di roccia, sughero e fibra di legno.",
    h1="Materiali isolanti a confronto: EPS, lana di roccia, sughero e fibra di legno",
    standfirst="Sintetici, minerali o naturali: i materiali isolanti termici non sono intercambiabili. Conducibilità, sfasamento estivo, reazione al fuoco e prezzo al mq cambiano molto tra EPS, lana di roccia, sughero e fibra di legno: ecco la comparazione completa per scegliere quello giusto.",
    kicker="Materiali da Costruzione · Confronto",
    breadcrumb_title="Materiali isolanti a confronto: EPS, lana di roccia, sughero e fibra di legno",
    author="Elena Riva", initials="ER",
    role="Redazione Il Cardine · Materiali e sistemi costruttivi",
    bio="Giornalista tecnica, si occupa di materiali da costruzione, sistemi di facciata e mercato dei produttori. Per Il Cardine cura le guide all'acquisto e le schede tecniche dei materiali per cantieri e privati.",
    date_iso="2026-07-16T08:00:00+02:00", date_it="16 luglio 2026", minutes=9,
    aria_cover="materiali isolanti termici a confronto",
    thumb_label="Materiali da Costruzione · Isolanti",
    answer="Tra i principali <strong>materiali isolanti termici</strong>, l'EPS isola meglio a parità di spesa (λ 0,031–0,038, 8–18 €/mq al mq in 10 cm), la lana di roccia aggiunge protezione al fuoco e acustica (λ 0,034–0,040), sughero e fibra di legno vincono su sfasamento estivo e sostenibilità (10–14 ore di ritardo termico) a prezzi 2–3 volte superiori.",
    toc=[
        ("come-si-valuta", "Come si valuta un isolante termico?"),
        ("eps", "EPS: il re del rapporto qualità-prezzo"),
        ("lana-di-roccia", "Lana di roccia: isolamento, fuoco e acustica"),
        ("sughero", "Sughero: il naturale per l'estate"),
        ("fibra-di-legno", "Fibra di legno: comfort estivo e bioedilizia"),
        ("tabella-confronto", "La tabella comparativa completa"),
        ("quale-scegliere", "Quale isolante scegliere per cappotto, parete e tetto?"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="come-si-valuta">Come si valuta un isolante termico?</h2>
          <p>Il confronto tra <strong>materiali isolanti termici</strong> si gioca su quattro parametri, non su uno. Il primo è la <strong>conducibilità termica λ</strong> (W/mK): più è bassa, minore lo spessore necessario a raggiungere una data trasmittanza. Il secondo è la <strong>densità</strong>, che determina lo sfasamento — il ritardo con cui il calore estivo attraversa la parete — decisivo per il comfort estivo: 10–12 ore di sfasamento significano che il picco di calore delle 14 arriva dentro quando fuori è ormai sera.</p>
          <p>Il terzo parametro è la <strong>reazione al fuoco</strong> (classi da A1, incombustibile, a F): vincolante per i cappotti sopra i 12 metri di altezza e per i locali con vie di fuga. Il quarto è il <strong>comportamento al vapore</strong> (μ): materiali traspiranti come fibra di legno e sughero gestiscono l'umidità in modo igroscopico, quelli a celle chiuse come l'EPS la bloccano. Il prezzo al mq — l'unico parametro che quasi tutti guardano — è in realtà il risultato degli altri quattro.</p>

          <h2 id="eps">EPS: il re del rapporto qualità-prezzo</h2>
          <p>Il polistirene espanso sinterizzato è il materiale dei cappotti italiani: copre oltre il 70% delle facciate isolate. La versione standard (λ 0,036–0,038 W/mK) e quella <strong>con grafite</strong> (λ 0,030–0,032) offrono la migliore prestazione invernale per euro speso: un pannello da 10 cm in grafite costa in cantiere 8–15 €/mq e porta una parete in laterizio degli anni Settanta da 1,3 a 0,25 W/mqK. Leggero, facile da tagliare, stabile: il cantiere lo ama.</p>
          <p>I limiti sono noti: reazione al fuoco classe E (nei sistemi a cappotto certificati ETAG 004 il problema è gestito dal rivestimento, ma sopra i 12 metri molti progettisti preferiscono alternative), densità bassa (15–25 kg/mc) che significa sfasamento estivo modesto, e origine fossile. Per le facciate nord e gli edifici in zone fredde resta però la scelta tecnicamente più razionale, soprattutto in abbinamento al <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico esterno</a> su edifici esistenti.</p>

          <h2 id="lana-di-roccia">Lana di roccia: isolamento, fuoco e acustica</h2>
          <p>La lana di roccia è un isolante minerale ottenuto dalla fusione di rocce basaltiche: classe <strong>A1 di reazione al fuoco</strong>, incombustibile per definizione, con λ di 0,034–0,040 W/mK. È il materiale obbligato dove il fuoco detta le regole — edifici alti, condomini con vie di fuga esterne, facciate ventilate — e il migliore dove conta l'acustica: la sua struttura fibrosa assorbe il rumore aereo come nessun pannello rigido sa fare.</p>
          <p>In cantiere costa il 30–50% in più dell'EPS (12–20 €/mq per i pannelli da cappotto da 10 cm a doppia densità) e richiede più attenzione in posa: i pannelli non devono comprimersi né bagnarsi. In compenso è traspirante, dimensionalmente stabile alle alte temperature e disponibile in densità da 40 a 150 kg/mc: le versioni ad alta densità offrono anche uno sfasamento estivo dignitoso, 7–9 ore con spessori da 12–14 cm.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="sughero">Sughero: il naturale per l'estate</h2>
          <p>Il sughero biondo espanso — ottenuto per agglomerazione a vapore della corteccia di quercia da sughero, senza collanti aggiunti — è l'isolante naturale con il pedigree più lungo: si usa in edilizia dagli anni Trenta. Conducibilità 0,037–0,045 W/mK, densità 110–130 kg/mc e sfasamento che con 12 cm supera le <strong>10–12 ore</strong>: nelle zone climatiche calde, dal Centro in giù, è la risposta più efficace al surriscaldamento estivo.</p>
          <p>Aggiunge qualità non trascurabili: stabilità dimensionale eccezionale, resistenza a muffe e insetti, durata misurata in decenni senza degrado e un bilancio ambientale che trattiene carbonio invece di emetterlo. Il prezzo è la controindicazione: 25–40 €/mq per 10 cm, due-tre volte l'EPS, anche se negli ultimi anni la produzione nazionale ha ammorbidito i listini. Si posa come un cappotto tradizionale e si rasatura con cicli specifici traspiranti.</p>

          <h2 id="fibra-di-legno">Fibra di legno: comfort estivo e bioedilizia</h2>
          <p>La fibra di legno è il materiale simbolo della bioedilizia: scarti di segheria pressati in pannelli da 50–265 kg/mc, λ 0,038–0,050 W/mK e una capacità termica che regala sfasamenti da <strong>10 a oltre 14 ore</strong> negli spessori da 14–16 cm. È l'isolante d'elezione per tetti e coperture — dove d'estate il calore picchia di più — e per le pareti in legno: si abbina naturalmente alle strutture in <a href="/materiali-costruzione/edilizia-legno-xlam/">XLAM</a> e a telaio, gestendo il vapore in modo igroscopico senza bisogno di freni al vapore calcolati al millimetro.</p>
          <p>I prezzi si collocano tra 20 e 45 €/mq per gli spessori da cappotto, con le versioni ad alta densità per tetti piani calpestabili nella parte alta del listino. La posa richiede fissaggi e rasature dedicate e nei climi umidi va protetta con cicli a base silicatica o silossanica. In cambio offre un comfort estivo che nessun isolante leggero riesce a eguagliare, e valori di trasmittanza pienamente in linea con i requisiti delle <a href="/normative/ntc-norme-tecniche-costruzioni/">norme tecniche</a> e del D.M. Requisiti Minimi.</p>

          <h2 id="tabella-confronto">La tabella comparativa completa</h2>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — I quattro isolanti a confronto (valori tipici 2026, pannelli da 10 cm)</caption>
            <thead>
              <tr><th>Materiale</th><th>Conducibilità λ</th><th>Densità</th><th>Sfasamento*</th><th>Reazione al fuoco</th><th>Prezzo indicativo</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>EPS / EPS grafite</strong></td><td>0,031–0,038 W/mK</td><td>15–25 kg/mc</td><td>4–6 ore</td><td>E (in sistema ETICS)</td><td>8–15 €/mq</td></tr>
              <tr><td><strong>Lana di roccia</strong></td><td>0,034–0,040 W/mK</td><td>40–150 kg/mc</td><td>6–9 ore</td><td>A1 (incombustibile)</td><td>12–20 €/mq</td></tr>
              <tr><td><strong>Sughero</strong></td><td>0,037–0,045 W/mK</td><td>110–130 kg/mc</td><td>10–12 ore</td><td>E</td><td>25–40 €/mq</td></tr>
              <tr><td><strong>Fibra di legno</strong></td><td>0,038–0,050 W/mK</td><td>50–265 kg/mc</td><td>10–14 ore</td><td>E</td><td>20–45 €/mq</td></tr>
            </tbody>
          </table>
          </div>
          <p><em>*Sfasamento stimato su parete tipo con 10–14 cm di isolante: il valore reale dipende dalla stratigrafia completa.</em></p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="quale-scegliere">Quale isolante scegliere per cappotto, parete e tetto?</h2>
          <ol>
            <li><strong>Cappotto su condominio, budget controllato, zone fredde</strong>: EPS con grafite. Massima efficienza invernale, costo minimo, cantiere veloce.</li>
            <li><strong>Edifici oltre 12 metri, facciate ventilate, requisiti antincendio</strong>: lana di roccia. La classe A1 semplifica la vita di progettisti e direttori lavori.</li>
            <li><strong>Centro-Sud, estati torride, edifici senza climatizzazione</strong>: sughero o fibra di legno. Lo sfasamento oltre le 10 ore vale più di un condizionatore in più.</li>
            <li><strong>Tetti, sottotetti e strutture in legno</strong>: fibra di legno ad alta densità, da sola o abbinata a lana di roccia nei pacchetti ventilati.</li>
            <li><strong>Murature in <a href="/materiali-costruzione/laterizi-blocchi-termici-guida/">blocchi termici di laterizio</a></strong>: lana di roccia o sughero, che rispettano la traspirabilità del supporto; l'EPS va valutato con verifica igrometrica.</li>
          </ol>
          <p>Qualunque sia il materiale, la soglia economica si sposta con le agevolazioni: gli isolamenti rientrano nell'<a href="/incentivi-bonus/ecobonus-2026-come-funziona/">ecobonus 2026</a> con detrazione del 50–65% secondo l'intervento, e nei cappotti che superano il 25% della superficie disperdente scatta l'obbligo di trasmittanza a norma. Il consiglio finale è quello di sempre: far verificare la stratigrafia da un termotecnico, perché l'isolante giusto nel posto sbagliato — tipico caso l'EPS su muri umidi controterra — può creare più problemi di quanti ne risolva.</p>
''',
    faq_title="Domande frequenti sui materiali isolanti termici",
    faqs=[
        ("Qual è il miglior materiale isolante termico?",
         "Non esiste un migliore assoluto: l'<strong>EPS con grafite</strong> vince sul rapporto prestazione invernale/prezzo, la <strong>lana di roccia</strong> su fuoco e acustica, <strong>sughero e fibra di legno</strong> su comfort estivo e sostenibilità. La scelta dipende da clima, stratigrafia della parete e vincoli di cantiere."),
        ("Meglio EPS o lana di roccia per il cappotto?",
         "Per prestazioni invernali e costo conviene l'<strong>EPS</strong> (λ fino a 0,031, 8–15 €/mq); dove servono incombustibilità, isolamento acustico o traspirabilità elevata conviene la <strong>lana di roccia</strong> (classe A1), che costa il 30–50% in più. Sopra i 12 metri di altezza molti capitolati la rendono obbligatoria."),
        ("Quanto costa al mq un isolante naturale come il sughero?",
         "Il <strong>sughero biondo espanso</strong> costa indicativamente 25–40 €/mq nel pannello da 10 cm, due-tre volte l'EPS. Il prezzo si giustifica con sfasamento estivo di 10–12 ore, durata pluri-decennale e assenza di collanti: nelle zone calde si ripaga con il minore uso del condizionatore."),
        ("Gli isolanti naturali isolano peggio dei sintetici?",
         "No: la conducibilità di <strong>sughero e fibra di legno</strong> (0,037–0,050 W/mK) è solo leggermente superiore a quella dell'EPS, e si compensa con 1–2 cm di spessore in più. Sul fronte estivo, la loro densità molto maggiore offre invece prestazioni che i materiali sintetici leggeri non raggiungono."),
        ("Gli isolanti termici rientrano nell'ecobonus 2026?",
         "Sì: l'isolamento delle pareti rientra nell'<strong>ecobonus 2026</strong> con detrazione del 50% sulla prima casa (65% per gli interventi trainanti sulle parti comuni condominiali), a condizione di rispettare le trasmittanze limite del D.M. Requisiti Minimi e di trasmettere la pratica ENEA entro 90 giorni."),
    ],
    sources="<strong>Fonti:</strong> UNI EN 13162-13171 (specifiche dei prodotti isolanti); ETAG 004 per i sistemi ETICS; D.M. Requisiti Minimi; ANIT — associazione nazionale isolamento termico; listini produttori 2026. Valori di conducibilità e sfasamento tipici: verificare sempre le schede tecniche del singolo prodotto. Contenuto a scopo informativo.",
    tags=[
        ("/materiali-costruzione/", "Isolanti termici"),
        ("/materiali-costruzione/", "EPS"),
        ("/materiali-costruzione/", "Lana di roccia"),
        ("/efficienza-energetica/", "Cappotto termico"),
    ],
    related=[
        dict(url="/materiali-costruzione/edilizia-legno-xlam/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Case in legno XLAM: costi, tempi di cantiere e prestazioni antisismiche",
             excerpt="Struttura a pannelli incrociati: quanto costa, quanto dura il cantiere e come si comporta col sisma.", date="9 lug 2026", mins="9 min"),
        dict(url="/materiali-costruzione/laterizi-blocchi-termici-guida/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Blocchi in laterizio termici: guida a murature portanti e tramezzi",
             excerpt="Foratura, conducibilità e posa: come funzionano le murature monostrato ad alta efficienza.", date="25 giu 2026", mins="8 min"),
        dict(url="/materiali-costruzione/calcestruzzo-tipologie-usi/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Tipi di calcestruzzo: classi di resistenza, usi e prezzi al metro cubo",
             excerpt="Dalle classi C alle miscele speciali: quale calcestruzzo per ogni struttura e quanto costa.", date="1 lug 2026", mins="8 min"),
    ],
))


ARTICLES.append(dict(
    silo="materiali-costruzione", silo_name="Materiali da Costruzione", thumb="t-materiali",
    slug="edilizia-legno-xlam",
    url="https://www.ilcardine.it/materiali-costruzione/edilizia-legno-xlam/",
    title_tag="Case in legno XLAM: costi, tempi e antisismica",
    desc="Case in legno XLAM: costi al mq, tempi di cantiere, prestazioni antisismiche ed energetiche. Guida completa alla costruzione in pannelli CLT.",
    keywords="case in legno xlam, costo casa xlam, edilizia in legno clt, casa antisismica legno, tempi costruzione casa legno",
    og_desc="Case in legno XLAM: quanto costano al mq, quanto dura il cantiere e come si comportano col sisma. Guida tecnica aggiornata al 2026.",
    tw_desc="Case in legno XLAM: costi, tempi di cantiere e prestazioni antisismiche.",
    h1="Case in legno XLAM: costi, tempi di cantiere e prestazioni antisismiche",
    standfirst="Pannelli di legno massiccio a strati incrociati, cantieri di pochi mesi e prestazioni antisismiche certificate: le case in XLAM sono passate da nicchia alpina a sistema costruttivo maturo. Ecco costi reali al mq, tempi veri di costruzione e i limiti da conoscere prima di scegliere.",
    kicker="Materiali da Costruzione · Sistemi costruttivi",
    breadcrumb_title="Case in legno XLAM: costi, tempi e prestazioni antisismiche",
    author="Elena Riva", initials="ER",
    role="Redazione Il Cardine · Materiali e sistemi costruttivi",
    bio="Giornalista tecnica, si occupa di materiali da costruzione, sistemi di facciata e mercato dei produttori. Per Il Cardine cura le guide ai sistemi costruttivi, dal legno strutturale ai laterizi evoluti.",
    date_iso="2026-07-09T08:00:00+02:00", date_it="9 luglio 2026", minutes=9,
    aria_cover="case in legno XLAM a pannelli di legno lamellare incrociato",
    thumb_label="Materiali da Costruzione · Legno XLAM",
    answer="Una <strong>casa in legno XLAM</strong> chiavi in mano costa nel 2026 indicativamente 1.500–2.200 €/mq, con tempi di cantiere di 4–7 mesi grazie alla prefabbricazione. I pannelli a strati incrociati offrono eccellente comportamento antisismico (leggerezza + duttilità dei collegamenti) e involucro ad alta efficienza, a fronte di un costo del 5–15% superiore al tradizionale.",
    toc=[
        ("cos-e-xlam", "Cos'è l'XLAM e come funziona"),
        ("costi", "Quanto costa una casa in XLAM al mq?"),
        ("tempi", "Quanto dura il cantiere? I tempi reali"),
        ("antisismica", "Le prestazioni antisismiche delle case in XLAM"),
        ("prestazioni-energetiche", "Efficienza energetica e comfort"),
        ("limiti", "I limiti e gli errori da evitare"),
        ("confronto", "XLAM o costruzione tradizionale: quale scegliere?"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="cos-e-xlam">Cos'è l'XLAM e come funziona</h2>
          <p>L'<strong>XLAM</strong> — acronimo di cross-laminated timber, in italiano legno lamellare a strati incrociati o CLT — è un pannello strutturale di legno massiccio composto da tavole sovrapposte a fibre incrociate a 90 gradi, incollate sotto pressione in strati dispari (3, 5 o 7). Il risultato è un elemento piano che lavora in due direzioni: le <strong>case in legno XLAM</strong> lo usano come parete portante, solaio e copertura, trasformando l'intero edificio in una scatola lignea monolitica.</p>
          <p>La differenza rispetto alla costruzione tradizionale è industriale: i pannelli vengono progettati al millimetro in ufficio tecnico, tagliati a controllo numerico in stabilimento — complete di fori per porte, finestre e tracce impiantistiche — e montati in cantiere con gru e viti strutturali. Il cantiere diventa un assemblaggio: niente getti, niente stagionature, niente tempi morti legati alle malte. Il sistema è nato in Austria negli anni Novanta e in Italia ha trovato terreno fertile dopo il sisma del 2009, quando la ricostruzione ha premiato la leggerezza del legno.</p>
          <p>Nel 2026 l'Italia conta una filiera matura: produttori nazionali di pannelli, centri di lavoro diffusi tra Nord e Centro, e un patrimonio di edifici realizzati che supera le diecimila unità, comprese scuole, residenze e palazzi fino a 8–9 piani.</p>

          <h2 id="costi">Quanto costa una casa in XLAM al mq?</h2>
          <p>Nel 2026 il costo chiavi in mano di una casa unifamiliare in XLAM si colloca tra <strong>1.500 e 2.200 euro al mq</strong>, fondazioni e opere esterne escluse, con finiture di fascia media. La struttura portante a pannelli incide per il 20–25% del totale: circa 350–550 €/mq di superficie lorda, comprensivi di pannelli, trasporto, montaggio e viteria strutturale. Le fasce variano per zona (il Centro-Nord con filiera vicina costa meno), complessità architettonica e livello di prefabbricazione scelto.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Struttura di costo di una casa in XLAM (valori medi 2026, villa unifamiliare 140 mq)</caption>
            <thead>
              <tr><th>Voce</th><th>Incidenza</th><th>Importo indicativo</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Struttura XLAM + montaggio</strong></td><td>20–25%</td><td>50.000–75.000 €</td><td>Pannelli, trasporto, gru, viteria</td></tr>
              <tr><td><strong>Fondazioni in c.a.</strong></td><td>8–12%</td><td>20.000–30.000 €</td><td>Platea o plinti, come il tradizionale</td></tr>
              <tr><td><strong>Involucro e finiture</strong></td><td>30–35%</td><td>65.000–90.000 €</td><td>Cappotto, copertura, serramenti, rivestimenti</td></tr>
              <tr><td><strong>Impianti</strong></td><td>20–25%</td><td>50.000–70.000 €</td><td>Elettrico, idraulico, VMC, riscaldamento</td></tr>
            </tbody>
          </table>
          </div>
          <p>Rispetto a una costruzione in latero-cemento di pari livello, il sovrapprezzo è nell'ordine del <strong>5–15%</strong>, ma il confronto va fatto a parità di prestazioni: le case in XLAM nascono quasi sempre in classe A4 con <a href="/materiali-costruzione/materiali-isolanti-confronto/">isolanti ad alta densità</a> nel pacchetto di parete, mentre il tradizionale in classe A richiede cappotti e contropareti che ne erodono il vantaggio di costo. I pacchetti parete si completano spesso con <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico esterno</a> in fibra di legno o lana di roccia, lasciando il legno a vista all'interno.</p>

          <h2 id="tempi">Quanto dura il cantiere? I tempi reali</h2>
          <p>La prefabbricazione comprime i tempi in modo misurabile. Per una villa di 120–160 mq la sequenza tipica è: <strong>2–4 mesi</strong> di progettazione esecutiva e produzione in stabilimento (che corrono in parallelo alle fondazioni), <strong>10–20 giorni</strong> per il montaggio della struttura grezza — la casa «in piedi» si vede in due-tre settimane — e 3–5 mesi per copertura, serramenti, impianti e finiture. Totale: <strong>4–7 mesi</strong> dalla platea alla consegna, contro i 12–18 di un cantiere tradizionale.</p>
          <p>I tempi certi sono il vero valore economico: il computo si chiude in fabbrica, le varianti in corso d'opera quasi spariscono e il rischio di sforare il budget si riduce drasticamente. È il motivo per cui l'XLAM domina nella ricostruzione post-sisma e negli appalti di edilizia scolastica, dove le scadenze non sono negoziabili.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="antisismica">Le prestazioni antisismiche delle case in XLAM</h2>
          <p>Il comportamento antisismico è il punto di forza documentato meglio: nel 2007 il CNR-IVALSA testò su tavola vibrante a Giappone un edificio XLAM di 7 piani a grandezza naturale, che superò senza danni strutturali la scossa di Kobe. La spiegazione fisica è duplice: il legno pesa un <strong>quinto del calcestruzzo</strong>, quindi le forze sismiche — proporzionali alla massa — sono molto minori; e i collegamenti metallici (viti, piastre, hold-down) dissipano energia deformandosi, dando al sistema la duttilità che la muratura non ha.</p>
          <p>Le scatole XLAM si comportano da diaframmi rigidi: pareti e solai lavorano insieme e i carichi orizzontali si ridistribuiscono su tutta la struttura. La progettazione segue le <a href="/normative/ntc-norme-tecniche-costruzioni/">Norme Tecniche per le Costruzioni</a> e l'Eurocodice 5 con i capitoli dedicati al CLT: la criticità non è mai il pannello, praticamente indistruttibile, ma il <strong>dettaglio dei collegamenti</strong> — ancoraggi alla platea, giunzioni parete-parete e parete-solaio — che devono essere calcolati e posati a regola d'arte.</p>
          <blockquote>«In zona sismica la domanda giusta non è "il legno resiste?" — è dimostrato che resiste benissimo — ma "chi progetta i collegamenti?". Un edificio XLAM è forte quanto il suo ancoraggio più debole.»</blockquote>

          <h2 id="prestazioni-energetiche">Efficienza energetica e comfort</h2>
          <p>Una parete XLAM da 10 cm ha da sola una trasmittanza di circa 0,8 W/mqK, insufficiente per gli standard attuali: il pacchetto si completa con 14–20 cm di isolante — fibra di legno, lana di roccia o sughero — portando la parete a 0,14–0,20 W/mqK, da casa passiva. Il legno aggiunge due qualità che i numeri non colgono: <strong>inerzia igrometrica</strong> (assorbe e rilascia umidità, stabilizzando il clima interno) e sfasamento estivo elevato grazie alla massa del pannello.</p>
          <p>Il punto critico è la <strong>tenuta all'aria</strong>: le giunzioni tra pannelli e i passaggi impiantistici vanno sigillati con nastri e guaine dedicate, obiettivo n50 sotto 1,5 ricambi/ora al blower door test. Abbinata alla ventilazione meccanica controllata e a <a href="/serramenti-infissi/serramenti-pvc-alluminio-legno-confronto/">serramenti ad alte prestazioni</a>, la casa XLAM consuma per il riscaldamento il 70–85% in meno di un edificio tradizionale anni Ottanta.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="limiti">I limiti e gli errori da evitare</h2>
          <ul>
            <li><strong>Umidità in cantiere</strong>: i pannelli non devono restare scoperti sotto la pioggia per settimane; serve un piano di protezione e una copertura rapida. L'umidità residua va misurata prima della chiusura dei pacchetti.</li>
            <li><strong>Acustica</strong>: il legno è leggero e i rumori da calpestio viaggiano; solai a secco con masse flottanti e controsoffitti sono parte del progetto, non optional.</li>
            <li><strong>Protezione al fuoco</strong>: l'XLAM carbonizza in modo prevedibile (circa 0,65 mm/minuto) e mantiene la portanza sotto lo strato carbonizzato, ma le classi REI richiedono spessori e rivestimenti calcolati.</li>
            <li><strong>Modifiche in corso d'opera</strong>: spostare una traccia dopo la produzione dei pannelli costa caro; il progetto impiantistico va congelato prima della lavorazione.</li>
            <li><strong>Filiera</strong>: affidarsi a produttori con certificazione CE strutturale dei pannelli e a imprese con referenze documentabili in costruzioni a secco.</li>
          </ul>

          <h2 id="confronto">XLAM o costruzione tradizionale: quale scegliere?</h2>
          <p>L'XLAM conviene quando pesano tempi certi, prestazioni antisismiche, obiettivi energetici spinti e sostenibilità (ogni metro cubo di legno stoccato sottrae all'atmosfera circa 0,9 tonnellate di CO₂ equivalente). Il latero-cemento resta competitivo su edilizia standard in zone non sismiche con budget molto tirati, e conserva il vantaggio dell'inerzia acustica «gratuita» della massa. Chi cerca una via di mezzo può valutare i sistemi ibridi — struttura XLAM con nuclei in <a href="/materiali-costruzione/calcestruzzo-tipologie-usi/">calcestruzzo</a> — ormai diffusi negli edifici multipiano, o le murature portanti in <a href="/materiali-costruzione/laterizi-blocchi-termici-guida/">blocchi termici di laterizio</a> per chi preferisce restare sul costruito tradizionale.</p>
''',
    faq_title="Domande frequenti sulle case in legno XLAM",
    faqs=[
        ("Quanto costa una casa in legno XLAM nel 2026?",
         "Nel 2026 una <strong>casa in XLAM chiavi in mano</strong> costa indicativamente 1.500–2.200 €/mq, fondazioni escluse, con la struttura a pannelli che pesa per 350–550 €/mq. Il sovrapprezzo rispetto al tradizionale è del 5–15%, compensato da tempi dimezzati e prestazioni energetiche di classe A."),
        ("Le case in legno XLAM sono sicure in caso di terremoto?",
         "Sì, sono tra le più sicure: il legno pesa un quinto del calcestruzzo, riducendo le forze sismiche, e i collegamenti metallici dissipano l'energia del sisma. I test su edifici XLAM di 7 piani hanno superato senza danni la scossa di Kobe. La progettazione segue le NTC e l'Eurocodice 5."),
        ("Quanto dura una casa in legno XLAM?",
         "Se protetta da umidità e progettata correttamente, una casa in XLAM ha una <strong>vita utile di 50–100 anni</strong>, paragonabile al costruito tradizionale. I punti di attenzione sono la protezione dall'acqua in cantiere e in esercizio e la manutenzione dei rivestimenti esterni."),
        ("Le case in legno bruciano più facilmente?",
         "No: l'XLAM carbonizza in modo lento e prevedibile (circa 0,65 mm al minuto) e mantiene la capacità portante sotto lo strato carbonizzato, a differenza dell'acciaio che collassa per calore. Le classi REI si raggiungono con spessori e rivestimenti calcolati in fase di progetto."),
        ("Si può costruire in XLAM ovunque in Italia?",
         "Sì, l'XLAM è un sistema strutturale a tutti gli effetti e può essere autorizzato in ogni zona, compresa quella sismica 1. Servono progetto strutturale firmato da un ingegnere, collaudo e rispetto delle NTC; i vincoli paesaggistici riguardano solo le finiture esterne, non la tecnologia costruttiva."),
    ],
    sources="<strong>Fonti:</strong> CNR-IVALSA — progetto SOFIE (test sismici su edifici CLT); NTC e Circolare applicativa, capitolo legno strutturale; Eurocodice 5; Consiglio Nazionale delle Ricerche e Assolegno per i dati di filiera; listini produttori XLAM 2026. Contenuto a scopo informativo.",
    tags=[
        ("/materiali-costruzione/", "Legno XLAM"),
        ("/materiali-costruzione/", "CLT"),
        ("/normative/", "Antisismica"),
        ("/efficienza-energetica/", "Casa passiva"),
    ],
    related=[
        dict(url="/materiali-costruzione/materiali-isolanti-confronto/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Materiali isolanti a confronto: EPS, lana di roccia, sughero e fibra di legno",
             excerpt="Conducibilità, sfasamento e prezzi: quale isolante per ogni pacchetto parete.", date="16 lug 2026", mins="9 min"),
        dict(url="/materiali-costruzione/calcestruzzo-tipologie-usi/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Tipi di calcestruzzo: classi di resistenza, usi e prezzi al metro cubo",
             excerpt="Dalle classi C alle miscele speciali: quale calcestruzzo per ogni struttura e quanto costa.", date="1 lug 2026", mins="8 min"),
        dict(url="/materiali-costruzione/laterizi-blocchi-termici-guida/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Blocchi in laterizio termici: guida a murature portanti e tramezzi",
             excerpt="Foratura, conducibilità e posa: come funzionano le murature monostrato ad alta efficienza.", date="25 giu 2026", mins="8 min"),
    ],
))


ARTICLES.append(dict(
    silo="materiali-costruzione", silo_name="Materiali da Costruzione", thumb="t-materiali",
    slug="calcestruzzo-tipologie-usi",
    url="https://www.ilcardine.it/materiali-costruzione/calcestruzzo-tipologie-usi/",
    title_tag="Tipi di calcestruzzo: classi, usi e prezzi al mc",
    desc="Tipi di calcestruzzo: classi di resistenza C, usi per ogni struttura e prezzi al metro cubo nel 2026. Guida completa con tabella e consigli di getto.",
    keywords="tipi di calcestruzzo, classi di resistenza calcestruzzo, prezzo calcestruzzo al mc, calcestruzzo c25/30, tipologie cls",
    og_desc="Classi di resistenza, miscele speciali e prezzi al metro cubo: la guida completa ai tipi di calcestruzzo aggiornata al 2026.",
    tw_desc="Tipi di calcestruzzo: classi di resistenza, usi e prezzi al metro cubo nel 2026.",
    h1="Tipi di calcestruzzo: classi di resistenza, usi e prezzi al metro cubo",
    standfirst="C20/25, C28/35, fibrorinforzato, autocompattante, drenante: dietro la sigla «cls» si nasconde una famiglia di materiali molto diversi per prestazioni e prezzo. La guida per capire quale calcestruzzo serve a ogni struttura, quanto costa al metro cubo nel 2026 e come non sbagliare il getto.",
    kicker="Materiali da Costruzione · Guida tecnica",
    breadcrumb_title="Tipi di calcestruzzo: classi, usi e prezzi al mc",
    author="Elena Riva", initials="ER",
    role="Redazione Il Cardine · Materiali e sistemi costruttivi",
    bio="Giornalista tecnica, si occupa di materiali da costruzione, sistemi di facciata e mercato dei produttori. Per Il Cardine cura le schede tecniche dei materiali strutturali e le guide al cantiere.",
    date_iso="2026-07-01T08:00:00+02:00", date_it="1 luglio 2026", minutes=8,
    aria_cover="tipi di calcestruzzo e classi di resistenza",
    thumb_label="Materiali da Costruzione · Calcestruzzo",
    answer="I principali <strong>tipi di calcestruzzo</strong> si distinguono per classe di resistenza: C20/25 per fondazioni semplici, C25/30 e C28/35 per strutture portanti in zona sismica, C32/40 e superiori per pilastri e opere speciali. Nel 2026 il prezzo al metro cubo pompato va da 110 a 160 €/mc, più 40–90 €/mc per le miscele speciali.",
    toc=[
        ("classi-resistenza", "Classi di resistenza: cosa significano le sigle"),
        ("tabella-classi", "Le classi e gli usi: la tabella completa"),
        ("miscele-speciali", "I calcestruzzi speciali: fibrorinforzato, SCC, drenante e alleggerito"),
        ("prezzi", "Quanto costa il calcestruzzo al metro cubo nel 2026?"),
        ("come-si-sceglie", "Come si sceglie la classe giusta?"),
        ("getto-stagionatura", "Getto e stagionatura: dove si gioca la qualità"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="classi-resistenza">Classi di resistenza: cosa significano le sigle</h2>
          <p>Quando si parla di <strong>tipi di calcestruzzo</strong>, il primo criterio è la <strong>classe di resistenza</strong>, definita dalla norma UNI EN 206 con la sigla C seguita da due numeri: il primo è la resistenza caratteristica cilindrica a compressione (fck), il secondo quella cubica, entrambe in N/mmq (MPa) a 28 giorni di maturazione. Un <strong>C25/30</strong> — la classe più diffusa nell'edilizia residenziale — garantisce 25 MPa su provino cilindrico e 30 su cubo.</p>
          <p>La classe non è un vezzo da tecnici: è il dato che il progettista strutturale fissa nel progetto, che la direzione lavori verifica sui provini prelevati in cantiere e che il collaudatore controlla prima di firmare. Le <a href="/normative/ntc-norme-tecniche-costruzioni/">Norme Tecniche per le Costruzioni</a> impongono per le strutture in c.a. un minimo di C20/25 (Rck ≥ 25 MPa), salito di fatto a C25/30 o C28/35 nelle zone sismiche, dove la duttilità richiede calcestruzzi più performanti e controllati.</p>
          <p>Oltre alla resistenza, la EN 206 classifica il calcestruzzo per <strong>classi di esposizione</strong> (XC per la carbonatazione, XD per i cloruri, XF per il gelo, XA per gli ambienti aggressivi), consistenza (S1–S5), massimo diametro dell'aggregato e tenore di cloruri. Una fornitura completa si ordina con tutti questi parametri, non con la sola sigla C.</p>

          <h2 id="tabella-classi">Le classi e gli usi: la tabella completa</h2>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Classi di calcestruzzo, usi tipici e prezzi indicativi (2026, fornitura con pompa, IVA esclusa)</caption>
            <thead>
              <tr><th>Classe</th><th>Resistenza cilindrica</th><th>Usi tipici</th><th>Prezzo indicativo al mc</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>C8/10 – C12/15</strong></td><td>8–12 MPa</td><td>Magrone, sottofondi, riempimenti</td><td>95–115 €/mc</td></tr>
              <tr><td><strong>C16/20</strong></td><td>16 MPa</td><td>Fondazioni semplici non armate, opere secondarie</td><td>100–120 €/mc</td></tr>
              <tr><td><strong>C20/25</strong></td><td>20 MPa</td><td>Minimo NTC per c.a., platee, travi di fondazione</td><td>105–125 €/mc</td></tr>
              <tr><td><strong>C25/30</strong></td><td>25 MPa</td><td>Strutture residenziali: pilastri, travi, solai</td><td>110–135 €/mc</td></tr>
              <tr><td><strong>C28/35</strong></td><td>28 MPa</td><td>Zone sismiche, strutture slanciate, muri controterra</td><td>115–140 €/mc</td></tr>
              <tr><td><strong>C32/40 e superiori</strong></td><td>32+ MPa</td><td>Pilastri molto caricati, opere speciali, prefabbricati</td><td>130–165 €/mc</td></tr>
            </tbody>
          </table>
          </div>

          <h2 id="miscele-speciali">I calcestruzzi speciali: fibrorinforzato, SCC, drenante e alleggerito</h2>
          <p>La seconda famiglia di tipi riguarda le <strong>miscele speciali</strong>, pensate per problemi specifici:</p>
          <ul>
            <li><strong>Calcestruzzo fibrorinforzato (FRC)</strong>: fibre d'acciaio o polimeriche nella miscela che sostituiscono in tutto o in parte la rete elettrosaldata. È lo standard per pavimentazioni industriali, piazzali e massetti strutturali: elimina il punto debole della rete posata male e migliora la resistenza a fessurazione e urto. Sovrapprezzo: 25–50 €/mc.</li>
            <li><strong>Calcestruzzo autocompattante (SCC)</strong>: si espande nei casseri senza vibratore, riempiendo armature fitte e forme complesse senza nidi di ghiaia. Indispensabile su strutture sottili o molto armate; richiede casseri perfettamente stagni. Sovrapprezzo: 30–60 €/mc.</li>
            <li><strong>Calcestruzzo drenante</strong>: senza inerte fine, lascia passare l'acqua (oltre 300 litri al mq al minuto). Lo usiamo per piazzali, parcheggi e piste ciclabili dove la norma chiede superfici permeabili. Prezzo: 140–190 €/mc posato.</li>
            <li><strong>Calcestruzzo alleggerito</strong> (argilla espansa, polistirolo): densità da 400 a 1.800 kg/mc per alleggerire solai, formare pendenze e migliorare l'isolamento di coperture e sottofondi. Prezzo: 120–180 €/mc.</li>
            <li><strong>Calcestruzzo impermeabile e per ambienti aggressivi</strong>: con additivi cristallizzanti o a ridotto rapporto acqua/cemento per vasche, muri controterra e opere in classe XA/XD.</li>
          </ul>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="prezzi">Quanto costa il calcestruzzo al metro cubo nel 2026?</h2>
          <p>Nel 2026 il calcestruzzo preconfezionato di classe strutturale costa tra <strong>110 e 160 euro al mc</strong> consegnato con autobetoniera, IVA esclusa, con la pompa che aggiunge 150–350 euro a getto o 3–6 €/mc. Le variabili sono la distanza dall'impianto (ogni 10 km possono aggiungere 5–10 €/mc), i quantitativi (sotto i 3–4 mc scattano maggiorazioni per il viaggio a vuoto) e la stagione, con i picchi di prezzo nei mesi di piena attività cantieristica.</p>
          <p>Per mettere in scala: la platea di una villetta da 140 mq richiede 15–20 mc di C25/30, cioè 1.800–2.800 euro di materiale; la struttura completa in c.a. della stessa casa ne assorbe 45–60 mc per 6.000–9.000 euro. In alternativa, le strutture in <a href="/materiali-costruzione/edilizia-legno-xlam/">legno XLAM</a> spostano il budget dalla materia prima alla prefabbricazione, mentre chi costruisce in muratura portante trova nel nostro articolo sui <a href="/materiali-costruzione/laterizi-blocchi-termici-guida/">blocchi termici in laterizio</a> il confronto sul sistema portante.</p>

          <h2 id="come-si-sceglie">Come si sceglie la classe giusta?</h2>
          <p>La risposta breve: <strong>non la sceglie il cliente, la sceglie il progettista</strong>. La classe deriva dal calcolo strutturale — carichi, luci, zona sismica, aggressività ambientale — e dalla durabilità richiesta: un muro controterra in classe XC2/XA1 richiede copriferri maggiori e rapporto acqua/cemento più basso di un solaio interno in XC1. Ordinare una classe superiore «per sicurezza» non è gratis né innocuo: più cemento significa più calore di idratazione, più ritiro e più fessurazione se la stagionatura non segue.</p>
          <p>Ciò che il committente deve invece pretendere è la <strong>tracciabilità</strong>: bolla di consegna con classe, consistenza e classe di esposizione; prelievo dei provini a norma (una serie ogni 100 mc o frazione di getto omogeneo); e conservazione dei certificati di controllo di produzione dell'impianto, che per legge opera sotto controllo del Servizio Tecnico Centrale.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="getto-stagionatura">Getto e stagionatura: dove si gioca la qualità</h2>
          <p>Lo stesso identico calcestruzzo può dare una struttura perfetta o una da demolire a seconda di getto e stagionatura. Le regole che non ammettono eccezioni:</p>
          <ol>
            <li><strong>Mai aggiungere acqua in cantiere</strong>: ogni 10 litri al mc fanno crollare la resistenza di 2–3 MPa e aprono la strada alla fessurazione. Se la consistenza non basta, si ordina una classe S superiore.</li>
            <li><strong>Getto per strati di 50–60 cm</strong> con vibrazione a immersione continua, senza separazioni tra gli strati; niente lancio da altezze superiori a 1,5 metri che segrega gli inerti.</li>
            <li><strong>Stagionatura umida per almeno 4–7 giorni</strong>: il calcestruzzo raggiunge la resistenza di progetto a 28 giorni solo se non disidrata nei primi. In estate si bagna o si copre con teli; sotto i 5 °C si protegge dal gelo.</li>
            <li><strong>Disarmo nei tempi giusti</strong>: i casseri verticali dopo 12–24 ore, quelli portanti di solai e travi solo quando la resistenza misurata sui provini lo consente — mai a calendario.</li>
          </ol>
          <blockquote>«Il calcestruzzo è l'unico materiale strutturale che viene fabbricato in cantiere: la qualità non la decide l'impianto che lo produce, ma chi lo getta, lo vibra e lo stagiona nei primi sette giorni.»</blockquote>
          <p>Chi ristruttura invece di costruire ex novo trova nel recupero delle strutture esistenti un capitolo a parte: i getti di integrazione e le solette collaboranti richiedono calcestruzzi tixotropici o autocompattanti specifici, spesso abbinati alla verifica del <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico</a> per chiudere il cerchio tra sicurezza strutturale ed efficienza energetica.</p>
''',
    faq_title="Domande frequenti sui tipi di calcestruzzo",
    faqs=[
        ("Quali sono i principali tipi di calcestruzzo?",
         "I <strong>tipi di calcestruzzo</strong> si dividono per classe di resistenza (da C8/10 per i magroni a C32/40 e oltre per opere speciali) e per miscela: ordinario, fibrorinforzato, autocompattante (SCC), drenante, alleggerito e impermeabile. La scelta spetta al progettista strutturale in base a carichi, zona sismica ed esposizione ambientale."),
        ("Cosa significa la sigla C25/30 sul calcestruzzo?",
         "La sigla C25/30 indica la <strong>classe di resistenza a compressione</strong> a 28 giorni: 25 MPa misurati su provino cilindrico e 30 MPa su provino cubico. È la classe più usata nelle strutture residenziali in c.a. e supera il minimo C20/25 richiesto dalle NTC per il calcestruzzo armato."),
        ("Quanto costa un metro cubo di calcestruzzo nel 2026?",
         "Nel 2026 il calcestruzzo strutturale preconfezionato costa <strong>110–160 euro al mc</strong> consegnato, IVA esclusa; il pompaggio aggiunge 150–350 euro a getto. Le miscele speciali (fibrorinforzato, SCC, drenante) comportano sovrapprezzi di 25–60 €/mc, i piccoli quantitativi maggiorazioni fisse."),
        ("Si può aggiungere acqua al calcestruzzo in cantiere?",
         "No: aggiungere acqua in autobetoniera è la causa principale di calcestruzzi fuori specifica. Ogni 10 litri al mc riducono la resistenza di 2–3 MPa e aumentano ritiro e fessurazione. Se serve più lavorabilità va ordinata una <strong>classe di consistenza superiore</strong> o un SCC in fase d'ordine."),
        ("Quanto tempo impiega il calcestruzzo a fare presa?",
         "La presa iniziale avviene in 2–6 ore, ma la resistenza cresce nel tempo: circa il 60–70% a 7 giorni e il <strong>100% di progetto a 28 giorni</strong>, solo con stagionatura umida corretta. Il disarmo dei casseri portanti va deciso sulla resistenza misurata sui provini, non sul calendario."),
    ],
    sources="<strong>Fonti:</strong> UNI EN 206 (specifiche del calcestruzzo); NTC e Circolare applicativa per le classi minime nelle strutture in c.a.; ATECAP — dati di settore sul preconfezionato; listini impianti di betonaggio rilevati a giugno 2026. I prezzi sono medie indicative nazionali. Contenuto a scopo informativo.",
    tags=[
        ("/materiali-costruzione/", "Calcestruzzo"),
        ("/materiali-costruzione/", "Classi di resistenza"),
        ("/normative/", "NTC"),
        ("/materiali-costruzione/", "Strutture"),
    ],
    related=[
        dict(url="/materiali-costruzione/laterizi-blocchi-termici-guida/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Blocchi in laterizio termici: guida a murature portanti e tramezzi",
             excerpt="Foratura, conducibilità e posa: come funzionano le murature monostrato ad alta efficienza.", date="25 giu 2026", mins="8 min"),
        dict(url="/materiali-costruzione/edilizia-legno-xlam/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Case in legno XLAM: costi, tempi di cantiere e prestazioni antisismiche",
             excerpt="Struttura a pannelli incrociati: quanto costa, quanto dura il cantiere e come si comporta col sisma.", date="9 lug 2026", mins="9 min"),
        dict(url="/materiali-costruzione/materiali-isolanti-confronto/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Materiali isolanti a confronto: EPS, lana di roccia, sughero e fibra di legno",
             excerpt="Conducibilità, sfasamento e prezzi: quale isolante per ogni pacchetto parete.", date="16 lug 2026", mins="9 min"),
    ],
))


ARTICLES.append(dict(
    silo="materiali-costruzione", silo_name="Materiali da Costruzione", thumb="t-materiali",
    slug="laterizi-blocchi-termici-guida",
    url="https://www.ilcardine.it/materiali-costruzione/laterizi-blocchi-termici-guida/",
    title_tag="Blocchi termici laterizio: murature portanti e tramezzi",
    desc="Blocchi termici in laterizio: tipologie, foratura, prestazioni termiche e acustiche, posa e prezzi per murature portanti e tramezzi. Guida 2026.",
    keywords="blocchi termici laterizio, laterizi porizzati, murature monostrato, blocchi per murature portanti, tramezzi in laterizio",
    og_desc="Blocchi termici in laterizio: come funzionano le murature monostrato, prestazioni termiche e acustiche, posa e prezzi aggiornati al 2026.",
    tw_desc="Blocchi termici in laterizio: guida a murature portanti e tramezzi, con prezzi 2026.",
    h1="Blocchi in laterizio termici: guida a murature portanti e tramezzi",
    standfirst="Porizzati, a giunti sottili, con foratura spinta: i blocchi termici in laterizio hanno trasformato il mattone da materiale tradizionale a sistema costruttivo ad alta efficienza. Come funzionano le murature monostrato, cosa chiedono le norme e quanto costano nel 2026.",
    kicker="Materiali da Costruzione · Laterizi",
    breadcrumb_title="Blocchi in laterizio termici: guida completa",
    author="Elena Riva", initials="ER",
    role="Redazione Il Cardine · Materiali e sistemi costruttivi",
    bio="Giornalista tecnica, si occupa di materiali da costruzione, sistemi di facciata e mercato dei produttori. Per Il Cardine cura le schede tecniche dei materiali e le guide ai sistemi murari.",
    date_iso="2026-06-25T08:00:00+02:00", date_it="25 giugno 2026", minutes=8,
    aria_cover="blocchi termici in laterizio per murature portanti",
    thumb_label="Materiali da Costruzione · Laterizi",
    answer="I <strong>blocchi termici in laterizio</strong> sono elementi in argilla porizzata con foratura fino all'80% e alveoli sottili, che portano la conducibilità a 0,08–0,18 W/mK. Permettono murature portanti monostrato da 30–38 cm con trasmittanze di 0,22–0,35 W/mqK, ottima inerzia e isolamento acustico, a 35–70 €/mq posati.",
    toc=[
        ("cosa-sono", "Cosa sono i blocchi termici in laterizio"),
        ("tipologie", "Le tipologie: porizzati, a giunti sottili, alleggeriti"),
        ("murature-portanti", "Murature portanti monostrato: come funzionano"),
        ("tramezzi", "Tramezzi e pareti interne in laterizio"),
        ("prestazioni", "Prestazioni termiche, acustiche e al fuoco"),
        ("posa-prezzi", "Posa in opera e prezzi nel 2026"),
        ("faq", "Domande frequenti"),
    ],
    body='''
          <h2 id="cosa-sono">Cosa sono i blocchi termici in laterizio</h2>
          <p>I <strong>blocchi termici in laterizio</strong> sono la versione evoluta del mattone forato: elementi in argilla cotta con <strong>impasto porizzato</strong> — la farina fossile o fibre vegetali aggiunte alla pasta bruciano in cottura lasciando micropori — e una geometria di fori che può superare il 70–80% della sezione, con setti sottilissimi e alveoli che interrompono i ponti termici. Il risultato è un blocco che isola quasi come un isolante leggero (λ 0,08–0,18 W/mK contro gli 0,40–0,60 del laterizio tradizionale) mantenendo la capacità portante richiesta alle murature strutturali.</p>
          <p>La logica del sistema è la <strong>muratura monostrato</strong>: un unico strato di blocco da 30–38 cm che assolve insieme portanza, isolamento, inerzia e protezione al fuoco, senza cappotto esterno né intercapedine. È la risposta del laterizio a due esigenze del costruire contemporaneo: eliminare i ponti termici di giunzione tra strutture e tamponamento, e semplificare il cantiere riducendo strati, fasi e possibilità di errore.</p>

          <h2 id="tipologie">Le tipologie: porizzati, a giunti sottili, alleggeriti</h2>
          <p>La famiglia si divide in tre grandi gruppi, più le varianti prestazionali:</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Tipologie di blocchi in laterizio e usi (valori tipici 2026)</caption>
            <thead>
              <tr><th>Tipologia</th><th>Spessori</th><th>Conducibilità λ</th><th>Uso principale</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Blocchi porizzati termici</strong></td><td>25–38 cm</td><td>0,12–0,18 W/mK</td><td>Murature portanti monostrato</td></tr>
              <tr><td><strong>Blocchi a giunti sottili (rettificati)</strong></td><td>25–38 cm</td><td>0,10–0,15 W/mK</td><td>Murature portanti senza malta orizzontale</td></tr>
              <tr><td><strong>Blocchi alleggeriti con isolante</strong></td><td>30–42 cm</td><td>0,08–0,11 W/mK</td><td>Climi freddi, classe A senza cappotto</td></tr>
              <tr><td><strong>Forati da tramezzo</strong></td><td>8–12 cm</td><td>0,25–0,35 W/mK</td><td>Pareti divisorie interne</td></tr>
              <tr><td><strong>Doppio UNI / elementi portanti standard</strong></td><td>12–25 cm</td><td>0,30–0,50 W/mK</td><td>Murature portanti tradizionali, setti</td></tr>
            </tbody>
          </table>
          </div>
          <p>La frontiera più interessante è quella dei blocchi <strong>rettificati a giunto sottile</strong>: le facce di appoggio sono rettificate al decimo di millimetro e la posa avviene con un velo di colla da 1–3 mm invece dei 10–15 mm di malta tradizionale. Il giunto orizzontale — che nella muratura classica è un ponte termico continuo — praticamente sparisce, la posa si velocizza del 30–40% e la parete risulta omogenea. Alcune serie integrano negli alveoli pannellini di <a href="/materiali-costruzione/materiali-isolanti-confronto/">isolante minerale o sughero</a>, spingendo la conducibilità equivalente sotto 0,10 W/mK.</p>

          <h2 id="murature-portanti">Murature portanti monostrato: come funzionano</h2>
          <p>Nella muratura portante monostrato il blocco termico sostituisce il binomio struttura + tamponamento: la parete stessa porta i solai. La resistenza meccanica si misura con la <strong>resistenza caratteristica a compressione della muratura (fk)</strong>, che i produttori certificano secondo la UNI EN 771-1 e le prove di laboratorio: i blocchi ad alta resistenza (fbk 10–18 N/mmq) permettono edifici fino a 3–4 piani anche in zona sismica, nel rispetto delle <a href="/normative/ntc-norme-tecniche-costruzioni/">Norme Tecniche per le Costruzioni</a> e del capitolo 7.8 delle NTC dedicato alle murature.</p>
          <p>In zona sismica il sistema si completa con <strong>cerchiature armate</strong> — cordoli in c.a. a ogni impalcato — e con l'ancoraggio dei solai, spesso realizzati con travetti e pignatte in laterizio (latero-cemento) per continuità igrometrica. Il dettaglio decisivo resta l'angolo e l'incrocio delle pareti: i produttori forniscono elementi speciali sagomati che eliminano i ponti termici e le discontinuità strutturali, e la loro corretta posa fa la differenza tra una parete che lavora e una che fessura.</p>
          <p>Per chi valuta l'alternativa a secco, il confronto naturale è con le <a href="/materiali-costruzione/edilizia-legno-xlam/">case in legno XLAM</a>: la muratura monostrato è più lenta in cantiere ma offre inerzia termica e acustica senza stratificazioni, e non richiede protezioni particolari all'umidità durante la costruzione.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="tramezzi">Tramezzi e pareti interne in laterizio</h2>
          <p>Sulle pareti interne il laterizio gioca ancora la partita contro cartongesso e blocchi in calcestruzzo. I <strong>forati da tramezzo</strong> da 8, 10 e 12 cm restano la scelta più diffusa nel residenziale tradizionale: massa superficiale di 80–110 kg/mq, buon isolamento acustico tra vani contigui (Rw 40–44 dB con intonaco su entrambi i lati), superficie dura che accetta tasselli e pensili senza rinforzi, e stabilità nel tempo che il cartongesso standard non eguaglia.</p>
          <p>La regola pratica 2026 è selettiva: laterizio dove servono carichi appesi, resistenza all'urto e acustica (cucine, bagni, pareti tra camere e zona giorno), cartongesso dove contano velocità, tracce impiantistiche e futura riconfigurazione. Nei bagni, le versioni in <strong>blocco pieno alleggerito o in calcestruzzo vibrocompresso</strong> sono preferibili dove si prevedono sanitari sospesi pesanti.</p>

          <h2 id="prestazioni">Prestazioni termiche, acustiche e al fuoco</h2>
          <p>Una muratura monostrato da 30 cm in blocco termico raggiunge trasmittanze di <strong>0,28–0,35 W/mqK</strong>; con 38 cm e blocchi alleggeriti si scende a 0,20–0,24, in fascia con i requisiti delle zone climatiche fredde senza cappotto. Dove i limiti del D.M. Requisiti Minimi o gli obiettivi di classe A4 chiedono di più, la risposta è il <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico esterno</a> su supporto in laterizio: un matrimonio tecnicamente felice, perché il blocco offre un fondo stabile, planare e traspirante per l'incollaggio dei pannelli.</p>
          <p>Sul fronte acustico, la massa del laterizio paga: una parete monostrato da 30 cm intonacata supera i <strong>50 dB di isolamento tra alloggi</strong>, e i sistemi a doppia parete con intercapedine e lana minerale arrivano a 58–62 dB. Quanto al fuoco, l'argilla cotta è per definizione classe A1: le murature in blocco termico offrono resistenze EI da 60 a 180 minuti a seconda dello spessore, senza rivestimenti aggiuntivi. Inerzia estiva, infine: con 10–12 ore di sfasamento la muratura spessa in laterizio resta il riferimento per il comfort estivo passivo del Centro-Sud.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="posa-prezzi">Posa in opera e prezzi nel 2026</h2>
          <p>Nel 2026 i blocchi termici portanti costano alla fornitura <strong>18–35 €/mq</strong> di parete (la fascia alta per i rettificati alleggeriti con isolante), e la muratura finita — blocco, colla o malta, intonaco — si attesta tra <strong>35 e 70 €/mq</strong> per le monostrato, contro i 45–85 €/mq del sistema tradizionale telaio + tamponamento doppio. I forati da tramezzo costano 6–11 €/mq alla fornitura, 20–35 €/mq intonacati.</p>
          <p>Tre raccomandazioni di cantiere chiudono il quadro. Primo: la posa a giunto sottile richiede <strong>prima fila perfettamente in bolla</strong> e manodopera formata dal produttore; il risparmio di malta non compensa gli errori di planarità. Secondo: le tracce impiantistiche vanno progettate — i blocchi da 30–38 cm accettano scanalature limitate per non intaccare portanza e isolamento — e qui il coordinamento con gli impiantisti conta quanto il blocco. Terzo: la scelta del sistema murario va fatta in fase di progetto strutturale, perché cambiano fondazioni, cordoli e nodi, con verifiche che seguono le stesse NTC citate per il <a href="/materiali-costruzione/calcestruzzo-tipologie-usi/">calcestruzzo strutturale</a>.</p>
          <blockquote>«La muratura monostrato in blocco termico è il sistema che risponde alla domanda più difficile dell'edilizia: come isolare senza cappotto, senza pannelli e senza stratificazioni, usando un materiale che i cantieri italiani conoscono da due secoli.»</blockquote>
''',
    faq_title="Domande frequenti sui blocchi termici in laterizio",
    faqs=[
        ("Cosa sono i blocchi termici in laterizio?",
         "I <strong>blocchi termici in laterizio</strong> sono elementi in argilla porizzata con foratura fino al 70–80% e alveoli ottimizzati, con conducibilità di 0,08–0,18 W/mK. Permettono murature portanti monostrato che uniscono portanza, isolamento termico, inerzia e protezione al fuoco in un unico strato da 25–42 cm."),
        ("Una parete monostrato in laterizio isola abbastanza?",
         "Con 30 cm di blocco termico si ottengono trasmittanze di 0,28–0,35 W/mqK; con 38 cm e blocchi alleggeriti si arriva a 0,20–0,24, adeguato a gran parte delle zone climatiche italiane. Per gli obiettivi più spinti (classe A4, zone E–F) si integra con un cappotto esterno su supporto in laterizio."),
        ("I blocchi termici in laterizio sono portanti?",
         "Sì: i blocchi portanti hanno resistenza caratteristica fbk di 5–18 N/mmq e permettono edifici fino a 3–4 piani, anche in zona sismica se completati con cordoli armati e ancoraggi secondo le NTC. La portata dichiarata deve risultare dalla marcatura CE secondo UNI EN 771-1."),
        ("Quanto costa una muratura in blocchi termici nel 2026?",
         "Nel 2026 una muratura monostrato in blocchi termici costa finita — blocco, giunti e intonaco — <strong>35–70 €/mq</strong>, con la fornitura dei blocchi tra 18 e 35 €/mq. I tramezzi in forato costano 20–35 €/mq intonacati. I prezzi variano per tipologia di blocco e zona."),
        ("Meglio tramezzi in laterizio o in cartongesso?",
         "Dipende dall'uso: il <strong>laterizio</strong> vince su acustica (40–44 dB), resistenza all'urto e capacità di reggere carichi appesi (pensili, sanitari sospesi); il <strong>cartongesso</strong> su velocità di posa, peso e facilità di passaggio impianti. La soluzione più diffusa combina entrambi per ambiente."),
    ],
    sources="<strong>Fonti:</strong> UNI EN 771-1 (specifiche degli elementi per muratura); NTC capitolo 7.8 (costruzioni in muratura); ANDIL — dati di settore laterizi; D.M. Requisiti Minimi per le trasmittanze limite; listini produttori 2026. Contenuto a scopo informativo.",
    tags=[
        ("/materiali-costruzione/", "Laterizi"),
        ("/materiali-costruzione/", "Blocchi termici"),
        ("/materiali-costruzione/", "Murature"),
        ("/efficienza-energetica/", "Efficienza energetica"),
    ],
    related=[
        dict(url="/materiali-costruzione/materiali-isolanti-confronto/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Materiali isolanti a confronto: EPS, lana di roccia, sughero e fibra di legno",
             excerpt="Conducibilità, sfasamento e prezzi: quale isolante per ogni pacchetto parete.", date="16 lug 2026", mins="9 min"),
        dict(url="/materiali-costruzione/edilizia-legno-xlam/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Case in legno XLAM: costi, tempi di cantiere e prestazioni antisismiche",
             excerpt="Struttura a pannelli incrociati: quanto costa, quanto dura il cantiere e come si comporta col sisma.", date="9 lug 2026", mins="9 min"),
        dict(url="/materiali-costruzione/calcestruzzo-tipologie-usi/", thumb="t-materiali", label="Materiali da Costruzione", cat="Materiali da Costruzione",
             title="Tipi di calcestruzzo: classi di resistenza, usi e prezzi al metro cubo",
             excerpt="Dalle classi C alle miscele speciali: quale calcestruzzo per ogni struttura e quanto costa.", date="1 lug 2026", mins="8 min"),
    ],
))

# ============================ RUN ============================
if __name__ == "__main__":
    print(f"{'file':70s} {'chars':>7s} {'words':>7s}")
    for a in ARTICLES:
        path, chars, words = build(a)
        rel = os.path.relpath(path, ROOT)
        print(f"{rel:70s} {chars:7d} {words:7d}")
