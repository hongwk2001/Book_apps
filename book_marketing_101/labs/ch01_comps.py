"""Lab 1 — Filter your comps.

Chapter 1 rules: recent (within 5 years), similar genre, not a giant bestseller.
Put your candidate titles in COMPS, then run the script to see which pass.

Run:  python ch01_comps.py
"""

CURRENT_YEAR = 2026
MAX_AGE_YEARS = 5

COMPS = [
    {"title": "Title A", "year": 2024, "genre": "cozy fantasy", "rank_k": 12},
    {"title": "Title B", "year": 2016, "genre": "cozy fantasy", "rank_k": 8},
    {"title": "Title C", "year": 2025, "genre": "epic fantasy", "rank_k": 40},
    {"title": "Title D", "year": 2023, "genre": "cozy fantasy", "rank_k": 3},
]

MY_GENRE = "cozy fantasy"
GIANT_RANK_K = 5  # top-5 overall rank counts as "giant" (rank in thousands here)


def passes(comp):
    reasons = []
    if CURRENT_YEAR - comp["year"] > MAX_AGE_YEARS:
        reasons.append("too old")
    if comp["genre"] != MY_GENRE:
        reasons.append("different genre")
    if comp["rank_k"] <= GIANT_RANK_K:
        reasons.append("giant")
    return (not reasons), reasons


if __name__ == "__main__":
    kept = 0
    for comp in COMPS:
        ok, reasons = passes(comp)
        kept += ok
        verdict = "KEEP" if ok else "DROP: " + ", ".join(reasons)
        print(f"{comp['title']:<8} {verdict}")
    print(f"{kept} of {len(COMPS)} comps kept")
