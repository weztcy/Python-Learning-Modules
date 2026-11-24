# Modul 10 — Fungsi Lanjutan

Modul ini memperluas fungsi sebagai nilai: lambda, higher-order function, closure, decorator, fungsi parsial, callable object, dan rekursi pada struktur bersarang. Setelah belajar, pembaca dapat memilih bentuk fungsi yang sesuai tanpa menambah abstraksi yang tidak diperlukan. Semua program memakai Python 3.10+ dan standard library. Jalankan setiap perintah dari folder modul ini. Screenshot jendela log eksekusi ditautkan per submodul.

## Daftar materi

1. [Lambda function](129_lambda_function.py)
2. [Higher-order functions](130_higher_order_functions.py)
3. [Fungsi map()](131_map_function.py)
4. [Fungsi filter()](132_filter_function.py)
5. [Fungsi reduce()](133_reduce_function.py)
6. [Pengurutan dengan key](134_sorted_key_function.py)
7. [Closure](135_closure_function.py)
8. [Nested function](136_nested_function.py)
9. [Decorator](137_decorator_basic.py)
10. [Decorator dengan parameter](138_decorator_with_arguments.py)
11. [Multiple decorators](139_multiple_decorators.py)
12. [Function annotations](140_function_annotations.py)
13. [Partial function](141_partial_function.py)
14. [Callable objects](142_callable_objects.py)
15. [Rekursi lanjutan](143_recursion_advanced.py)

### 129. Lambda function
**Tujuan:** Membuat fungsi singkat berbasis ekspresi. **Konsep dan cara kerja:** `lambda` menerima angka dan mengembalikan kuadrat. **Jalankan:** `python 129_lambda_function.py`. **Hasil:** kuadrat 5 adalah 25. **Source code:** [129_lambda_function.py](129_lambda_function.py). **Screenshot:** [Lihat hasil eksekusi](output/129_lambda_function.png).

### 130. Higher-order functions
**Tujuan:** Mengirim fungsi sebagai argumen. **Konsep dan cara kerja:** `terapkan` memanggil `dua_kali` pada setiap data dan membuat list baru. **Jalankan:** `python 130_higher_order_functions.py`. **Hasil:** `[2, 4, 6]`. **Source code:** [130_higher_order_functions.py](130_higher_order_functions.py). **Screenshot:** [Lihat hasil eksekusi](output/130_higher_order_functions.png).

### 131. Fungsi `map()`
**Tujuan:** Memetakan fungsi ke setiap elemen. **Konsep dan cara kerja:** iterator `map` menghitung kuadrat ketika `list` mengonsumsinya. **Jalankan:** `python 131_map_function.py`. **Hasil:** `[1, 4, 9]`. **Source code:** [131_map_function.py](131_map_function.py). **Screenshot:** [Lihat hasil eksekusi](output/131_map_function.png).

### 132. Fungsi `filter()`
**Tujuan:** Memilih data berdasarkan predicate. **Konsep dan cara kerja:** lambda menghasilkan `True` untuk angka genap, lalu `list` mengonsumsi hasil filter. **Jalankan:** `python 132_filter_function.py`. **Hasil:** `[2, 4]`. **Source code:** [132_filter_function.py](132_filter_function.py). **Screenshot:** [Lihat hasil eksekusi](output/132_filter_function.png).

### 133. Fungsi `reduce()`
**Tujuan:** Menggabungkan koleksi menjadi satu hasil. **Konsep dan cara kerja:** akumulator awal 1 dikalikan dengan masing-masing angka memakai `functools.reduce`. **Jalankan:** `python 133_reduce_function.py`. **Hasil:** 24. **Source code:** [133_reduce_function.py](133_reduce_function.py). **Screenshot:** [Lihat hasil eksekusi](output/133_reduce_function.png).

### 134. Pengurutan dengan parameter `key`
**Tujuan:** Menentukan kriteria urut tanpa mengubah objek yang diurutkan. **Konsep dan cara kerja:** `sorted(..., key=len)` membandingkan panjang nama. **Jalankan:** `python 134_sorted_key_function.py`. **Hasil:** Ayu, Budi, Christopher. **Source code:** [134_sorted_key_function.py](134_sorted_key_function.py). **Screenshot:** [Lihat hasil eksekusi](output/134_sorted_key_function.png).

