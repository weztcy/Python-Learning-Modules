from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

# Arsip zip menunjukkan komponen paket tanpa menginstalnya pada komputer.
with TemporaryDirectory() as folder:
    arsip = Path(folder) / "contoh_paket.zip"
    with ZipFile(arsip, "w") as berkas:
        berkas.writestr("contoh_paket/__init__.py", "# Paket contoh\n")
    with ZipFile(arsip) as berkas:
        print("Isi arsip:", berkas.namelist())