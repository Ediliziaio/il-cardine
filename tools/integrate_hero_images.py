#!/usr/bin/env python3
"""Integrazione immagini hero WebP + PWA leggera per Il Cardine."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "assets" / "img"
SITE = "https://www.ilcardine.it"
LOGO_ABS = f"{SITE}/assets/logo.png"

SILOS = ["ristrutturazioni", "serramenti-infissi", "efficienza-energetica",
         "materiali-costruzione", "impianti", "incentivi-bonus",
         "tecnologie-innovazione", "normative"]

# ---------- mappa articoli: slug -> (silo, path, h1) ----------
articles = {}
for silo in SILOS:
    for d in sorted((ROOT / silo).iterdir()):
        if d.is_dir() and (d / "index.html").exists():
            slug = d.name
            html = (d / "index.html").read_text(encoding="utf-8")
            m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
            h1 = re.sub(r"<[^>]+>", "", m.group(1)).strip()
            h1 = re.sub(r"\s+", " ", h1)
            articles[slug] = {"silo": silo, "path": d / "index.html", "h1": h1}

assert len(articles) == 33, f"attesi 33 articoli, trovati {len(articles)}"
for slug in articles:
    assert (IMG_DIR / f"{slug}.webp").exists(), f"immagine mancante: {slug}.webp"

def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")

report = {"articles_ok": [], "cards_home": 0, "cards_categorie": 0,
          "cards_related": 0, "pwa_pages": 0, "warnings": []}

# ---------- pattern card con thumb CSS ----------
CARD_RE = re.compile(
    r'<a href="/([a-z0-9-]+)/([a-z0-9-]+)/">\s*'
    r'<div class="thumb [^"]*"><span class="thumb-label">[^<]*</span></div>\s*</a>')

def convert_cards(html, counter_key, hero_slug=None, hero_alt=None):
    """Sostituisce i thumb CSS delle card con <img>. hero_slug -> fetchpriority."""
    def repl(m):
        slug = m.group(2)
        if slug not in articles or not (IMG_DIR / f"{slug}.webp").exists():
            return m.group(0)  # mantieni thumb CSS
        if hero_slug and slug == hero_slug and "ar-16-9" in m.group(0):
            img = (f'<a href="/{articles[slug]["silo"]}/{slug}/">'
                   f'<img src="/assets/img/{slug}.webp" alt="{esc(hero_alt)}" '
                   f'width="1200" height="675" fetchpriority="high" class="thumb-img"></a>')
        else:
            img = (f'<a href="/{articles[slug]["silo"]}/{slug}/">'
                   f'<img src="/assets/img/{slug}.webp" alt="{esc(articles[slug]["h1"])}" '
                   f'width="1200" height="675" loading="lazy" class="thumb-img"></a>')
        report[counter_key] += 1
        return img
    return CARD_RE.sub(repl, html)

def fix_head_image(html, slug):
    """og:image + dimensioni + twitter:image + JSON-LD NewsArticle.image."""
    new_url = f"{SITE}/assets/img/{slug}.webp"
    old_meta = f'<meta property="og:image" content="{LOGO_ABS}">'
    assert old_meta in html, "og:image logo non trovato"
    new_meta = (f'<meta property="og:image" content="{new_url}">\n'
                f'  <meta property="og:image:width" content="1200">\n'
                f'  <meta property="og:image:height" content="675">')
    html = html.replace(old_meta, new_meta, 1)
    # twitter:image (non presente nel sito: lo aggiungiamo dopo twitter:card)
    if 'name="twitter:image"' not in html:
        tw_card = '<meta name="twitter:card" content="summary_large_image">'
        assert tw_card in html, "twitter:card non trovato"
        html = html.replace(
            tw_card,
            tw_card + f'\n  <meta name="twitter:image" content="{new_url}">', 1)
    return html

# ---------- TASK 1: articoli ----------
HERO_RE = re.compile(
    r'<figure class="thumb [^"]*"[^>]*>\s*<span class="thumb-label">[^<]*</span>\s*</figure>')

for slug, a in articles.items():
    p = a["path"]
    html = p.read_text(encoding="utf-8")

    # a) hero figure al posto del thumb segnaposto (stessa posizione: dopo meta-bar, prima di answer-box)
    hero = (f'<figure class="article-hero">\n'
            f'            <img src="/assets/img/{slug}.webp" alt="{esc(a["h1"])}" '
            f'width="1200" height="675" fetchpriority="high">\n'
            f'          </figure>')
    html, n = HERO_RE.subn(hero, html, count=1)
    assert n == 1, f"figure thumb non trovata in {slug}"
    # sanity: la hero deve stare prima dell'answer-box e dopo la meta-bar
    i_hero = html.index('class="article-hero"')
    assert html.index('class="article-meta-bar"') < i_hero < html.index('class="answer-box"'), slug

    # b) head + JSON-LD
    html = fix_head_image(html, slug)
    old_img = f'"image": "{LOGO_ABS}"'
    assert html.count(old_img) == 1, f'JSON-LD image refs = {html.count(old_img)} in {slug}'
    html = html.replace(old_img, f'"image": "{SITE}/assets/img/{slug}.webp"', 1)

    # c) related-grid
    html = convert_cards(html, "cards_related")

    p.write_text(html, encoding="utf-8")
    report["articles_ok"].append(slug)

# ---------- TASK 2: home ----------
home = ROOT / "index.html"
html = home.read_text(encoding="utf-8")
html = convert_cards(html, "cards_home",
                     hero_slug="pannelli-solari-guida",
                     hero_alt="Pannelli solari su tetto di casa italiana ristrutturata")
html = fix_head_image(html, "pannelli-solari-guida")
home.write_text(html, encoding="utf-8")

# ---------- TASK 3: categorie ----------
for silo in SILOS:
    p = ROOT / silo / "index.html"
    html = p.read_text(encoding="utf-8")
    html = convert_cards(html, "cards_categorie")
    p.write_text(html, encoding="utf-8")

# ---------- TASK 5 (head): theme-color + manifest in TUTTE le pagine ----------
FAVICON = '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">'
PWA_TAGS = ('\n  <meta name="theme-color" content="#16324f">'
            '\n  <link rel="manifest" href="/manifest.webmanifest">')
all_pages = [p for p in ROOT.rglob("index.html")
             if "node_modules" not in p.parts and "build" not in p.parts]
for p in all_pages:
    html = p.read_text(encoding="utf-8")
    if 'rel="manifest"' in html:
        continue
    assert FAVICON in html, f"favicon non trovata in {p}"
    html = html.replace(FAVICON, FAVICON + PWA_TAGS, 1)
    p.write_text(html, encoding="utf-8")
    report["pwa_pages"] += 1

print(json.dumps({k: (len(v) if isinstance(v, list) else v)
                  for k, v in report.items()}, ensure_ascii=False, indent=2))
print(f"pagine index.html totali processate: {len(all_pages)}")
