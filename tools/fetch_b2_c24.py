import urllib.request
import re

url = "https://standardebooks.org/ebooks/charles-dickens/a-tale-of-two-cities/text/book-2-chapter-24"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
    idx = html.find("I wish I were going myself")
    if idx != -1:
        snippet = html[idx-100:idx+2500]
        clean = re.sub(r'<[^>]+>', '', snippet)
        print("=== STANDARDEBOOKS TEXT ===")
        print(clean)
    else:
        print("Not found in HTML")
except Exception as e:
    print("Fetch error:", e)
