#!/usr/bin/env python3
"""
Il Cardine — genera /assets/search-index.json per la ricerca client-side (/cerca/).

Legge tutti gli articoli (directory <silo>/<slug>/index.html), estrae:
  - title    : dal <title> della pagina, senza il suffisso brand " | Il Cardine"
  - url      : percorso assoluto da root (/<silo>/<slug>/)
  - category : nome leggibile del silo
  - date     : data ISO (da article:published_time, fallback datePublished)
  - excerpt  : meta description

Uso:  python tools/build_search_index.py
Output: assets/search-index.json
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "search-index.json"

SILOS = {
    "ristrutturazioni": "Ristrutturazioni",
    "serramenti-infissi": "Serramenti e Infissi",
    "efficienza-energetica": "Efficienza Energetica",
    "materiali-costruzione": "Materiali da Costruzione",
    "impianti": "Impianti",
    "incentivi-bonus": "Incentivi e Bonus",
    "tecnologie-innovazione": "Tecnologie e Innovazione",
    "normative": "Normative",
}

BRAND_SUFFIX = " | Il Cardine"


def extract(pattern, html, flags=0):
    m = re.search(pattern, html, flags)
    return m.group(1).strip() if m else ""


def build_entry(path: Path):
    html = path.read_text(encoding="utf-8")

    title = extract(r"<title>(.*?)</title>", html, re.S)
    if title.endswith(BRAND_SUFFIX):
        title = title[: -len(BRAND_SUFFIX)].strip()

    excerpt = extract(r'<meta\s+name="description"\s+content="([^"]*)"', html)
    date = extract(r'article:published_time"\s+content="([^"]*)"', html)
    if not date:
        date = extract(r'"datePublished"\s*:\s*"([^"]*)"', html)

    rel = path.relative_to(ROOT).parent  # <silo>/<slug>
    silo = rel.parts[0]
    return {
        "title": title,
        "url": "/" + rel.as_posix() + "/",
        "category": SILOS.get(silo, silo),
        "date": date,
        "excerpt": excerpt,
    }


def main():
    articles = []
    for silo in SILOS:
        silo_dir = ROOT / silo
        if not silo_dir.is_dir():
            print(f"ATTENZIONE: silo mancante {silo_dir}", file=sys.stderr)
            continue
        for article_dir in sorted(p for p in silo_dir.iterdir() if p.is_dir()):
            index = article_dir / "index.html"
            if index.exists():
                articles.append(build_entry(index))

    # Ordina per data discendente (stringa ISO: ordinamento lessicografico ok)
    articles.sort(key=lambda a: a["date"], reverse=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(articles, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"OK: {len(articles)} articoli -> {OUT}")


if __name__ == "__main__":
    main()
