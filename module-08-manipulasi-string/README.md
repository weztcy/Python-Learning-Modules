# Modul 8 — Manipulasi String

Modul ini membahas akses karakter, pengirisan, metode string, validasi, pembersihan teks, Unicode, dan pemeriksaan palindrom. Setelah mempelajarinya, pembaca dapat membentuk dan memeriksa teks tanpa mengubah objek string yang sudah ada. Gunakan Python 3.10+ tanpa pustaka tambahan; setiap perintah dijalankan dari folder modul ini. Screenshot jendela log eksekusi tersedia di tiap submodul.

## Daftar materi

1. [Indexing string](99_string_indexing.py)
2. [Slicing string](100_string_slicing.py)
3. [Metode string](101_string_methods.py)
4. [Penggabungan string](102_string_concatenation.py)
5. [Repetisi string](103_string_repetition.py)
6. [Pencarian teks](104_string_search.py)
7. [Penggantian teks](105_string_replace.py)
8. [Memisahkan string](106_string_split.py)
9. [Menggabungkan elemen string](107_string_join.py)
10. [Validasi string](108_string_validation.py)
11. [Pembersihan teks](109_string_cleaning.py)
12. [Pemformatan string](110_string_formatting.py)
13. [Unicode dan teks multibahasa](111_unicode_strings.py)
14. [Pemeriksaan palindrom](112_palindrome_checker.py)

### 99. Indexing string
**Tujuan:** Mengambil satu karakter. **Konsep dan cara kerja:** indeks 0 mengakses awal, indeks -1 mengakses akhir. **Jalankan:** `python 99_string_indexing.py`. **Hasil:** `P` dan `n`. **Source code:** [99_string_indexing.py](99_string_indexing.py). **Screenshot:** [Lihat hasil eksekusi](output/99_string_indexing.png).

### 100. Slicing string
**Tujuan:** Mengambil bagian teks. **Konsep dan cara kerja:** slice memilih awalan, akhiran, atau urutan terbalik tanpa mengubah sumber. **Jalankan:** `python 100_string_slicing.py`. **Hasil:** `Pemro`, `graman`, `namargormeP`. **Source code:** [100_string_slicing.py](100_string_slicing.py). **Screenshot:** [Lihat hasil eksekusi](output/100_string_slicing.png).

### 101. Metode string
**Tujuan:** Menghapus spasi pinggir dan mengubah kapitalisasi. **Konsep dan cara kerja:** `strip` dan `title` menghasilkan string baru, sedangkan `repr` memperlihatkan spasi yang tersembunyi. **Jalankan:** `python 101_string_methods.py`. **Hasil:** teks awal, `halo python`, dan `Halo Python`. **Source code:** [101_string_methods.py](101_string_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/101_string_methods.png).

### 102. Penggabungan string
**Tujuan:** Menyusun teks dari bagian-bagian terpisah. **Konsep dan cara kerja:** operator `+` menyambungkan dua kata dengan spasi sebagai pemisah. **Jalankan:** `python 102_string_concatenation.py`. **Hasil:** `Selamat belajar`. **Source code:** [102_string_concatenation.py](102_string_concatenation.py). **Screenshot:** [Lihat hasil eksekusi](output/102_string_concatenation.png).

### 103. Repetisi string
**Tujuan:** Mengulang pola pendek. **Konsep dan cara kerja:** operator `*` mengulang string sejumlah kali sesuai integer. **Jalankan:** `python 103_string_repetition.py`. **Hasil:** `ababab` dan sepuluh tanda hubung. **Source code:** [103_string_repetition.py](103_string_repetition.py). **Screenshot:** [Lihat hasil eksekusi](output/103_string_repetition.png).

### 104. Pencarian teks
**Tujuan:** Mengetahui keberadaan dan posisi substring. **Konsep dan cara kerja:** `in` menghasilkan boolean; `find` menghasilkan indeks awal atau -1 bila tidak ada. **Jalankan:** `python 104_string_search.py`. **Hasil:** `True`, 8, dan -1. **Source code:** [104_string_search.py](104_string_search.py). **Screenshot:** [Lihat hasil eksekusi](output/104_string_search.png).

