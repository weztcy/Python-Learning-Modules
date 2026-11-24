import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

# Contoh menyalin dalam direktori sementara agar tidak mengubah file pengguna.
with TemporaryDirectory() as folder:
    asal = Path(folder) / "asal.txt"
    tujuan = Path(folder) / "salinan.txt"
    asal.write_text("Isi contoh", encoding="utf-8")
    shutil.copyfile(asal, tujuan)
    print("Hasil salinan:", tujuan.read_text(encoding="utf-8"))