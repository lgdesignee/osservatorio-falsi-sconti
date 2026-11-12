"""Dal file JSON dell'osservatorio alle tabelle CSV: un mese per riga, una catena per riga,
e i casi del mese (i peggiori e quelli dove il volantino conviene).

Uso: python scripts/csv.py   (legge data/falsi-sconti.json, scrive data/*.csv)
"""
import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def scrivi(nome, righe):
    if not righe:
        return
    campi = list(righe[0].keys())
    with open(DATA / nome, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campi, lineterminator="\n")
        w.writeheader()
        for r in righe:
            w.writerow({k: ("; ".join(v) if isinstance(v, list) else v) for k, v in r.items()})


def main():
    d = json.loads((DATA / "falsi-sconti.json").read_text(encoding="utf-8"))
    mesi, catene, casi = [], [], []
    for m in sorted(d["months"], key=lambda x: x["month"]):
        mesi.append({"month": m["month"], **m.get("summary", {}), **m.get("funnel", {}), "url": m["url"]})
        for c in m.get("chains", []):
            catene.append({"month": m["month"], **c})
        for tipo, chiave in (("worst_case", "worst_cases"), ("flyer_win", "flyer_wins")):
            for x in m.get(chiave, []):
                casi.append({"month": m["month"], "kind": tipo, **x})
    scrivi("mesi.csv", mesi)
    scrivi("catene.csv", catene)
    # i casi hanno campi in più o in meno da un mese all'altro: l'unione, nell'ordine in cui compaiono
    if casi:
        campi = list(dict.fromkeys(k for r in casi for k in r))
        scrivi("casi.csv", [{k: r.get(k, "") for k in campi} for r in casi])


if __name__ == "__main__":
    main()
