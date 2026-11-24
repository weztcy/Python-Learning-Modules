# Modul 13 — Standard Library Python

Modul ini mengenalkan pustaka bawaan untuk matematika, waktu, data, proses, logging, file, dan database. Tujuannya agar pembelajar memakai komponen yang telah tersedia daripada membangun ulang fungsi umum. Semua contoh berjalan dengan Python 3.10+ tanpa dependensi tambahan. Jalankan perintah berikut dari folder modul ini. Keluaran acak, tanggal, durasi, dan path bergantung pada lingkungan; screenshot menunjukkan satu eksekusi aktual.

## Daftar materi

1. [math](188_math_module.py)
2. [statistics](189_statistics_module.py)
3. [random](190_random_module.py)
4. [secrets](191_secrets_module.py)
5. [datetime](192_datetime_module.py)
6. [time](193_time_module.py)
7. [calendar](194_calendar_module.py)
8. [os](195_os_module.py)
9. [sys](196_sys_module.py)
10. [collections](197_collections_module.py)
11. [itertools](198_itertools_module.py)
12. [functools](199_functools_module.py)
13. [Regular expressions](200_re_module.py)
14. [logging](201_logging_module.py)
15. [argparse](202_argparse_module.py)
16. [subprocess](203_subprocess_module.py)
17. [shutil](204_shutil_module.py)
18. [hashlib](205_hashlib_module.py)
19. [sqlite3](206_sqlite3_module.py)
20. [copy](207_copy_module.py)

### 188. Modul `math`
**Tujuan:** Memakai operasi matematis bawaan. **Konsep dan cara kerja:** `sqrt` menghitung akar; `pi` dipakai untuk luas lingkaran. **Jalankan:** `python 188_math_module.py`. **Hasil:** 9.0 dan luas sekitar 12.57. **Source code:** [188_math_module.py](188_math_module.py). **Screenshot:** [Lihat hasil eksekusi](output/188_math_module.png).

### 189. Modul `statistics`
**Tujuan:** Merangkum kumpulan angka. **Konsep dan cara kerja:** mean, median, dan mode dihitung dari empat skor. **Jalankan:** `python 189_statistics_module.py`. **Hasil:** rata-rata 80, median 80, modus 80. **Source code:** [189_statistics_module.py](189_statistics_module.py). **Screenshot:** [Lihat hasil eksekusi](output/189_statistics_module.png).

### 190. Modul `random`
**Tujuan:** Memilih nilai untuk simulasi. **Konsep dan cara kerja:** `randint` melempar dadu dan `choice` memilih warna; hasil tidak cocok untuk keamanan. **Jalankan:** `python 190_random_module.py`. **Hasil:** angka 1–6 dan satu warna acak. **Source code:** [190_random_module.py](190_random_module.py). **Screenshot:** [Lihat hasil eksekusi](output/190_random_module.png).

### 191. Modul `secrets`
**Tujuan:** Membuat token dari sumber acak yang sesuai kebutuhan keamanan. **Konsep dan cara kerja:** `token_hex(4)` menghasilkan empat byte acak dalam delapan karakter heksadesimal. **Jalankan:** `python 191_secrets_module.py`. **Hasil:** token berbeda pada tiap eksekusi. **Source code:** [191_secrets_module.py](191_secrets_module.py). **Screenshot:** [Lihat hasil eksekusi](output/191_secrets_module.png).

### 192. Modul `datetime`
**Tujuan:** Menghitung tanggal relatif. **Konsep dan cara kerja:** `date.today` mengambil tanggal lokal; `timedelta(days=1)` menghasilkan besok. **Jalankan:** `python 192_datetime_module.py`. **Hasil:** tanggal hari ini dan hari berikutnya. **Source code:** [192_datetime_module.py](192_datetime_module.py). **Screenshot:** [Lihat hasil eksekusi](output/192_datetime_module.png).

### 193. Modul `time`
**Tujuan:** Mengukur durasi. **Konsep dan cara kerja:** selisih `monotonic` sebelum dan sesudah penjumlahan menunjukkan waktu berlalu. **Jalankan:** `python 193_time_module.py`. **Hasil:** jumlah 499500 dan durasi bergantung komputer. **Source code:** [193_time_module.py](193_time_module.py). **Screenshot:** [Lihat hasil eksekusi](output/193_time_module.png).

### 194. Modul `calendar`
**Tujuan:** Memeriksa jumlah hari dan tahun kabisat. **Konsep dan cara kerja:** `monthrange` menghitung hari Februari 2024 dan `isleap` mengecek tahunnya. **Jalankan:** `python 194_calendar_module.py`. **Hasil:** 29 dan `True`. **Source code:** [194_calendar_module.py](194_calendar_module.py). **Screenshot:** [Lihat hasil eksekusi](output/194_calendar_module.png).

### 195. Modul `os`
**Tujuan:** Membaca informasi lingkungan sistem. **Konsep dan cara kerja:** `os.sep` menunjukkan pemisah path; `getenv` membaca variabel atau default. **Jalankan:** `python 195_os_module.py`. **Hasil:** pemisah sesuai OS, nilai variabel atau `belum diatur`. **Source code:** [195_os_module.py](195_os_module.py). **Screenshot:** [Lihat hasil eksekusi](output/195_os_module.png).

### 196. Modul `sys`
**Tujuan:** Membaca konteks interpreter dan argumen skrip. **Konsep dan cara kerja:** `sys.executable` memberi path Python, `sys.argv[1:]` memberi argumen tambahan. **Jalankan:** `python 196_sys_module.py contoh`. **Hasil:** path interpreter dan `['contoh']`. **Source code:** [196_sys_module.py](196_sys_module.py). **Screenshot:** [Lihat hasil eksekusi](output/196_sys_module.png).

