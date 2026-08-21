import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')
f = open('bad_ps.json', encoding='utf-8')
d = json.load(f)
def split_sentences(text):
    sentences = re.split(r'(?<=[.?!])\s+(?=[A-Z0-9가-힣\'\"“])|(?<=[.?!])\s*$', text.strip())
    return [s.strip() for s in sentences if s.strip()]

out = []
for item in d:
    p = item['p']
    en_s = split_sentences(item['en'])
    ko_s = split_sentences(item['ko'])
    out.append(f"==== {p} ====")
    for i, e in enumerate(en_s):
        out.append(f"EN {i}: {e}")
    for i, k in enumerate(ko_s):
        out.append(f"KO {i}: {k}")
    out.append("")

with open('sentences_dump.txt', 'w', encoding='utf-8') as f2:
    f2.write('\n'.join(out))
