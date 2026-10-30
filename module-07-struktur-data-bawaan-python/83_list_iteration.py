nilai = [80, 75, 90]

# enumerate memberi indeks dan nilai tanpa menghitung posisi secara manual.
for indeks, skor in enumerate(nilai, start=1):
    print(f"Peserta {indeks}: {skor}")