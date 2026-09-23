import re
import os

input_path = r'c:\work\kenji.blog\content\post\history-of-salesforce\index.md'
output_path = r'c:\work\kenji.blog\content\post\history-of-salesforce\index.ar.md'

with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements
content = content.replace('title: "企業史: Salesforceの歴史 - SaaS（クラウドソフトウェア）の開拓者"', 'title: "تاريخ الشركة: تاريخ Salesforce - رائد SaaS (البرمجيات السحابية)"')
content = content.replace('# 企業史: Salesforceの歴史 - SaaS（クラウドソフトウェア）の開拓者', '# تاريخ الشركة: تاريخ Salesforce - رائد SaaS (البرمجيات السحابية)')
content = content.replace('SalesforceはSaaSのパイオニアです。', 'Salesforce هي رائدة في مجال SaaS.')
content = content.replace('## クラウドコンピューティングの進化', '## تطور الحوسبة السحابية')
content = content.replace('## 数学モデル', '## النموذج الرياضي')
content = content.replace('SaaSの成長モデルは以下のようになります：', 'نموذج نمو SaaS هو كما يلي:')

# Translating Mermaid nodes
content = content.replace('A["On-Premise (1990s)"]', 'A["داخل المؤسسة (التسعينيات)"]')
content = content.replace('B["Cloud Computing (2000s)"]', 'B["الحوسبة السحابية (الألفينات)"]')
content = content.replace('C["SaaS (Salesforce)"]', 'C["SaaS (Salesforce)"]')

# Repeated blocks
content = re.sub(r'## 追加技術検証パート (\d+)', r'## جزء التحقق الفني الإضافي \1', content)
content = content.replace('このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。', 'في هذا القسم، نتعمق في مزيد من التفاصيل الفنية ودراسات الحالة. نقوم بتقييم الأداء في ظل ظروف مختلفة ونفحص التحديات والحلول المتعلقة بالتكامل مع الأنظمة الأخرى. كما نناقش الآفاق والقيود المستقبلية.')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)
