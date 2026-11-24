"""Lab 3 — Email list growth.

Simulates a newsletter list month by month: new signups minus unsubscribes.
Shows how many months a target list size takes at your current pace.

Run:  python ch03_list_growth.py
"""


def months_to_target(start, signups_per_month, unsubs_per_month, target):
    """Return the first month number at which the list reaches target (or None)."""
    size = start
    month = 0
    net = signups_per_month - unsubs_per_month
    if net <= 0:
        return None  # the list never grows at this pace
    while size < target:
        size += net
        month += 1
    return month


if __name__ == "__main__":
    start = 40          # subscribers today
    signups = 25        # new subscribers per month (reader magnet + social)
    unsubs = 4          # people who leave per month
    target = 500

    print(f"Start {start}, net +{signups - unsubs}/month")
    print(f"Months to reach {target}: {months_to_target(start, signups, unsubs, target)}")

    print("Pace check:")
    for s in [10, 20, 30]:
        print(f"  signups {s}/month -> {months_to_target(start, s, unsubs, target)} months")