### 135. Closure
**Tujuan:** Mengingat data dari lingkup fungsi pembungkus. **Konsep dan cara kerja:** `buat_pengali(2)` mengembalikan fungsi yang tetap memakai `faktor=2`. **Jalankan:** `python 135_closure_function.py`. **Hasil:** 10. **Source code:** [135_closure_function.py](135_closure_function.py). **Screenshot:** [Lihat hasil eksekusi](output/135_closure_function.png).

### 136. Nested function
**Tujuan:** Membatasi fungsi bantu pada lingkup tempatnya diperlukan. **Konsep dan cara kerja:** `subtotal` membaca harga dan jumlah dari fungsi luar, lalu ongkir 2000 ditambahkan. **Jalankan:** `python 136_nested_function.py`. **Hasil:** tagihan 17000. **Source code:** [136_nested_function.py](136_nested_function.py). **Screenshot:** [Lihat hasil eksekusi](output/136_nested_function.png).

### 137. Decorator
**Tujuan:** Menambah perilaku fungsi tanpa mengubah isinya. **Konsep dan cara kerja:** `@beri_label` membungkus `kuadrat`, sedangkan `wraps` mempertahankan metadata fungsi. **Jalankan:** `python 137_decorator_basic.py`. **Hasil:** `Hasil: 16`. **Source code:** [137_decorator_basic.py](137_decorator_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/137_decorator_basic.png).

### 138. Decorator dengan parameter
**Tujuan:** Memberi konfigurasi pada decorator. **Konsep dan cara kerja:** `ulangi(2)` menghasilkan decorator yang memanggil fungsi target dua kali. **Jalankan:** `python 138_decorator_with_arguments.py`. **Hasil:** `Halo, Ayu` dua kali. **Source code:** [138_decorator_with_arguments.py](138_decorator_with_arguments.py). **Screenshot:** [Lihat hasil eksekusi](output/138_decorator_with_arguments.png).

### 139. Multiple decorators
**Tujuan:** Memahami urutan pembungkus. **Konsep dan cara kerja:** `tambah_satu` diterapkan lebih dulu, kemudian `dua_kali`, sehingga (3+1)×2. **Jalankan:** `python 139_multiple_decorators.py`. **Hasil:** 8. **Source code:** [139_multiple_decorators.py](139_multiple_decorators.py). **Screenshot:** [Lihat hasil eksekusi](output/139_multiple_decorators.png).

### 140. Function annotations
**Tujuan:** Membaca metadata tipe pada fungsi. **Konsep dan cara kerja:** parameter dan hasil `luas` diberi anotasi `float`; `__annotations__` menampilkannya tanpa pemeriksaan runtime otomatis. **Jalankan:** `python 140_function_annotations.py`. **Hasil:** luas 10.0 dan anotasi tipe. **Source code:** [140_function_annotations.py](140_function_annotations.py). **Screenshot:** [Lihat hasil eksekusi](output/140_function_annotations.png).

### 141. Partial function
**Tujuan:** Menetapkan sebagian argumen fungsi. **Konsep dan cara kerja:** `partial` menetapkan eksponen 2 sehingga pemanggil hanya mengirim basis. **Jalankan:** `python 141_partial_function.py`. **Hasil:** kuadrat 5 adalah 25. **Source code:** [141_partial_function.py](141_partial_function.py). **Screenshot:** [Lihat hasil eksekusi](output/141_partial_function.png).

### 142. Callable objects
**Tujuan:** Membuat instance yang dapat dipanggil seperti fungsi. **Konsep dan cara kerja:** `__call__` mengalikan input dengan faktor pada instance `Pengali`. **Jalankan:** `python 142_callable_objects.py`. **Hasil:** 12. **Source code:** [142_callable_objects.py](142_callable_objects.py). **Screenshot:** [Lihat hasil eksekusi](output/142_callable_objects.png).

### 143. Rekursi lanjutan
**Tujuan:** Menelusuri list bersarang dengan kedalaman yang bervariasi. **Konsep dan cara kerja:** fungsi menjumlahkan angka langsung atau memanggil dirinya lagi ketika bertemu sub-list. **Jalankan:** `python 143_recursion_advanced.py`. **Hasil:** 15. **Source code:** [143_recursion_advanced.py](143_recursion_advanced.py). **Screenshot:** [Lihat hasil eksekusi](output/143_recursion_advanced.png).

## Ringkasan

Fungsi dapat disimpan, dikirim, dan dibungkus seperti nilai lain. Closure dan decorator memanfaatkan scope; rekursi cocok untuk struktur bersarang selama kasus berhentinya jelas.