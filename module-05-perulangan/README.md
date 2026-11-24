# Modul 5 — Perulangan

Modul ini menjelaskan `for`, `while`, kontrol loop, akumulasi, pola, serta penerapan pada bilangan dan permainan. Tujuannya agar pembaca memahami kapan loop selesai dan bagaimana hasil dihitung pada setiap putaran. Gunakan Python 3.10+; tidak perlu pustaka eksternal.

## Daftar materi

1. [Perulangan for](49_for_loop.py)
2. [Perulangan while](50_while_loop.py)
3. [Fungsi range()](51_range_function.py)
4. [Nested loop](52_nested_loop.py)
5. [Pernyataan break](53_break_statement.py)
6. [Pernyataan continue](54_continue_statement.py)
7. [Else pada perulangan](55_loop_else.py)
8. [Penghitung perulangan](56_loop_counter.py)
9. [Penjumlahan bilangan](57_sum_numbers.py)
10. [Faktorial menggunakan loop](58_factorial_loop.py)
11. [Tabel perkalian](59_multiplication_table.py)
12. [Pola angka](60_number_patterns.py)
13. [Pola bintang](61_star_patterns.py)
14. [Pemeriksaan bilangan prima](62_prime_number.py)
15. [Permainan tebak angka](63_guessing_game.py)

Jalankan setiap perintah dari folder modul ini. Screenshot tiap submodul menampilkan jendela log eksekusi; nilai acak pada permainan dapat berbeda antar-run.

### 49. Perulangan `for`
**Tujuan dan konsep:** Mengunjungi elemen iterable. **Cara kerja:** `for` mengambil setiap buah dari tuple secara berurutan. **Jalankan:** `python 49_for_loop.py`. **Hasil:** apel, mangga, jeruk. **Source code:** [49_for_loop.py](49_for_loop.py). **Screenshot:** [Lihat hasil eksekusi](output/49_for_loop.png).

### 50. Perulangan `while`
**Tujuan dan konsep:** Mengulang selama syarat benar. **Cara kerja:** angka bertambah agar loop berhenti setelah putaran ketiga. **Jalankan:** `python 50_while_loop.py`. **Hasil:** putaran 1–3. **Source code:** [50_while_loop.py](50_while_loop.py). **Screenshot:** [Lihat hasil eksekusi](output/50_while_loop.png).

### 51. Fungsi `range()`
**Tujuan dan konsep:** Membuat deret dengan awal, akhir eksklusif, dan langkah. **Cara kerja:** `range(2, 11, 2)` menghasilkan bilangan genap hingga 10. **Jalankan:** `python 51_range_function.py`. **Hasil:** 2, 4, 6, 8, 10. **Source code:** [51_range_function.py](51_range_function.py). **Screenshot:** [Lihat hasil eksekusi](output/51_range_function.png).

### 52. Nested loop
**Tujuan dan konsep:** Mengulang loop dalam loop. **Cara kerja:** tiap baris memproses tiga kolom sebelum pindah ke baris berikutnya. **Jalankan:** `python 52_nested_loop.py`. **Hasil:** pasangan koordinat dua baris dan tiga kolom. **Source code:** [52_nested_loop.py](52_nested_loop.py). **Screenshot:** [Lihat hasil eksekusi](output/52_nested_loop.png).

### 53. Pernyataan `break`
**Tujuan dan konsep:** Menghentikan loop lebih awal. **Cara kerja:** pencarian berhenti saat angka 4 ditemukan. **Jalankan:** `python 53_break_statement.py`. **Hasil:** `Ditemukan: 4`. **Source code:** [53_break_statement.py](53_break_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/53_break_statement.png).

### 54. Pernyataan `continue`
**Tujuan dan konsep:** Melewatkan putaran tertentu. **Cara kerja:** angka genap tidak dicetak karena `continue` melompati sisa badan loop. **Jalankan:** `python 54_continue_statement.py`. **Hasil:** 1, 3, dan 5. **Source code:** [54_continue_statement.py](54_continue_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/54_continue_statement.png).

### 55. Else pada perulangan
**Tujuan dan konsep:** Membedakan pencarian selesai dari penghentian oleh `break`. **Cara kerja:** target 4 tidak ada dalam tuple, sehingga blok `else` berjalan setelah loop. **Jalankan:** `python 55_loop_else.py`. **Hasil:** `Target tidak ditemukan`. **Source code:** [55_loop_else.py](55_loop_else.py). **Screenshot:** [Lihat hasil eksekusi](output/55_loop_else.png).

