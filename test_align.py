import json
from align import split_sentences_en, split_sentences_ko, align_sentences

data = json.load(open('C:\\git_repo\\Book_apps\\dracula\\src\\main\\assets\\books\\ch_04.json', encoding='utf-8'))
with open('C:\\git_repo\\Book_apps\\output.txt', 'w', encoding='utf-8') as f:
    for d in data:
        if d['tag'] == 'P005':
            en_sents = split_sentences_en(d['en'])
            ko_sents = split_sentences_ko(d['ko'])
            chunks = align_sentences(en_sents, ko_sents)
            for i, (ec, kc) in enumerate(chunks):
                f.write(f"Chunk {i+1}:\n")
                f.write(f"EN: {' '.join(ec)}\n")
                f.write(f"KO: {' '.join(kc)}\n")
                f.write("-" * 20 + "\n")
            break
