import re
import os

filepath = r'c:\work\kenji.blog\content\post\history-of-apple\index.md'
outpath = r'c:\work\kenji.blog\content\post\history-of-apple\index.pt.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Front matter
text = text.replace('title: "Appleの歴史: ガレージから時価総額世界一への軌跡と革新のDNA"', 'title: "A História da Apple: Da Garagem à Empresa Mais Valiosa do Mundo e o DNA da Inovação"')
text = text.replace('description: "スティーブ・ジョブズとウォズニアックのガレージ創業から、iPhone革命、時価総額世界一に至るAppleの歴史と技術的革新を徹底解説。"', 'description: "Uma análise aprofundada da história e inovação tecnológica da Apple, desde sua fundação na garagem por Steve Jobs e Wozniak, até a revolução do iPhone e tornar-se a empresa mais valiosa do mundo."')

# Sections with potential dynamic prefixes
text = re.sub(r'(#+ .*?)創世記：ガレージから始まった革命 \(1976-1980\)', r'\1Gênese: A Revolução que Começou em uma Garagem (1976-1980)', text)
text = re.sub(r'(#+ .*?)マッキントッシュとGUIの夜明け \(1984\)', r'\1A Aurora do Macintosh e da Interface Gráfica (1984)', text)

text = text.replace('## 3. 暗黒時代とジョブズの復帰 (1985-1997)', '## 3. A Era das Trevas e o Retorno de Jobs (1985-1997)')
text = text.replace('## 4. iMac, iPod, そして iTunes (1998-2006)', '## 4. iMac, iPod e iTunes (1998-2006)')
text = text.replace('## 5. iPhone革命とモバイル時代 (2007-2011)', '## 5. A Revolução do iPhone e a Era Móvel (2007-2011)')
text = text.replace('## 6. ティム・クック時代とサービス企業への転換 (2011-現在)', '## 6. A Era Tim Cook e a Transição para uma Empresa de Serviços (2011-Presente)')
text = text.replace('## 7. AI時代のApple (Apple Intelligence)', '## 7. A Apple na Era da IA (Apple Intelligence)')
text = text.replace('## まとめ', '## Resumo')

# Additional headers
text = re.sub(r'## 追加考察 (\d+): Appleの経営戦略と技術の深掘り', r'## Análise Adicional \1: Aprofundamento na Estratégia de Negócios e Tecnologia da Apple', text)

# Paragraphs
text = text.replace('1976年、スティーブ・ジョブズ、スティーブ・ウォズニアック、ロナルド・ウェインの3人は、カリフォルニア州ロスアルトスのジョブズの実家のガレージで「Apple Computer Company」を設立しました。', 'Em 1976, Steve Jobs, Steve Wozniak e Ronald Wayne fundaram a "Apple Computer Company" na garagem da casa dos pais de Jobs, em Los Altos, Califórnia.')
text = text.replace('最初の製品である **Apple I** は、マザーボードのみが提供される組み立てキットでした。ウォズニアックの天才的なハードウェア設計能力と、ジョブズの先見性とマーケティング能力が融合した瞬間です。', 'O primeiro produto, o **Apple I** , era um kit de montagem que fornecia apenas a placa-mãe. Foi o momento em que a genialidade do design de hardware de Wozniak se fundiu com a visão e capacidade de marketing de Jobs.')
text = text.replace('### Apple II の大成功', '### O Grande Sucesso do Apple II')
text = text.replace('1977年に発売された **Apple II** は、プラスチックケースにキーボードを統合し、カラーグラフィックスを表示できる画期的な製品でした。VisiCalc（世界初の表計算ソフト）の登場により、Apple II はビジネス市場にも浸透し、爆発的な大ヒットを記録します。', 'Lançado em 1977, o **Apple II** foi um produto revolucionário que integrava um teclado em um gabinete de plástico e era capaz de exibir gráficos coloridos. Com o surgimento do VisiCalc (o primeiro software de planilha eletrônica do mundo), o Apple II penetrou também no mercado corporativo e registrou um sucesso estrondoso.')

