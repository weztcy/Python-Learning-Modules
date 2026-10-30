# Modul 12 — Exception, File Handling, dan Modul

Modul ini mengajarkan penanganan exception, pengelolaan file teks dan format data, serta pemisahan kode ke modul dan package. Tujuan: menjaga program tetap terarah saat input gagal dan menggunakan ulang kode tanpa menyalin implementasi. Gunakan Python 3.10+ dan standard library; semua perintah dijalankan dari folder ini. File sementara pada contoh penulisan dihapus otomatis. Screenshot jendela log eksekusi tersedia di tiap submodul.

## Daftar materi

1. [try-except](168_try_except.py)
2. [Multiple exception handling](169_multiple_exceptions.py)
3. [else dan finally](170_else_finally.py)
4. [Pernyataan raise](171_raise_exception.py)
5. [Custom exception](172_custom_exceptions.py)
6. [Exception chaining](173_exception_chaining.py)
7. [Membaca file](174_file_reading.py)
8. [Menulis file](175_file_writing.py)
9. [Menambahkan data ke file](176_file_append.py)
10. [Membaca file per baris](177_read_file_lines.py)
11. [Context manager with](178_with_statement.py)
12. [Pathlib](179_pathlib_basic.py)
13. [JSON](180_json_read_write.py)
14. [CSV](181_csv_read_write.py)
15. [Pickle](182_pickle_basic.py)
16. [Import module](183_import_modules.py)
17. [Membuat modul sendiri](184_create_module.py)
18. [Membuat package](185_create_package.py)
19. [Main guard](186_main_guard.py)
20. [Relative imports](187_relative_imports.py)

### 168. `try-except`
**Tujuan:** Menangani konversi yang gagal. **Konsep dan cara kerja:** `int` pada teks nonangka memunculkan `ValueError`, lalu `except` mencetak jenisnya. **Jalankan:** `python 168_try_except.py`. **Hasil:** konversi gagal (`ValueError`). **Source code:** [168_try_except.py](168_try_except.py). **Screenshot:** [Lihat hasil eksekusi](output/168_try_except.png).

### 169. Multiple exception handling
**Tujuan:** Membedakan kesalahan input dan pembagian. **Konsep dan cara kerja:** fungsi menangkap `ValueError` dan `ZeroDivisionError` melalui cabang berbeda. **Jalankan:** `python 169_multiple_exceptions.py`. **Hasil:** pesan bukan bilangan dan pembagi nol. **Source code:** [169_multiple_exceptions.py](169_multiple_exceptions.py). **Screenshot:** [Lihat hasil eksekusi](output/169_multiple_exceptions.png).

### 170. `else` dan `finally`
**Tujuan:** Mengetahui alur berhasil dan penyelesaian operasi. **Konsep dan cara kerja:** `else` mencetak hasil jika tidak ada exception; `finally` selalu mencetak penutup. **Jalankan:** `python 170_else_finally.py`. **Hasil:** 4.0 dan pesan selesai. **Source code:** [170_else_finally.py](170_else_finally.py). **Screenshot:** [Lihat hasil eksekusi](output/170_else_finally.png).

### 171. Pernyataan `raise`
**Tujuan:** Menolak data tidak valid secara eksplisit. **Konsep dan cara kerja:** fungsi mengangkat `ValueError` untuk usia negatif; pemanggil menangkap pesannya. **Jalankan:** `python 171_raise_exception.py`. **Hasil:** `Usia tidak boleh negatif`. **Source code:** [171_raise_exception.py](171_raise_exception.py). **Screenshot:** [Lihat hasil eksekusi](output/171_raise_exception.png).

### 172. Custom exception
**Tujuan:** Menamai kegagalan spesifik domain. **Konsep dan cara kerja:** subclass `Exception` menyatakan saldo tidak cukup saat jumlah penarikan melebihi saldo. **Jalankan:** `python 172_custom_exceptions.py`. **Hasil:** `Saldo tidak cukup`. **Source code:** [172_custom_exceptions.py](172_custom_exceptions.py). **Screenshot:** [Lihat hasil eksekusi](output/172_custom_exceptions.png).

