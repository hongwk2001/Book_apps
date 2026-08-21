import json, re

def split_sentences(text):
    text = text.replace('\n', ' ')
    matches = re.finditer(r'([^.!?]+[.!?]+[\"\']?)(\s+|$)', text)
    sents = [m.group(1).strip() for m in matches]
    if not sents:
        return [text.strip()]
    return sents

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_20.ch16.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\sentences_out.txt', 'w', encoding='utf-8') as out:
    for item in data:
        en_sents = split_sentences(item['en'])
        ko_sents = split_sentences(item['ko'])
        out.write(f"--- ID {item['id']} ---\n")
        out.write(f"EN: {en_sents}\n")
        out.write(f"KO: {ko_sents}\n\n")
