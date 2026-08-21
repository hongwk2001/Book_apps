import json, re

data = json.load(open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_07.json', encoding='utf-8'))

for i, d in enumerate(data):
    # Cross-paragraph shifts
    if d['id'] == 15:
        en_text = d['en']
        parts = en_text.split('Some waves completely jumped')
        data[i]['en'] = parts[0].strip()
        data[i+1]['en'] = 'Some waves completely jumped' + parts[1] + ' ' + data[i+1]['en']
    elif d['id'] == 20:
        ko_text = d['ko']
        parts = ko_text.split('만조가 가까운')
        data[i]['ko'] = parts[0].strip()
        data[i+1]['ko'] = '만조가 가까운' + parts[1] + ' ' + data[i+1]['ko']
    elif d['id'] == 93:
        # shift EN 1 to 92
        en_text = d['en']
        parts = en_text.split('If he appears')
        data[i-1]['en'] = data[i-1]['en'] + ' ' + parts[0].strip()
        data[i]['en'] = 'If he appears' + parts[1]
    elif d['id'] == 104:
        en_text = d['en']
        parts = en_text.split('Meanwhile, the funeral procession')
        data[i]['en'] = parts[0].strip()
        data[i+1]['en'] = 'Meanwhile, the funeral procession' + parts[1] + ' ' + data[i+1]['en']
    
    # Internal merges (converting period to comma to match sentence counts)
    if d['id'] == 6:
        data[i]['ko'] = data[i]['ko'].replace('휘몰아쳤다. 기록에', '휘몰아쳤다, 기록에')
    elif d['id'] == 59:
        data[i]['ko'] = data[i]['ko'].replace('선언했다. 너희들이', '선언했다, 너희들이')
    elif d['id'] == 62:
        data[i]['ko'] = data[i]['ko'].replace('정신이 없었다. 두려움에', '정신이 없었다, 두려움에')
    elif d['id'] == 106:
        data[i]['ko'] = data[i]['ko'].replace('수도 있겠다. 거기다', '수도 있겠다, 거기다')

def get_sentences(text):
    text = re.sub(r'(Mr|Mrs|Dr|Ms|Prof|St)\.', r'\1<DOT>', text)
    text = text.replace('." ', '."<SPLIT>')
    text = text.replace('?" ', '?"<SPLIT>')
    text = text.replace('!" ', '!"<SPLIT>')
    sents = []
    for part in text.split('<SPLIT>'):
        sents.extend([s.replace('<DOT>', '.') for s in re.split(r'(?<=[.!?])\s+', part.strip()) if s.strip()])
    return sents

mismatched = []
for d in data:
    en_s = get_sentences(d.get('en', ''))
    ko_s = get_sentences(d.get('ko', ''))
    if len(en_s) > 3:
        if len(en_s) != len(ko_s):
            mismatched.append((d['id'], len(en_s), len(ko_s)))

print('Mismatched > 3 sentences:', mismatched)