### 173. Exception chaining
**Tujuan:** Menyimpan penyebab kegagalan saat menambahkan konteks. **Konsep dan cara kerja:** `raise ... from` membuat `ValueError` baru dengan `__cause__` yang menunjuk kegagalan konversi. **Jalankan:** `python 173_exception_chaining.py`. **Hasil:** pesan input dan penyebab `ValueError`. **Source code:** [173_exception_chaining.py](173_exception_chaining.py). **Screenshot:** [Lihat hasil eksekusi](output/173_exception_chaining.png).

### 174. Membaca file
**Tujuan:** Mengambil isi file teks. **Konsep dan cara kerja:** path dihitung dari lokasi skrip; `with` membuka [contoh_data.txt](contoh_data.txt) dengan UTF-8. **Jalankan:** `python 174_file_reading.py`. **Hasil:** dua baris teks contoh. **Source code:** [174_file_reading.py](174_file_reading.py). **Screenshot:** [Lihat hasil eksekusi](output/174_file_reading.png).

### 175. Menulis file
**Tujuan:** Menyimpan teks dan membacanya kembali. **Konsep dan cara kerja:** `write_text` membuat file pada `TemporaryDirectory`, lalu `read_text` memverifikasi isi sebelum folder dihapus. **Jalankan:** `python 175_file_writing.py`. **Hasil:** `Belajar Python`. **Source code:** [175_file_writing.py](175_file_writing.py). **Screenshot:** [Lihat hasil eksekusi](output/175_file_writing.png).

### 176. Menambahkan data ke file
**Tujuan:** Menambah tanpa menimpa isi awal. **Konsep dan cara kerja:** mode `a` menambahkan baris kedua ke file sementara. **Jalankan:** `python 176_file_append.py`. **Hasil:** dua baris berurutan. **Source code:** [176_file_append.py](176_file_append.py). **Screenshot:** [Lihat hasil eksekusi](output/176_file_append.png).

### 177. Membaca file per baris
**Tujuan:** Mengiterasi file teks. **Konsep dan cara kerja:** loop membaca [contoh_data.txt](contoh_data.txt) baris demi baris, `enumerate` memberi nomor. **Jalankan:** `python 177_read_file_lines.py`. **Hasil:** dua baris bernomor. **Source code:** [177_read_file_lines.py](177_read_file_lines.py). **Screenshot:** [Lihat hasil eksekusi](output/177_read_file_lines.png).

### 178. Context manager dengan `with`
**Tujuan:** Menutup file secara otomatis. **Konsep dan cara kerja:** `with` membuka [contoh_data.txt](contoh_data.txt), `readline` membaca satu baris dan file ditutup setelah blok. **Jalankan:** `python 178_with_statement.py`. **Hasil:** baris pertama `Belajar Python`. **Source code:** [178_with_statement.py](178_with_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/178_with_statement.png).

### 179. Pengelolaan path dengan `pathlib`
**Tujuan:** Mengambil bagian-bagian path secara lintas platform. **Konsep dan cara kerja:** `with_name` menemukan [contoh_data.txt](contoh_data.txt); `.name`, `.suffix`, dan `.is_file()` memeriksa path. **Jalankan:** `python 179_pathlib_basic.py`. **Hasil:** nama, ekstensi `.txt`, keberadaan `True`. **Source code:** [179_pathlib_basic.py](179_pathlib_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/179_pathlib_basic.png).

### 180. Membaca dan menulis JSON
**Tujuan:** Menyimpan struktur data dalam format pertukaran teks. **Konsep dan cara kerja:** `json.dumps` menulis dictionary pada file sementara; `json.loads` membacanya kembali. **Jalankan:** `python 180_json_read_write.py`. **Hasil:** dictionary Ayu dengan nilai 90. **Source code:** [180_json_read_write.py](180_json_read_write.py). **Screenshot:** [Lihat hasil eksekusi](output/180_json_read_write.png).

