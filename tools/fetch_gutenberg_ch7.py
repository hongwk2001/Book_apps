import urllib.request
import re

url = "https://www.gutenberg.org/files/98/98-0.txt"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
    
    # Search for Hanging-sword Alley
    idx = content.find("Hanging-sword Alley")
    if idx != -1:
        print("=== GUTENBERG TEXT AROUND HANGING-SWORD ALLEY ===")
        print(content[idx-100:idx+600])
except Exception as e:
    print("Could not fetch Gutenberg:", e)
