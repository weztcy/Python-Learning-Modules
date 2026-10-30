# Modul 18 — Proyek Praktik Python

Modul ini menggabungkan konsep dasar hingga pustaka ekosistem ke dalam 20 proyek kecil yang terpisah. Tujuannya membangun, menjalankan, dan menguji alur inti tanpa menuntut layanan publik atau akses data pribadi. Gunakan Python 3.10+; proyek Excel, API, scraper, serta dashboard memerlukan dependensi pada [`../requirements.txt`](../requirements.txt). Jalankan dari folder ini dengan interpreter virtual environment (`..\.venv\Scripts\python.exe` di Windows, atau aktifkan environment lalu gunakan `python`). Proyek yang menyimpan data hanya menggunakan memori atau direktori sementara kecuali Anda mengadaptasinya sendiri. Screenshot jendela log eksekusi tersedia untuk setiap demo proyek.

## Daftar proyek

1. [Kalkulator konsol](281_calculator_project.py)
2. [Permainan tebak angka](282_number_guessing_project.py)
3. [Aplikasi kuis](283_quiz_application.py)
4. [Sistem nilai mahasiswa](284_student_grade_project.py)
5. [Database mahasiswa](285_student_database_project.py)
6. [Sistem inventaris barang](286_inventory_management_project.py)
7. [Sistem kasir](287_cashier_system_project.py)
8. [Pencatatan pengeluaran](288_expense_tracker_project.py)
9. [Sistem perpustakaan](289_library_management_project.py)
10. [Sistem data pegawai](290_employee_management_project.py)
11. [Buku kontak](291_contact_book_project.py)
12. [Generator kata sandi](292_password_generator_project.py)
13. [Pengorganisasian file](293_file_organizer_project.py)
14. [Analisis CSV](294_csv_data_analyzer_project.py)
15. [Laporan Excel](295_excel_report_project.py)
16. [Cuaca berbasis API](296_weather_api_project.py)
17. [Web scraper](297_web_scraper_project.py)
18. [REST API](298_rest_api_project.py)
19. [Dashboard data](299_data_dashboard_project.py)
20. [Manajemen tugas](300_task_management_project.py)

### 281. Kalkulator konsol
**Tujuan:** Menghitung berdasarkan operator masukan. **Konsep dan cara kerja:** fungsi memetakan `+`, `-`, `*`, `/` ke operasi dan menolak pembagian nol; argumen CLI opsional memudahkan demo. **Jalankan:** `python 281_calculator_project.py 8 / 2`. **Hasil:** 4.0. **Source code:** [281_calculator_project.py](281_calculator_project.py). **Screenshot:** [Lihat hasil eksekusi](output/281_calculator_project.png).

### 282. Permainan tebak angka
**Tujuan:** Membandingkan satu tebakan dengan angka acak. **Konsep dan cara kerja:** `randint` memilih rahasia 1–10; fungsi memberi petunjuk atau jawaban tepat. Ini demo satu giliran, bukan loop permainan lengkap. **Jalankan:** `python 282_number_guessing_project.py 5`. **Hasil:** petunjuk serta jawaban yang berubah tiap run. **Source code:** [282_number_guessing_project.py](282_number_guessing_project.py). **Screenshot:** [Lihat hasil eksekusi](output/282_number_guessing_project.png).

### 283. Aplikasi kuis
**Tujuan:** Menilai respons terhadap beberapa pertanyaan. **Konsep dan cara kerja:** jawaban dinormalisasi dan dibandingkan dengan kunci, jumlah respons divalidasi; demo menggunakan dua jawaban tetap. **Jalankan:** `python 283_quiz_application.py`. **Hasil:** skor 2/2. **Source code:** [283_quiz_application.py](283_quiz_application.py). **Screenshot:** [Lihat hasil eksekusi](output/283_quiz_application.png).

### 284. Sistem nilai mahasiswa
**Tujuan:** Membuat rapor dari daftar skor. **Konsep dan cara kerja:** nilai 0–100 divalidasi, rata-rata dihitung, kelulusan ditentukan dari batas 75. **Jalankan:** `python 284_student_grade_project.py`. **Hasil:** rapor Ayu, rata-rata 85, lulus. **Source code:** [284_student_grade_project.py](284_student_grade_project.py). **Screenshot:** [Lihat hasil eksekusi](output/284_student_grade_project.png).

