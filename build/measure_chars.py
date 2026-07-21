#!/usr/bin/env python3
"""Misura i caratteri di testo contenuto (strip tag) dei file index.html degli articoli."""
import re, sys, html
from pathlib import Path

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

ROOT = Path(__file__).resolve().parent.parent

def measure(path: Path):
    src = path.read_text(encoding="utf-8")
    # strip script/style blocks first
    body = re.sub(r"<script\b[^>]*>.*?</script>", " ", src, flags=re.S | re.I)
    body = re.sub(r"<style\b[^>]*>.*?</style>", " ", body, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", body)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)

if __name__ == "__main__":
    total = 0
    for a in ARTICLES:
        p = ROOT / a / "index.html"
        n = measure(p)
        total += n
        print(f"{a}: {n}")
    print(f"TOTALE: {total}")
