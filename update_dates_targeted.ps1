$now = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$files = Get-ChildItem -Path "content/post" -Filter "*.md" -Recurse

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    $updated = $false
    
    # +++か---かを判別
    $isToml = ($content -match '^\+\+\+')
    
    # 既存のdateがあるか
    if ($content -match '(?m)^date\s*[:=]\s*"(.*?)"') {
        $existingDate = $matches[1]
        if ($existingDate -match '^0001') {
            if ($isToml) {
                $content = $content -replace '(?m)^date\s*[:=].*$', ("date = `"$now`"")
            } else {
                $content = $content -replace '(?m)^date\s*[:=].*$', ("date: `"$now`"")
            }
            $updated = $true
        }
    } else {
        # dateがない場合、titleの下に追加する
        if ($content -match '(?m)^title\s*[:=].*$') {
            if ($isToml) {
                $content = $content -replace '(?m)^(title\s*[:=].*)$', ("`$1`n" + "date = `"$now`"")
            } else {
                $content = $content -replace '(?m)^(title\s*[:=].*)$', ("`$1`n" + "date: `"$now`"")
            }
            $updated = $true
        }
    }
    
    if ($updated) {
        Set-Content -Path $f.FullName -Value $content -NoNewline
    }
}
Write-Output "Done targeted updates."
