with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
old_paywall = r'@Composable\nprivate fun PaywallScreen.*?\}\n\}\n'
new_paywall = '''@Composable
private fun PaywallScreen(chapterNumber: Int, bookConfig: com.tkprof.shared.model.BookConfig, onBuy: () -> Unit) {
    Box(modifier = Modifier.fillMaxSize().background(MaterialTheme.colorScheme.background), contentAlignment = Alignment.Center) {
        Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(16.dp), modifier = Modifier.padding(32.dp)) {
            Icon(Icons.Default.Lock, contentDescription = null, modifier = Modifier.size(64.dp), tint = MaterialTheme.colorScheme.primary)
            Text(stringResource(R.string.paywall_locked_desc, chapterNumber), style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold, textAlign = TextAlign.Center)
            Text(stringResource(R.string.paywall_purchase_desc), style = MaterialTheme.typography.bodyMedium, textAlign = TextAlign.Center, color = MaterialTheme.colorScheme.onSurfaceVariant)
            Button(onClick = onBuy, modifier = Modifier.fillMaxWidth()) { Icon(Icons.Default.ShoppingCart, contentDescription = null); Spacer(Modifier.width(8.dp)); Text(stringResource(R.string.btn_unlock_now)) }
        }
    }
}
'''
text = re.sub(old_paywall, new_paywall, text, flags=re.DOTALL)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
