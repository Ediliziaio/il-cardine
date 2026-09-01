#!/usr/bin/env python3
"""Verifica finale integrazione hero images + PWA — Il Cardine."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "assets" / "img"
SILOS = ["ristrutturazioni", "serramenti-infissi", "efficienza-energetica",
         "materiali-costruzione", "impianti", "incentivi-bonus",
         "tecnologie-innovazione", "normative"]
VOID = {"area","base","br","col","embed","hr","img","input","link","meta",
        "param","source","track","wbr"}

class WellFormed(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors = [], []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"chiusura senza apertura </{tag}> riga {self.getpos()[0]}")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            # cerca il tag nello stack (chiusura implicita di <li>/<p> ecc. non usata nel sito)
            names = [t for t, _ in self.stack]
            if tag in names:
                while self.stack and self.stack[-1][0] != tag:
                    t, pos = self.stack.pop()
                    self.errors.append(f"<{t}> aperto riga {pos[0]} chiuso implicitamente da </{tag}> riga {self.getpos()[0]}")
                self.stack.pop()
            else:
                self.errors.append(f"</{tag}> senza apertura riga {self.getpos()[0]}")

errors, ok_articles = [], 0
all_pages = sorted(ROOT.rglob("index.html"))
all_pages = [p for p in all_pages if "node_modules" not in p.parts and "build" not in p.parts]

# ---- 33 articoli ----
for silo in SILOS:
    for d in sorted((ROOT / silo).iterdir()):
        if not (d.is_dir() and (d / "index.html").exists()):
            continue
        slug = d.name
        html = (d / "index.html").read_text(encoding="utf-8")
        good = True
        # 1) figure.article-hero con img fetchpriority
        if not re.search(r'<figure class="article-hero">\s*<img src="/assets/img/'
                         + re.escape(slug) + r'\.webp" [^>]*fetchpriority="high"', html):
            errors.append(f"{slug}: figure.article-hero/fetchpriority mancante"); good = False
        # 2) og:image punta allo slug giusto
        if f'<meta property="og:image" content="https://www.ilcardine.it/assets/img/{slug}.webp">' not in html:
            errors.append(f"{slug}: og:image errato"); good = False
        if 'og:image:width" content="1200"' not in html or 'og:image:height" content="675"' not in html:
            errors.append(f"{slug}: og:image width/height mancanti"); good = False
        # 3) JSON-LD valido e image aggiornata
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                data = json.loads(m.group(1))
            except Exception as e:
                errors.append(f"{slug}: JSON-LD non valido: {e}"); good = False; continue
            for node in data.get("@graph", []):
                if node.get("@type") == "Article":
                    img = node.get("image", "")
                    if img != f"https://www.ilcardine.it/assets/img/{slug}.webp":
                        errors.append(f"{slug}: Article.image = {img}"); good = False
                if node.get("@type") == "Article" and \
                   node.get("publisher", {}).get("logo", {}).get("url", "").endswith("logo.png") is False:
                    errors.append(f"{slug}: publisher logo modificato per errore"); good = False
        if good:
            ok_articles += 1

# ---- tutte le pagine: img esistenti, HTML ben formato, PWA tags ----
img_refs, missing_imgs = 0, []
for p in all_pages:
    html = p.read_text(encoding="utf-8")
    for m in re.finditer(r'<img src="(/assets/img/[^"]+)"', html):
        img_refs += 1
        if not (ROOT / m.group(1).lstrip("/")).exists():
            missing_imgs.append(f"{p.relative_to(ROOT)}: {m.group(1)}")
    wf = WellFormed(); wf.feed(html); wf.close()
    if wf.errors or wf.stack:
        errors.append(f"{p.relative_to(ROOT)}: HTML malformato: {wf.errors[:3]} residui {[t for t,_ in wf.stack][:5]}")
    if 'name="theme-color" content="#16324f"' not in html or 'rel="manifest"' not in html:
        errors.append(f"{p.relative_to(ROOT)}: tag PWA mancanti")
    # nessun doppio inserimento
    if html.count('rel="manifest"') != 1:
        errors.append(f"{p.relative_to(ROOT)}: manifest link duplicato")

# ---- conteggio card convertite home + categorie ----
def count_cards(p):
    html = p.read_text(encoding="utf-8")
    return len(re.findall(r'<img src="/assets/img/[^"]+"[^>]*class="thumb-img"', html)), \
           len(re.findall(r'<div class="thumb [^"]*"><span class="thumb-label">', html))

home_img, home_thumb = count_cards(ROOT / "index.html")
cat_img = cat_thumb = 0
for silo in SILOS:
    i, t = count_cards(ROOT / silo / "index.html")
    cat_img += i; cat_thumb += t

# hero home = fetchpriority
home_html = (ROOT / "index.html").read_text(encoding="utf-8")
hero_ok = bool(re.search(r'<img src="/assets/img/pannelli-solari-guida\.webp" alt="Pannelli solari su tetto di casa italiana ristrutturata"[^>]*fetchpriority="high" class="thumb-img">', home_html))
home_lazy = len(re.findall(r'class="thumb-img"', home_html)) - 1
lazy_ok = home_lazy == len(re.findall(r'loading="lazy" class="thumb-img"', home_html))

# manifest + icone
man = json.loads((ROOT / "manifest.webmanifest").read_text(encoding="utf-8"))
man_ok = (man["name"] == "Il Cardine" and man["short_name"] == "Il Cardine"
          and man["start_url"] == "/" and man["display"] == "browser"
          and man["background_color"] == "#ffffff" and man["theme_color"] == "#16324f"
          and len(man["icons"]) == 2)
icons_ok = (ROOT / "assets/icon-192.png").exists() and (ROOT / "assets/icon-512.png").exists()

print("=" * 60)
print("REPORT VERIFICA FINALE — Il Cardine")
print("=" * 60)
print(f"Articoli verificati OK (hero+og:image+JSON-LD): {ok_articles}/33")
print(f"Pagine index.html controllate:                    {len(all_pages)}")
print(f"Riferimenti <img /assets/img/...> trovati:        {img_refs} (mancanti: {len(missing_imgs)})")
print(f"Card convertite in home:                          {home_img} (hero fetchpriority: {'OK' if hero_ok else 'KO'}, lazy corrette: {'OK' if lazy_ok else 'KO'}, thumb CSS residui: {home_thumb})")
print(f"Card convertite nelle 8 categorie:                {cat_img} (thumb CSS residui: {cat_thumb})")
print(f"manifest.webmanifest valido:                      {'OK' if man_ok else 'KO'}")
print(f"Icone PWA 192/512:                                {'OK' if icons_ok else 'KO'}")
if missing_imgs:
    print("\nIMMAGINI MANCANTI:"); [print("  -", m) for m in missing_imgs]
if errors:
    print(f"\nERRORI ({len(errors)}):"); [print("  -", e) for e in errors]
else:
    print("\nNESSUN ERRORE: tutte le verifiche superate.")
