"""Lab 2 — Royalty calculator.

Simplified KDP royalty rules from Chapter 2 (delivery fees and file-size
costs are left out on purpose, so you can see the core math).

Run:  python ch02_royalty.py
"""


def ebook_royalty(price, delivery_fee=0.0):
    """70% inside the $2.99–$12.99 band, 35% outside it."""
    if 2.99 <= price <= 12.99:
        return round(price * 0.70 - delivery_fee, 2)
    return round(price * 0.35, 2)


def paperback_royalty(list_price, print_cost):
    """60% at or above $9.99, 50% below it, minus printing cost."""
    rate = 0.60 if list_price >= 9.99 else 0.50
    return round(list_price * rate - print_cost, 2)


if __name__ == "__main__":
    print("== Ebook ==")
    for price in [2.99, 4.99, 9.99, 12.99, 13.99]:
        print(f"price ${price:.2f} -> royalty ${ebook_royalty(price):.2f}")

    print("== Paperback ==")
    print(f"list $9.99, print $3.50 -> royalty ${paperback_royalty(9.99, 3.50):.2f}")
    print(f"list $8.99, print $3.50 -> royalty ${paperback_royalty(8.99, 3.50):.2f}")
