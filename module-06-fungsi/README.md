# Modul 6 — Fungsi

Modul ini memperkenalkan fungsi, parameter, argumen, nilai balik, scope, rekursi, docstring, dan type hints. Tujuannya agar pembelajar dapat mengemas perilaku yang dipakai kembali dan memahami bagaimana data berpindah masuk maupun keluar fungsi. Semua contoh berjalan dengan Python 3.10+ tanpa pustaka eksternal.

## Daftar materi

1. [Fungsi dasar](64_function_basic.py)
2. [Parameter fungsi](65_function_parameters.py)
3. [Nilai balik fungsi](66_return_statement.py)
4. [Fungsi tanpa nilai balik eksplisit](67_void_like_function.py)
5. [Default arguments](68_default_arguments.py)
6. [Keyword arguments](69_keyword_arguments.py)
7. [Positional arguments](70_positional_arguments.py)
8. [Arbitrary arguments](71_arbitrary_arguments.py)
9. [Keyword arbitrary arguments](72_keyword_arbitrary_arguments.py)
10. [Local dan global scope](73_function_scope.py)
11. [Keyword global](74_global_keyword.py)
12. [Keyword nonlocal](75_nonlocal_keyword.py)
13. [Fungsi rekursif](76_recursive_function.py)
14. [Docstring fungsi](77_function_docstring.py)
15. [Type hints pada fungsi](78_function_type_hints.py)

Jalankan perintah berikut dari folder modul ini. Tautan screenshot per submodul menampilkan jendela log dari eksekusi aktual.

### 64. Fungsi dasar
**Tujuan dan konsep:** Mengenal `def` dan pemanggilan. **Cara kerja:** satu fungsi `sapa` dipanggil dua kali tanpa menduplikasi perintah `print`. **Jalankan:** `python 64_function_basic.py`. **Hasil:** dua baris sapaan. **Source code:** [64_function_basic.py](64_function_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/64_function_basic.png).

### 65. Parameter fungsi
**Tujuan dan konsep:** Memberi data berbeda pada fungsi yang sama. **Cara kerja:** `nama` menerima Ayu dan Budi pada pemanggilan terpisah. **Jalankan:** `python 65_function_parameters.py`. **Hasil:** dua sapaan dengan nama berbeda. **Source code:** [65_function_parameters.py](65_function_parameters.py). **Screenshot:** [Lihat hasil eksekusi](output/65_function_parameters.png).

### 66. Nilai balik fungsi
**Tujuan dan konsep:** Memisahkan perhitungan dari tampilan. **Cara kerja:** `return` mengirim luas kuadrat sisi 4 ke `print` di luar fungsi. **Jalankan:** `python 66_return_statement.py`. **Hasil:** `Luas: 16`. **Source code:** [66_return_statement.py](66_return_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/66_return_statement.png).

### 67. Fungsi tanpa nilai balik eksplisit
**Tujuan dan konsep:** Mengenali nilai balik implisit `None`. **Cara kerja:** fungsi mencetak pesan tetapi tidak memiliki `return`; pemanggil mencetak nilai baliknya. **Jalankan:** `python 67_void_like_function.py`. **Hasil:** pesan dan `Nilai balik: None`. **Source code:** [67_void_like_function.py](67_void_like_function.py). **Screenshot:** [Lihat hasil eksekusi](output/67_void_like_function.png).

### 68. Default arguments
**Tujuan dan konsep:** Menyediakan argumen opsional. **Cara kerja:** sapaan memakai `teman` jika nama tidak diberikan, tetapi memakai Rani bila diberikan. **Jalankan:** `python 68_default_arguments.py`. **Hasil:** `Halo, teman!` dan `Halo, Rani!`. **Source code:** [68_default_arguments.py](68_default_arguments.py). **Screenshot:** [Lihat hasil eksekusi](output/68_default_arguments.png).

### 69. Keyword arguments
**Tujuan dan konsep:** Memberikan argumen dengan menyebut nama parameter. **Cara kerja:** `kota` disebut sebelum `nama` tanpa mengubah pemetaan datanya. **Jalankan:** `python 69_keyword_arguments.py`. **Hasil:** Ayu tinggal di Bandung. **Source code:** [69_keyword_arguments.py](69_keyword_arguments.py). **Screenshot:** [Lihat hasil eksekusi](output/69_keyword_arguments.png).

