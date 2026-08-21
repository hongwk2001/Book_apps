import os
import re

directory = r'c:\git_repo\Book_apps\secret_garden'

paras = []
for ch_num in [f"{i:02d}" for i in range(1, 28)]:
    en_file = os.path.join(directory, f'ch_{ch_num}_en.txt')
    with open(en_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^(P\d+[a-z]?)\|', line)
            if match:
                prefix = match.group(1)
                text = line[len(prefix)+1:].strip()
                paras.append((len(text), ch_num, prefix, text))

# Sort by length descending
paras.sort(key=lambda x: x[0], reverse=True)

with open(r'c:\git_repo\Book_apps\secret_garden\long_paragraphs.txt', 'w', encoding='utf-8') as out:
    out.write("# Top 50 Longest Paragraphs\n\n")
    for length, ch, prefix, text in paras[:50]:
        snippet = text[:100] + "..." if len(text) > 100 else text
        out.write(f"- **Chapter {ch} - {prefix}** ({length} characters): `{snippet}`\n")
