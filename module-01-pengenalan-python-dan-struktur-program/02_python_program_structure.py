"""Contoh struktur sederhana file Python yang dapat dijalankan langsung."""


def sapa(nama):
    """Kembalikan teks sapaan untuk nama yang diterima."""
    return f"Halo, {nama}!"


# Guard ini mencegah kode utama berjalan ketika file di-import sebagai modul.
if __name__ == "__main__":
    print(sapa("Python"))