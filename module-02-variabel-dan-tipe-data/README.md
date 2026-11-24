# Modul 2 — Variabel dan Tipe Data

Modul ini membahas penamaan nilai, tipe bawaan, konversi, dan perbedaan objek mutable dengan immutable. Tujuannya adalah memahami bagaimana nilai disimpan dan digunakan dalam ekspresi. Semua contoh menggunakan Python 3.10+ tanpa pustaka eksternal.

## Daftar materi

1. [Variabel](11_variables.py)
2. [Assignment](12_variable_assignment.py)
3. [Integer](13_integer_type.py)
4. [Float](14_float_type.py)
5. [Complex](15_complex_type.py)
6. [String](16_string_type.py)
7. [Boolean](17_boolean_type.py)
8. [None](18_none_type.py)
9. [Fungsi type()](19_type_function.py)
10. [Konversi tipe data](20_type_conversion.py)
11. [Type casting](21_type_casting.py)
12. [Multiple assignment](22_multiple_assignment.py)
13. [Konvensi konstanta](23_constants.py)
14. [Mutable dan immutable objects](24_mutable_immutable.py)

Jalankan perintah berikut dari folder modul ini. Tautan screenshot per submodul memperlihatkan jendela log hasil eksekusi dengan input demo.

### 11. Variabel
**Tujuan dan konsep:** Memahami nama yang merujuk ke nilai. **Cara kerja:** `nama` dan `umur` disimpan terpisah lalu dipakai bersama saat dicetak. **Jalankan:** `python 11_variables.py`. **Hasil:** nama dan umur Ayu. **Source code:** [11_variables.py](11_variables.py). **Screenshot:** [Lihat hasil eksekusi](output/11_variables.png).

### 12. Assignment
**Tujuan dan konsep:** Mengenali penugasan ulang. **Cara kerja:** variabel `skor` mula-mula merujuk ke 70, kemudian ke 85. **Jalankan:** `python 12_variable_assignment.py`. **Hasil:** skor awal 70 dan terbaru 85. **Source code:** [12_variable_assignment.py](12_variable_assignment.py). **Screenshot:** [Lihat hasil eksekusi](output/12_variable_assignment.png).

### 13. Tipe data integer
**Tujuan dan konsep:** Mengolah bilangan bulat dengan `int`. **Cara kerja:** stok 12 dijumlahkan dengan perubahan -3. **Jalankan:** `python 13_integer_type.py`. **Hasil:** sisa stok 9 dan tipe `int`. **Source code:** [13_integer_type.py](13_integer_type.py). **Screenshot:** [Lihat hasil eksekusi](output/13_integer_type.png).

### 14. Tipe data float
**Tujuan dan konsep:** Mengolah bilangan pecahan dengan `float`. **Cara kerja:** harga 12.5 dikalikan jumlah 3. **Jalankan:** `python 14_float_type.py`. **Hasil:** total 37.5 dan tipe `float`. **Source code:** [14_float_type.py](14_float_type.py). **Screenshot:** [Lihat hasil eksekusi](output/14_float_type.png).

### 15. Tipe data complex
**Tujuan dan konsep:** Mengetahui komponen real dan imajiner. **Cara kerja:** `3 + 4j` dibaca melalui atribut `.real` dan `.imag`. **Jalankan:** `python 15_complex_type.py`. **Hasil:** bilangan kompleks beserta bagian 3.0 dan 4.0. **Source code:** [15_complex_type.py](15_complex_type.py). **Screenshot:** [Lihat hasil eksekusi](output/15_complex_type.png).

### 16. Tipe data string
**Tujuan dan konsep:** Menggunakan teks, indexing, dan panjangnya. **Cara kerja:** karakter pertama `Python` diambil dengan indeks 0; `len` menghitung karakter. **Jalankan:** `python 16_string_type.py`. **Hasil:** `Python`, `P`, dan 6. **Source code:** [16_string_type.py](16_string_type.py). **Screenshot:** [Lihat hasil eksekusi](output/16_string_type.png).

