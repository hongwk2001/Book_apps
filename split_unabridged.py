import os
import re

raw_path = r"c:\git_repo\TKprof_book\books\frankenstein\raw_source.txt"
prep_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data"

with open(raw_path, "r", encoding="utf-8") as f:
    text = f.read()

# The actual content starts around "Letter 1" and ends before "End of the Project Gutenberg eBook"
start_idx = text.find("Letter 1")
end_idx = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
if end_idx == -1:
    end_idx = text.find("End of the Project Gutenberg eBook")
if end_idx == -1:
    end_idx = len(text)

content = text[start_idx:end_idx]

# Split by Letter X and Chapter X
pattern = r'^(Letter \d+|Chapter \d+)$'
parts = re.split(pattern, content, flags=re.MULTILINE)

# parts[0] is empty or whatever is before the first Letter 1 (since we started at Letter 1, it's empty)
if not parts[0].strip():
    parts = parts[1:]

# Now parts alternates between title (e.g. "Letter 1") and content.
files = [
    "1.Lt1", "2.Lt2", "3.Lt3", "4.Lt4",
    "5.ch1", "6.ch2", "7.ch3", "8.ch4", "9.ch5", "10.ch6",
    "11.ch7", "12.ch8", "13.ch9", "14.ch10", "15.ch11", "16.ch12",
    "17.ch13", "18.ch14", "19.ch15", "20.ch16", "21.ch17", "22.ch18",
    "23.ch19", "24.ch20", "25.ch21", "26.ch22", "27.ch23", "28.ch24"
]

for i in range(0, len(parts), 2):
    title = parts[i]
    body = parts[i+1].strip()
    
    file_idx = i // 2
    if file_idx < len(files):
        filename = f"{files[file_idx]}_en.txt"
        filepath = os.path.join(prep_dir, filename)
        
        # Write title + body
        full_text = f"{title}\n\n{body}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"Wrote {filename}")

