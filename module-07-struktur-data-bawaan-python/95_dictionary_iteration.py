stok = {"apel": 4, "jeruk": 2}

# items menghasilkan pasangan kunci-nilai untuk dibaca dalam satu putaran.
for nama, jumlah in stok.items():
    print(f"{nama}: {jumlah}")