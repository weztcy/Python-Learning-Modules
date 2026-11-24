def jumlah_harga(harga, jumlah):
    # Periksa nilai antara untuk menemukan sumber perhitungan yang salah.
    print(f"DEBUG harga={harga}, jumlah={jumlah}")
    return harga * jumlah


print("Total:", jumlah_harga(5000, 3))