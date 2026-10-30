usia, punya_tiket = 20, True

# and mengharuskan kedua kondisi benar; or cukup salah satunya.
print("Boleh masuk:", usia >= 18 and punya_tiket)
print("Punya akses khusus:", usia < 12 or usia >= 65)
print("Tidak punya tiket:", not punya_tiket)