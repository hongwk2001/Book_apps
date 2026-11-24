"""Lab 7 — Monthly check: compare two sources.

Chapter 7's core habit is checking one number against another.
Here: ad-dashboard royalties vs KDP report royalties, week by week.
A gap that keeps growing is the signal to investigate.

Run:  python ch07_monthly_check.py
"""

WEEKS = [
    # (week, ad_spend, ad_dashboard_royalties, kdp_report_royalties)
    ("W1", 20.00, 14.00, 13.50),
    ("W2", 20.00, 18.00, 16.00),
    ("W3", 20.00, 15.00, 11.00),
    ("W4", 20.00, 22.00, 12.50),
]

FLAG_GAP = 0.20  # flag weeks where the two sources differ by more than 20%


def check(rows):
    for week, spend, dash, kdp in rows:
        gap = (dash - kdp) / kdp if kdp else 0.0
        flag = "CHECK" if abs(gap) > FLAG_GAP else "ok"
        print(f"{week}: spend ${spend:.2f}  dash ${dash:.2f}  kdp ${kdp:.2f}  "
              f"gap {gap:+.0%}  {flag}")
    total_spend = sum(r[1] for r in rows)
    total_kdp = sum(r[3] for r in rows)
    print(f"Total spend ${total_spend:.2f}, KDP royalties ${total_kdp:.2f}, "
          f"ROAS (KDP) {total_kdp / total_spend:.2f}")


if __name__ == "__main__":
    check(WEEKS)
