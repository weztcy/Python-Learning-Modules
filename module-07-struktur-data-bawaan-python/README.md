# Modul 7 — Struktur Data Bawaan Python

Tujuan modul ini adalah membandingkan list, tuple, set, dan dictionary, termasuk operasi pencarian, penyalinan, serta iterasinya. Gunakan Python 3.10+; semua contoh memakai standard library dan dijalankan dari folder modul dengan `python nama_file.py`. Setiap submodul menautkan screenshot jendela log eksekusi.

## Daftar materi

1. [List](79_list_basic.py)
2. [Indexing pada list](80_list_indexing.py)
3. [Slicing pada list](81_list_slicing.py)
4. [Metode list](82_list_methods.py)
5. [Iterasi list](83_list_iteration.py)
6. [Pencarian elemen list](84_list_search.py)
7. [Pengurutan list](85_list_sorting.py)
8. [Perbandingan list](86_list_comparison.py)
9. [Nested list](87_nested_list.py)
10. [Menyalin list](88_list_copying.py)
11. [Tuple](89_tuple_basic.py)
12. [Tuple unpacking](90_tuple_unpacking.py)
13. [Set](91_set_basic.py)
14. [Operasi himpunan](92_set_operations.py)
15. [Dictionary](93_dictionary_basic.py)
16. [Metode dictionary](94_dictionary_methods.py)
17. [Iterasi dictionary](95_dictionary_iteration.py)
18. [Nested dictionary](96_nested_dictionary.py)
19. [Perbandingan dictionary](97_dictionary_comparison.py)
20. [Konversi antarkoleksi](98_collection_conversion.py)

### 79. List
**Tujuan:** Menyimpan urutan yang bisa diubah. **Konsep dan cara kerja:** `append` menambah buah pada list; `len` menghitung jumlahnya. **Jalankan:** `python 79_list_basic.py`. **Hasil:** empat buah, jumlah 4. **Source code:** [79_list_basic.py](79_list_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/79_list_basic.png).

### 80. Indexing pada list
**Tujuan:** Mengakses elemen menurut posisi. **Konsep dan cara kerja:** indeks 0 memilih awal, -1 memilih akhir. **Jalankan:** `python 80_list_indexing.py`. **Hasil:** merah dan biru. **Source code:** [80_list_indexing.py](80_list_indexing.py). **Screenshot:** [Lihat hasil eksekusi](output/80_list_indexing.png).

### 81. Slicing pada list
**Tujuan:** Memilih bagian koleksi. **Konsep dan cara kerja:** `[:3]`, `[2:5]`, dan `[::2]` menghasilkan list baru dengan batas akhir eksklusif. **Jalankan:** `python 81_list_slicing.py`. **Hasil:** tiga irisan dari angka 0–5. **Source code:** [81_list_slicing.py](81_list_slicing.py). **Screenshot:** [Lihat hasil eksekusi](output/81_list_slicing.png).

### 82. Metode list
**Tujuan:** Mengubah isi dan urutan list. **Konsep dan cara kerja:** `append` menambah elemen, `sort` mengurutkan di tempat, `remove` menghapus nilai. **Jalankan:** `python 82_list_methods.py`. **Hasil:** list terurut `[1, 2, 3, 4]`, lalu `[1, 3, 4]`. **Source code:** [82_list_methods.py](82_list_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/82_list_methods.png).

### 83. Iterasi list
**Tujuan:** Membaca setiap nilai beserta posisinya. **Konsep dan cara kerja:** `enumerate(..., start=1)` menghasilkan nomor peserta dan skor. **Jalankan:** `python 83_list_iteration.py`. **Hasil:** skor tiga peserta. **Source code:** [83_list_iteration.py](83_list_iteration.py). **Screenshot:** [Lihat hasil eksekusi](output/83_list_iteration.png).

### 84. Pencarian elemen list
**Tujuan:** Menemukan posisi nilai dengan aman. **Konsep dan cara kerja:** `in` memastikan target ada sebelum `index` dipanggil. **Jalankan:** `python 84_list_search.py`. **Hasil:** indeks pisang 1. **Source code:** [84_list_search.py](84_list_search.py). **Screenshot:** [Lihat hasil eksekusi](output/84_list_search.png).

### 85. Pengurutan list
**Tujuan:** Mengurutkan tanpa mengubah data awal. **Konsep dan cara kerja:** `sorted` mengembalikan list baru, dengan opsi `reverse=True` untuk urutan turun. **Jalankan:** `python 85_list_sorting.py`. **Hasil:** list awal, urutan naik, dan urutan turun. **Source code:** [85_list_sorting.py](85_list_sorting.py). **Screenshot:** [Lihat hasil eksekusi](output/85_list_sorting.png).

### 86. Perbandingan list
**Tujuan:** Memahami perbandingan isi dan urutan. **Konsep dan cara kerja:** perbandingan leksikografis berhenti pada elemen pertama yang berbeda. **Jalankan:** `python 86_list_comparison.py`. **Hasil:** `a == b` salah, `a < b` benar. **Source code:** [86_list_comparison.py](86_list_comparison.py). **Screenshot:** [Lihat hasil eksekusi](output/86_list_comparison.png).

### 87. Nested list
**Tujuan:** Merepresentasikan data dua dimensi. **Konsep dan cara kerja:** dua indeks mengakses baris dan kolom matriks. **Jalankan:** `python 87_nested_list.py`. **Hasil:** baris `[3, 4]`, elemen 3. **Source code:** [87_nested_list.py](87_nested_list.py). **Screenshot:** [Lihat hasil eksekusi](output/87_nested_list.png).

