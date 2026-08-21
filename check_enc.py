import json
with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_1.Lt1_done.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data[0]["chunks"][0]["ko"])
