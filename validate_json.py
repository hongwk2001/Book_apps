import json
import os
import sys

books_dir = r"C:\git_repo\Book_apps\dracula\src\main\assets\books"
required_keys = {"id", "tag", "en", "ko", "is_header"}

errors = []

for i in range(1, 28):
    filename = f"ch_{i:02d}.json"
    filepath = os.path.join(books_dir, filename)
    
    if not os.path.exists(filepath):
        errors.append(f"Missing file: {filename}")
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            errors.append(f"{filename} is not a JSON array.")
            continue
            
        for idx, item in enumerate(data):
            missing = required_keys - set(item.keys())
            if missing:
                errors.append(f"{filename} item {idx} missing keys: {missing}")
                break # Only report first error per file to avoid spam
                
    except json.JSONDecodeError as e:
        errors.append(f"{filename} is not valid JSON: {e}")
    except Exception as e:
        errors.append(f"{filename} error: {e}")

if errors:
    print("Validation failed with the following errors:")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)
else:
    print("All 27 JSON files are structurally valid!")
    sys.exit(0)