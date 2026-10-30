# split memisahkan teks pada spasi, lalu map mengonversi setiap bagian.
teks = input("Masukkan dua bilangan dipisahkan spasi: ")
try:
    pertama, kedua = map(int, teks.split())
except ValueError:
    print("Masukkan tepat dua bilangan bulat.")
else:
    print("Jumlah:", pertama + kedua)