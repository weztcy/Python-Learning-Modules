from pathlib import Path
from tempfile import TemporaryDirectory

# Direktori sementara menjaga source code tidak tercampur file hasil latihan.
with TemporaryDirectory() as folder:
    path = Path(folder) / "catatan.txt"
    path.write_text("Belajar Python", encoding="utf-8")
    print("Isi tersimpan:", path.read_text(encoding="utf-8"))