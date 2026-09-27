import os
import json
import random

def main():
    books_dir = r"c:\git_repo\Book_apps\two_cities\src\main\assets\books"
    raw_dir = r"c:\git_repo\Book_apps\two_cities\raw_reference_data"
    output_file = "audit_report.md"
    
    all_paragraphs = []
    
    # Collect all paragraphs
    for filename in os.listdir(books_dir):
        if filename.startswith("ch_") and filename.endswith(".json"):
            chapter_num = filename[3:5] # e.g. "01"
            filepath = os.path.join(books_dir, filename)
            
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for item in data:
                        if not item.get("is_header", False):
                            item["chapter"] = chapter_num
                            all_paragraphs.append(item)
                except json.JSONDecodeError:
                    print(f"Error reading {filename}")

    # Randomly pick 30
    if len(all_paragraphs) > 30:
        sampled = random.sample(all_paragraphs, 30)
    else:
        sampled = all_paragraphs
        
    print(f"Sampled {len(sampled)} paragraphs.")
    
    # Load raw data as needed
    raw_cache = {}
    
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("# Translation Audit Report (30 Random Paragraphs)\n\n")
        
        for idx, para in enumerate(sampled):
            ch_num = para["chapter"]
            raw_id = para.get("raw_ref_id")
            
            # Load raw chapter if not loaded
            if ch_num not in raw_cache:
                raw_path = os.path.join(raw_dir, f"raw_ch_{ch_num}.json")
                if os.path.exists(raw_path):
                    with open(raw_path, "r", encoding="utf-8") as f:
                        try:
                            raw_data = json.load(f)
                            # map id to raw text
                            raw_cache[ch_num] = {r.get("raw_ref_id"): r.get("raw") for r in raw_data}
                        except json.JSONDecodeError:
                            raw_cache[ch_num] = {}
                else:
                    raw_cache[ch_num] = {}
            
            raw_text = raw_cache[ch_num].get(raw_id, "RAW TEXT NOT FOUND")
            en_text = para.get("en", "")
            ko_text = para.get("ko", "")
            para_tag = para.get("tag", "NoTag")
            
            out.write(f"## {idx+1}. Chapter {ch_num}, Tag: {para_tag}, RawRef: {raw_id}\n")
            out.write(f"**Raw Text:**\n> {raw_text}\n\n")
            out.write(f"**English:**\n> {en_text}\n\n")
            out.write(f"**Korean:**\n> {ko_text}\n\n")
            out.write("---\n\n")

    print(f"Report generated at {output_file}")

if __name__ == "__main__":
    main()
