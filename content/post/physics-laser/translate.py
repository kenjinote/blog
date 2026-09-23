import re

input_file = r"c:\work\kenji.blog\content\post\physics-laser\index.md"
output_file = r"c:\work\kenji.blog\content\post\physics-laser\index.fr.md"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements
content = content.replace('title: "物理学: レーザーの仕組み - 誘導放出と光の増幅"', 'title: "Physique : Le mécanisme du laser - Émission stimulée et amplification de la lumière"')
content = content.replace('# 物理学: レーザーの仕組み', '# Physique : Le mécanisme du laser')
content = content.replace('レーザーは誘導放出によって光を増幅します。', 'Le laser amplifie la lumière par émission stimulée.')
content = content.replace('## 誘導放出プロセス', '## Processus d\'émission stimulée')

# Mermaid
content = content.replace('A["Atom in Excited State"]', 'A["Atome à l\'état excité"]')
content = content.replace('B["Incident Photon"]', 'B["Photon incident"]')
content = content.replace('C["Two Coherent Photons"]', 'C["Deux photons cohérents"]')

content = content.replace('## レート方程式', '## Équations de taux')

# Loop for repetitive parts
content = re.sub(r'## 追加技術検証パート (\d+)', r'## Validation technique supplémentaire partie \1', content)
content = content.replace(
    'このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。',
    "Dans cette section, nous approfondissons les détails techniques et les études de cas. Nous évaluons les performances dans diverses conditions et examinons les défis et les solutions liés à l'intégration avec d'autres systèmes. Nous discutons également des perspectives futures et des limites."
)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Translation completed")
