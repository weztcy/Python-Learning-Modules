kalimat = "Belajar Python itu menyenangkan"
target = "Python"

# in memeriksa keberadaan; find memberi indeks awal atau -1 jika tidak ditemukan.
print("Ada target:", target in kalimat)
print("Indeks awal:", kalimat.find(target))
print("Tidak ada:", kalimat.find("Java"))