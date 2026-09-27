import json
import glob
import os
import re

app_dir = 'C:/git_repo/Book_apps/two_cities/src/main/assets/books'
raw_dir = 'C:/git_repo/Book_apps/two_cities/raw_reference_data'

report = ['# Hallucination Audit Report\n']
report.append('| Chapter | Raw ID | Raw Words | EN Words | Ratio | Raw Sents | EN Sents | Flag Reason | Snippet |')
report.append('|---|---|---|---|---|---|---|---|---|')

total_checked = 0
total_flagged = 0

for i in range(1, 46):
    ch_str = f'{i:02d}'
    app_file = os.path.join(app_dir, f'ch_{ch_str}.json')
    raw_file = os.path.join(raw_dir, f'raw_ch_{ch_str}.json')
    
    if not os.path.exists(app_file) or not os.path.exists(raw_file):
        continue
        
    with open(app_file, 'r', encoding='utf-8') as f:
        app_data = json.load(f)
    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        
    # Group EN text by raw_ref_id
    en_by_ref = {}
    is_header_by_ref = {}
    for item in app_data:
        ref_id = item.get('raw_ref_id')
        if ref_id is None: continue
        
        en_text = item.get('en', '').strip()
        is_header = item.get('is_header', False)
        is_header_by_ref[ref_id] = is_header
        
        if ref_id in en_by_ref:
            en_by_ref[ref_id] += ' ' + en_text
        else:
            en_by_ref[ref_id] = en_text
            
    # Process raw data
    for raw_item in raw_data:
        ref_id = raw_item.get('raw_ref_id')
        if ref_id is None: continue
        
        # Skip headers, they're not sentences
        if is_header_by_ref.get(ref_id, False):
            continue
            
        raw_text = raw_item.get('raw', '').strip()
        en_text = en_by_ref.get(ref_id, '').strip()
        
        if not raw_text and not en_text:
            continue
            
        total_checked += 1
        
        # Word counts
        raw_words = len(raw_text.split())
        en_words = len(en_text.split())
        
        # Sentence counts (rough split)
        raw_sents = len([s for s in re.split(r'[.!?]+', raw_text) if s.strip()])
        en_sents = len([s for s in re.split(r'[.!?]+', en_text) if s.strip()])
        
        # Avoid division by zero
        if raw_words == 0: 
            wc_ratio = 999.0
        else:
            wc_ratio = en_words / raw_words
            
        sc_diff = abs(en_sents - raw_sents)
        
        flags = []
        if raw_words > 10: # Only flag significant differences in actual paragraphs
            if wc_ratio > 1.3:
                flags.append('EN too long')
            elif wc_ratio < 0.6:
                flags.append('EN too short')
            
            if sc_diff > 3:
                flags.append('Sent count diff > 3')
                
        if flags:
            total_flagged += 1
            reason = ', '.join(flags)
            snippet = en_text[:50].replace('\n', ' ') + '...'
            report.append(f'| Ch {ch_str} | {ref_id} | {raw_words} | {en_words} | {wc_ratio:.2f} | {raw_sents} | {en_sents} | {reason} | {snippet} |')

report.append('\n')
report.append(f'**Summary:** Checked {total_checked} paragraphs. Flagged {total_flagged} potential hallucinations.')

with open('C:/Users/hongw/.gemini/antigravity/brain/844f8e09-ad2f-4e50-a446-a46263703e90/hallucination_report.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print(f'Audit complete! {total_flagged} items flagged.')