### 285. Database mahasiswa
**Tujuan:** Menyimpan data dengan SQL berparameter. **Konsep dan cara kerja:** tabel SQLite `:memory:` dibuat dan diisi dua siswa lalu dibaca; database hilang setelah proses berhenti. **Jalankan:** `python 285_student_database_project.py`. **Hasil:** Ayu dan Budi. **Source code:** [285_student_database_project.py](285_student_database_project.py). **Screenshot:** [Lihat hasil eksekusi](output/285_student_database_project.png).

### 286. Sistem inventaris barang
**Tujuan:** Menambah dan mengurangi jumlah stok. **Konsep dan cara kerja:** dictionary barang menyimpan jumlah; penambahan harus positif dan pengambilan tidak boleh melewati stok. **Jalankan:** `python 286_inventory_management_project.py`. **Hasil:** stok Buku 7. **Source code:** [286_inventory_management_project.py](286_inventory_management_project.py). **Screenshot:** [Lihat hasil eksekusi](output/286_inventory_management_project.png).

### 287. Sistem kasir
**Tujuan:** Menghitung total keranjang dengan harga integer. **Konsep dan cara kerja:** tiap baris harga×jumlah dijumlahkan dan item tidak valid ditolak. **Jalankan:** `python 287_cashier_system_project.py`. **Hasil:** total 26000. **Source code:** [287_cashier_system_project.py](287_cashier_system_project.py). **Screenshot:** [Lihat hasil eksekusi](output/287_cashier_system_project.png).

### 288. Pencatatan pengeluaran
**Tujuan:** Menyimpan transaksi dan menghitung total. **Konsep dan cara kerja:** class menambah pasangan kategori/jumlah positif ke list lalu menjumlahkannya; data hanya dalam memori. **Jalankan:** `python 288_expense_tracker_project.py`. **Hasil:** 35000. **Source code:** [288_expense_tracker_project.py](288_expense_tracker_project.py). **Screenshot:** [Lihat hasil eksekusi](output/288_expense_tracker_project.png).

### 289. Sistem perpustakaan
**Tujuan:** Melacak ketersediaan pinjam/kembali. **Konsep dan cara kerja:** dua set memisahkan buku tersedia dan dipinjam; transisi yang salah memunculkan `ValueError`. **Jalankan:** `python 289_library_management_project.py`. **Hasil:** Python sempat dipinjam, lalu kembali tersedia. **Source code:** [289_library_management_project.py](289_library_management_project.py). **Screenshot:** [Lihat hasil eksekusi](output/289_library_management_project.png).

### 290. Sistem data pegawai
**Tujuan:** Menambah pegawai berdasarkan nomor unik. **Konsep dan cara kerja:** dictionary memetakan nomor ke nama/gaji; duplikat dan gaji negatif ditolak. **Jalankan:** `python 290_employee_management_project.py`. **Hasil:** pegawai Ayu dengan gaji 5000000. **Source code:** [290_employee_management_project.py](290_employee_management_project.py). **Screenshot:** [Lihat hasil eksekusi](output/290_employee_management_project.png).

### 291. Buku kontak
**Tujuan:** Menyimpan dan mencari nomor. **Konsep dan cara kerja:** nama adalah kunci dictionary, string kosong ditolak; `get` memberi pesan saat tidak ditemukan. **Jalankan:** `python 291_contact_book_project.py`. **Hasil:** nomor Ayu. **Source code:** [291_contact_book_project.py](291_contact_book_project.py). **Screenshot:** [Lihat hasil eksekusi](output/291_contact_book_project.png).

### 292. Generator kata sandi
**Tujuan:** Membuat string acak dengan sumber yang cocok untuk keamanan. **Konsep dan cara kerja:** `secrets.choice` memilih 16 karakter dari huruf, digit, tanda baca; panjang minimal 8, tetapi tidak menjamin aturan semua layanan. **Jalankan:** `python 292_password_generator_project.py`. **Hasil:** kata sandi acak dan panjang 16. **Source code:** [292_password_generator_project.py](292_password_generator_project.py). **Screenshot:** [Lihat hasil eksekusi](output/292_password_generator_project.png).

### 293. Pengorganisasian file otomatis
**Tujuan:** Mengelompokkan file menurut ekstensi. **Konsep dan cara kerja:** dua file dalam direktori sementara dipindah ke subfolder `txt` dan `csv`; file pengguna tidak disentuh. **Jalankan:** `python 293_file_organizer_project.py`. **Hasil:** daftar dua file dan subfolder tujuan. **Source code:** [293_file_organizer_project.py](293_file_organizer_project.py). **Screenshot:** [Lihat hasil eksekusi](output/293_file_organizer_project.png).

