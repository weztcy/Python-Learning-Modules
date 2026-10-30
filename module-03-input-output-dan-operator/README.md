# Modul 3 — Input, Output, dan Operator

Modul ini membahas pembacaan input, validasi sederhana, operator Python, serta pemformatan keluaran. Tujuannya adalah mengolah data yang diberikan pengguna dan memilih operator yang tepat. Gunakan Python 3.10+; tidak ada dependensi tambahan.

## Daftar materi

1. [Input menggunakan input()](25_input_function.py)
2. [Input numerik](26_numeric_input.py)
3. [Validasi input](27_input_validation.py)
4. [Operator aritmetika](28_arithmetic_operators.py)
5. [Operator penugasan](29_assignment_operators.py)
6. [Operator perbandingan](30_comparison_operators.py)
7. [Operator logika](31_logical_operators.py)
8. [Operator identitas](32_identity_operators.py)
9. [Operator keanggotaan](33_membership_operators.py)
10. [Operator bitwise](34_bitwise_operators.py)
11. [Prioritas operator](35_operator_precedence.py)
12. [F-string](36_f_string_formatting.py)
13. [Format angka](37_format_numbers.py)
14. [Input beberapa nilai](38_multiple_input_values.py)

Jalankan perintah di bawah dari folder modul ini. Untuk contoh interaktif, ketik nilai saat diminta lalu tekan Enter. Screenshot per submodul menampilkan masukan demo dan keluaran program pada jendela log eksekusi.

### 25. Input menggunakan `input()`
**Tujuan dan konsep:** Membaca teks dari terminal. **Cara kerja:** `input` mengembalikan nama sebagai string, lalu `print` menampilkan sapaan. **Jalankan:** `python 25_input_function.py`; ketik `Ayu`. **Hasil:** `Halo, Ayu`. **Source code:** [25_input_function.py](25_input_function.py). **Screenshot:** [Lihat hasil eksekusi](output/25_input_function.png).

### 26. Input numerik
**Tujuan dan konsep:** Mengubah input teks menjadi integer. **Cara kerja:** dua masukan dikonversi dengan `int` sebelum dijumlahkan; input bukan bilangan bulat menimbulkan `ValueError`. **Jalankan:** `python 26_numeric_input.py`; ketik `3` lalu `4`. **Hasil:** jumlah 7. **Source code:** [26_numeric_input.py](26_numeric_input.py). **Screenshot:** [Lihat hasil eksekusi](output/26_numeric_input.png).

### 27. Validasi input
**Tujuan dan konsep:** Meminta ulang input sampai bilangan bulat positif diperoleh. **Cara kerja:** `try-except` menangani konversi yang gagal; loop mengulang untuk nol atau nilai negatif. **Jalankan:** `python 27_input_validation.py`; ketik `-1` lalu `5`. **Hasil:** pesan penolakan dan `Input valid: 5`. **Source code:** [27_input_validation.py](27_input_validation.py). **Screenshot:** [Lihat hasil eksekusi](output/27_input_validation.png).

### 28. Operator aritmetika
**Tujuan dan konsep:** Menghitung jumlah, selisih, produk, hasil bagi, sisa, dan pangkat. **Cara kerja:** operasi pada 13 dan 5 memperlihatkan perbedaan `/`, `//`, dan `%`. **Jalankan:** `python 28_arithmetic_operators.py`. **Hasil:** antara lain bagi 2.6, bagi bulat 2, sisa 3. **Source code:** [28_arithmetic_operators.py](28_arithmetic_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/28_arithmetic_operators.png).

### 29. Operator penugasan
**Tujuan dan konsep:** Memperbarui variabel dengan operator gabungan. **Cara kerja:** `+=`, `*=`, dan `-=` diterapkan berurutan ke skor. **Jalankan:** `python 29_assignment_operators.py`. **Hasil:** skor 15, 30, lalu 26. **Source code:** [29_assignment_operators.py](29_assignment_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/29_assignment_operators.png).

### 30. Operator perbandingan
**Tujuan dan konsep:** Membandingkan dua nilai menjadi `bool`. **Cara kerja:** enam operator membandingkan 4 dan 7. **Jalankan:** `python 30_comparison_operators.py`. **Hasil:** hasil `True`/`False` untuk sama, tidak sama, dan batas urutan. **Source code:** [30_comparison_operators.py](30_comparison_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/30_comparison_operators.png).

