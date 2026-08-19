import base64
with open(r'C:\git_repo\Book_apps\dracula\src\main\res\mipmap-xxxhdpi\ic_launcher.png', 'rb') as f:
    print(base64.b64encode(f.read()[:20]).decode('utf-8'))
