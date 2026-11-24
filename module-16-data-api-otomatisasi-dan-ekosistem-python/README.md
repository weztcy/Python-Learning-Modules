# Modul 16 — Data, API, Otomatisasi, dan Ekosistem Python

Modul ini mengenalkan array numerik, DataFrame, grafik, HTTP, parsing HTML, otomasi berkas, aplikasi web, validasi API, dan ORM. Tujuan: menggunakan pustaka sesuai tugas dan memisahkan pengujian lokal dari layanan jaringan nyata. Gunakan Python 3.10+ dan pasang dependensi dari [`../requirements.txt`](../requirements.txt) di virtual environment. Jalankan perintah dari folder modul ini memakai interpreter virtual environment: pada Windows `..\.venv\Scripts\python.exe` (atau aktifkan environment dan gunakan `python`). Seluruh demo HTTP memakai request yang dipersiapkan, respons lokal, mock, atau test client; tidak ada klaim layanan publik telah dihubungi. Screenshot per submodul menampilkan jendela log eksekusi demo lokal.

## Daftar materi

1. [NumPy arrays](248_numpy_arrays.py)
2. [NumPy operations](249_numpy_operations.py)
3. [pandas DataFrame](250_pandas_dataframe.py)
4. [pandas data cleaning](251_pandas_data_cleaning.py)
5. [pandas groupby](252_pandas_groupby.py)
6. [Matplotlib](253_matplotlib_basic.py)
7. [Data visualization](254_data_visualization.py)
8. [HTTP requests](255_http_requests.py)
9. [REST API client](256_rest_api_client.py)
10. [API JSON processing](257_api_json_processing.py)
11. [Web scraping](258_web_scraping_basic.py)
12. [File automation](259_automation_files.py)
13. [Excel automation](260_automation_excel.py)
14. [Flask](261_flask_basic.py)
15. [FastAPI](262_fastapi_basic.py)
16. [SQLAlchemy](263_sqlalchemy_basic.py)
17. [API validation](264_web_api_validation.py)

### 248. Array menggunakan NumPy
**Tujuan:** Membuat ndarray. **Konsep dan cara kerja:** `np.array` mengubah list menjadi array dengan dtype; dtype bergantung platform. **Jalankan:** `python 248_numpy_arrays.py`. **Hasil:** `[1 2 3]` dan tipe integer. **Source code:** [248_numpy_arrays.py](248_numpy_arrays.py). **Screenshot:** [Lihat hasil eksekusi](output/248_numpy_arrays.png).

### 249. Operasi numerik NumPy
**Tujuan:** Menghitung seluruh elemen sekaligus. **Konsep dan cara kerja:** perkalian array berlaku per elemen; `mean` menghitung rata-rata. **Jalankan:** `python 249_numpy_operations.py`. **Hasil:** `[2 4 6]` dan rata-rata 2.0. **Source code:** [249_numpy_operations.py](249_numpy_operations.py). **Screenshot:** [Lihat hasil eksekusi](output/249_numpy_operations.png).

### 250. DataFrame menggunakan pandas
**Tujuan:** Menyimpan tabel dengan nama kolom. **Konsep dan cara kerja:** dictionary kolom membentuk dua baris; `to_string(index=False)` menghilangkan indeks tampilan. **Jalankan:** `python 250_pandas_dataframe.py`. **Hasil:** tabel Ayu 90 dan Budi 80. **Source code:** [250_pandas_dataframe.py](250_pandas_dataframe.py). **Screenshot:** [Lihat hasil eksekusi](output/250_pandas_dataframe.png).

### 251. Pembersihan data dengan pandas
**Tujuan:** Merapikan teks dan menangani nilai hilang. **Konsep dan cara kerja:** `str.strip` menghapus spasi nama, `fillna(0)` mengisi skor Budi yang kosong. **Jalankan:** `python 251_pandas_data_cleaning.py`. **Hasil:** tabel tiga siswa tanpa spasi pinggir atau nilai kosong. **Source code:** [251_pandas_data_cleaning.py](251_pandas_data_cleaning.py). **Screenshot:** [Lihat hasil eksekusi](output/251_pandas_data_cleaning.png).

### 252. Agregasi data dengan pandas
**Tujuan:** Merangkum nilai per kelompok. **Konsep dan cara kerja:** `groupby("kelas")` memisahkan siswa dan `mean` menghitung rata-rata tiap kelas. **Jalankan:** `python 252_pandas_groupby.py`. **Hasil:** A 85.0, B 70.0. **Source code:** [252_pandas_groupby.py](252_pandas_groupby.py). **Screenshot:** [Lihat hasil eksekusi](output/252_pandas_groupby.png).

### 253. Visualisasi dengan Matplotlib
**Tujuan:** Membuat grafik garis. **Konsep dan cara kerja:** `plot` menggambar data hari dan nilai; backend Agg merender ke memori tanpa menyimpan file pada tahap uji. **Jalankan:** `python 253_matplotlib_basic.py`. **Hasil:** konfirmasi ukuran canvas grafik yang dirender. **Source code:** [253_matplotlib_basic.py](253_matplotlib_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/253_matplotlib_basic.png).

### 254. Grafik dan visualisasi data
**Tujuan:** Membandingkan kategori dengan diagram batang. **Konsep dan cara kerja:** `bar` menggambar tiga kelas; backend Agg merender ke memori lalu figure ditutup. **Jalankan:** `python 254_data_visualization.py`. **Hasil:** konfirmasi ukuran canvas diagram. **Source code:** [254_data_visualization.py](254_data_visualization.py). **Screenshot:** [Lihat hasil eksekusi](output/254_data_visualization.png).