text = text.replace('1984年、Appleは **Macintosh（マッキントッシュ）** を発売します。これは、GUI（グラフィカル・ユーザー・インターフェース）とマウスを備えた初の一般向けパソコンでした。', 'Em 1984, a Apple lançou o **Macintosh** . Este foi o primeiro computador pessoal voltado para o público geral equipado com uma GUI (Interface Gráfica do Usuário) e um mouse.')
text = text.replace('当時の画期的な技術として、ビットマップディスプレイとオブジェクト指向プログラミングの概念が導入されました。', 'Como tecnologias inovadoras da época, foram introduzidos os conceitos de tela de bitmap e programação orientada a objetos.')

text = text.replace('1985年、社内対立によりジョブズはAppleを追放されます。その後、Appleは低迷期に入ります。一方ジョブズはNeXT社とPixar社を立ち上げ、成功を収めます。', 'Em 1985, devido a conflitos internos, Jobs foi expulso da Apple. Depois disso, a Apple entrou em um período de declínio. Por outro lado, Jobs fundou a NeXT e a Pixar, alcançando o sucesso.')
text = text.replace('1996年、Appleは次世代OSの開発に行き詰まり、ジョブズのNeXT社を買収することを決定。1997年にジョブズはAppleに復帰し、暫定CEOに就任します。', 'Em 1996, a Apple chegou a um impasse no desenvolvimento de seu sistema operacional de próxima geração e decidiu comprar a NeXT, empresa de Jobs. Em 1997, Jobs retornou à Apple e assumiu o cargo de CEO interino.')
text = text.replace('### NeXTSTEPからmacOSへの進化', '### A Evolução do NeXTSTEP para o macOS')
text = text.replace('NeXT社のOSである **NeXTSTEP** の技術（Machカーネル、Objective-C）は、後の Mac OS X（現在のmacOS）およびiOSの強固な基盤となりました。', 'A tecnologia do **NeXTSTEP** , o sistema operacional da NeXT (kernel Mach, Objective-C), tornou-se a base sólida para o posterior Mac OS X (atual macOS) e iOS.')

text = text.replace('ジョブズは製品ラインナップを劇的に絞り込み、1998年に **iMac** を発表。トランスルーセント（半透明）のデザインは世界中に衝撃を与えました。', 'Jobs reduziu drasticamente a linha de produtos e, em 1998, anunciou o **iMac** . O design translúcido (semitransparente) chocou o mundo todo.')
text = text.replace('2001年には **iPod** と **iTunes** を発表し、音楽業界に革命を起こします。「ポケットに1000曲を」というキャッチコピーは、技術とユーザー体験の完璧な融合を示していました。', 'Em 2001, ele anunciou o **iPod** e o **iTunes** , revolucionando a indústria da música. O slogan "1.000 músicas no seu bolso" demonstrou a fusão perfeita entre tecnologia e experiência do usuário.')

text = text.replace('2007年1月、ジョブズは **iPhone** を発表しました。', 'Em janeiro de 2007, Jobs anunciou o **iPhone** .')
text = text.replace('「iPod、電話、インターネットコミュニケーター。これらは3つの独立したデバイスではなく、1つのデバイスだ。」', '"Um iPod, um telefone e um comunicador de internet. Estes não são três dispositivos separados, mas sim um único dispositivo."')
text = text.replace('iPhoneはマルチタッチインターフェースを採用し、物理キーボードを排除しました。これは人類のコミュニケーションの歴史を変える出来事でした。', 'O iPhone adotou uma interface multitoque e eliminou o teclado físico. Esse foi um evento que mudou a história da comunicação humana.')

