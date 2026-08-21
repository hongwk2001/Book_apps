import urllib.request
import json
try:
    url = "https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/bat.svg"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
