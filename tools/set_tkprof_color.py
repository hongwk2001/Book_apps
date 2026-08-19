import os

color_xml_path = r'C:\git_repo\Book_apps\dracula\src\main\res\values\colors.xml'
content = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="tkprof_purple">#130319</color>
    <color name="ic_launcher_background">@color/tkprof_purple</color>
</resources>
'''
with open(color_xml_path, 'w') as f:
    f.write(content)

shared_color_xml = r'C:\git_repo\Book_apps\shared\src\main\res\values\colors.xml'
if not os.path.exists(os.path.dirname(shared_color_xml)):
    os.makedirs(os.path.dirname(shared_color_xml), exist_ok=True)
    
shared_content = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="tkprof_purple">#130319</color>
</resources>
'''
with open(shared_color_xml, 'w') as f:
    f.write(shared_content)

print("Updated colors.xml")
