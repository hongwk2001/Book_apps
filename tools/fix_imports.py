import sys

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    vm_content = f.read()

vm_imports = '''import android.media.AudioManager
import android.media.AudioFocusRequest
import android.content.Context
import android.os.Build
'''
vm_content = vm_content.replace('import android.app.Application', 'import android.app.Application\n' + vm_imports)
with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(vm_content)


with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    rs_content = f.read()

rs_imports = '''import androidx.compose.ui.res.stringResource
import com.tkprof.shared.R
'''
rs_content = rs_content.replace('import android.app.Activity', 'import android.app.Activity\n' + rs_imports)

# Fix the broken paywall text replacements
rs_content = rs_content.replace('Text("Chapter  is locked"', 'Text(stringResource(R.string.paywall_locked_desc, chapterNumber)')
import re
rs_content = re.sub(r'Text\("You\'ve read \$\{bookConfig\.freeChapters\} free chapters.*?"', 'Text(stringResource(R.string.paywall_purchase_desc)"', rs_content)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(rs_content)
