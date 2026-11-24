# type() mengembalikan kelas dari objek pada saat program berjalan.
for nilai in (7, 2.5, "halo", True):
    print(repr(nilai), "->", type(nilai).__name__)