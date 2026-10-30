from unittest.mock import Mock

import requests


def ambil_pengguna(sesi, nomor):
    # Session dapat diganti mock untuk menguji alur tanpa jaringan.
    respons = sesi.get(f"https://example.org/api/users/{nomor}", timeout=5)
    respons.raise_for_status()
    return respons.json()


if __name__ == "__main__":
    sesi = Mock(spec=requests.Session)
    sesi.get.return_value.json.return_value = {"id": 1, "nama": "Ayu"}
    print("Pengguna:", ambil_pengguna(sesi, 1))