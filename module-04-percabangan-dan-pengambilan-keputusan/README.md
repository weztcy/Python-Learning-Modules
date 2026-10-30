# Modul 4 — Percabangan dan Pengambilan Keputusan

Modul ini mengajarkan pengambilan keputusan melalui `if`, `elif`, `else`, conditional expression, dan `match-case`, kemudian menerapkannya pada beberapa aturan sederhana. Tujuannya agar pembaca mampu mengubah syarat menjadi keluaran yang tepat. Gunakan Python 3.10+ karena `match-case` membutuhkan Python 3.10 atau lebih baru.

## Daftar materi

1. [Percabangan if](39_if_statement.py)
2. [Percabangan if-else](40_if_else.py)
3. [Percabangan elif](41_elif_statement.py)
4. [Nested if](42_nested_if.py)
5. [Kondisi gabungan](43_multiple_conditions.py)
6. [Conditional expression](44_ternary_expression.py)
7. [Pattern matching](45_match_case.py)
8. [Program penentuan nilai](46_grade_calculator.py)
9. [Bilangan genap dan ganjil](47_even_odd.py)
10. [Tahun kabisat](48_leap_year.py)

Jalankan setiap perintah dari folder modul ini. Screenshot jendela log eksekusi tersedia pada tiap submodul.

### 39. Percabangan `if`
**Tujuan dan konsep:** Menjalankan blok hanya jika syarat benar. **Cara kerja:** skor 80 dibandingkan dengan batas 75. **Jalankan:** `python 39_if_statement.py`. **Hasil:** `Lulus`. **Source code:** [39_if_statement.py](39_if_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/39_if_statement.png).

### 40. Percabangan `if-else`
**Tujuan dan konsep:** Memilih salah satu dari dua hasil. **Cara kerja:** harga dibandingkan dengan saldo; cabang `else` berjalan ketika saldo kurang. **Jalankan:** `python 40_if_else.py`. **Hasil:** `Saldo tidak mencukupi`. **Source code:** [40_if_else.py](40_if_else.py). **Screenshot:** [Lihat hasil eksekusi](output/40_if_else.png).

### 41. Percabangan `elif`
**Tujuan dan konsep:** Mengevaluasi kondisi berjenjang. **Cara kerja:** skor 82 diperiksa dari ambang A hingga B, lalu hanya satu kategori dipilih. **Jalankan:** `python 41_elif_statement.py`. **Hasil:** kategori B. **Source code:** [41_elif_statement.py](41_elif_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/41_elif_statement.png).

### 42. Nested if
**Tujuan dan konsep:** Membuat pemeriksaan bertingkat. **Cara kerja:** tiket hanya diperiksa jika usia setidaknya 18 tahun. **Jalankan:** `python 42_nested_if.py`. **Hasil:** `Silakan masuk`. **Source code:** [42_nested_if.py](42_nested_if.py). **Screenshot:** [Lihat hasil eksekusi](output/42_nested_if.png).

### 43. Kondisi gabungan
**Tujuan dan konsep:** Mengharuskan dua kriteria terpenuhi. **Cara kerja:** `and` memeriksa skor serta kehadiran peserta. **Jalankan:** `python 43_multiple_conditions.py`. **Hasil:** `Lulus`. **Source code:** [43_multiple_conditions.py](43_multiple_conditions.py). **Screenshot:** [Lihat hasil eksekusi](output/43_multiple_conditions.png).

### 44. Conditional expression
**Tujuan dan konsep:** Memilih nilai dari kondisi dalam satu ekspresi. **Cara kerja:** sisa bagi dua menentukan label genap atau ganjil. **Jalankan:** `python 44_ternary_expression.py`. **Hasil:** `11 adalah bilangan ganjil`. **Source code:** [44_ternary_expression.py](44_ternary_expression.py). **Screenshot:** [Lihat hasil eksekusi](output/44_ternary_expression.png).

### 45. Pattern matching dengan `match-case`
**Tujuan dan konsep:** Memilih cabang berdasarkan pola string. **Cara kerja:** `match` mencocokkan perintah dengan `mulai`, `berhenti`, atau pola default `_`. **Jalankan:** `python 45_match_case.py`. **Hasil:** `Program dimulai`. **Source code:** [45_match_case.py](45_match_case.py). **Screenshot:** [Lihat hasil eksekusi](output/45_match_case.png).

### 46. Program penentuan nilai
**Tujuan dan konsep:** Menerapkan batas nilai dan validasi rentang. **Cara kerja:** nilai di luar 0–100 ditolak; ambang grade diperiksa dari tertinggi ke terendah. **Jalankan:** `python 46_grade_calculator.py`. **Hasil:** `Grade: A` untuk 86. **Source code:** [46_grade_calculator.py](46_grade_calculator.py). **Screenshot:** [Lihat hasil eksekusi](output/46_grade_calculator.png).

### 47. Bilangan genap dan ganjil
**Tujuan dan konsep:** Menggunakan sisa bagi dalam percabangan. **Cara kerja:** bilangan dengan sisa 0 saat dibagi 2 adalah genap. **Jalankan:** `python 47_even_odd.py`. **Hasil:** `17 ganjil`. **Source code:** [47_even_odd.py](47_even_odd.py). **Screenshot:** [Lihat hasil eksekusi](output/47_even_odd.png).

### 48. Program tahun kabisat
**Tujuan dan konsep:** Menggabungkan aturan pembagian 4, 100, dan 400. **Cara kerja:** tahun abad harus habis dibagi 400; tahun lainnya cukup habis dibagi 4 dan tidak habis dibagi 100. **Jalankan:** `python 48_leap_year.py`. **Hasil:** `2024 kabisat`. **Source code:** [48_leap_year.py](48_leap_year.py). **Screenshot:** [Lihat hasil eksekusi](output/48_leap_year.png).

## Ringkasan

Percabangan memungkinkan program merespons kondisi yang berbeda; periksa syarat sesuai urutan prioritas agar aturan tidak saling menimpa.