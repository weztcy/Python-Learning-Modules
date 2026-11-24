# Modul 9 — Comprehension, Iterator, dan Generator

Modul ini memperlihatkan cara membangun koleksi ringkas, membaca elemen bertahap, dan menunda perhitungan sampai nilainya diperlukan. Tujuan pembelajaran: membedakan koleksi yang langsung terbentuk dari iterator atau generator yang dikonsumsi saat diminta. Gunakan Python 3.10+ tanpa dependensi tambahan. Jalankan perintah berikut dari folder modul ini; screenshot jendela log eksekusi ditautkan di tiap submodul.

## Daftar materi

1. [List comprehension](113_list_comprehension.py)
2. [Conditional comprehension](114_list_comprehension_conditions.py)
3. [Nested comprehension](115_nested_comprehension.py)
4. [Dictionary comprehension](116_dictionary_comprehension.py)
5. [Set comprehension](117_set_comprehension.py)
6. [Generator expression](118_generator_expression.py)
7. [Fungsi iter()](119_iter_function.py)
8. [Fungsi next()](120_next_function.py)
9. [Custom iterator](121_custom_iterator.py)
10. [Iterator protocol](122_iterator_protocol.py)
11. [Generator function](123_generator_function.py)
12. [Keyword yield](124_yield_keyword.py)
13. [yield from](125_yield_from.py)
14. [Generator pipeline](126_generator_pipeline.py)
15. [Lazy evaluation](127_lazy_evaluation.py)
16. [Fungsi enumerate() dan zip()](128_enumerate_zip.py)

### 113. List comprehension
**Tujuan:** Membuat list dari transformasi iterable. **Konsep dan cara kerja:** setiap angka 1–5 dikuadratkan dalam satu ekspresi. **Jalankan:** `python 113_list_comprehension.py`. **Hasil:** `[1, 4, 9, 16, 25]`. **Source code:** [113_list_comprehension.py](113_list_comprehension.py). **Screenshot:** [Lihat hasil eksekusi](output/113_list_comprehension.png).

### 114. Conditional comprehension
**Tujuan:** Menyaring elemen saat membangun list. **Konsep dan cara kerja:** hanya angka dengan sisa bagi dua nol yang dimasukkan. **Jalankan:** `python 114_list_comprehension_conditions.py`. **Hasil:** `[2, 4, 6, 8, 10]`. **Source code:** [114_list_comprehension_conditions.py](114_list_comprehension_conditions.py). **Screenshot:** [Lihat hasil eksekusi](output/114_list_comprehension_conditions.png).

### 115. Nested comprehension
**Tujuan:** Menggabungkan dua perulangan dalam satu ekspresi. **Konsep dan cara kerja:** untuk setiap baris 1–2 dibuat pasangan dengan kolom 1–3. **Jalankan:** `python 115_nested_comprehension.py`. **Hasil:** enam pasangan koordinat. **Source code:** [115_nested_comprehension.py](115_nested_comprehension.py). **Screenshot:** [Lihat hasil eksekusi](output/115_nested_comprehension.png).

### 116. Dictionary comprehension
**Tujuan:** Membuat pasangan kunci-nilai. **Konsep dan cara kerja:** bilangan 1–4 menjadi kunci dan kuadratnya menjadi nilai. **Jalankan:** `python 116_dictionary_comprehension.py`. **Hasil:** `{1: 1, 2: 4, 3: 9, 4: 16}`. **Source code:** [116_dictionary_comprehension.py](116_dictionary_comprehension.py). **Screenshot:** [Lihat hasil eksekusi](output/116_dictionary_comprehension.png).

### 117. Set comprehension
**Tujuan:** Menghilangkan duplikat hasil transformasi. **Konsep dan cara kerja:** set menampung kuadrat unik, lalu `sorted` membuat tampilan deterministik. **Jalankan:** `python 117_set_comprehension.py`. **Hasil:** `[1, 4, 9]`. **Source code:** [117_set_comprehension.py](117_set_comprehension.py). **Screenshot:** [Lihat hasil eksekusi](output/117_set_comprehension.png).

### 118. Generator expression
**Tujuan:** Menghitung nilai sesuai kebutuhan tanpa membuat list hasil antara. **Konsep dan cara kerja:** `sum` meminta kuadrat satu per satu dari generator. **Jalankan:** `python 118_generator_expression.py`. **Hasil:** jumlah 55. **Source code:** [118_generator_expression.py](118_generator_expression.py). **Screenshot:** [Lihat hasil eksekusi](output/118_generator_expression.png).

### 119. Fungsi `iter()`
**Tujuan:** Mengambil iterator dari list. **Konsep dan cara kerja:** dua pemanggilan `next` mengonsumsi elemen secara berurutan. **Jalankan:** `python 119_iter_function.py`. **Hasil:** apel lalu jeruk. **Source code:** [119_iter_function.py](119_iter_function.py). **Screenshot:** [Lihat hasil eksekusi](output/119_iter_function.png).

