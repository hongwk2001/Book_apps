import os

dst_file = r'c:\git_repo\Book_apps\secret_garden\src\main\res\values\themes.xml'
content = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.SecretGarden" parent="android:Theme.Material.Light.NoActionBar" />
</resources>
"""
with open(dst_file, 'w', encoding='utf-8') as f:
    f.write(content)

manifest_file = r'c:\git_repo\Book_apps\secret_garden\src\main\AndroidManifest.xml'
manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.SecretGarden">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

    <!-- Required for TTS voice discovery on Android 11+ -->
    <queries>
        <intent>
            <action android:name="android.intent.action.TTS_SERVICE" />
        </intent>
    </queries>

</manifest>
"""
with open(manifest_file, 'w', encoding='utf-8') as f:
    f.write(manifest)
print("Saved themes and manifest as proper UTF-8")
