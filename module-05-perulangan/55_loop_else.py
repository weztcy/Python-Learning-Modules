data = (3, 5, 7)
target = 4

# else pada loop berjalan hanya jika perulangan selesai tanpa break.
for nilai in data:
    if nilai == target:
        print("Target ditemukan")
        break
else:
    print("Target tidak ditemukan")