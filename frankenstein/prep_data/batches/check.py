import json
import re

def split_sentences(text):
    text = text.replace('\n', ' ')
    # Split by punctuation followed by space and then a capital letter or Korean char or quote
    sents = re.split(r'(?<=[.!?])\s+(?=[\"\'“‘A-Z가-힣])', text)
    return [s.strip() for s in sents if s.strip()]

def main():
    data = json.load(open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_11.ch7.json', encoding='utf-8'))
    mismatches = []
    
    for idx, item in enumerate(data):
        en_sents = split_sentences(item['en'])
        ko_sents = split_sentences(item['ko'])
        if len(en_sents) != len(ko_sents):
            mismatches.append((idx, len(en_sents), len(ko_sents), item['tag']))
    
    print(f'Total mismatches: {len(mismatches)}')
    for m in mismatches:
        print(m)

if __name__ == '__main__':
    main()
