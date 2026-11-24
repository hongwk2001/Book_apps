"""Bonus lab — Track this book's own launch.

Mark each task True when it is done. The script reports progress by stage,
the same way Appendix A is organized.

Run:  python bonus_launch_check.py
"""

STAGES = {
    "Book ready": {
        "Manuscript edited and proofread": False,
        "Cover tested at thumbnail size": False,
        "Blurb final and tested on readers": False,
        "Categories, keywords and price set": False,
    },
    "Platform ready": {
        "Website live with book page and buy links": False,
        "Newsletter sign-up and reader magnet working": False,
        "Welcome sequence written and switched on": False,
    },
    "Pre-launch done": {
        "ARC team recruited and copies sent": False,
        "Cover reveal done": False,
        "Outreach pitches sent and tracked": False,
    },
}

if __name__ == "__main__":
    total = done = 0
    for stage, tasks in STAGES.items():
        stage_done = sum(tasks.values())
        total += len(tasks)
        done += stage_done
        print(f"{stage}: {stage_done}/{len(tasks)}")
        for task, is_done in tasks.items():
            print(f"  [{'x' if is_done else ' '}] {task}")
    print(f"Overall: {done}/{total} ({done / total:.0%})")
