# Ulangi permintaan sampai teks dapat dikonversi menjadi bilangan bulat positif.
while True:
    teks = input("Masukkan bilangan bulat positif: ")
    try:
        angka = int(teks)
    except ValueError:
        print("Input harus bilangan bulat.")
        continue
    if angka > 0:
        break
    print("Bilangan harus lebih besar dari nol.")
print("Input valid:", angka)