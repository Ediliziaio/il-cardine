#!/usr/bin/env python3
"""Verifica post-ampliamento: caratteri, ancore TOC, FAQ visibili vs JSON-LD, validità JSON."""
import re, html, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = [
    "serramenti-infissi/serramenti-pvc-alluminio-legno-confronto",
    "serramenti-infissi/finestre-triplo-vetro-conviene",
    "serramenti-infissi/prezzi-infissi-al-mq-2026",
    "serramenti-infissi/top-5-produttori-serramenti-italia",
    "materiali-costruzione/materiali-isolanti-confronto",
    "materiali-costruzione/edilizia-legno-xlam",
    "materiali-costruzione/calcestruzzo-tipologie-usi",
    "materiali-costruzione/laterizi-blocchi-termici-guida",
]

def strip_text(src):
    s = re.sub(r"<script\b[^>]*>.*?</script>", " ", src, flags=re.S | re.I)
    s = re.sub(r"<style\b[^>]*>.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

def norm(s):
    s = html.unescape(s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()

ok_all = True
for a in ARTICLES:
    p = ROOT / a / "index.html"
    src = p.read_text(encoding="utf-8")
    issues = []

    # 1. chars
    n_chars = len(strip_text(src))

    # 2. TOC anchors vs h2 ids
    toc = re.findall(r'<nav class="article-toc".*?</nav>', src, flags=re.S)[0]
    anchors = re.findall(r'href="#([^"]+)"', toc)
    h2ids = re.findall(r'<h2 id="([^"]+)"', src)
    for anch in anchors:
        if anch not in h2ids:
            issues.append(f"TOC anchor #{anch} senza h2")
    # h2 present in body but missing in TOC (excluding 'correlati')
    body_h2 = [i for i in h2ids if i != "correlati"]
    for hid in body_h2:
        if hid not in anchors:
            issues.append(f"h2 #{hid} non in TOC")
    # order check
    toc_idx = [body_h2.index(x) for x in anchors if x in body_h2]
    if toc_idx != sorted(toc_idx):
        issues.append("ordine TOC non coerente con il corpo")

    # 3. FAQ visible vs JSON-LD
    visible_q = [norm(q) for q in re.findall(r"<summary>(.*?)</summary>", src, flags=re.S)]
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, flags=re.S)
    try:
        data = json.loads(m.group(1))
        graph = data["@graph"]
        faq_ld = next((g for g in graph if g.get("@type") == "FAQPage"), None)
        ld_q = [norm(q["name"]) for q in faq_ld["mainEntity"]]
        if visible_q != ld_q:
            issues.append(f"FAQ mismatch: visibili={len(visible_q)} jsonld={len(ld_q)}")
            for i, (v, l) in enumerate(zip(visible_q, ld_q)):
                if v != l:
                    issues.append(f"  diff #{i}: '{v[:60]}' != '{l[:60]}'")
    except Exception as e:
        issues.append(f"JSON-LD non valido: {e}")

    # 4. dateModified coherence
    dm_meta = re.search(r'itemprop="dateModified">([^<]+)<', src)
    dm_ld = re.search(r'"dateModified": "([^"]+)"', src)
    if not dm_meta or "21 luglio 2026" not in dm_meta.group(1):
        issues.append("dateModified meta-bar non aggiornata")
    if not dm_ld or "2026-07-21" not in dm_ld.group(1):
        issues.append("dateModified JSON-LD non aggiornata")

    # 5. basic tag balance for key tags
    for tag in ["div", "section", "article", "table", "details", "ol", "ul", "nav"]:
        op = len(re.findall(rf"<{tag}[\s>]", src))
        cl = len(re.findall(rf"</{tag}>", src))
        if op != cl:
            issues.append(f"tag <{tag}> sbilanciato: {op} aperti vs {cl} chiusi")

    status = "OK" if not issues else "PROBLEMI"
    if issues:
        ok_all = False
    print(f"\n{a}: {n_chars} caratteri — {status}")
    for i in issues:
        print(f"   - {i}")

print("\n=== ESITO COMPLESSIVO:", "TUTTO OK" if ok_all else "DA CORREGGERE", "===")
