import json, re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

def split_ko(text):
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
        en_text = item['en'].replace('\n', ' ')
        en_sents = nltk.sent_tokenize(en_text)
        ko_sents = split_ko(item['ko'])
        out.write(f"--- ID {item['id']} ---\n")
        out.write(f"EN ({len(en_sents)}): {en_sents}\n")
        out.write(f"KO ({len(ko_sents)}): {ko_sents}\n\n")
