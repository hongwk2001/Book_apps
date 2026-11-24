"""Lab 6 — Ad math: ROAS, break-even and read-through.

Uses one test campaign's numbers. Change the inputs and rerun.

Run:  python ch06_ads.py
"""


def roas(royalties, ad_spend):
    """Return of ad spend: royalties earned per dollar spent."""
    return royalties / ad_spend if ad_spend else 0.0


def break_even_cpc(royalty_per_sale, conversion_rate):
    """Highest cost per click you can pay and still break even on sales.

    conversion_rate: share of clicks that become a sale (0.02 = 2%).
    """
    return royalty_per_sale * conversion_rate


def read_through(book1_readers, book2_buyers):
    """Share of book 1 readers who buy book 2."""
    return book2_buyers / book1_readers if book1_readers else 0.0


if __name__ == "__main__":
    spend = 60.00
    sales = 9
    royalty_per_sale = 3.50
    royalties = sales * royalty_per_sale

    print(f"Spend ${spend:.2f}, royalties ${royalties:.2f}")
    print(f"ROAS: {roas(royalties, spend):.2f}")
    print(f"Break-even CPC at 2% conversion: ${break_even_cpc(royalty_per_sale, 0.02):.2f}")
    print(f"Break-even CPC at 5% conversion: ${break_even_cpc(royalty_per_sale, 0.05):.2f}")
    print(f"Read-through: {read_through(1000, 400):.0%}")