### 181. Membaca dan menulis CSV
**Tujuan:** Menangani data tabular sederhana. **Konsep dan cara kerja:** `csv.writer` membuat header serta satu baris; `csv.reader` mengembalikan setiap kolom sebagai teks. **Jalankan:** `python 181_csv_read_write.py`. **Hasil:** dua list, header dan data Ayu. **Source code:** [181_csv_read_write.py](181_csv_read_write.py). **Screenshot:** [Lihat hasil eksekusi](output/181_csv_read_write.png).

### 182. Serialisasi dengan `pickle`
**Tujuan:** Mengubah objek Python ke byte dan kembali. **Konsep dan cara kerja:** `dumps`/`loads` bekerja pada dictionary lokal; jangan pernah memuat pickle dari sumber yang tidak tepercaya karena dapat menjalankan kode. **Jalankan:** `python 182_pickle_basic.py`. **Hasil:** data Ayu dipulihkan. **Source code:** [182_pickle_basic.py](182_pickle_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/182_pickle_basic.png).

### 183. Import module
**Tujuan:** Menggunakan standard library. **Konsep dan cara kerja:** `math.sqrt` menghitung akar dan `math.ceil` membulatkan ke atas. **Jalankan:** `python 183_import_modules.py`. **Hasil:** 9.0 dan 3. **Source code:** [183_import_modules.py](183_import_modules.py). **Screenshot:** [Lihat hasil eksekusi](output/183_import_modules.png).

### 184. Membuat modul sendiri
**Tujuan:** Memanggil fungsi dari file lain. **Konsep dan cara kerja:** file utama meng-import [pembantu_belajar.py](pembantu_belajar.py) dalam folder sama dan memanggil `sapa`. **Jalankan:** `python 184_create_module.py`. **Hasil:** sapaan untuk Ayu. **Source code:** [184_create_module.py](184_create_module.py). **Screenshot:** [Lihat hasil eksekusi](output/184_create_module.png).

### 185. Membuat package
**Tujuan:** Mengorganisasi modul dalam package. **Konsep dan cara kerja:** [paket_belajar/__init__.py](paket_belajar/__init__.py) mengekspos `sapa` dari [paket_belajar/pesan.py](paket_belajar/pesan.py). **Jalankan:** `python 185_create_package.py`. **Hasil:** `Halo, Budi!`. **Source code:** [185_create_package.py](185_create_package.py). **Screenshot:** [Lihat hasil eksekusi](output/185_create_package.png).

### 186. Penggunaan `if __name__ == "__main__"`
**Tujuan:** Memisahkan eksekusi skrip dari import. **Konsep dan cara kerja:** `sapa` dapat di-import tanpa mencetak; blok main hanya berjalan ketika file dieksekusi langsung. **Jalankan:** `python 186_main_guard.py`. **Hasil:** `Skrip berjalan langsung`. **Source code:** [186_main_guard.py](186_main_guard.py). **Screenshot:** [Lihat hasil eksekusi](output/186_main_guard.png).

### 187. Relative imports
**Tujuan:** Memanggil modul saudara dalam package. **Konsep dan cara kerja:** [paket_belajar/contoh_relatif.py](paket_belajar/contoh_relatif.py) memakai `from .pesan import sapa`; skrip utama meng-import anggota package tersebut. **Jalankan:** `python 187_relative_imports.py`. **Hasil:** `Halo, Dina!`. **Source code:** [187_relative_imports.py](187_relative_imports.py). **Screenshot:** [Lihat hasil eksekusi](output/187_relative_imports.png).

## Ringkasan

Exception memisahkan jalur berhasil dan gagal. Context manager menjaga file tertutup, sedangkan modul dan package membantu menggunakan kembali kode secara terorganisasi.