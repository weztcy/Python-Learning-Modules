# Modul 17 — Testing, Debugging, dan Pengelolaan Proyek

Modul ini memperkenalkan debugging, assertion, unittest, pytest, mocking, profiling, virtual environment, pip, struktur proyek, dan alat mutu kode. Tujuannya adalah menguji perilaku serta memahami alat sebelum menggunakannya dalam proyek. Gunakan Python 3.10+; contoh pytest perlu dependensi di [`../requirements.txt`](../requirements.txt). Jalankan dari folder modul ini menggunakan interpreter virtual environment (`..\.venv\Scripts\python.exe` pada Windows, atau aktifkan environment lalu gunakan `python`). Screenshot jendela log eksekusi ditautkan per submodul.

## Daftar materi

1. [Debugging dasar](265_debugging_basic.py)
2. [Assertion](266_assert_statement.py)
3. [unittest](267_unittest_basic.py)
4. [pytest](268_pytest_basic.py)
5. [Mock testing](269_mock_testing.py)
6. [Edge cases](270_test_edge_cases.py)
7. [Profiling](271_code_profiling.py)
8. [Virtual environment](272_virtual_environment.py)
9. [pip](273_pip_package_management.py)
10. [Requirements file](274_requirements_file.py)
11. [Project structure](275_project_structure.py)
12. [Package building](276_package_building.py)
13. [Linting](277_code_linting.py)
14. [Formatting](278_code_formatting.py)
15. [Static type checking](279_static_type_checking.py)
16. [Environment variables](280_environment_variables.py)

### 265. Debugging dasar
**Tujuan:** Melihat nilai antara dalam proses hitung. **Konsep dan cara kerja:** pesan DEBUG menampilkan harga dan jumlah sebelum perkalian. **Jalankan:** `python 265_debugging_basic.py`. **Hasil:** nilai input dan total 15000. **Source code:** [265_debugging_basic.py](265_debugging_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/265_debugging_basic.png).

### 266. Assertion
**Tujuan:** Menyatakan asumsi saat pengembangan. **Konsep dan cara kerja:** dua `assert` memeriksa hasil kuadrat dan program mencetak sukses hanya jika keduanya lolos; assertion dapat dimatikan dengan opsi optimasi Python. **Jalankan:** `python 266_assert_statement.py`. **Hasil:** dua assertion berhasil. **Source code:** [266_assert_statement.py](266_assert_statement.py). **Screenshot:** [Lihat hasil eksekusi](output/266_assert_statement.png).

### 267. Unit testing menggunakan `unittest`
**Tujuan:** Mengelompokkan test kasus positif dan negatif. **Konsep dan cara kerja:** subclass `TestCase` memverifikasi hasil `tambah`, runner menampilkan status dan exit code. **Jalankan:** `python 267_unittest_basic.py`. **Hasil:** dua test OK. **Source code:** [267_unittest_basic.py](267_unittest_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/267_unittest_basic.png).

### 268. Pengujian menggunakan pytest
**Tujuan:** Menjalankan fungsi test berbasis `assert`. **Konsep dan cara kerja:** pytest menemukan `test_perkalian` dan melaporkan satu test lulus; cache provider dimatikan agar tidak membuat file. **Jalankan:** `python 268_pytest_basic.py` (atau `python -m pytest 268_pytest_basic.py -q -p no:cacheprovider`). **Hasil:** 1 passed. **Source code:** [268_pytest_basic.py](268_pytest_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/268_pytest_basic.png).

### 269. Mocking dalam pengujian
**Tujuan:** Mengisolasi sumber data dari perhitungan. **Konsep dan cara kerja:** `Mock` memberi harga tetap 5000; `assert_called_once_with` memastikan argumen pemanggilan. **Jalankan:** `python 269_mock_testing.py`. **Hasil:** mock berhasil diverifikasi. **Source code:** [269_mock_testing.py](269_mock_testing.py). **Screenshot:** [Lihat hasil eksekusi](output/269_mock_testing.png).

### 270. Pengujian kasus batas
**Tujuan:** Memeriksa input tunggal dan kosong. **Konsep dan cara kerja:** rata-rata satu nilai dihitung, sedangkan list kosong mengangkat `ValueError` agar tidak terjadi pembagian nol. **Jalankan:** `python 270_test_edge_cases.py`. **Hasil:** pesan kasus kosong. **Source code:** [270_test_edge_cases.py](270_test_edge_cases.py). **Screenshot:** [Lihat hasil eksekusi](output/270_test_edge_cases.png).

### 271. Profiling program
**Tujuan:** Melihat waktu dan jumlah pemanggilan fungsi. **Konsep dan cara kerja:** `cProfile` menjalankan pekerjaan lalu `pstats` merangkum fungsi teratas. **Jalankan:** `python 271_code_profiling.py`. **Hasil:** 332833500 dan statistik dengan waktu berbeda menurut komputer. **Source code:** [271_code_profiling.py](271_code_profiling.py). **Screenshot:** [Lihat hasil eksekusi](output/271_code_profiling.png).

