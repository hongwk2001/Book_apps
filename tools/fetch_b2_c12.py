import urllib.request
import re

url = "https://standardebooks.org/ebooks/charles-dickens/a-tale-of-two-cities/text/book-2-chapter-12"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
    # search
    idx = html.find("Can I do anything for you")
    if idx != -1:
        snippet = html[idx-200:idx+600]
        # remove html tags
        clean = re.sub(r'<[^>]+>', '', snippet)
        print("=== STANDARDEBOOKS TEXT ===")
        print(clean)
except Exception as e:
    print("Fetch error:", e)
