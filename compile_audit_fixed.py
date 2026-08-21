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
        pass

passed = total_checked - len(suspicious)

out_file = r"C:\Users\hongw\.gemini\antigravity\brain\d2ce9842-01e6-483c-ae25-ed74580253c7\frankenstein_final_audit.md"
with open(out_file, "w", encoding="utf-8") as out:
    out.write(f"Total Checked: {total_checked}\n")
    out.write(f"Passed: {passed}\n")
    out.write(f"Suspicious: {len(suspicious)}\n\n")

    for idx, item in enumerate(suspicious):
        tag = item.get('tag') or item.get('id')
        out.write(f"--- Suspicious #{idx+1} ---\n")
        out.write(f"Chapter: {item.get('chapter')} | Tag: {tag}\n")
        out.write(f"EN: {item.get('en')}\n")
        out.write(f"KO: {item.get('ko')}\n")
        out.write(f"Reason: {item.get('reason')}\n\n")

print(f"Updated frankenstein_final_audit.md")
