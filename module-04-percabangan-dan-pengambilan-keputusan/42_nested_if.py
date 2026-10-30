usia = 20
punya_tiket = True

# Kondisi tiket baru diperiksa jika syarat usia telah terpenuhi.
if usia >= 18:
    if punya_tiket:
        print("Silakan masuk")
    else:
        print("Tiket diperlukan")
else:
    print("Usia belum mencukupi")