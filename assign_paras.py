import os
import glob

prep_dir = r'c:\git_repo\Book_apps\frankenstein\prep_data'
num_dir = os.path.join(prep_dir, 'numbered')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        
    paras = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    numbered = []
    for i, p in enumerate(paras):
        numbered.append(f"[{i}] {p}")
        
    out_path = os.path.join(num_dir, os.path.basename(filepath))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(numbered))

for filepath in glob.glob(os.path.join(prep_dir, '*_en.txt')):
    process_file(filepath)
    process_file(filepath.replace('_en.txt', '_ko.txt'))
    
print("Assigned paragraph numbers and saved to numbered/")
