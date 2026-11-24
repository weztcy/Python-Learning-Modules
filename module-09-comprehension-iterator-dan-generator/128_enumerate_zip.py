nama = ["Ayu", "Budi"]
nilai = [90, 80]

# zip memasangkan elemen hingga iterable terpendek habis; enumerate memberi nomor.
for nomor, (murid, skor) in enumerate(zip(nama, nilai), start=1):
    print(f"{nomor}. {murid}: {skor}")