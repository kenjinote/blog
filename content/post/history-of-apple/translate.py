import sys
import re

def translate(text):
    # Frontmatter
    text = text.replace('title: "Appleの歴史: ガレージから時価総額世界一への軌跡と革新のDNA"', 'title: "Die Geschichte von Apple: Von der Garage zum weltweit wertvollsten Unternehmen und die DNA der Innovation"')
    text = text.replace('description: "スティーブ・ジョブズとウォズニアックのガレージ創業から、iPhone革命、時価総額世界一に至るAppleの歴史と技術的革新を徹底解説。"', 'description: "Eine detaillierte Erklärung der Geschichte und der technologischen Innovationen von Apple, angefangen bei der Gründung in der Garage durch Steve Jobs und Wozniak über die iPhone-Revolution bis hin zur weltweit höchsten Marktkapitalisierung."')
    
    # Headers and general text
    text = re.sub(r'(#+ .*?)創世記：ガレージから始まった革命 \(1976-1980\)', r'\1Genesis: Die Revolution, die in einer Garage begann (1976-1980)', text)
    text = text.replace('1976年、スティーブ・ジョブズ、スティーブ・ウォズニアック、ロナルド・ウェインの3人は、カリフォルニア州ロスアルトスのジョブズの実家のガレージで「Apple Computer Company」を設立しました。', 'Im Jahr 1976 gründeten Steve Jobs, Steve Wozniak und Ronald Wayne die "Apple Computer Company" in der Garage von Jobs\' Elternhaus in Los Altos, Kalifornien.')
    text = text.replace('最初の製品である **Apple I** は、マザーボードのみが提供される組み立てキットでした。ウォズニアックの天才的なハードウェア設計能力と、ジョブズの先見性とマーケティング能力が融合した瞬間です。', 'Das erste Produkt, der **Apple I**, war ein Bausatz, bei dem nur das Motherboard geliefert wurde. Dies war der Moment, in dem Wozniaks geniale Fähigkeiten im Hardware-Design mit Jobs\' Weitsicht und Marketing-Fähigkeiten verschmolzen.')
    
    text = text.replace('### Apple II の大成功', '### Der große Erfolg des Apple II')
    text = text.replace('1977年に発売された **Apple II** は、プラスチックケースにキーボードを統合し、カラーグラフィックスを表示できる画期的な製品でした。VisiCalc（世界初の表計算ソフト）の登場により、Apple II はビジネス市場にも浸透し、爆発的な大ヒットを記録します。', 'Der 1977 auf den Markt gebrachte **Apple II** war ein bahnbrechendes Produkt, das eine Tastatur in einem Kunststoffgehäuse integrierte und Farbgrafiken anzeigen konnte. Mit dem Erscheinen von VisiCalc (der weltweit ersten Tabellenkalkulationssoftware) drang der Apple II auch in den Geschäftsmarkt ein und verzeichnete einen explosiven Mega-Hit.')

    text = re.sub(r'(#+ .*?)マッキントッシュとGUIの夜明け \(1984\)', r'\1Der Beginn des Macintosh und der GUI (1984)', text)
    text = text.replace('1984年、Appleは **Macintosh（マッキントッシュ）** を発売します。これは、GUI（グラフィカル・ユーザー・インターフェース）とマウスを備えた初の一般向けパソコンでした。', '1984 brachte Apple den **Macintosh** auf den Markt. Dies war der erste PC für die breite Öffentlichkeit, der mit einer GUI (grafischen Benutzeroberfläche) und einer Maus ausgestattet war.')
    text = text.replace('当時の画期的な技術として、ビットマップディスプレイとオブジェクト指向プログラミングの概念が導入されました。', 'Als damals bahnbrechende Technologien wurden das Bitmap-Display und das Konzept der objektorientierten Programmierung eingeführt.')

    text = re.sub(r'(#+ .*?)暗黒時代とジョブズの復帰 \(1985-1997\)', r'\1Die dunkle Zeit und die Rückkehr von Jobs (1985-1997)', text)
    text = text.replace('1985年、社内対立によりジョブズはAppleを追放されます。その後、Appleは低迷期に入ります。一方ジョブズはNeXT社とPixar社を立ち上げ、成功を収めます。', '1985 wurde Jobs aufgrund von internen Konflikten aus Apple verdrängt. Danach geriet Apple in eine Phase des Niedergangs. Jobs hingegen gründete NeXT und Pixar und feierte Erfolge.')
    text = text.replace('1996年、Appleは次世代OSの開発に行き詰まり、ジョブズのNeXT社を買収することを決定。1997年にジョブズはAppleに復帰し、暫定CEOに就任します。', '1996 geriet Apple bei der Entwicklung eines Next-Generation-OS in eine Sackgasse und beschloss, Jobs\' Unternehmen NeXT zu kaufen. 1997 kehrte Jobs zu Apple zurück und wurde Interims-CEO.')

    text = text.replace('### NeXTSTEPからmacOSへの進化', '### Die Entwicklung von NeXTSTEP zu macOS')
    text = text.replace('NeXT社のOSである **NeXTSTEP** の技術（Machカーネル、Objective-C）は、後の Mac OS X（現在のmacOS）およびiOSの強固な基盤となりました。', 'Die Technologie des OS von NeXT, **NeXTSTEP** (Mach-Kernel, Objective-C), wurde zum starken Fundament des späteren Mac OS X (dem heutigen macOS) und iOS.')
    text = text.replace('// Objective-C の例 (NeXTSTEP由来の技術)', '// Beispiel in Objective-C (aus NeXTSTEP stammende Technologie)')

    text = re.sub(r'(#+ .*?)iMac, iPod, そして iTunes \(1998-2006\)', r'\1iMac, iPod und iTunes (1998-2006)', text)
    text = text.replace('ジョブズは製品ラインナップを劇的に絞り込み、1998年に **iMac** を発表。トランスルーセント（半透明）のデザインは世界中に衝撃を与えました。', 'Jobs reduzierte die Produktpalette drastisch und kündigte 1998 den **iMac** an. Das transluzente (halbtransparente) Design versetzte die Welt in Staunen.')
    text = text.replace('2001年には **iPod** と **iTunes** を発表し、音楽業界に革命を起こします。「ポケットに1000曲を」というキャッチコピーは、技術とユーザー体験の完璧な融合を示していました。', '2001 wurden der **iPod** und **iTunes** angekündigt und revolutionierten die Musikindustrie. Der Slogan "1.000 Songs in deiner Tasche" zeigte die perfekte Verschmelzung von Technologie und Nutzererfahrung.')

    text = re.sub(r'(#+ .*?)iPhone革命とモバイル時代 \(2007-2011\)', r'\1Die iPhone-Revolution und die mobile Ära (2007-2011)', text)
    text = text.replace('2007年1月、ジョブズは **iPhone** を発表しました。', 'Im Januar 2007 kündigte Jobs das **iPhone** an.')
    text = text.replace('「iPod、電話、インターネットコミュニケーター。これらは3つの独立したデバイスではなく、1つのデバイスだ。」', '"Ein iPod, ein Telefon und ein Internet-Kommunikator. Dies sind nicht drei separate Geräte, sondern ein einziges Gerät."')
    text = text.replace('iPhoneはマルチタッチインターフェースを採用し、物理キーボードを排除しました。これは人類のコミュニケーションの歴史を変える出来事でした。', 'Das iPhone nutzte eine Multi-Touch-Oberfläche und verzichtete auf eine physische Tastatur. Dies war ein Ereignis, das die Geschichte der menschlichen Kommunikation veränderte.')

    text = re.sub(r'(#+ .*?)ティム・クック時代とサービス企業への転換 \(2011-現在\)', r'\1Die Tim-Cook-Ära und der Wandel zum Dienstleistungsunternehmen (2011-Gegenwart)', text)
    text = text.replace('2011年のジョブズの逝去後、ティム・クックがCEOを引き継ぎました。クックの卓越したサプライチェーン管理と、Apple Watch、AirPodsなどのウェアラブルデバイスの成功により、Appleは世界初の時価総額1兆ドル、2兆ドル、3兆ドル企業へと成長しました。', 'Nach dem Tod von Jobs im Jahr 2011 übernahm Tim Cook die Position des CEO. Durch Cooks exzellentes Supply-Chain-Management und den Erfolg von Wearables wie der Apple Watch und den AirPods wuchs Apple zum weltweit ersten Unternehmen mit einer Marktkapitalisierung von 1 Billion, 2 Billionen und 3 Billionen US-Dollar.')

    text = text.replace('### Apple Silicon (M1/M2/M3) の衝撃', '### Der Schock von Apple Silicon (M1/M2/M3)')
    text = text.replace('近年では、Intel製チップから自社設計の **Apple Silicon (ARMアーキテクチャ)** への移行を完了させました。高いパフォーマンスと圧倒的な電力効率を両立させています。', 'In den letzten Jahren wurde der Übergang von Intel-Chips zu selbstentwickeltem **Apple Silicon (ARM-Architektur)** abgeschlossen. Es vereint hohe Leistung mit einer überwältigenden Energieeffizienz.')

    text = re.sub(r'(#+ .*?)AI時代のApple \(Apple Intelligence\)', r'\1Apple im KI-Zeitalter (Apple Intelligence)', text)
    text = text.replace('2024年、Appleは **Apple Intelligence** を発表し、パーソナルコンテキストを理解するオンデバイスAIへの本格参入を果たしました。プライバシーを重視しつつ、Siriの劇的な進化や文章生成・画像生成をOSレベルで統合しています。', '2024 kündigte Apple **Apple Intelligence** an und stieg ernsthaft in die On-Device-KI ein, die den persönlichen Kontext versteht. Unter Wahrung der Privatsphäre wurden eine drastische Weiterentwicklung von Siri sowie die Text- und Bilderzeugung auf OS-Ebene integriert.')

    text = re.sub(r'(#+ )まとめ', r'\1Zusammenfassung', text)
    text = text.replace('Appleの歴史は、テクノロジーとリベラルアーツの交差点に立ち続けた歴史です。ガレージから始まった小さな会社は、今や世界中の人々の生活に欠かせないデジタルエコシステムを構築しています。', 'Die Geschichte von Apple ist eine Geschichte des ständigen Stehens an der Kreuzung von Technologie und freien Künsten (Liberal Arts). Das kleine Unternehmen, das in einer Garage begann, hat nun ein digitales Ökosystem aufgebaut, das aus dem Leben von Menschen auf der ganzen Welt nicht mehr wegzudenken ist.')

    text = re.sub(r'## 追加考察 (\d+): Appleの経営戦略と技術の深掘り', r'## Zusätzliche Überlegung \1: Eine tiefergehende Betrachtung der Geschäftsstrategie und Technologie von Apple', text)

    text = text.replace('subgraph "Apple Founders"', 'subgraph "Apple-Gründer"')
    text = text.replace('SJ["Steve Jobs (Marketing/Vision)"]', 'SJ["Steve Jobs (Marketing/Vision)"]')
    text = text.replace('SW["Steve Wozniak (Engineering)"]', 'SW["Steve Wozniak (Technik)"]')
    text = text.replace('RW["Ronald Wayne (Administration)"]', 'RW["Ronald Wayne (Verwaltung)"]')

    text = text.replace('Xerox["Xerox PARC (GUI Concept)"]', 'Xerox["Xerox PARC (GUI-Konzept)"]')
    text = text.replace('Jobs["Steve Jobs Visit (1979)"]', 'Jobs["Steve Jobs Besuch (1979)"]')
    text = text.replace('Lisa["Apple Lisa (1983)"]', 'Lisa["Apple Lisa (1983)"]')
    text = text.replace('Mac["Macintosh (1984)"]', 'Mac["Macintosh (1984)"]')
    text = text.replace('Modern["Modern GUI OS"]', 'Modern["Modernes GUI-Betriebssystem"]')

    text = text.replace('pie title "Mobile OS Market Share Shift (Concept)"', 'pie title "Marktanteilsverschiebung bei mobilen Betriebssystemen (Konzept)"')
    text = text.replace('"Others" : 15', '"Andere" : 15')
    text = text.replace('"Others" : 2', '"Andere" : 2')
    text = text.replace('%% ↓ After iPhone/Android', '%% ↓ Nach iPhone/Android')

    # Fix mangled math block and translate
    text = text.replace('\x09ext{Performance per Watt}', '\\\\text{Leistung pro Watt}')
    text = text.replace('\x09ext{Computation Output (FLOPS)}', '\\\\text{Rechenleistung (FLOPS)}')
    text = text.replace('\x09ext{Power Consumption (Watts)}', '\\\\text{Stromverbrauch (Watt)}')
    text = text.replace('\x0crac{', '\\\\frac{')

    return text

with open('c:/work/kenji.blog/content/post/history-of-apple/index.md', 'r', encoding='utf-8') as f:
    content = f.read()

content_de = translate(content)

with open('c:/work/kenji.blog/content/post/history-of-apple/index.de.md', 'w', encoding='utf-8') as f:
    f.write(content_de)