### 294. Analisis data CSV
**Tujuan:** Menghitung rata-rata kolom angka dari CSV. **Konsep dan cara kerja:** `DictReader` membaca teks via `StringIO`, data kosong ditolak, skor dikonversi ke float. **Jalankan:** `python 294_csv_data_analyzer_project.py`. **Hasil:** rata-rata 85.0. **Source code:** [294_csv_data_analyzer_project.py](294_csv_data_analyzer_project.py). **Screenshot:** [Lihat hasil eksekusi](output/294_csv_data_analyzer_project.png).

### 295. Pembuatan laporan Excel
**Tujuan:** Membuat workbook dan baris rumus. **Konsep dan cara kerja:** openpyxl menulis file XLSX sementara dengan dua siswa dan formula rata-rata; openpyxl tidak menghitung formula, hanya menyimpannya untuk aplikasi spreadsheet. **Jalankan:** `python 295_excel_report_project.py`. **Hasil:** baris siswa dan rumus AVERAGE. **Source code:** [295_excel_report_project.py](295_excel_report_project.py). **Screenshot:** [Lihat hasil eksekusi](output/295_excel_report_project.png).

### 296. Aplikasi cuaca berbasis API
**Tujuan:** Mengolah respons suhu dari antarmuka HTTP. **Konsep dan cara kerja:** fungsi melakukan `.get`, memeriksa status, membaca JSON; demo memakai Mock dan `example.org` sebagai alamat ilustrasi, **bukan** layanan cuaca live. **Jalankan:** `python 296_weather_api_project.py`. **Hasil demo:** Bandung 27°C. **Source code:** [296_weather_api_project.py](296_weather_api_project.py). **Screenshot:** [Lihat hasil eksekusi](output/296_weather_api_project.png).

### 297. Aplikasi web scraping
**Tujuan:** Mengambil judul artikel HTML. **Konsep dan cara kerja:** Beautiful Soup menyeleksi `article h2` dari HTML lokal; situs nyata perlu mematuhi aturan situs dan batas request. **Jalankan:** `python 297_web_scraper_project.py`. **Hasil:** Belajar Python dan Proyek Data. **Source code:** [297_web_scraper_project.py](297_web_scraper_project.py). **Screenshot:** [Lihat hasil eksekusi](output/297_web_scraper_project.png).

### 298. Pembuatan REST API
**Tujuan:** Membuat dan membaca tugas lewat endpoint. **Konsep dan cara kerja:** FastAPI menyediakan POST dan GET dengan 404 untuk id tak ada; `TestClient` menguji keduanya tanpa server publik, data disimpan hanya di memori. **Jalankan:** `python 298_rest_api_project.py`. **Hasil:** respons POST dan GET tugas Belajar. **Source code:** [298_rest_api_project.py](298_rest_api_project.py). **Screenshot:** [Lihat hasil eksekusi](output/298_rest_api_project.png).

### 299. Dashboard analisis data
**Tujuan:** Merangkum kategori dan menggambarkan grafik. **Konsep dan cara kerja:** pandas `groupby` menghasilkan total A=30 dan B=15, Matplotlib merender grafik dalam memori; ini prototipe statis, bukan dashboard web interaktif. **Jalankan:** `python 299_data_dashboard_project.py`. **Hasil:** dictionary total kategori. **Source code:** [299_data_dashboard_project.py](299_data_dashboard_project.py). **Screenshot:** [Lihat hasil eksekusi](output/299_data_dashboard_project.png).

### 300. Aplikasi manajemen tugas
**Tujuan:** Membuat dan menyelesaikan tugas. **Konsep dan cara kerja:** list dictionary menyimpan judul serta status, judul kosong ditolak; tidak ada penyimpanan permanen. **Jalankan:** `python 300_task_management_project.py`. **Hasil:** satu tugas Belajar Python berstatus selesai. **Source code:** [300_task_management_project.py](300_task_management_project.py). **Screenshot:** [Lihat hasil eksekusi](output/300_task_management_project.png).

## Ringkasan

Setiap proyek memiliki alur inti yang dapat dijalankan dan diadaptasi. Dataset, HTTP, serta visualisasi sengaja dibatasi untuk demo yang dapat diuji secara lokal; fitur produksi seperti persistensi, autentikasi, dan deployment memerlukan pekerjaan lanjutan.