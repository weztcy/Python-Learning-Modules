import sqlite3

# Database :memory: tidak meninggalkan file setelah koneksi ditutup.
with sqlite3.connect(":memory:") as koneksi:
    koneksi.execute("CREATE TABLE siswa (nama TEXT, nilai INTEGER)")
    koneksi.execute("INSERT INTO siswa VALUES (?, ?)", ("Ayu", 90))
    # Placeholder ? memisahkan data dari teks query SQL.
    print("Data:", koneksi.execute("SELECT nama, nilai FROM siswa").fetchall())