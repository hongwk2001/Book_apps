import os

strings_xml = r'c:\git_repo\Book_apps\secret_garden\src\main\res\values\strings.xml'
content = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
<resources>
    <string name=\"app_name\">Secret Garden: 빴밀의 화원</string>
    <string name=\"app_name_en\">Secret Garden</string>
    <string name=\"app_name_ko\">비밀의 화원</string>
    <string name=\"iap_product_id\">com.tkprof.secretgarden.full</string>
    <integer name=\"free_chapters\">2</integer>
    <integer name=\"total_chapters\">27</integer>
</resources>"""

with open(strings_xml, 'w', encoding='utf-8') as f:
    f.write(content)