text = text.replace('2011年のジョブズの逝去後、ティム・クックがCEOを引き継ぎました。クックの卓越したサプライチェーン管理と、Apple Watch、AirPodsなどのウェアラブルデバイスの成功により、Appleは世界初の時価総額1兆ドル、2兆ドル、3兆ドル企業へと成長しました。', 'Após o falecimento de Jobs em 2011, Tim Cook assumiu o cargo de CEO. O excelente gerenciamento da cadeia de suprimentos de Cook e o sucesso de dispositivos vestíveis, como o Apple Watch e os AirPods, fizeram com que a Apple crescesse e se tornasse a primeira empresa do mundo com valor de mercado de 1 trilhão, 2 trilhões e 3 trilhões de dólares.')
text = text.replace('### Apple Silicon (M1/M2/M3) の衝撃', '### O Impacto do Apple Silicon (M1/M2/M3)')
text = text.replace('近年では、Intel製チップから自社設計の **Apple Silicon (ARMアーキテクチャ)** への移行を完了させました。高いパフォーマンスと圧倒的な電力効率を両立させています。', 'Nos últimos anos, a empresa concluiu a transição dos chips da Intel para o **Apple Silicon (arquitetura ARM)** de design próprio. Eles alcançaram um equilíbrio entre alto desempenho e eficiência energética esmagadora.')

text = text.replace('2024年、Appleは **Apple Intelligence** を発表し、パーソナルコンテキストを理解するオンデバイスAIへの本格参入を果たしました。プライバシーを重視しつつ、Siriの劇的な進化や文章生成・画像生成をOSレベルで統合しています。', 'Em 2024, a Apple anunciou a **Apple Intelligence** , marcando sua entrada em grande escala na IA no dispositivo (on-device) que entende o contexto pessoal. Mantendo o foco na privacidade, eles integraram uma evolução dramática da Siri e a geração de textos e imagens em nível de sistema operacional.')

text = text.replace('Appleの歴史は、テクノロジーとリベラルアーツの交差点に立ち続けた歴史です。ガレージから始まった小さな会社は、今や世界中の人々の生活に欠かせないデジタルエコシステムを構築しています。', 'A história da Apple é a história de estar constantemente na interseção entre a tecnologia e as artes liberais. A pequena empresa que começou em uma garagem agora construiu um ecossistema digital que é indispensável para a vida das pessoas em todo o mundo.')

# Code blocks
text = text.replace('// Objective-C の例 (NeXTSTEP由来の技術)', '// Exemplo em Objective-C (tecnologia originada do NeXTSTEP)')
text = text.replace('NSLog(@"Hello, Think Different!");', 'NSLog(@"Olá, Pense Diferente!");')

# Math blocks
text = text.replace(r'\text{Performance per Watt}', r'\text{Desempenho por Watt}')
text = text.replace(r'\text{Computation Output (FLOPS)}', r'\text{Saída de Computação (FLOPS)}')
text = text.replace(r'\text{Power Consumption (Watts)}', r'\text{Consumo de Energia (Watts)}')

# Mermaid
text = text.replace('subgraph "Apple Founders"', 'subgraph "Fundadores da Apple"')
text = text.replace('SJ["Steve Jobs (Marketing/Vision)"]', 'SJ["Steve Jobs (Marketing/Visão)"]')
text = text.replace('SW["Steve Wozniak (Engineering)"]', 'SW["Steve Wozniak (Engenharia)"]')
text = text.replace('RW["Ronald Wayne (Administration)"]', 'RW["Ronald Wayne (Administração)"]')

text = text.replace('Xerox["Xerox PARC (GUI Concept)"]', 'Xerox["Xerox PARC (Conceito de GUI)"]')
text = text.replace('Jobs["Steve Jobs Visit (1979)"]', 'Jobs["Visita de Steve Jobs (1979)"]')
text = text.replace('Lisa["Apple Lisa (1983)"]', 'Lisa["Apple Lisa (1983)"]')
text = text.replace('Mac["Macintosh (1984)"]', 'Mac["Macintosh (1984)"]')
text = text.replace('Modern["Modern GUI OS"]', 'Modern["Sistemas Operacionais GUI Modernos"]')

text = text.replace('pie title "Mobile OS Market Share Shift (Concept)"', 'pie title "Mudança na Participação de Mercado de SO Móvel (Conceito)"')
text = text.replace('"Others" :', '"Outros" :')
text = text.replace('%% ↓ After iPhone/Android', '%% ↓ Depois do iPhone/Android')

with open(outpath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Translation script pt completed.")
