import json
with open(r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_14.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    if item["tag"] == "P014-5":
        orig_en = item["en"]
        fixed_en = orig_en.replace('\n', ' ')
        # clean double spaces
        fixed_en = " ".join(fixed_en.split())
        print(f"ORIGINAL:\n{orig_en}\n")
        print(f"FIXED:\n{fixed_en}\n")
