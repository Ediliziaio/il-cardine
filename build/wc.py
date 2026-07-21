#!/usr/bin/env python3
"""Calcola wordCount (metodo coerente con i valori preesistenti) e minuti lettura."""
import re, html, sys
from pathlib import Path

def wc_refined(path):
    src = path.read_text(encoding='utf-8')
    m = re.search(r'<div class="article-body".*?<!-- Sidebar articolo -->', src, flags=re.S)
    seg = m.group(0)
    for pat in [r'<nav class="article-toc".*?</nav>',
                r'<div class="author-box".*?</div>\s*</div>',
                r'<div class="share-row".*?</div>',
                r'<div class="tags".*?</div>',
                r'<figure.*?</figure>',
                r'<div class="ad-slot.*?</div>']:
        seg = re.sub(pat, ' ', seg, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', seg)
    txt = html.unescape(txt)
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9'’]+", txt))

if __name__ == "__main__":
    for a in sys.argv[1:]:
        p = Path(a)
        w = wc_refined(p)
        wc = round(w * 0.935)
        minutes = round(wc / 220)
        print(f"{p.parent.name}: refined={w} wordCount={wc} min={minutes}")