### 105. Penggantian teks
**Tujuan:** Menghasilkan teks baru dengan bagian yang diganti. **Konsep dan cara kerja:** `replace` tidak memodifikasi string sumber. **Jalankan:** `python 105_string_replace.py`. **Hasil:** teks awal berisi Java dan teks baru berisi Python. **Source code:** [105_string_replace.py](105_string_replace.py). **Screenshot:** [Lihat hasil eksekusi](output/105_string_replace.png).

### 106. Memisahkan string
**Tujuan:** Mengubah baris berisi nilai berpisah koma menjadi list. **Konsep dan cara kerja:** `split(",")` memotong pada setiap koma. **Jalankan:** `python 106_string_split.py`. **Hasil:** list tiga nama buah. **Source code:** [106_string_split.py](106_string_split.py). **Screenshot:** [Lihat hasil eksekusi](output/106_string_split.png).

### 107. Menggabungkan elemen string
**Tujuan:** Membuat satu kalimat dari list kata. **Konsep dan cara kerja:** pemisah spasi memanggil `join` atas semua kata. **Jalankan:** `python 107_string_join.py`. **Hasil:** `Python mudah dipelajari`. **Source code:** [107_string_join.py](107_string_join.py). **Screenshot:** [Lihat hasil eksekusi](output/107_string_join.png).

### 108. Validasi string
**Tujuan:** Memeriksa karakter digit, huruf, dan teks kosong. **Konsep dan cara kerja:** `isdecimal`, `isalpha`, dan `strip` memeriksa tiga syarat berbeda; pemeriksaan karakter tidak menggantikan validasi data secara menyeluruh. **Jalankan:** `python 108_string_validation.py`. **Hasil:** ketiga pemeriksaan bernilai `True`. **Source code:** [108_string_validation.py](108_string_validation.py). **Screenshot:** [Lihat hasil eksekusi](output/108_string_validation.png).

### 109. Pembersihan teks
**Tujuan:** Menyeragamkan teks sebelum diproses. **Konsep dan cara kerja:** `strip` membuang spasi pinggir dan `lower` menormalkan huruf kapital. **Jalankan:** `python 109_string_cleaning.py`. **Hasil:** `'halo, python!'` dari input dengan spasi dan kapitalisasi berbeda. **Source code:** [109_string_cleaning.py](109_string_cleaning.py). **Screenshot:** [Lihat hasil eksekusi](output/109_string_cleaning.png).

### 110. Pemformatan string
**Tujuan:** Menyisipkan nilai dengan aturan format. **Konsep dan cara kerja:** `format` mengganti dua placeholder serta menampilkan skor satu angka desimal. **Jalankan:** `python 110_string_formatting.py`. **Hasil:** `Nama: Dina, Nilai: 87.5`. **Source code:** [110_string_formatting.py](110_string_formatting.py). **Screenshot:** [Lihat hasil eksekusi](output/110_string_formatting.png).

### 111. Unicode dan teks multibahasa
**Tujuan:** Menampilkan karakter dari beberapa sistem penulisan. **Konsep dan cara kerja:** string Unicode mengandung teks Latin, Mandarin, dan Arab; `sys.stdout.reconfigure` memakai UTF-8 agar terminal dengan encoding lama tidak gagal menampilkannya. **Jalankan:** `python 111_unicode_strings.py` pada terminal yang mendukung UTF-8. **Hasil:** sapaan multibahasa beserta jumlah karakter; bentuk glif bergantung pada font terminal. **Source code:** [111_unicode_strings.py](111_unicode_strings.py). **Screenshot:** [Lihat hasil eksekusi](output/111_unicode_strings.png).

### 112. Pemeriksaan palindrom
**Tujuan:** Menguji kesamaan urutan teks maju dan mundur. **Konsep dan cara kerja:** normalisasi menghapus karakter non-alfanumerik dan perbedaan kapitalisasi, lalu membandingkan string dengan `[::-1]`. **Jalankan:** `python 112_palindrome_checker.py`. **Hasil:** `Kasur rusak` adalah palindrom (`True`). **Source code:** [112_palindrome_checker.py](112_palindrome_checker.py). **Screenshot:** [Lihat hasil eksekusi](output/112_palindrome_checker.png).

## Ringkasan

String tidak bisa diubah pada tempatnya: slicing, penggabungan, dan metode mengembalikan teks baru. Normalisasi membantu pencarian dan validasi yang konsisten, sedangkan encoding terminal memengaruhi tampilan teks Unicode.