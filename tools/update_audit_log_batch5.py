import json
from datetime import datetime

audit_log_path = r"C:\git_repo\Book_apps\PARAGRAPH_SPLITTING_AUDIT_LOG.md"

with open('split_validation_report.txt', encoding='utf-8') as f:
    report = f.read()

log_entry = f"""
## Batch 5: 23 Multi-Sentence Mega-Paragraphs (400–499 Characters) Split ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
- **Scope**: All 23 multi-sentence paragraphs $\ge 400$ characters in *A Tale of Two Cities*.
- **Splitting Strategy**: 1-to-1 Bilingual Sentence Boundary Matching.
- **Invariant Checking**: 100% character and word conservation verified for both English and Korean.
- **Result**: Zero multi-sentence paragraphs $\ge 400$ characters remain in *Two Cities*!
- **Build Status**: `:shared:testDebugUnitTest` $\rightarrow$ `BUILD SUCCESSFUL`.

```
{report[:1200]}... [Full report saved in split_validation_report.txt]
```

"""

with open(audit_log_path, 'a', encoding='utf-8') as f:
    f.write(log_entry)

print("Updated PARAGRAPH_SPLITTING_AUDIT_LOG.md")
