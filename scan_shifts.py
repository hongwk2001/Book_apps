import os
import json

assets = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books"
out_file = r"C:\Users\hongw\.gemini\antigravity\brain\d2ce9842-01e6-483c-ae25-ed74580253c7\remaining_shifts_scan.md"

suspicious = []

for i in range(1, 29):
    path = os.path.join(assets, f"ch_{i:02d}.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for item in data:
        en = item.get("en", "").strip()
        ko = item.get("ko", "").strip()
        
        # 1. Truncated or empty
        if len(en) < 3 or len(ko) < 3:
            # allow things like "Chapter 1" if it's super short? 3 is tiny anyway.
            # actually if it's literally just "."
            if en == "." or ko == "." or not en or not ko:
                if item["tag"] == "P004-3": # already known
                    continue
                suspicious.append({"tag": item["tag"], "en": en, "ko": ko, "reason": "Empty or truncated string"})
            continue
            
        # 2. Highly skewed lengths
        en_len = len(en)
        ko_len = len(ko)
        ratio = ko_len / en_len
        
        if ratio > 3.0 or ratio < 0.3:
            # Only flag if it's a reasonably long sentence where this actually matters
            if en_len > 20 and ko_len > 20:
                suspicious.append({"tag": item["tag"], "en": en, "ko": ko, "reason": f"Highly skewed length ratio ({ratio:.2f})"})
                
with open(out_file, "w", encoding="utf-8") as out:
    out.write("# Remaining Partial Shifts Scan\n\n")
    if not suspicious:
        out.write("No remaining suspicious shifts found!\n")
    else:
        out.write(f"Found {len(suspicious)} potentially lopsided chunks:\n\n")
        for idx, item in enumerate(suspicious):
            out.write(f"### {idx+1}. Tag: `{item['tag']}`\n")
            out.write(f"**Reason:** {item['reason']}\n")
            out.write(f"**EN:** {item['en']}\n")
            out.write(f"**KO:** {item['ko']}\n\n")

print(f"Scan complete. Found {len(suspicious)} items.")
