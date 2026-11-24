try:
    hasil = 8 / 2
except ZeroDivisionError:
    print("Pembagi nol")
else:
    # else hanya dijalankan jika blok try tidak memunculkan exception.
    print("Hasil:", hasil)
finally:
    # finally dijalankan baik operasi berhasil maupun gagal.
    print("Pemeriksaan selesai")