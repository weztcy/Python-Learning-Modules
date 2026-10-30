# Modul 1 — Pengenalan Python dan Struktur Program

Modul ini memperkenalkan eksekusi skrip, sintaks dasar, struktur file, dan keluaran terminal. Setelah mempelajarinya, pembaca dapat membuat serta menjalankan skrip Python sederhana. Tidak diperlukan pustaka eksternal; gunakan Python 3.10+.

## Daftar materi

1. [Program pertama Python](01_hello_world.py)
2. [Struktur program Python](02_python_program_structure.py)
3. [Komentar program](03_comments.py)
4. [Fungsi print()](04_print_function.py)
5. [Escape sequences](05_escape_sequences.py)
6. [Indentasi Python](06_indentation.py)
7. [Pernyataan program](07_multiple_statements.py)
8. [Kesalahan sintaks](08_syntax_errors.py)
9. [Interpreter Python](09_python_interpreter.py)
10. [Menjalankan file Python](10_run_python_script.py)

Jalankan setiap perintah di bawah dari folder modul ini. Hasil yang disebutkan adalah keluaran yang diharapkan; setiap submodul menautkan screenshot jendela log dari eksekusi nyata pada input demo.

### 1. Program pertama Python

**Tujuan dan konsep:** Mengenali skrip dan keluaran standar. **Cara kerja:** `print` menulis sapaan ke terminal. **Jalankan:** `python 01_hello_world.py`. **Hasil:** `Halo, dunia!`. **Source code:** [01_hello_world.py](01_hello_world.py). **Screenshot:** [Lihat hasil eksekusi](output/01_hello_world.png).

### 2. Struktur program Python

**Tujuan dan konsep:** Mengenal docstring, fungsi, dan main guard. **Cara kerja:** fungsi `sapa` menghasilkan teks; blok `if __name__ == "__main__"` mencetaknya hanya ketika skrip dijalankan langsung. **Jalankan:** `python 02_python_program_structure.py`. **Hasil:** `Halo, Python!`. **Source code:** [02_python_program_structure.py](02_python_program_structure.py). **Screenshot:** [Lihat hasil eksekusi](output/02_python_program_structure.png).

### 3. Komentar program

**Tujuan dan konsep:** Memahami bahwa komentar menjelaskan maksud kode tanpa dieksekusi. **Cara kerja:** angka dikalikan dua, lalu hasilnya dicetak; baris komentar tidak muncul di terminal. **Jalankan:** `python 03_comments.py`. **Hasil:** `Dua kali angka: 10`. **Source code:** [03_comments.py](03_comments.py). **Screenshot:** [Lihat hasil eksekusi](output/03_comments.png).

### 4. Fungsi `print()`

**Tujuan dan konsep:** Menggunakan banyak argumen serta parameter `sep` dan `end`. **Cara kerja:** `sep` mengubah pemisah tanggal, sedangkan `end` membuat dua pemanggilan `print` berbagi satu baris. **Jalankan:** `python 04_print_function.py`. **Hasil:** informasi nama dan usia, tanggal `2026-10-17`, serta `Satu baris`. **Source code:** [04_print_function.py](04_print_function.py). **Screenshot:** [Lihat hasil eksekusi](output/04_print_function.png).

### 5. Escape sequences

**Tujuan dan konsep:** Menggunakan `\n`, `\t`, `\\`, dan kutip yang di-escape. **Cara kerja:** karakter escape mengatur baris, tab, dan tampilan karakter khusus tanpa mengakhiri string. **Jalankan:** `python 05_escape_sequences.py`. **Hasil:** dua baris teks, baris bertab, path Windows, dan teks dalam tanda kutip. **Source code:** [05_escape_sequences.py](05_escape_sequences.py). **Screenshot:** [Lihat hasil eksekusi](output/05_escape_sequences.png).

### 6. Indentasi Python

**Tujuan dan konsep:** Mengetahui batas blok berdasarkan indentasi. **Cara kerja:** dua pernyataan di dalam `if` dijalankan saat nilai memenuhi syarat; pernyataan tanpa indentasi tetap berjalan setelahnya. **Jalankan:** `python 06_indentation.py`. **Hasil:** `Hasil: Lulus` dan `Pemeriksaan selesai`. **Source code:** [06_indentation.py](06_indentation.py). **Screenshot:** [Lihat hasil eksekusi](output/06_indentation.png).

### 7. Pernyataan program

**Tujuan dan konsep:** Menyusun beberapa pernyataan berurutan. **Cara kerja:** variabel ukuran diisi, luas dihitung, lalu dicetak pada baris terpisah dalam source code. **Jalankan:** `python 07_multiple_statements.py`. **Hasil:** `Luas persegi panjang: 24`. **Source code:** [07_multiple_statements.py](07_multiple_statements.py). **Screenshot:** [Lihat hasil eksekusi](output/07_multiple_statements.png).

### 8. Kesalahan sintaks

**Tujuan dan konsep:** Mengenali `SyntaxError` tanpa membuat file contoh tidak dapat dijalankan. **Cara kerja:** `compile` memeriksa contoh string yang salah dan exception-nya ditangkap; versi sintaks benar dikompilasi dan dijalankan. **Jalankan:** `python 08_syntax_errors.py`. **Hasil:** pesan kesalahan sintaks dan `Halo`. **Source code:** [08_syntax_errors.py](08_syntax_errors.py). **Screenshot:** [Lihat hasil eksekusi](output/08_syntax_errors.png).

### 9. Interpreter Python

**Tujuan dan konsep:** Mengenali implementasi, versi, dan lokasi interpreter yang sedang digunakan. **Cara kerja:** `platform` menyediakan informasi implementasi serta versi; `sys.executable` menyediakan path interpreter. **Jalankan:** `python 09_python_interpreter.py`. **Hasil:** tiga baris informasi sesuai komputer pengguna. **Source code:** [09_python_interpreter.py](09_python_interpreter.py). **Screenshot:** [Lihat hasil eksekusi](output/09_python_interpreter.png).

### 10. Menjalankan file Python

**Tujuan dan konsep:** Menjalankan skrip lain dengan interpreter Python. **Cara kerja:** `Path(__file__)` menemukan [01_hello_world.py](01_hello_world.py) di folder yang sama; `subprocess.run` memanggilnya sebagai proses terpisah. **Jalankan:** `python 10_run_python_script.py`. **Hasil:** nama skrip yang dijalankan dan `Halo, dunia!`. **Source code:** [10_run_python_script.py](10_run_python_script.py). **Screenshot:** [Lihat hasil eksekusi](output/10_run_python_script.png).

## Ringkasan

Mulai dari keluaran sederhana, modul ini menunjukkan bagaimana Python membaca pernyataan, menggunakan indentasi dan komentar, memeriksa sintaks, serta menjalankan skrip secara langsung atau dari skrip lain.