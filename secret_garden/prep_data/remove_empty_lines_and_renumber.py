import os
import glob
import re

def process_files():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    files = glob.glob(os.path.join(directory, '*.txt'))
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        numbered_lines = []
        counter = 1
        for line in lines:
            # Remove existing P#| prefix if it exists
            clean_line = re.sub(r'^P\d+\|\s*', '', line).strip()
            if clean_line: # Only add if not empty
                numbered_lines.append(f'P{counter}| {clean_line}\n')
                counter += 1
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(numbered_lines)
        print(f'Processed: {os.path.basename(filepath)}')

if __name__ == '__main__':
    process_files()