### 31. Operator logika
**Tujuan dan konsep:** Menggabungkan atau membalik syarat. **Cara kerja:** `and`, `or`, dan `not` dipakai pada usia dan kepemilikan tiket. **Jalankan:** `python 31_logical_operators.py`. **Hasil:** boleh masuk `True`, akses khusus `False`, tidak punya tiket `False`. **Source code:** [31_logical_operators.py](31_logical_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/31_logical_operators.png).

### 32. Operator identitas
**Tujuan dan konsep:** Membedakan kesamaan isi dari objek yang sama. **Cara kerja:** alias merujuk list asli, salinan berisi data sama tetapi memiliki identitas berbeda. **Jalankan:** `python 32_identity_operators.py`. **Hasil:** `==` bernilai `True`, `is alias` `True`, `is salinan` `False`. **Source code:** [32_identity_operators.py](32_identity_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/32_identity_operators.png).

### 33. Operator keanggotaan
**Tujuan dan konsep:** Menguji ada atau tidaknya elemen dalam koleksi. **Cara kerja:** `in` mencari biru dan `not in` memeriksa ketiadaan kuning. **Jalankan:** `python 33_membership_operators.py`. **Hasil:** kedua pemeriksaan `True`. **Source code:** [33_membership_operators.py](33_membership_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/33_membership_operators.png).

### 34. Operator bitwise
**Tujuan dan konsep:** Mengoperasikan bit bilangan bulat. **Cara kerja:** AND, OR, XOR, dan pergeseran diterapkan pada `0b1100` dan `0b1010`, lalu ditampilkan sebagai biner. **Jalankan:** `python 34_bitwise_operators.py`. **Hasil:** antara lain AND `0b1000`, OR `0b1110`. **Source code:** [34_bitwise_operators.py](34_bitwise_operators.py). **Screenshot:** [Lihat hasil eksekusi](output/34_bitwise_operators.png).

### 35. Prioritas operator
**Tujuan dan konsep:** Memahami urutan operasi. **Cara kerja:** ekspresi tanpa kurung menghitung perkalian terlebih dahulu; kurung mendahulukan penjumlahan. **Jalankan:** `python 35_operator_precedence.py`. **Hasil:** 14 dan 20. **Source code:** [35_operator_precedence.py](35_operator_precedence.py). **Screenshot:** [Lihat hasil eksekusi](output/35_operator_precedence.png).

### 36. F-string
**Tujuan dan konsep:** Menyisipkan nilai serta ekspresi dalam string. **Cara kerja:** bagian `{...}` diganti hasil evaluasi nama, skor, dan bonus. **Jalankan:** `python 36_f_string_formatting.py`. **Hasil:** Sari memperoleh 87 poin; nilai bonus 92. **Source code:** [36_f_string_formatting.py](36_f_string_formatting.py). **Screenshot:** [Lihat hasil eksekusi](output/36_f_string_formatting.png).

### 37. Format angka
**Tujuan dan konsep:** Mengatur angka desimal, ribuan, dan persen. **Cara kerja:** format `:,.2f` dipakai untuk harga dan `:.1%` untuk rasio. **Jalankan:** `python 37_format_numbers.py`. **Hasil:** `12,345.68` dan `87.5%`. **Source code:** [37_format_numbers.py](37_format_numbers.py). **Screenshot:** [Lihat hasil eksekusi](output/37_format_numbers.png).

### 38. Input beberapa nilai
**Tujuan dan konsep:** Memecah satu baris input menjadi dua integer. **Cara kerja:** `split` memisahkan pada spasi, `map(int, ...)` mengonversi, dan unpacking mengharuskan tepat dua nilai. **Jalankan:** `python 38_multiple_input_values.py`; ketik `2 3`. **Hasil:** jumlah 5; masukan salah menghasilkan pesan validasi. **Source code:** [38_multiple_input_values.py](38_multiple_input_values.py). **Screenshot:** [Lihat hasil eksekusi](output/38_multiple_input_values.png).

## Ringkasan

Input pada awalnya berupa teks; program dapat memvalidasi serta mengonversinya sebelum memakai operator untuk menghitung, membandingkan, dan memformat hasil.