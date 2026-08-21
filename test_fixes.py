import json, re

data = json.load(open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_07.json', encoding='utf-8'))

# Apply text shifts
for i, d in enumerate(data):
    if d['id'] == 15:
        # move last EN sentence to 16
        en_text = d['en']
        parts = en_text.split('Some waves completely jumped')
        data[i]['en'] = parts[0].strip()
        data[i+1]['en'] = 'Some waves completely jumped' + parts[1] + ' ' + data[i+1]['en']
    elif d['id'] == 20:
        # move last KO sentence to 21
        ko_text = d['ko']
        parts = ko_text.split('만조가 가까운')
        data[i]['ko'] = parts[0].strip()
        data[i+1]['ko'] = '만조가 가까운' + parts[1] + ' ' + data[i+1]['ko']
    elif d['id'] == 92:
        # move last KO sentence to 93
        ko_text = d['ko']
        parts = ko_text.split('나는 점점 기력이 다해가고')
        data[i]['ko'] = parts[0].strip()
        data[i+1]['ko'] = '나는 점점 기력이 다해가고' + parts[1] + ' ' + data[i+1]['ko']
    elif d['id'] == 104:
        # move last EN sentence to 105
        en_text = d['en']
        parts = en_text.split('Meanwhile, the funeral procession')
        data[i]['en'] = parts[0].strip()
        data[i+1]['en'] = 'Meanwhile, the funeral procession' + parts[1] + ' ' + data[i+1]['en']

def get_sentences(text):
    text = re.sub(r'(Mr|Mrs|Dr|Ms|Prof|St)\.', r'\1<DOT>', text)
    # Fix the quote issue
    text = text.replace('." ', '."<SPLIT>')
    text = text.replace('?" ', '?"<SPLIT>')
    text = text.replace('!" ', '!"<SPLIT>')
    
    # We must also split on Korean quotes if necessary, but usually standard punct suffices
    # Split by punctuation
    sents = []
    for part in text.split('<SPLIT>'):
        sents.extend([s.replace('<DOT>', '.') for s in re.split(r'(?<=[.!?])\s+', part.strip()) if s.strip()])
    return sents

mismatched = []
for d in data:
    en_s = get_sentences(d.get('en', ''))
    ko_s = get_sentences(d.get('ko', ''))
    if len(en_s) != len(ko_s):
        mismatched.append((d['id'], len(en_s), len(ko_s)))

print('Mismatched after fixes:', mismatched)