### 17. Tipe data boolean
**Tujuan dan konsep:** Memperoleh nilai `True` atau `False` dari perbandingan. **Cara kerja:** skor 80 diuji terhadap batas 75. **Jalankan:** `python 17_boolean_type.py`. **Hasil:** `Lulus: True` dan tipe `bool`. **Source code:** [17_boolean_type.py](17_boolean_type.py). **Screenshot:** [Lihat hasil eksekusi](output/17_boolean_type.png).

### 18. Nilai `None`
**Tujuan dan konsep:** Menandai nilai yang belum diisi. **Cara kerja:** `is None` memeriksa identitas nilai awal, sebelum diganti dengan angka 42. **Jalankan:** `python 18_none_type.py`. **Hasil:** pemeriksaan `True`, lalu 42. **Source code:** [18_none_type.py](18_none_type.py). **Screenshot:** [Lihat hasil eksekusi](output/18_none_type.png).

### 19. Fungsi `type()`
**Tujuan dan konsep:** Mengamati tipe objek saat runtime. **Cara kerja:** loop mencetak representasi dan nama tipe dari empat nilai berbeda. **Jalankan:** `python 19_type_function.py`. **Hasil:** tipe `int`, `float`, `str`, dan `bool`. **Source code:** [19_type_function.py](19_type_function.py). **Screenshot:** [Lihat hasil eksekusi](output/19_type_function.png).

### 20. Konversi tipe data
**Tujuan dan konsep:** Mengubah teks numerik agar bisa dihitung. **Cara kerja:** `int("25")` menghasilkan angka yang dijumlahkan dengan lima; `str` mengubahnya kembali ke teks. **Jalankan:** `python 20_type_conversion.py`. **Hasil:** 30 dan teks 25. **Source code:** [20_type_conversion.py](20_type_conversion.py). **Screenshot:** [Lihat hasil eksekusi](output/20_type_conversion.png).

### 21. Type casting
**Tujuan dan konsep:** Memahami hasil casting eksplisit. **Cara kerja:** `int(7.9)` membuang pecahan; `float` dan `bool` menunjukkan konversi lainnya. **Jalankan:** `python 21_type_casting.py`. **Hasil:** 7, 7.0, dan `False`. **Source code:** [21_type_casting.py](21_type_casting.py). **Screenshot:** [Lihat hasil eksekusi](output/21_type_casting.png).

### 22. Multiple assignment
**Tujuan dan konsep:** Memasangkan dan menukar nilai serentak. **Cara kerja:** unpacking mengisi `nama, nilai`, lalu `a, b = b, a` menukar dua nilai. **Jalankan:** `python 22_multiple_assignment.py`. **Hasil:** nama Rani dan angka setelah ditukar: 2, 1. **Source code:** [22_multiple_assignment.py](22_multiple_assignment.py). **Screenshot:** [Lihat hasil eksekusi](output/22_multiple_assignment.png).

### 23. Konvensi konstanta
**Tujuan dan konsep:** Menggunakan nama kapital untuk nilai yang dimaksudkan tetap. **Cara kerja:** `PAJAK` mengalikan harga dengan faktor pajak; Python tidak mencegah penugasan ulang nama kapital. **Jalankan:** `python 23_constants.py`. **Hasil:** total dengan pajak. **Source code:** [23_constants.py](23_constants.py). **Screenshot:** [Lihat hasil eksekusi](output/23_constants.png).

### 24. Mutable dan immutable objects
**Tujuan dan konsep:** Membedakan perubahan objek dan pembuatan nilai baru. **Cara kerja:** `append` mengubah list yang sama, sedangkan penggabungan string menghasilkan string baru. **Jalankan:** `python 24_mutable_immutable.py`. **Hasil:** list dua buah dan teks `Python`. **Source code:** [24_mutable_immutable.py](24_mutable_immutable.py). **Screenshot:** [Lihat hasil eksekusi](output/24_mutable_immutable.png).

## Ringkasan

Variabel merujuk pada objek bertipe tertentu; konversi mengubah representasi nilai, sedangkan sifat mutable menentukan apakah objek dapat diubah langsung.