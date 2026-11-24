from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    asal = Path(folder) / "catatan.txt"
    asal.write_text("Belajar otomatisasi", encoding="utf-8")
    # rename memindahkan berkas tanpa mengubah file pengguna.
    tujuan = asal.rename(Path(folder) / "catatan_baru.txt")
    print("Nama baru:", tujuan.name, "Isi:", tujuan.read_text(encoding="utf-8"))