$now = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$files = Get-ChildItem -Path "content/post" -Filter "*.md" -Recurse

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    
    # 既存の date を置換
    if ($content -match '(?m)^date\s*[:=].*$') {
        $newContent = $content -replace '(?m)^date\s*[:=].*$', ("date: `"$now`"")
        Set-Content -Path $f.FullName -Value $newContent -NoNewline
    } else {
        # dateがない場合、titleの下に追加する
        if ($content -match '(?m)^title\s*[:=].*$') {
            $newContent = $content -replace '(?m)^(title\s*[:=].*)$', ("`$1`n" + "date: `"$now`"")
            Set-Content -Path $f.FullName -Value $newContent -NoNewline
        }
    }
}
Write-Output "Done updating dates."
