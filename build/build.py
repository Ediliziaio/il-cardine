# -*- coding: utf-8 -*-
"""Build + verifica degli 8 articoli."""
import re, os, sys, json
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tpl import render, strip_tags, DOMAIN
from art_t12 import ARTICLES as T12
from art_t34 import ARTICLES as T34
from art_n56 import ARTICLES as N56
from art_n78 import ARTICLES as N78

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALL = T12 + T34 + N56 + N78

class Checker(HTMLParser):
    VOID = {"meta","link","img","br","hr","input","source","wbr","col","area","base","embed","track","param"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self.VOID: return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.errors.append(f"tag non chiuso: <{self.stack[-1]}>")
                self.stack.pop()
            self.stack.pop()
        else:
            self.errors.append(f"chiusura imprevista </{tag}>")

def extract_block(html, start_marker):
    i = html.index(start_marker)
    return html[i:]

report = []
for a in ALL:
    html, wc = render(a)
    outdir = os.path.join(ROOT, a["silo"], a["slug"])
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    # --- verifica HTML ben formato ---
    ck = Checker(); ck.feed(html)
    tag_ok = not ck.errors and not ck.stack
    if ck.stack: tag_ok = False

    # --- verifica ancore TOC <-> id H2 ---
    toc_anchors = set(re.findall(r'class="article-toc".*?</nav>', html, re.S)[0] and re.findall(r'href="#([^"]+)"', re.search(r'class="article-toc".*?</nav>', html, re.S).group(0)))
    h2_ids = set(re.findall(r'<h2 id="([^"]+)"', html))
    anchor_ok = toc_anchors <= (h2_ids | {"faq"}) and h2_ids <= (toc_anchors | {"correlati", "piu-letti"})
    missing = toc_anchors - h2_ids

    # --- verifica FAQ visibili == JSON-LD ---
    visible_faq = re.findall(r'<summary>(.*?)</summary>', html)
    ld_raw = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1)
    ld = json.loads(ld_raw)
    faq_ld = [q["name"] for g in ld["@graph"] if g.get("@type") == "FAQPage" for q in g["mainEntity"]]
    faq_ok = visible_faq == faq_ld

    # --- conteggio caratteri testo contenuto (article-body, strip tag) ---
    body = re.search(r'<div class="article-body".*?(?=<!-- Sidebar articolo -->)', html, re.S).group(0)
    # escludo TOC e blocco condivisione/tags dal conteggio contenuto? includiamo tutto il testo editoriale
    text = strip_tags(body)
    chars = len(text)

    # --- verifica componenti obbligatori ---
    checks = {
        "answer-box": 'class="answer-box"' in html,
        "breadcrumb": 'class="breadcrumbs"' in html,
        "author-box": 'class="author-box"' in html,
        "share-row": 'class="share-row"' in html,
        "related-grid": 'class="related-grid"' in html,
        "ad-halfpage": 'ad-halfpage' in html,
        "piu-letti": 'I più letti' in html,
        "canonical": f'<link rel="canonical" href="{DOMAIN}/{a["silo"]}/{a["slug"]}/">' in html,
        "table_o_lista": ("<table" in html) or ("<ol>" in body) or ("<ul>" in body),
        "title<=60": len(re.search(r'<title>(.*?)</title>', html).group(1)) <= 60,
        "desc<=155": len(a["description"]) <= 155,
        "no_placeholder": ("giornale-edile" not in html.lower()) and ("giornale edile" not in html.lower()),
    }
    comps_ok = all(checks.values())

    report.append({
        "path": f'{a["silo"]}/{a["slug"]}/index.html',
        "chars": chars, "words": wc,
        "tag_ok": tag_ok, "anchor_ok": anchor_ok and not missing,
        "faq_ok": faq_ok, "comps_ok": comps_ok,
        "faq_n": len(visible_faq),
        "checks_ko": [k for k,v in checks.items() if not v],
        "missing_anchors": list(missing),
        "tag_errors": ck.errors[:3] + ([f"aperti: {ck.stack}"] if ck.stack else []),
    })

print(f"{'FILE':60} {'CHARS':>6} {'WORDS':>6} OK")
all_ok = True
for r in report:
    ok = r["tag_ok"] and r["anchor_ok"] and r["faq_ok"] and r["comps_ok"] and r["chars"] >= 5000
    all_ok = all_ok and ok
    print(f"{r['path']:60} {r['chars']:>6} {r['words']:>6} {'OK' if ok else 'FAIL'}")
    if not ok:
        if r["checks_ko"]: print("   componenti KO:", r["checks_ko"])
        if r["missing_anchors"]: print("   ancore mancanti:", r["missing_anchors"])
        if r["tag_errors"]: print("   errori tag:", r["tag_errors"])
        if not r["faq_ok"]: print(f"   FAQ visibili={r['faq_n']}")
print("\nTUTTO OK" if all_ok else "\nPROBLEMI DA CORREGGERE")
