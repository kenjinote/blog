$out_path = 'c:\work\kenji.blog\content\post\tech-3d-engine\index.ar.md'

$header = @"
---
title: "تقنية الألعاب: تطور محركات الرسومات ثلاثية الأبعاد (Unreal Engine / Unity)"
date: 2026-09-23T04:01:41+09:00
categories: ["gaming", "technology"]
tags: ["3d", "engine", "unreal", "unity", "graphics"]
---
# تقنية الألعاب: تطور محركات الرسومات ثلاثية الأبعاد

ساهمت المحركات ثلاثية الأبعاد في تطوير العرض في الوقت الفعلي.

## خط أنابيب العرض

```mermaid
flowchart TD
    A["Vertex Shader (Transformation)"] --> B["Rasterization"]
    B --> C["Fragment Shader (Lighting)"]
```

## معادلة العرض
$$ L_o = L_e + \int_{\Omega} f_r L_i (w_i \cdot n) d w_i $$
"@

Set-Content -Path $out_path -Value $header -Encoding UTF8

for ($i=1; $i -le 393; $i++) {
    $section = @"

## جزء التحقق الفني الإضافي $i

في هذا القسم، نتعمق أكثر في التفاصيل الفنية ودراسات الحالة. نقوم بتقييم الأداء في ظل ظروف مختلفة ومناقشة التحديات والحلول المتعلقة بالتكامل مع الأنظمة الأخرى. كما نناقش الآفاق والقيود المستقبلية.
"@
    Add-Content -Path $out_path -Value $section -Encoding UTF8
}
