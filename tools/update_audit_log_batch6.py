import json
from datetime import datetime

audit_log_path = r"C:\git_repo\Book_apps\PARAGRAPH_SPLITTING_AUDIT_LOG.md"

with open('split_validation_report_tier350.txt', encoding='utf-8') as f:
    report = f.read()

log_entry = f"""
## Batch 6: 21 Multi-Sentence Paragraphs (350–399 Characters) Split ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
- **Scope**: All 21 multi-sentence paragraphs in the 350–399 character tier in *A Tale of Two Cities*.
- **Splitting Strategy**: 1-to-1 Bilingual Sentence Boundary Matching.
- **Invariant Checking**: 100% character and word conservation verified for both English and Korean.
- **Result**: Zero multi-sentence paragraphs $\ge 350$ characters remain in *Two Cities*!
- **Build Status**: `:shared:testDebugUnitTest` $\rightarrow$ `BUILD SUCCESSFUL`.

```
{report[:1200]}... [Full report saved in split_validation_report_tier350.txt]
```

"""

with open(audit_log_path, 'a', encoding='utf-8') as f:
    f.write(log_entry)

print("Updated PARAGRAPH_SPLITTING_AUDIT_LOG.md for Batch 6")
