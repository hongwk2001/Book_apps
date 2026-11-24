"""Lab 5 — Plan launch week day by day.

Spreads one activity per day across the week, as Chapter 5 recommends.
Edit the ACTIVITIES list with your own tasks.

Run:  python ch05_launch_week.py
"""
from datetime import date, timedelta

ACTIVITIES = [
    "Email your list; post on social; remind ARC readers",
    "Share a behind-the-scenes story",
    "First promo newsletter or ad push",
    "Guest post, podcast or interview goes live",
    "Second promo newsletter; share an excerpt",
    "Live reading or Q&A",
    "Thank-you email with a reminder link; review numbers",
]


def week_plan(launch: date):
    for offset, task in enumerate(ACTIVITIES):
        day = launch + timedelta(days=offset)
        yield f"Day {offset + 1} ({day.strftime('%a %b %d')}): {task}"


if __name__ == "__main__":
    for line in week_plan(date(2027, 3, 1)):
        print(line)