### 56. Penghitung perulangan
**Tujuan dan konsep:** Menghitung banyak elemen yang diproses. **Cara kerja:** variabel `jumlah` bertambah tiap iterasi dan ditampilkan bersama buah. **Jalankan:** `python 56_loop_counter.py`. **Hasil:** tiga elemen, total 3. **Source code:** [56_loop_counter.py](56_loop_counter.py). **Screenshot:** [Lihat hasil eksekusi](output/56_loop_counter.png).

### 57. Penjumlahan bilangan
**Tujuan dan konsep:** Memakai akumulator. **Cara kerja:** `total` menyimpan hasil sementara penjumlahan 1 hingga 5. **Jalankan:** `python 57_sum_numbers.py`. **Hasil:** 15. **Source code:** [57_sum_numbers.py](57_sum_numbers.py). **Screenshot:** [Lihat hasil eksekusi](output/57_sum_numbers.png).

### 58. Faktorial menggunakan loop
**Tujuan dan konsep:** Mengalikan bilangan berurutan. **Cara kerja:** `hasil` dimulai dari 1 dan dikalikan setiap angka sampai 5. **Jalankan:** `python 58_factorial_loop.py`. **Hasil:** `5! = 120`. **Source code:** [58_factorial_loop.py](58_factorial_loop.py). **Screenshot:** [Lihat hasil eksekusi](output/58_factorial_loop.png).

### 59. Tabel perkalian
**Tujuan dan konsep:** Menghasilkan deret hasil kali. **Cara kerja:** angka 7 dikalikan pengali 1 hingga 10 pada setiap putaran. **Jalankan:** `python 59_multiplication_table.py`. **Hasil:** tabel 7 × 1 hingga 7 × 10. **Source code:** [59_multiplication_table.py](59_multiplication_table.py). **Screenshot:** [Lihat hasil eksekusi](output/59_multiplication_table.png).

### 60. Pola angka
**Tujuan dan konsep:** Membentuk pola segitiga dengan nested loop. **Cara kerja:** baris ke-n mencetak angka 1 sampai n. **Jalankan:** `python 60_number_patterns.py`. **Hasil:** lima baris pola angka yang bertambah panjang. **Source code:** [60_number_patterns.py](60_number_patterns.py). **Screenshot:** [Lihat hasil eksekusi](output/60_number_patterns.png).

### 61. Pola bintang
**Tujuan dan konsep:** Menggabungkan perulangan dan pengulangan string. **Cara kerja:** tiap baris mencetak bintang sebanyak nomor barisnya. **Jalankan:** `python 61_star_patterns.py`. **Hasil:** lima baris, dari satu sampai lima bintang. **Source code:** [61_star_patterns.py](61_star_patterns.py). **Screenshot:** [Lihat hasil eksekusi](output/61_star_patterns.png).

### 62. Pemeriksaan bilangan prima
**Tujuan dan konsep:** Mencari pembagi bilangan secara efisien. **Cara kerja:** loop hanya memeriksa pembagi hingga akar bilangan; bila ditemukan pembagi, `break` menghentikan pencarian. **Jalankan:** `python 62_prime_number.py`. **Hasil:** `29 prima`. **Source code:** [62_prime_number.py](62_prime_number.py). **Screenshot:** [Lihat hasil eksekusi](output/62_prime_number.png).

### 63. Permainan tebak angka
**Tujuan dan konsep:** Menggabungkan loop berbatas, input, dan percabangan. **Cara kerja:** `random.randint` memilih angka 1–10; pemain mendapat maksimal tiga percobaan dan petunjuk lebih besar/kecil. Input bukan integer memakai satu kesempatan. **Jalankan:** `python 63_guessing_game.py`; masukkan tebakan saat diminta. **Hasil:** pesan tepat atau jawaban setelah kesempatan habis; hasil berbeda karena acak. **Source code:** [63_guessing_game.py](63_guessing_game.py). **Screenshot:** [Lihat hasil eksekusi](output/63_guessing_game.png).

## Ringkasan

Perulangan memproses koleksi atau syarat yang berulang. `break` dan `continue` memengaruhi alurnya, sedangkan penghitung dan akumulator memungkinkan perhitungan bertahap.