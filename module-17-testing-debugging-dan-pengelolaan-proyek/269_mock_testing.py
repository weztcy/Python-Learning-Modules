from unittest.mock import Mock


def total_harga(penyedia, nama):
    return penyedia.harga(nama) * 2


# Mock menggantikan sumber harga eksternal agar hasil tes dapat diprediksi.
penyedia = Mock()
penyedia.harga.return_value = 5000
assert total_harga(penyedia, "buku") == 10000
penyedia.harga.assert_called_once_with("buku")
print("Mock berhasil diverifikasi")