### 272. Virtual environment
**Tujuan:** Mengetahui apakah interpreter berjalan dalam venv. **Konsep dan cara kerja:** `sys.prefix` dibandingkan dengan `sys.base_prefix`; skrip hanya menampilkan contoh perintah pembuatan environment. **Jalankan:** `python 272_virtual_environment.py`. **Hasil:** `True` jika venv aktif dan petunjuk `python -m venv .venv`. **Source code:** [272_virtual_environment.py](272_virtual_environment.py). **Screenshot:** [Lihat hasil eksekusi](output/272_virtual_environment.png).

### 273. Pengelolaan paket dengan pip
**Tujuan:** Memanggil pip dari interpreter yang tepat. **Konsep dan cara kerja:** subprocess menjalankan `sys.executable -m pip --version` tanpa memasang paket. **Jalankan:** `python 273_pip_package_management.py`. **Hasil:** versi/path pip aktif dan contoh perintah instalasi. **Source code:** [273_pip_package_management.py](273_pip_package_management.py). **Screenshot:** [Lihat hasil eksekusi](output/273_pip_package_management.png).

### 274. Penggunaan requirements file
**Tujuan:** Membaca deklarasi dependensi. **Konsep dan cara kerja:** skrip membaca [`../requirements.txt`](../requirements.txt) dari root dan menghitung paket langsung, tanpa memasang apa pun. **Jalankan:** `python 274_requirements_file.py`. **Hasil:** jumlah dependensi serta contoh nama paket. **Source code:** [274_requirements_file.py](274_requirements_file.py). **Screenshot:** [Lihat hasil eksekusi](output/274_requirements_file.png).

### 275. Struktur proyek Python
**Tujuan:** Menemukan file root terlepas dari lokasi terminal. **Konsep dan cara kerja:** `Path(__file__)` mengarah ke root repository dan memeriksa keberadaan kurikulum serta README. **Jalankan:** `python 275_project_structure.py`. **Hasil:** dua pemeriksaan `True`. **Source code:** [275_project_structure.py](275_project_structure.py). **Screenshot:** [Lihat hasil eksekusi](output/275_project_structure.png).

### 276. Pembuatan paket Python
**Tujuan:** Mengenali struktur folder paket dan arsipnya. **Konsep dan cara kerja:** `ZipFile` menaruh `__init__.py` dalam arsip sementara; ini demonstrasi struktur, **bukan** wheel yang dapat dipasang pip. **Jalankan:** `python 276_package_building.py`. **Hasil:** nama berkas paket dalam arsip. **Source code:** [276_package_building.py](276_package_building.py). **Screenshot:** [Lihat hasil eksekusi](output/276_package_building.png).

### 277. Linting kode
**Tujuan:** Memahami satu tahap pemeriksaan source. **Konsep dan cara kerja:** `ast.parse` memastikan skrip ini valid secara sintaks; ini **bukan** linter penuh yang memeriksa gaya atau kualitas. **Jalankan:** `python 277_code_linting.py`. **Hasil:** sintaks valid dan pengingat batasannya. **Source code:** [277_code_linting.py](277_code_linting.py). **Screenshot:** [Lihat hasil eksekusi](output/277_code_linting.png).

### 278. Pemformatan kode
**Tujuan:** Melihat penataan lebar baris sebagai ilustrasi. **Konsep dan cara kerja:** `textwrap.fill` membungkus kalimat pada lebar 40; ini **bukan** formatter source Python. **Jalankan:** `python 278_code_formatting.py`. **Hasil:** teks dalam beberapa baris. **Source code:** [278_code_formatting.py](278_code_formatting.py). **Screenshot:** [Lihat hasil eksekusi](output/278_code_formatting.png).

### 279. Pemeriksaan tipe statis
**Tujuan:** Membedakan metadata anotasi dan analisis statis. **Konsep dan cara kerja:** `get_type_hints` membaca anotasi fungsi, tetapi tidak membuktikan kebenaran tipe program; pemeriksaan nyata perlu alat terpisah. **Jalankan:** `python 279_static_type_checking.py`. **Hasil:** anotasi `int` dan penjelasan batasannya. **Source code:** [279_static_type_checking.py](279_static_type_checking.py). **Screenshot:** [Lihat hasil eksekusi](output/279_static_type_checking.png).

### 280. Environment variables
**Tujuan:** Mengambil konfigurasi tanpa menaruh nilai sensitif dalam source. **Konsep dan cara kerja:** `os.getenv` membaca `MODE_APLIKASI`, dengan default pengembangan. **Jalankan:** `python 280_environment_variables.py`. **Hasil:** mode yang diatur atau `pengembangan`. **Source code:** [280_environment_variables.py](280_environment_variables.py). **Screenshot:** [Lihat hasil eksekusi](output/280_environment_variables.png).

## Ringkasan

Test menguji perilaku; mock mengisolasi dependensi dan profiler mengukur pekerjaan. Demo pengenalan alat lint/format/type-check dan packaging menjelaskan konsep serta batasnya, bukan menggantikan tool khusus untuk produksi.