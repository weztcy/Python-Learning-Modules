# Loop kedua mengulang untuk setiap nilai loop pertama, membentuk pasangan.
pasangan = [(baris, kolom) for baris in range(1, 3) for kolom in range(1, 4)]
print("Pasangan:", pasangan)