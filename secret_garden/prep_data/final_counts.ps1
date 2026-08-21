$chapters = 1..27 | ForEach-Object { '{0:D2}' -f $_ }
$results = @()
foreach ($ch in $chapters) {
    $raw_lines = (Get-Content "c:\git_repo\Book_apps\secret_garden\raw_ch_${ch}.txt" | Where-Object { $_.Trim() -ne '' }).Count
    $en_lines = (Get-Content "c:\git_repo\Book_apps\secret_garden\ch_${ch}_en.txt" | Where-Object { $_.Trim() -ne '' }).Count
    $ko_lines = (Get-Content "c:\git_repo\Book_apps\secret_garden\ch_${ch}_ko.txt" | Where-Object { $_.Trim() -ne '' }).Count
    $results += [PSCustomObject]@{
        Chapter = $ch
        RAW = $raw_lines
        EN = $en_lines
        KO = $ko_lines
    }
}
$results | Export-Csv -Path c:\git_repo\Book_apps\secret_garden\final_counts.csv -NoTypeInformation
