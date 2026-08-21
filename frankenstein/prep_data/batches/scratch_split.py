import json
import re

def split_sentences(text):
    sentences = []
    # A simple but better regex that handles multiple sentences correctly
    # It looks for punctuation followed by space or end of string, keeping punctuation attached.
    # We use re.split with a capturing group to keep the delimiter.
    parts = re.split(r'([.?!]+[\"”\']?)(?:\s+|$)', text)
    
    current_sent = ""
    for i in range(0, len(parts)-1, 2):
        if parts[i]:
            current_sent += parts[i]
        if i+1 < len(parts) and parts[i+1]:
            current_sent += parts[i+1]
            sentences.append(current_sent.strip())
            current_sent = ""
    if parts[-1].strip():
        current_sent += parts[-1]
    if current_sent.strip():
        sentences.append(current_sent.strip())
        
    return sentences

with open('batch_4.Lt4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for idx, item in enumerate(data):
    en_sents = split_sentences(item['en'])
    ko_sents = split_sentences(item['ko'])
    out.append(f"ID {item['id']}: EN({len(en_sents)}) KO({len(ko_sents)})")
    if len(en_sents) != len(ko_sents):
        out.append(f"Mismatch at ID {item['id']}:")
        out.append("EN: " + str(en_sents))
        out.append("KO: " + str(ko_sents))

with open('out.log', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