### 197. Modul `collections`
**Tujuan:** Menghitung frekuensi dan melayani antrian. **Konsep dan cara kerja:** `Counter` menghitung huruf banana; `deque.popleft` mengambil Ayu dari depan. **Jalankan:** `python 197_collections_module.py`. **Hasil:** frekuensi huruf dan `Dilayani: Ayu`. **Source code:** [197_collections_module.py](197_collections_module.py). **Screenshot:** [Lihat hasil eksekusi](output/197_collections_module.png).

### 198. Modul `itertools`
**Tujuan:** Membangun kombinasi dan mengambil bagian iterable. **Konsep dan cara kerja:** `combinations` membentuk pasangan AB, AC, BC; `islice` membaca tiga angka awal. **Jalankan:** `python 198_itertools_module.py`. **Hasil:** tiga pasangan dan `[0, 1, 2]`. **Source code:** [198_itertools_module.py](198_itertools_module.py). **Screenshot:** [Lihat hasil eksekusi](output/198_itertools_module.png).

### 199. Modul `functools`
**Tujuan:** Memakai cache fungsi dan reduksi data. **Konsep dan cara kerja:** `lru_cache` menghindari rekursi Fibonacci berulang; `reduce` menjumlahkan list. **Jalankan:** `python 199_functools_module.py`. **Hasil:** Fibonacci ke-10 = 55 dan jumlah 6. **Source code:** [199_functools_module.py](199_functools_module.py). **Screenshot:** [Lihat hasil eksekusi](output/199_functools_module.png).

### 200. Regular expressions
**Tujuan:** Menemukan pola teks. **Konsep dan cara kerja:** `re.search` mencari deretan 10–13 digit utuh menggunakan batas kata. **Jalankan:** `python 200_re_module.py`. **Hasil:** `081234567890`. **Source code:** [200_re_module.py](200_re_module.py). **Screenshot:** [Lihat hasil eksekusi](output/200_re_module.png).

### 201. Logging
**Tujuan:** Menampilkan pesan berdasarkan tingkat kepentingan. **Konsep dan cara kerja:** konfigurasi `basicConfig` mengirim pesan INFO dan WARNING ke stdout. **Jalankan:** `python 201_logging_module.py`. **Hasil:** dua pesan dengan label level. **Source code:** [201_logging_module.py](201_logging_module.py). **Screenshot:** [Lihat hasil eksekusi](output/201_logging_module.png).

### 202. Argument parsing
**Tujuan:** Membaca dan memvalidasi argumen baris perintah. **Konsep dan cara kerja:** `argparse` mengonversi sisi ke float; bila kosong, default 4 dipakai. **Jalankan:** `python 202_argparse_module.py 5`. **Hasil:** luas 25.0; `--help` menampilkan petunjuk. **Source code:** [202_argparse_module.py](202_argparse_module.py). **Screenshot:** [Lihat hasil eksekusi](output/202_argparse_module.png).

### 203. Menjalankan proses eksternal
**Tujuan:** Menjalankan proses anak dan membaca keluarannya. **Konsep dan cara kerja:** `subprocess.run` memakai `sys.executable`, menangkap stdout, serta memeriksa kode keluar. **Jalankan:** `python 203_subprocess_module.py`. **Hasil:** keluaran proses anak 5. **Source code:** [203_subprocess_module.py](203_subprocess_module.py). **Screenshot:** [Lihat hasil eksekusi](output/203_subprocess_module.png).

### 204. Operasi file dan direktori
**Tujuan:** Menyalin file dengan `shutil`. **Konsep dan cara kerja:** file sumber dan salinannya berada dalam direktori sementara, kemudian isi salinan dibaca. **Jalankan:** `python 204_shutil_module.py`. **Hasil:** `Isi contoh`. **Source code:** [204_shutil_module.py](204_shutil_module.py). **Screenshot:** [Lihat hasil eksekusi](output/204_shutil_module.png).

### 205. Hashing
**Tujuan:** Membuat digest data. **Konsep dan cara kerja:** teks diubah menjadi UTF-8 lalu dihitung SHA-256; hash tidak bisa didekripsi. **Jalankan:** `python 205_hashlib_module.py`. **Hasil:** digest heksadesimal 64 karakter. **Source code:** [205_hashlib_module.py](205_hashlib_module.py). **Screenshot:** [Lihat hasil eksekusi](output/205_hashlib_module.png).

### 206. Database SQLite
**Tujuan:** Membuat tabel dan membaca data secara lokal. **Konsep dan cara kerja:** koneksi `:memory:` membuat tabel siswa, query berparameter menyisipkan Ayu, lalu SELECT membaca hasil; tidak ada file database permanen. **Jalankan:** `python 206_sqlite3_module.py`. **Hasil:** `[('Ayu', 90)]`. **Source code:** [206_sqlite3_module.py](206_sqlite3_module.py). **Screenshot:** [Lihat hasil eksekusi](output/206_sqlite3_module.png).

### 207. Shallow copy dan deep copy
**Tujuan:** Membedakan objek dalam yang masih berbagi referensi. **Konsep dan cara kerja:** `copy.copy` hanya menyalin list luar; `deepcopy` juga menyalin list dalam, sehingga perubahan asli tidak merambat. **Jalankan:** `python 207_copy_module.py`. **Hasil:** asli dan dangkal berubah bersama; mendalam tetap. **Source code:** [207_copy_module.py](207_copy_module.py). **Screenshot:** [Lihat hasil eksekusi](output/207_copy_module.png).

## Ringkasan

Standard library menyediakan komponen yang siap dipakai untuk tugas umum. Pilih modul menurut kebutuhan: data, sistem, keamanan, waktu, atau proses; perhatikan efek samping dan variasi keluaran pada tiap lingkungan.