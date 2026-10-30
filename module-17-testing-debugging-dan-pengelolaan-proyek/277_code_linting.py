import ast
from pathlib import Path

# Parse AST mendeteksi kesalahan sintaks, bukan menggantikan linter penuh.
kode = Path(__file__).read_text(encoding="utf-8")
ast.parse(kode)
print("Sintaks Python valid; linter juga dapat memeriksa gaya dan aturan tambahan.")