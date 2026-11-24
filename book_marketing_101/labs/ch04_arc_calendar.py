"""Lab 4 — Build the pre-launch calendar from one date.

Give the launch date, get every milestone counted back from it.
This is the same logic as Appendix B, computed for you.

Run:  python ch04_arc_calendar.py
"""
from datetime import date, timedelta

MILESTONES = [
    (12, "Finalize cover and blurb; recruit ARC readers"),
    (9, "Send ARCs; pitch bloggers and podcasts; cover reveal"),
    (6, "Share teasers; book launch events; line up promo newsletters"),
    (3, "Remind ARC readers; finalize launch-week schedule"),
    (1, "Schedule launch emails and posts; confirm events"),
]


def calendar(launch: date):
    """Yield (date, weeks_before, task) for each milestone, earliest first."""
    for weeks_before, task in sorted(MILESTONES, reverse=True):
        yield launch - timedelta(weeks=weeks_before), weeks_before, task


if __name__ == "__main__":
    launch = date(2027, 3, 1)  # replace with your own launch date
    print(f"Launch day: {launch.isoformat()} ({launch.strftime('%A')})")
    for when, weeks, task in calendar(launch):
        print(f"{when.isoformat()}  {weeks:>2} wk before  {task}")
