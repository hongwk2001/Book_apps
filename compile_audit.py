import json
import glob
import os

report_files = glob.glob(r"c:\git_repo\Book_apps\frankenstein\audit_batches\*_report.json")
suspicious = []
total_checked = 84

for rf in report_files:
    try:
        with open(rf, "r", encoding="utf-8") as f:
            data = json.load(f)
            suspicious.extend(data)
    except Exception as e:
        print(f"Error reading {rf}: {e}")

passed = total_checked - len(suspicious)

with open(r"c:\git_repo\Book_apps\frankenstein\audit_batches\audit_findings.md", "w", encoding="utf-8") as out:
    out.write(f"Total Checked: {total_checked}\n")
    out.write(f"Passed: {passed}\n")
    out.write(f"Suspicious: {len(suspicious)}\n\n")

    for idx, item in enumerate(suspicious):
        out.write(f"--- Suspicious #{idx+1} ---\n")
        out.write(f"Chapter: {item.get('chapter')} | Tag: {item.get('tag')}\n")
        out.write(f"EN: {item.get('en')}\n")
        out.write(f"KO: {item.get('ko')}\n")
        out.write(f"Reason: {item.get('reason')}\n\n")

print(f"Compiled to audit_findings.md")
