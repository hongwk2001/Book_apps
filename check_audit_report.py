import json
with open(r"c:\git_repo\Book_apps\frankenstein\audit_batches\audit_batch_4_report.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(json.dumps(data, ensure_ascii=False, indent=2))
