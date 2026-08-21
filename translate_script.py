import json
import time
from deep_translator import GoogleTranslator

file_path = 'c:/git_repo/Book_apps/frankenstein/src/main/assets/books/ch_28.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

translator = GoogleTranslator(source='ko', target='en')

print("Starting translation...")
for i, chunk in enumerate(data):
    ko_text = chunk.get('ko', '').strip()
    if ko_text:
        try:
            res = translator.translate(ko_text)
            chunk['en'] = res
            if i % 10 == 0:
                print(f"[{i+1}/{len(data)}] Translated")
        except Exception as e:
            print(f"Error on chunk {i}: {e}")
            time.sleep(2)
            try:
                chunk['en'] = translator.translate(ko_text)
            except Exception as e:
                print(f"Double error on chunk {i}")
        time.sleep(0.2)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Translation and save complete.")
