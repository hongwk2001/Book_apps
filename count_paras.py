import os
import glob

prep_dir = r'c:\git_repo\Book_apps\frankenstein\prep_data'

# Get all _en.txt files
en_files = glob.glob(os.path.join(prep_dir, '*_en.txt'))
en_files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))

print(f"{'Filename':<20} | {'EN Paras':<10} | {'KO Paras':<10} | {'Diff'}")
print("-" * 55)

for en_file in en_files:
    ko_file = en_file.replace('_en.txt', '_ko.txt')
    
    with open(en_file, 'r', encoding='utf-8') as f:
        en_paras = [p for p in f.read().split('\n\n') if p.strip()]
        
    with open(ko_file, 'r', encoding='utf-8') as f:
        ko_paras = [p for p in f.read().split('\n\n') if p.strip()]
        
    base_name = os.path.basename(en_file).replace('_en.txt', '')
    diff = len(en_paras) - len(ko_paras)
    diff_str = str(diff) if diff != 0 else "OK"
    
    print(f"{base_name:<20} | {len(en_paras):<10} | {len(ko_paras):<10} | {diff_str}")

