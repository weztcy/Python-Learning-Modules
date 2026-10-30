import csv
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "nilai.csv"
    with path.open("w", newline="", encoding="utf-8") as berkas:
        penulis = csv.writer(berkas)
        penulis.writerow(["nama", "nilai"])
        penulis.writerow(["Ayu", 90])
    # newline="" mencegah baris kosong tambahan pada platform tertentu.
    with path.open(newline="", encoding="utf-8") as berkas:
        for baris in csv.reader(berkas):
            print(baris)