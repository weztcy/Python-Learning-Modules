def pilih_aktivitas(aktivitas):
    hasil, selesai = [], 0
    # Pilihan berakhir paling awal menyisakan ruang untuk kegiatan berikutnya.
    for mulai, akhir in sorted(aktivitas, key=lambda item: item[1]):
        if mulai >= selesai:
            hasil.append((mulai, akhir))
            selesai = akhir
    return hasil


print("Jadwal:", pilih_aktivitas([(1, 4), (3, 5), (4, 6), (6, 8)]))