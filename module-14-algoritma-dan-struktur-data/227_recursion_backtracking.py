def susunan(terpilih, sisa):
    if not sisa:
        yield terpilih
        return
    for indeks, nilai in enumerate(sisa):
        # Pilih satu nilai lalu rekursi; loop berikutnya mencoba pilihan lain.
        yield from susunan(terpilih + [nilai], sisa[:indeks] + sisa[indeks + 1:])


print("Susunan:", list(susunan([], [1, 2, 3])))