with open(r"C:\git_repo\Book_apps\frankenstein\src\main\res\values\strings.xml", "w", encoding="utf-8") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Frankenstein: 프랑켄슈타인</string>
    <string name="app_name_en">Frankenstein</string>
    <string name="app_name_ko">프랑켄슈타인</string>
    <string name="iap_product_id">com.tkprof.frankenstein.full</string>
    <integer name="free_chapters">2</integer>
    <integer name="total_chapters">28</integer>
</resources>""")