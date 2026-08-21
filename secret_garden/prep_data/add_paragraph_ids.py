import os
import glob

def process_files():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    files = glob.glob(os.path.join(directory, 'ch_*_en.txt')) + glob.glob(os.path.join(directory, 'ch_*_ko.txt'))
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        numbered_lines = []
        for i, line in enumerate(lines, 1):
            clean_line = line.rstrip('\r\n')
            numbered_lines.append(f'P{i}| {clean_line}\n')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(numbered_lines)
        print(f'Processed: {os.path.basename(filepath)}')

if __name__ == '__main__':
    process_files()
