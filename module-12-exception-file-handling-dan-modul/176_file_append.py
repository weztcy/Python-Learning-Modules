from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "log.txt"
    path.write_text("Baris pertama\n", encoding="utf-8")
    # Mode a menambahkan data tanpa menimpa isi yang sudah ada.
    with path.open("a", encoding="utf-8") as berkas:
        berkas.write("Baris kedua\n")
    print(path.read_text(encoding="utf-8"), end="")