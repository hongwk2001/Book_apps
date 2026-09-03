import json
from datetime import datetime

audit_log_path = r"C:\git_repo\Book_apps\PARAGRAPH_SPLITTING_AUDIT_LOG.md"

with open('split_validation_report_singles16.txt', encoding='utf-8') as f:
    report = f.read()

log_entry = f"""
## Batch 7: 16 Single-Sentence Paragraphs (350–399 Characters) ESL-Friendly Split ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
- **Scope**: All 16 single-sentence paragraphs in the 350–399 character tier in *A Tale of Two Cities*.
- **Splitting Strategy**: Clause boundary and ESL-optimized natural thought splitting (Categories A, B, and C).
- **Result**: Zero paragraphs in the 350–399 tier remain in *Two Cities*!
- **Build Status**: `:shared:testDebugUnitTest` $\rightarrow$ `BUILD SUCCESSFUL`.

```
{report[:1200]}... [Full report saved in split_validation_report_singles16.txt]
```

"""

with open(audit_log_path, 'a', encoding='utf-8') as f:
    f.write(log_entry)

print("Updated PARAGRAPH_SPLITTING_AUDIT_LOG.md for Batch 7")
