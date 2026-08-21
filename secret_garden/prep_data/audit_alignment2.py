import os
import glob
import re

def get_paragraphs(filepath):
    paras = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^P(\d+)([a-z]?)\|(.*)', line)
            if match:
                num = int(match.group(1))
                suffix = match.group(2)
                text = match.group(3).strip()
                if num not in paras:
                    paras[num] = []
                paras[num].append((suffix, text))
    return paras

def snippet(text, length=80):
    if len(text) > length:
        return text[:length] + "..."
    return text

def audit_files():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    raw_files = glob.glob(os.path.join(directory, 'raw_ch_*.txt'))
    
    suspicious = []
    
    for raw_file in sorted(raw_files):
        basename = os.path.basename(raw_file)
        match = re.search(r'raw_ch_(\d+)\.txt', basename)
        if not match: continue
        ch_num = match.group(1)
        en_file = os.path.join(directory, f'ch_{ch_num}_en.txt')
        if not os.path.exists(en_file): continue
        
        raw_paras = get_paragraphs(raw_file)
        en_paras = get_paragraphs(en_file)
        
        for num in sorted(raw_paras.keys()):
            r_text = raw_paras[num][0][1]
            r_len = len(r_text)
            
            if num not in en_paras:
                suspicious.append(f"\n### Chapter {ch_num} - P{num}")
                suspicious.append(f"- **Issue**: Missing in English (Raw length {r_len})")
                suspicious.append(f"- **RAW**: `{snippet(r_text)}`")
                continue
                
            e_items = en_paras[num]
            e_len = sum(len(t) for _, t in e_items)
            
            issues = []
            if len(e_items) > 1:
                suffixes = [s for s, _ in e_items]
                issues.append(f"Split into {len(e_items)} parts in EN ({', '.join(suffixes)})")
            
            if r_len > 50:
                ratio = e_len / r_len
                if ratio < 0.5:
                    issues.append(f"EN is suspiciously short (Ratio {ratio:.2f})")
                elif ratio > 2.0:
                    issues.append(f"EN is suspiciously long (Ratio {ratio:.2f})")
                    
            if issues:
                suspicious.append(f"\n### Chapter {ch_num} - P{num}")
                for issue in issues:
                    suspicious.append(f"- **Issue**: {issue}")
                suspicious.append(f"- **RAW**: `{snippet(r_text)}`")
                for suffix, e_text in e_items:
                    suspicious.append(f"- **EN (P{num}{suffix})**: `{snippet(e_text)}`")

    with open(r'C:\Users\hongw\.gemini\antigravity\brain\d2ce9842-01e6-483c-ae25-ed74580253c7\audit_report.md', 'w', encoding='utf-8') as f:
        f.write("# Suspicious Alignments (With Snippets)\n")
        for s in suspicious:
            f.write(s + "\n")

if __name__ == '__main__':
    audit_files()
