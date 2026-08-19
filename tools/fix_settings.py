with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\settings\SettingsDialog.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Speed
text = text.replace('Text(stringResource(R.string.setting_speed, enSpeed), style = MaterialTheme.typography.bodySmall)', 'Text(stringResource(R.string.setting_speed, koSpeed), style = MaterialTheme.typography.bodySmall)', 2)
text = text.replace('Text(stringResource(R.string.setting_speed, koSpeed), style = MaterialTheme.typography.bodySmall)', 'Text(stringResource(R.string.setting_speed, enSpeed), style = MaterialTheme.typography.bodySmall)', 1)

# Fix Pitch
text = text.replace('Text(stringResource(R.string.setting_pitch, koPitch), style = MaterialTheme.typography.bodySmall)', 'Text(stringResource(R.string.setting_pitch, enPitch), style = MaterialTheme.typography.bodySmall)')
text = text.replace('Text(stringResource(R.string.setting_pitch, enPitch), style = MaterialTheme.typography.bodySmall)', 'Text(stringResource(R.string.setting_pitch, koPitch), style = MaterialTheme.typography.bodySmall)', 2)
text = text.replace('Text(stringResource(R.string.setting_pitch, koPitch), style = MaterialTheme.typography.bodySmall)', 'Text(stringResource(R.string.setting_pitch, enPitch), style = MaterialTheme.typography.bodySmall)', 1)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\settings\SettingsDialog.kt', 'w', encoding='utf-8') as f:
    f.write(text)
