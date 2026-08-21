import json
import re

def split_sentences(text):
    # Treat semicolon as a sentence boundary to help reduce sentence counts
    parts = re.split(r'([.?!;]+[\"”\']?)(?:\s+|$)', text)
    sentences = []
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

with open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_4.Lt4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for idx, item in enumerate(data):
    en_sents = split_sentences(item['en'])
    ko_sents = split_sentences(item['ko'])
    out.append(f"ID {item['id']}: EN({len(en_sents)}) KO({len(ko_sents)})")
    if len(en_sents) != len(ko_sents):
        out.append(f"Mismatch at ID {item['id']}:")
        for i, s in enumerate(en_sents): out.append(f"EN {i}: {s}")
        for i, s in enumerate(ko_sents): out.append(f"KO {i}: {s}")

with open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/out2.log', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
