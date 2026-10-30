def hitung_mundur(awal):
    while awal > 0:
        # yield memberi satu nilai dan menyimpan posisi fungsi untuk permintaan berikutnya.
        yield awal
        awal -= 1


print("Mundur:", list(hitung_mundur(3)))