### 120. Fungsi `next()`
**Tujuan:** Mengambil elemen berikutnya dan menangani akhir iterator. **Konsep dan cara kerja:** argumen default `habis` mencegah `StopIteration` ketika data kosong. **Jalankan:** `python 120_next_function.py`. **Hasil:** 10, 20, dan `habis`. **Source code:** [120_next_function.py](120_next_function.py). **Screenshot:** [Lihat hasil eksekusi](output/120_next_function.png).

### 121. Custom iterator
**Tujuan:** Menerapkan protokol iterator pada sebuah class. **Konsep dan cara kerja:** `__iter__` mengembalikan objek yang sama; `__next__` mengurangi angka sampai mengangkat `StopIteration`. **Jalankan:** `python 121_custom_iterator.py`. **Hasil:** 3, 2, 1. **Source code:** [121_custom_iterator.py](121_custom_iterator.py). **Screenshot:** [Lihat hasil eksekusi](output/121_custom_iterator.png).

### 122. Iterator protocol
**Tujuan:** Membuat iterable yang dapat dibaca ulang. **Konsep dan cara kerja:** `__iter__` membuat iterator range baru pada setiap loop, berbeda dari iterator yang telah habis. **Jalankan:** `python 122_iterator_protocol.py`. **Hasil:** `[2, 4, 6]` dua kali. **Source code:** [122_iterator_protocol.py](122_iterator_protocol.py). **Screenshot:** [Lihat hasil eksekusi](output/122_iterator_protocol.png).

### 123. Generator function
**Tujuan:** Membuat iterator dengan fungsi yang memakai `yield`. **Konsep dan cara kerja:** fungsi menghitung mundur; `list` mengonsumsi semua nilai yang dihasilkan. **Jalankan:** `python 123_generator_function.py`. **Hasil:** `[3, 2, 1]`. **Source code:** [123_generator_function.py](123_generator_function.py). **Screenshot:** [Lihat hasil eksekusi](output/123_generator_function.png).

### 124. Keyword `yield`
**Tujuan:** Melihat fungsi berhenti sementara dan melanjutkan dari posisi sebelumnya. **Konsep dan cara kerja:** dua `next` mengambil hasil dari dua titik `yield` yang terpisah. **Jalankan:** `python 124_yield_keyword.py`. **Hasil:** 1 lalu 2. **Source code:** [124_yield_keyword.py](124_yield_keyword.py). **Screenshot:** [Lihat hasil eksekusi](output/124_yield_keyword.png).

### 125. `yield from`
**Tujuan:** Meneruskan hasil iterable lain. **Konsep dan cara kerja:** dua tuple didelegasikan dengan `yield from` ke generator pemanggil. **Jalankan:** `python 125_yield_from.py`. **Hasil:** `[1, 2, 3, 4]`. **Source code:** [125_yield_from.py](125_yield_from.py). **Screenshot:** [Lihat hasil eksekusi](output/125_yield_from.png).

### 126. Generator pipeline
**Tujuan:** Menghubungkan transformasi tanpa list perantara. **Konsep dan cara kerja:** generator pertama menyaring angka genap dan generator kedua menghitung kuadratnya. **Jalankan:** `python 126_generator_pipeline.py`. **Hasil:** `[4, 16, 36]`. **Source code:** [126_generator_pipeline.py](126_generator_pipeline.py). **Screenshot:** [Lihat hasil eksekusi](output/126_generator_pipeline.png).

### 127. Lazy evaluation
**Tujuan:** Mengamati waktu evaluasi generator. **Konsep dan cara kerja:** pesan menghitung baru tampil ketika `next` meminta nilai, bukan saat generator dibuat; angka ketiga belum dihitung. **Jalankan:** `python 127_lazy_evaluation.py`. **Hasil:** pesan pembuatan, lalu perhitungan 1 dan 2 beserta kuadratnya. **Source code:** [127_lazy_evaluation.py](127_lazy_evaluation.py). **Screenshot:** [Lihat hasil eksekusi](output/127_lazy_evaluation.png).

### 128. Fungsi `enumerate()` dan `zip()`
**Tujuan:** Memasangkan dua iterable sekaligus memberi nomor. **Konsep dan cara kerja:** `zip` memasangkan nama dengan skor; `enumerate` menambahkan nomor urut mulai dari 1. **Jalankan:** `python 128_enumerate_zip.py`. **Hasil:** dua peserta, Ayu 90 dan Budi 80. **Source code:** [128_enumerate_zip.py](128_enumerate_zip.py). **Screenshot:** [Lihat hasil eksekusi](output/128_enumerate_zip.png).

## Ringkasan

Comprehension membangun koleksi langsung. Iterator dan generator mengembalikan data bertahap; `yield`, `next`, dan `iter` mengatur kapan suatu nilai diproduksi atau dikonsumsi.