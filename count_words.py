import os

def get_stats(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    chars = len(text)
    words = len(text.split())
    return chars, words

en_file = r'c:\git_repo\Book_apps\frankenstein\prep_data\numbered\20.ch16_en.txt'
ko_file = r'c:\git_repo\Book_apps\frankenstein\prep_data\numbered\20.ch16_ko.txt'

en_c, en_w = get_stats(en_file)
ko_c, ko_w = get_stats(ko_file)

print(f"EN File ({os.path.basename(en_file)}):")
print(f"Characters: {en_c}")
print(f"Words: {en_w}")
print("\nKO File ({os.path.basename(ko_file)}):")
print(f"Characters: {ko_c}")
print(f"Words: {ko_w}")