### 88. Menyalin list
**Tujuan:** Membedakan alias dan salinan dangkal. **Konsep dan cara kerja:** `alias.append` mengubah list asli, sedangkan `copy()` menghasilkan list lain yang tidak ikut bertambah pada contoh datar ini. **Jalankan:** `python 88_list_copying.py`. **Hasil:** asli `[1, 2, 3]`, salinan `[1, 2]`. **Source code:** [88_list_copying.py](88_list_copying.py). **Screenshot:** [Lihat hasil eksekusi](output/88_list_copying.png).

### 89. Tuple
**Tujuan:** Menyimpan urutan yang immutable. **Konsep dan cara kerja:** pasangan koordinat disimpan sebagai tuple dan elemen pertama dibaca dengan indeks 0. **Jalankan:** `python 89_tuple_basic.py`. **Hasil:** `(3, 5)` dan 3. **Source code:** [89_tuple_basic.py](89_tuple_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/89_tuple_basic.png).

### 90. Tuple unpacking
**Tujuan:** Membagi isi tuple ke beberapa variabel. **Konsep dan cara kerja:** `x, y` menerima dua koordinat menurut posisi. **Jalankan:** `python 90_tuple_unpacking.py`. **Hasil:** x 4, y 7. **Source code:** [90_tuple_unpacking.py](90_tuple_unpacking.py). **Screenshot:** [Lihat hasil eksekusi](output/90_tuple_unpacking.png).

### 91. Set
**Tujuan:** Memahami keunikan dan keanggotaan. **Konsep dan cara kerja:** duplikat 2 dihapus otomatis, `add` memasukkan 4, `in` memeriksa anggota tanpa bergantung pada urutan. **Jalankan:** `python 91_set_basic.py`. **Hasil:** 4 anggota unik dan keanggotaan 2 benar. **Source code:** [91_set_basic.py](91_set_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/91_set_basic.png).

### 92. Operasi himpunan
**Tujuan:** Menghitung union, intersection, dan difference. **Konsep dan cara kerja:** operator `|`, `&`, `-` menghasilkan set; `sorted` menampilkan hasil secara konsisten. **Jalankan:** `python 92_set_operations.py`. **Hasil:** gabungan 1–5, irisan 3, selisih `[1, 2]`. **Source code:** [92_set_operations.py](92_set_operations.py). **Screenshot:** [Lihat hasil eksekusi](output/92_set_operations.png).

### 93. Dictionary
**Tujuan:** Mengaitkan kunci dengan nilai. **Konsep dan cara kerja:** kunci `nama` dibaca dan nilai pada kunci `nilai` ditimpa. **Jalankan:** `python 93_dictionary_basic.py`. **Hasil:** Ayu dan nilai 90. **Source code:** [93_dictionary_basic.py](93_dictionary_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/93_dictionary_basic.png).

### 94. Metode dictionary
**Tujuan:** Membaca kunci opsional dan menghapus entri. **Konsep dan cara kerja:** `get` memberi default untuk kelas yang tidak ada; `pop` mengembalikan nilai yang dihapus. **Jalankan:** `python 94_dictionary_methods.py`. **Hasil:** kelas belum diisi dan nilai 80 dihapus. **Source code:** [94_dictionary_methods.py](94_dictionary_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/94_dictionary_methods.png).

### 95. Iterasi dictionary
**Tujuan:** Menelusuri pasangan kunci-nilai. **Konsep dan cara kerja:** `items()` memberi nama barang sekaligus stoknya. **Jalankan:** `python 95_dictionary_iteration.py`. **Hasil:** apel 4, jeruk 2. **Source code:** [95_dictionary_iteration.py](95_dictionary_iteration.py). **Screenshot:** [Lihat hasil eksekusi](output/95_dictionary_iteration.png).

### 96. Nested dictionary
**Tujuan:** Mengakses data terstruktur bertingkat. **Konsep dan cara kerja:** kunci nama memilih siswa, kunci `nilai` atau `kelas` memilih atributnya. **Jalankan:** `python 96_nested_dictionary.py`. **Hasil:** nilai Ayu 90 dan kelas dua siswa. **Source code:** [96_nested_dictionary.py](96_nested_dictionary.py). **Screenshot:** [Lihat hasil eksekusi](output/96_nested_dictionary.png).

### 97. Perbandingan dictionary
**Tujuan:** Membandingkan isi tanpa bergantung pada urutan entri. **Konsep dan cara kerja:** dua dictionary setara hingga satu nilai diubah. **Jalankan:** `python 97_dictionary_comparison.py`. **Hasil:** `True` kemudian `False`. **Source code:** [97_dictionary_comparison.py](97_dictionary_comparison.py). **Screenshot:** [Lihat hasil eksekusi](output/97_dictionary_comparison.png).

### 98. Konversi antarkoleksi
**Tujuan:** Mengubah representasi data. **Konsep dan cara kerja:** `set` membuang duplikat; `sorted` mengurutkannya sebelum diubah menjadi list tampilan atau tuple. **Jalankan:** `python 98_collection_conversion.py`. **Hasil:** `[1, 2, 3]` dan `(1, 2, 3)`. **Source code:** [98_collection_conversion.py](98_collection_conversion.py). **Screenshot:** [Lihat hasil eksekusi](output/98_collection_conversion.png).

## Ringkasan

List dan tuple menjaga urutan; set menekankan anggota unik; dictionary memetakan kunci ke nilai. Pilih struktur sesuai kebutuhan akses, perubahan, dan keunikan data.