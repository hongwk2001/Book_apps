with open('bad_endings_report.txt', encoding='utf-8') as f:
    text = f.read()

tc_section = text.split('BOOK: Dracula')[0]
entries = tc_section.split('[')

with open('mr_endings.txt', 'w', encoding='utf-8') as out:
    for e in entries:
        if "abbreviation 'mr.'" in e or "abbreviation 'mrs.'" in e:
            out.write('[' + e.strip() + '\n' + '-'*50 + '\n')

print("Wrote mr_endings.txt")
