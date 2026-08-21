import os
import glob
import re

def process_files():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    files = glob.glob(os.path.join(directory, 'raw_ch_*.txt'))
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Normalize newlines
        content = content.replace('\r\n', '\n')
        
        # Split by empty lines (2 or more newlines)
        blocks = re.split(r'\n{2,}', content)
        
        numbered_lines = []
        counter = 1
        for block in blocks:
            block = block.strip()
            if block:
                # Unwrap by replacing internal newlines with spaces
                unwrapped_block = re.sub(r'\s+', ' ', block)
                numbered_lines.append(f'P{counter}| {unwrapped_block}\n')
                counter += 1
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(numbered_lines)
        print(f'Processed: {os.path.basename(filepath)}')

if __name__ == '__main__':
    process_files()
