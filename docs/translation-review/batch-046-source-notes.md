# Batch 046 source and editorial notes

Reviewed on 2026-11-23. Article: `content/post/search-algorithms-linear-binary-hash-table-principles/index.md` and all twelve localized versions.

## Primary references

- [Python 3.14 time complexity reference](https://docs.python.org/3.14/builtins/time-complexity.html): CPython dictionary average-case costs assume suitable hash distribution, uncommon collisions, and constant-time hashing/comparison; worst-case lookup/insertion can be O(n).
- [Python FAQ: dictionaries in CPython](https://docs.python.org/3.14/faq/design.html#how-are-dictionaries-implemented-in-cpython): CPython dictionaries are resizable hash tables; key hash values use a per-process seed.
- Binary search is explained for ordered arrays with indexed access. The iterative sample uses ascending order; the prose and flowchart now state that requirement and use floor for the midpoint.

## Corrections made

- Restored the original 2026-09-22 publication date from the initial article commit `778cd02c3`; removed the later duplicate date created by the bulk date correction and set `lastmod: 2026-11-23` across all thirteen versions.
- Removed repeated identical prose from each article while preserving the unique explanation, headings, lists, diagrams, tables, and all seven fenced code/diagram blocks. This removed 224 duplicate paragraphs from Japanese and 226 from each translation.
- Removed a misleading open-addressing link to a C pointer article.
- Clarified the sorted-input and random-access requirements for binary search, and aligned the ascending-order sample and midpoint pseudocode.
- Reframed hash-table O(1) as an expected average under suitable hashing/load conditions; stated collision handling and the O(n) worst case.
- Clarified that the sample separate-chaining implementation has fixed capacity and omits resizing/deletion. Distinguished auxiliary search space from hash-table key/value storage space.
- Localized these corrections and the Python complexity reference across all twelve translations.

## Verification scope and limitations

The local production Hugo render is checked for all thirteen routes, canonical/language/RTL metadata, code rendering, the official Python reference, absence of the incorrect pointer link, and all hreflang targets. Python snippets are parsed as Python syntax; they are not executed or benchmarked. The algorithm descriptions are educational summaries, not formal proofs. Translation proofreading is AI-only; no native-speaker or human certification was performed.
