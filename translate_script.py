import json
import os

replacements = {
  "content/post/pedigree-collapse/index.de.md": {
    "（※実際の系図はさらに複雑に絡み合っていますが、上記はその異常な重複を示す概念図です）": "(* Der tatsächliche Stammbaum ist noch komplexer miteinander verflochten, aber das Obige ist ein konzeptionelles Diagramm, das diese ungewöhnliche Überschneidung zeigt *)"
  },
  "content/post/floyds-cycle-finding/index.en.md": {
    "// リストのノード定義": "// List node definition",
    "// 循環が存在するかどうかを判定する": "// Determine if a cycle exists",
    "slow = slow->next;          // カメは1歩進む": "slow = slow->next;          // Tortoise moves 1 step",
    "fast = fast->next->next;    // ウサギは2歩進む": "fast = fast->next->next;    // Hare moves 2 steps",
    "return true; // 衝突したら循環あり": "return true; // Cycle exists if they collide",
    "return false; // ウサギがゴールに到達したら循環なし": "return false; // No cycle if hare reaches the end",
    "// サイクルの開始地点のノードを返す": "// Return the node where the cycle begins",
    "// どちらか一方（ここではslow）を先頭に戻す": "// Move one of them (slow in this case) back to the start",
    "// 両者を1歩ずつ進め、出会った場所がサイクルの開始地点": "// Move both 1 step at a time; where they meet is the start of the cycle",
    "// 1 -> 2 -> 3 -> 4 -> 5 -> 3(サイクル) の構築": "// Construct 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)",
    "// メモリ解放はサイクルがあるため単純なdeleteでは不可（無限ループ防止が必要）": "// Memory deallocation cannot be done with simple delete due to cycle (infinite loop prevention needed)",
    "// 本来はサイクルを解消してからdeleteするなどの処理が必要です。": "// Normally, you would need to resolve the cycle before deleting.",
    "// 次に移動する先のインデックスを持つ配列を仮想的な連結リストとみなす": "// Treat an array holding indices of the next destination as a virtual linked list",
    "// 例: arr[i] が次のノード。": "// Example: arr[i] is the next node.",
    "// カメを1歩進める": "// Move tortoise 1 step",
    "// ウサギを2歩進める": "// Move hare 2 steps",
    "// カメをスタート地点に戻す": "// Move tortoise back to the start",
    "// 1歩ずつ進める": "// Move 1 step at a time",
    "// インデックスによる遷移グラフ:": "// Transition graph by index:",
    "// 0 -> 1 -> 2 -> 3 -> 4 -> 2 (2から始まるサイクル)": "// 0 -> 1 -> 2 -> 3 -> 4 -> 2 (cycle starting from 2)",
    "// 値が範囲外(例: usize::MAX)なら終端とするが、今回はサイクルありを構築。": "// If value is out of bounds (e.g. usize::MAX) treat as end, but this time construct with a cycle."
  },
  "content/post/halting-problem/index.en.md": {
    "%% D に D 自身を入力する": "%% Input D into D itself",
    "%% 矛盾のハイライト": "%% Highlight contradiction"
  },
  "content/post/monte-carlo-and-las-vegas-algorithms/index.en.md": {
    "print(f\"円周率の近似値: {pi_approx}\")": "print(f\"Approximate value of pi: {pi_approx}\")",
    "print(f\"ソート結果: {sorted_data}\")": "print(f\"Sorted result: {sorted_data}\")"
  },
  "content/post/halting-problem/index.es.md": {
    "%% D に D 自身を入力する": "%% Ingresar D en sí mismo",
    "%% 矛盾のハイライト": "%% Destacar contradicción"
  },
  "content/post/ship-of-theseus/index.id.md": {
    "B -->|\"Migrasi Fitur B dan C\"| C[\"Sistem Campuran Lama dan Baru（新メイン）\"]": "B -->|\"Migrasi Fitur B dan C\"| C[\"Sistem Campuran Lama dan Baru (Utama Baru)\"]"
  },
  "content/post/halting-problem/index.id.md": {
    "\\text{true} & (\\text{プログラム } P \\text{ が入力 } I \\text{ で停止する場合}) \\\\": "\\text{true} & (\\text{Jika program } P \\text{ berhenti pada masukan } I) \\\\",
    "\\text{false} & (\\text{プログラム } P \\text{ が入力 } I \\text{ で無限ループする場合})": "\\text{false} & (\\text{Jika program } P \\text{ berulang tanpa batas pada masukan } I)",
    "H -->|\"false (Infinite loopする)\"| HALT[\"Berhenti\"]": "H -->|\"false (Loop tanpa batas)\"| HALT[\"Berhenti\"]",
    "%% D に D 自身をInputする": "%% Memasukkan D ke dalam D itu sendiri",
    "%% Kontradiksiのハイライト": "%% Sorotan Kontradiksi",
    "HALT -.->|\"Hの判定(false)とKontradiksi!\"| FAIL_2((\"Kontradiksi\"))": "HALT -.->|\"Keputusan H (false) dan Kontradiksi!\"| FAIL_2((\"Kontradiksi\"))"
  },
  "content/post/pigeonhole-principle-hash-collision/index.id.md": {
    "H2{\"Fungsi Hash (数万回ループ)\"}": "H2{\"Fungsi Hash (Puluhan ribu loop)\"}"
  }
}

base_dir = "c:/work/kenji.blog/"

for file_path, changes in replacements.items():
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in changes.items():
        if old not in content:
            print(f"Warning: {old} not found in {full_path}")
        content = content.replace(old, new)
        
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Translation replacements completed.")
