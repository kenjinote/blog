import unittest
from mermaid_sources import blocks
from repair_mermaid import repair


class MermaidRepairs(unittest.TestCase):
    def test_lithium_group(self):
        source='graph LR\n    subgraph 放電時の動き (スマホ使用中)\n        A["負極"] --> B["正極"]\n    end\n'
        self.assertEqual(repair(source,''),source.replace('subgraph 放電時の動き (スマホ使用中)','subgraph "放電時の動き (スマホ使用中)"'))

    def test_existing_edge_label_is_not_an_identifier(self):
        source='graph LR\n A["one"] -->|"added to"| B["two"]\n'
        self.assertEqual(repair(source,''),source)

    def test_array_labels_not_requoted(self):
        self.assertEqual(repair('graph LR\n A["dp[i][j]"] --> B\n',''),'graph LR\n A["dp[i][j]"] --> B\n')

    def test_quoted_node_identity(self):
        fixed=repair('graph LR\n "Page" -->|"Request"| "Service Worker"\n "Service Worker" --> "Page"\n','')
        self.assertIn('repairedNode1["Service Worker"]',fixed)
        self.assertIn('Page -->|"Request"| repairedNode1',fixed)
        self.assertIn('repairedNode1 --> Page',fixed)

    def test_state_action_and_nesting(self):
        source='stateDiagram-v2\n [*] --> Normal["Normal Mode"]\n Command --> Normal["Execute command"]\n state Nested {\n  A["Inner state"]\n }\n'
        fixed=repair(source,'')
        self.assertIn('Command --> Normal : Execute command',fixed)
        self.assertIn('state Nested {\n  state "Inner state" as A',fixed)

    def test_chart_numbers_unchanged(self):
        source='xychart-beta\n title 日本語 (比較)\n x-axis ["A, B"]\n line [1.5, 2.5]\n'
        fixed=repair(source,'')
        self.assertIn('title "日本語 (比較)"',fixed)
        self.assertIn('x-axis ["A", "B"]',fixed)
        self.assertIn('line [1.5, 2.5]',fixed)

    def test_line_endings(self):
        for newline in ('\n','\r\n','\r\r\n'):
            source=('graph LR\n subgraph x (y)\n end\n').replace('\n',newline)
            self.assertEqual(repair(source,''),source.replace('subgraph x (y)','subgraph "x (y)"'))

    def test_only_diagram_interiors(self):
        text='---\ntitle: test\n---\n$E=mc^2$\n```python\n```mermaid\nA --> B\n```\n\n~~~mermaid\ngraph LR\n A --> B\n~~~\n{{<mermaid>}}graph TD\n X --> Y\n{{</mermaid>}}\n'
        found=list(blocks(text))
        self.assertEqual(len(found),2)
        for a,b,s in found:self.assertEqual(text[a:b],s)

    def test_gantt_start_only(self):
        source='gantt\n dateFormat s\n task : a, 2s, 4s\n'
        self.assertEqual(repair(source,'browser-rendering-mechanism-dom-paint/index.md'),source.replace('2s,','2,'))


if __name__=='__main__':unittest.main()
