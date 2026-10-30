from pathlib import Path

# pathlib menggabungkan komponen path dengan / secara lintas platform.
berkas = Path(__file__).with_name("contoh_data.txt")
print("Nama:", berkas.name)
print("Ekstensi:", berkas.suffix)
print("Ada:", berkas.is_file())