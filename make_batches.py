import os
import json
import glob

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data"
batches_dir = os.path.join(base_dir, "batches")
os.makedirs(batches_dir, exist_ok=True)

files = [
    "1.Lt1", "2.Lt2", "3.Lt3", "4.Lt4",
    "5.ch1", "6.ch2", "7.ch3", "8.ch4", "9.ch5", "10.ch6",
    "11.ch7", "12.ch8", "13.ch9", "14.ch10", "15.ch11", "16.ch12",
    "17.ch13", "18.ch14", "19.ch15", "20.ch16", "21.ch17", "22.ch18",
    "23.ch19", "24.ch20", "25.ch21", "26.ch22", "27.ch23", "28.ch24"
]

for file_prefix in files:
    en_path = os.path.join(base_dir, f"{file_prefix}_en.txt")
    ko_path = os.path.join(base_dir, f"{file_prefix}_ko.txt")
    
    with open(en_path, "r", encoding="utf-8") as f:
        en_paras = [p for p in f.read().split("\n\n") if p.strip()]
    with open(ko_path, "r", encoding="utf-8") as f:
        ko_paras = [p for p in f.read().split("\n\n") if p.strip()]
        
    batch_data = []
    for i in range(len(en_paras)):
        batch_data.append({
            "id": i,
            "tag": f"P{i:03d}",
            "en": en_paras[i].strip(),
            "ko": ko_paras[i].strip()
        })
        
    out_path = os.path.join(batches_dir, f"batch_{file_prefix}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Generated 28 batch JSON files.")
