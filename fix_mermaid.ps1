$files = Get-ChildItem -Path "C:\work\kenji.blog\content\post\quantum-computer-ultimate-guide" -Filter "*.md"
foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    # Pattern 1
    $content = [regex]::Replace($content, 'Uf -->\|"([^"]+)"\|([^⟩]+)⟩ \| (QFT\["[^"]+"\])', 'Uf -- "$1 |$2⟩" --> $3')
    # Pattern 2 (Discard)
    $content = [regex]::Replace($content, 'Uf -->\|"([^"]+)"\|([^⟩]+)⟩ \| (Discard\["[^"]+"\])', 'Uf -- "$1 |$2⟩" --> $3')
    Set-Content -Path $f.FullName -Value $content -NoNewline
}
Write-Output "Replacement done."