### 70. Positional arguments
**Tujuan dan konsep:** Memahami pengaruh urutan argumen. **Cara kerja:** pengurangan 10−3 dan 3−10 memakai fungsi yang sama dengan posisi terbalik. **Jalankan:** `python 70_positional_arguments.py`. **Hasil:** 7 dan -7. **Source code:** [70_positional_arguments.py](70_positional_arguments.py). **Screenshot:** [Lihat hasil eksekusi](output/70_positional_arguments.png).

### 71. `*args`
**Tujuan dan konsep:** Menerima banyak argumen posisi. **Cara kerja:** `*angka` menjadi tuple untuk dihitung `sum`. **Jalankan:** `python 71_arbitrary_arguments.py`. **Hasil:** total 10. **Source code:** [71_arbitrary_arguments.py](71_arbitrary_arguments.py). **Screenshot:** [Lihat hasil eksekusi](output/71_arbitrary_arguments.png).

### 72. `**kwargs`
**Tujuan dan konsep:** Menerima banyak argumen bernama. **Cara kerja:** `**data` menjadi dictionary, lalu setiap pasangan kunci-nilai dicetak. **Jalankan:** `python 72_keyword_arbitrary_arguments.py`. **Hasil:** nama Sari dan usia 22. **Source code:** [72_keyword_arbitrary_arguments.py](72_keyword_arbitrary_arguments.py). **Screenshot:** [Lihat hasil eksekusi](output/72_keyword_arbitrary_arguments.png).

### 73. Local dan global scope
**Tujuan dan konsep:** Membedakan nama lokal dengan nama di tingkat modul. **Cara kerja:** assignment `nama` di fungsi tidak mengubah `nama` di luar. **Jalankan:** `python 73_function_scope.py`. **Hasil:** `lokal` di dalam dan `global` di luar. **Source code:** [73_function_scope.py](73_function_scope.py). **Screenshot:** [Lihat hasil eksekusi](output/73_function_scope.png).

### 74. Keyword `global`
**Tujuan dan konsep:** Memodifikasi nama di lingkup modul dari sebuah fungsi. **Cara kerja:** `global` memungkinkan `jumlah_panggilan` diperbarui dua kali. **Jalankan:** `python 74_global_keyword.py`. **Hasil:** jumlah panggilan 2. **Source code:** [74_global_keyword.py](74_global_keyword.py). **Screenshot:** [Lihat hasil eksekusi](output/74_global_keyword.png).

### 75. Keyword `nonlocal`
**Tujuan dan konsep:** Memodifikasi nilai pada lingkup fungsi pembungkus. **Cara kerja:** closure `tambah` menyimpan penghitung dengan `nonlocal` antar pemanggilan. **Jalankan:** `python 75_nonlocal_keyword.py`. **Hasil:** `1 2`. **Source code:** [75_nonlocal_keyword.py](75_nonlocal_keyword.py). **Screenshot:** [Lihat hasil eksekusi](output/75_nonlocal_keyword.png).

### 76. Fungsi rekursif
**Tujuan dan konsep:** Fungsi dapat memanggil dirinya untuk masalah yang lebih kecil. **Cara kerja:** faktorial mengalikan n dengan faktorial n−1 hingga base case n≤1. **Jalankan:** `python 76_recursive_function.py`. **Hasil:** `5! = 120`. **Source code:** [76_recursive_function.py](76_recursive_function.py). **Screenshot:** [Lihat hasil eksekusi](output/76_recursive_function.png).

### 77. Docstring fungsi
**Tujuan dan konsep:** Menaruh dokumentasi pada objek fungsi. **Cara kerja:** `__doc__` membaca deskripsi di dalam definisi, kemudian luas dihitung. **Jalankan:** `python 77_function_docstring.py`. **Hasil:** teks dokumentasi dan luas 12. **Source code:** [77_function_docstring.py](77_function_docstring.py). **Screenshot:** [Lihat hasil eksekusi](output/77_function_docstring.png).

### 78. Type hints pada fungsi
**Tujuan dan konsep:** Menyatakan tipe parameter dan hasil yang diharapkan. **Cara kerja:** anotasi pada `kali` dapat dibaca dari `__annotations__`; Python tidak memaksakan tipenya saat runtime. **Jalankan:** `python 78_function_type_hints.py`. **Hasil:** hasil 12 dan informasi anotasi. **Source code:** [78_function_type_hints.py](78_function_type_hints.py). **Screenshot:** [Lihat hasil eksekusi](output/78_function_type_hints.png).

## Ringkasan

Fungsi mengurangi pengulangan kode dan memperjelas input serta hasil. Variasi argumen, scope, rekursi, dan dokumentasi memperluas cara fungsi dipakai tanpa mengubah konsep dasar pemanggilan.