### 255. HTTP request menggunakan `requests`
**Tujuan:** Menyusun metode dan parameter URL. **Konsep dan cara kerja:** `requests.Request(...).prepare()` menyiapkan GET berparameter tanpa mengirimkannya. **Jalankan:** `python 255_http_requests.py`. **Hasil:** metode GET dan URL `https://example.org/api?halaman=1`. **Source code:** [255_http_requests.py](255_http_requests.py). **Screenshot:** [Lihat hasil eksekusi](output/255_http_requests.png).

### 256. Client REST API
**Tujuan:** Memisahkan pemanggilan HTTP dari pengguna client. **Konsep dan cara kerja:** fungsi memanggil `Session.get`, memeriksa status, dan mem-parsing JSON; `Mock` mensimulasikan respons saat demo, bukan panggilan layanan nyata. **Jalankan:** `python 256_rest_api_client.py`. **Hasil:** pengguna Ayu id 1. **Source code:** [256_rest_api_client.py](256_rest_api_client.py). **Screenshot:** [Lihat hasil eksekusi](output/256_rest_api_client.png).

### 257. Pemrosesan respons JSON API
**Tujuan:** Mengambil data dari respons JSON. **Konsep dan cara kerja:** string JSON lokal dibaca oleh `json.loads`, lalu nama dipilih dari list `data`. **Jalankan:** `python 257_api_json_processing.py`. **Hasil:** `['Ayu', 'Budi']`. **Source code:** [257_api_json_processing.py](257_api_json_processing.py). **Screenshot:** [Lihat hasil eksekusi](output/257_api_json_processing.png).

### 258. Web scraping dengan Beautiful Soup
**Tujuan:** Memilih elemen HTML. **Konsep dan cara kerja:** `BeautifulSoup` mem-parsing HTML lokal dan selector `.produk` mengambil teks tiap item; tidak mengunduh halaman web. **Jalankan:** `python 258_web_scraping_basic.py`. **Hasil:** Buku dan Pensil. **Source code:** [258_web_scraping_basic.py](258_web_scraping_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/258_web_scraping_basic.png).

### 259. Otomatisasi file
**Tujuan:** Mengganti nama berkas secara terprogram. **Konsep dan cara kerja:** file teks dibuat di `TemporaryDirectory`, diganti nama dengan `Path.rename`, dan isinya dibaca kembali. **Jalankan:** `python 259_automation_files.py`. **Hasil:** nama `catatan_baru.txt` serta teksnya. **Source code:** [259_automation_files.py](259_automation_files.py). **Screenshot:** [Lihat hasil eksekusi](output/259_automation_files.png).

### 260. Otomatisasi Excel menggunakan openpyxl
**Tujuan:** Membuat dan membaca spreadsheet. **Konsep dan cara kerja:** workbook diisi header serta satu baris, disimpan sebagai XLSX sementara, lalu dibuka kembali. **Jalankan:** `python 260_automation_excel.py`. **Hasil:** dua baris berisi Nama/Nilai dan Ayu/90. **Source code:** [260_automation_excel.py](260_automation_excel.py). **Screenshot:** [Lihat hasil eksekusi](output/260_automation_excel.png).

### 261. Aplikasi web dasar dengan Flask
**Tujuan:** Mendefinisikan route GET. **Konsep dan cara kerja:** dekorator `@app.get` menghubungkan `/` ke fungsi `beranda`; test client memanggil route tanpa port terbuka. **Jalankan:** `python 261_flask_basic.py`. **Hasil:** `GET /: Halo dari Flask!`. **Source code:** [261_flask_basic.py](261_flask_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/261_flask_basic.png).

### 262. API menggunakan FastAPI
**Tujuan:** Mengembalikan JSON dari route dinamis. **Konsep dan cara kerja:** `/halo/{nama}` menerima path parameter; `TestClient` memanggil endpoint secara lokal. **Jalankan:** `python 262_fastapi_basic.py`. **Hasil:** `{'pesan': 'Halo, Ayu!'}`. **Source code:** [262_fastapi_basic.py](262_fastapi_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/262_fastapi_basic.png).

### 263. ORM dengan SQLAlchemy
**Tujuan:** Memetakan class ke tabel. **Konsep dan cara kerja:** model Siswa dibuat di SQLite in-memory, disimpan lewat Session, lalu nama dibaca dengan `select`. **Jalankan:** `python 263_sqlalchemy_basic.py`. **Hasil:** `['Ayu']`. **Source code:** [263_sqlalchemy_basic.py](263_sqlalchemy_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/263_sqlalchemy_basic.png).

### 264. Validasi input API
**Tujuan:** Menolak payload yang melanggar aturan. **Konsep dan cara kerja:** model Pydantic mengharuskan harga positif; test client mengirim satu payload sah dan satu harga nol. **Jalankan:** `python 264_web_api_validation.py`. **Hasil:** payload sah dan HTTP 422 untuk harga nol. **Source code:** [264_web_api_validation.py](264_web_api_validation.py). **Screenshot:** [Lihat hasil eksekusi](output/264_web_api_validation.png).

## Ringkasan

Pustaka ekosistem mempercepat pengolahan data, grafik, file, serta API. Test client dan data lokal memungkinkan verifikasi konsep tanpa mengandalkan layanan publik; koneksi jaringan nyata memerlukan endpoint serta kredensial yang sesuai.