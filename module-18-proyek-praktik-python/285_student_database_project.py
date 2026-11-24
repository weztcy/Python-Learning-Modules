import sqlite3


def daftar_siswa(koneksi):
    koneksi.execute("CREATE TABLE siswa (id INTEGER PRIMARY KEY, nama TEXT NOT NULL)")
    koneksi.executemany("INSERT INTO siswa (nama) VALUES (?)", [("Ayu",), ("Budi",)])
    return koneksi.execute("SELECT nama FROM siswa ORDER BY id").fetchall()


if __name__ == "__main__":
    # Database :memory: tidak meninggalkan file atau perlu server.
    with sqlite3.connect(":memory:") as koneksi:
        print("Siswa:", daftar_siswa(koneksi))