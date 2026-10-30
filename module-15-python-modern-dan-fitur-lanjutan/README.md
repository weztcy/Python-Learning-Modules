# Modul 15 — Python Modern dan Fitur Lanjutan

Modul ini memperkenalkan typing, structural pattern matching, context manager, referensi lemah, manajemen memori, semantik penyalinan, unpacking, caching, ABC, dan introspeksi. Tujuannya memahami perilaku fitur modern tanpa menganggap type hints sebagai validasi runtime. Gunakan Python 3.10+ dan standard library. Jalankan perintah dari folder ini. Screenshot jendela log eksekusi tersedia di setiap submodul.

## Daftar materi

1. [Type hints](231_type_hints_basic.py)
2. [Union types](232_union_types.py)
3. [Generic types](233_generic_types.py)
4. [Protocol dan structural typing](234_protocol_typing.py)
5. [Typing cast](235_typing_cast.py)
6. [Structural pattern matching](236_pattern_matching.py)
7. [Custom context manager](237_context_manager_class.py)
8. [contextlib](238_contextlib_module.py)
9. [Weak references](239_weakref_module.py)
10. [Garbage collection](240_garbage_collection.py)
11. [Copy semantics](241_copy_semantics.py)
12. [Memory profiling](242_memory_profiling.py)
13. [Iterable unpacking](243_iterable_unpacking.py)
14. [Assignment expression](244_walrus_operator.py)
15. [Caching dengan lru_cache](245_functools_cache.py)
16. [Abstract Base Classes](246_abstract_base_classes.py)
17. [Reflection dan introspection](247_reflection_introspection.py)

### 231. Type hints
**Tujuan:** Menjelaskan tipe parameter dan hasil fungsi. **Konsep dan cara kerja:** anotasi `str` membantu alat statis dan pembaca, tetapi tidak diperiksa otomatis oleh interpreter. **Jalankan:** `python 231_type_hints_basic.py`. **Hasil:** `Halo, Ayu!`. **Source code:** [231_type_hints_basic.py](231_type_hints_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/231_type_hints_basic.png).

### 232. Union types
**Tujuan:** Menyatakan lebih dari satu tipe yang diterima. **Konsep dan cara kerja:** `int | str` pada anotasi mengizinkan dua bentuk input secara konseptual; fungsi mengembalikan teks. **Jalankan:** `python 232_union_types.py`. **Hasil:** `3 tiga`. **Source code:** [232_union_types.py](232_union_types.py). **Screenshot:** [Lihat hasil eksekusi](output/232_union_types.png).

### 233. Generic types
**Tujuan:** Menyatakan tipe elemen koleksi. **Konsep dan cara kerja:** `list[int]` menggambarkan list bilangan bulat, dan fungsi mengambil elemen pertama. **Jalankan:** `python 233_generic_types.py`. **Hasil:** 3. **Source code:** [233_generic_types.py](233_generic_types.py). **Screenshot:** [Lihat hasil eksekusi](output/233_generic_types.png).

### 234. Protocol dan structural typing
**Tujuan:** Menyatakan antarmuka berdasarkan metode yang tersedia. **Konsep dan cara kerja:** Kucing memiliki `bersuara` yang cocok dengan Protocol tanpa inheritance langsung. **Jalankan:** `python 234_protocol_typing.py`. **Hasil:** `Meong`. **Source code:** [234_protocol_typing.py](234_protocol_typing.py). **Screenshot:** [Lihat hasil eksekusi](output/234_protocol_typing.png).

### 235. Type casting pada sistem typing
**Tujuan:** Membedakan petunjuk pemeriksa tipe dan konversi nyata. **Konsep dan cara kerja:** `typing.cast` mengubah pengetahuan alat statis tetapi tetap mengembalikan objek string yang sama. **Jalankan:** `python 235_typing_cast.py`. **Hasil:** `PYTHON`, identitas `True`. **Source code:** [235_typing_cast.py](235_typing_cast.py). **Screenshot:** [Lihat hasil eksekusi](output/235_typing_cast.png).

### 236. Structural pattern matching
**Tujuan:** Memilih cabang berdasarkan bentuk data. **Konsep dan cara kerja:** pola dua elemen dan dictionary dengan kunci nama membongkar nilai; `_` menampung selainnya. **Jalankan:** `python 236_pattern_matching.py`. **Hasil:** titik 2,3 dan nama Ayu. **Source code:** [236_pattern_matching.py](236_pattern_matching.py). **Screenshot:** [Lihat hasil eksekusi](output/236_pattern_matching.png).

### 237. Custom context manager
**Tujuan:** Mengatur awal dan akhir blok `with`. **Konsep dan cara kerja:** `__enter__` berjalan sebelum blok, `__exit__` setelah blok; return False tidak menyembunyikan exception. **Jalankan:** `python 237_context_manager_class.py`. **Hasil:** Mulai, Bekerja, Selesai. **Source code:** [237_context_manager_class.py](237_context_manager_class.py). **Screenshot:** [Lihat hasil eksekusi](output/237_context_manager_class.png).

### 238. Modul `contextlib`
**Tujuan:** Membuat context manager dari generator. **Konsep dan cara kerja:** kode sebelum `yield` membuka sesi, blok pemanggil berjalan, `finally` menutup sesi. **Jalankan:** `python 238_contextlib_module.py`. **Hasil:** Buka, Proses, Tutup. **Source code:** [238_contextlib_module.py](238_contextlib_module.py). **Screenshot:** [Lihat hasil eksekusi](output/238_contextlib_module.png).

### 239. Weak references
**Tujuan:** Mengamati referensi yang tidak menjaga objek tetap hidup. **Konsep dan cara kerja:** `weakref.ref` tidak menambah kepemilikan kuat; setelah objek dihapus, referensi mengembalikan None pada CPython. **Jalankan:** `python 239_weakref_module.py`. **Hasil pada CPython:** sebelum `True`, sesudah `True`; waktu pengumpulan dapat berbeda pada implementasi lain. **Source code:** [239_weakref_module.py](239_weakref_module.py). **Screenshot:** [Lihat hasil eksekusi](output/239_weakref_module.png).

### 240. Garbage collection
**Tujuan:** Memahami pengumpulan objek siklik. **Konsep dan cara kerja:** list yang memuat dirinya sendiri dilepas, lalu `gc.collect` meminta pengumpulan; jumlah pasti hasil pengumpulan bisa berbeda. **Jalankan:** `python 240_garbage_collection.py`. **Hasil:** pemeriksaan terkumpul `True` pada eksekusi contoh. **Source code:** [240_garbage_collection.py](240_garbage_collection.py). **Screenshot:** [Lihat hasil eksekusi](output/240_garbage_collection.png).

### 241. Semantik penyalinan objek
**Tujuan:** Membedakan shallow copy dan deep copy. **Konsep dan cara kerja:** list skor di dalam salinan dangkal masih merujuk objek asli; deep copy menyalinnya juga. **Jalankan:** `python 241_copy_semantics.py`. **Hasil:** dangkal `[80, 90]`, mendalam `[80]`. **Source code:** [241_copy_semantics.py](241_copy_semantics.py). **Screenshot:** [Lihat hasil eksekusi](output/241_copy_semantics.png).

### 242. Pemeriksaan penggunaan memori
**Tujuan:** Mengamati alokasi yang dilacak Python. **Konsep dan cara kerja:** `tracemalloc` mengukur penggunaan sebelum dan setelah list berisi 10.000 angka dibuat. **Jalankan:** `python 242_memory_profiling.py`. **Hasil:** 10.000 item, jumlah byte saat ini dan puncak bervariasi. **Source code:** [242_memory_profiling.py](242_memory_profiling.py). **Screenshot:** [Lihat hasil eksekusi](output/242_memory_profiling.png).

### 243. Iterable unpacking
**Tujuan:** Memisahkan ujung dan bagian tengah iterable. **Konsep dan cara kerja:** `*tengah` menampung nilai antara pertama dan terakhir sebagai list. **Jalankan:** `python 243_iterable_unpacking.py`. **Hasil:** pertama 1, tengah `[2, 3]`, terakhir 4. **Source code:** [243_iterable_unpacking.py](243_iterable_unpacking.py). **Screenshot:** [Lihat hasil eksekusi](output/243_iterable_unpacking.png).

### 244. Assignment expression
**Tujuan:** Memakai hasil perhitungan di kondisi dan badan loop. **Konsep dan cara kerja:** `:=` menyimpan panjang kata ketika membandingkannya dengan 4. **Jalankan:** `python 244_walrus_operator.py`. **Hasil:** `pisang panjang: 6`. **Source code:** [244_walrus_operator.py](244_walrus_operator.py). **Screenshot:** [Lihat hasil eksekusi](output/244_walrus_operator.png).

### 245. Caching dengan `lru_cache`
**Tujuan:** Menghindari penghitungan rekursi berulang. **Konsep dan cara kerja:** decorator mengingat hasil `fib(n)` untuk nilai n yang telah dihitung; `cache_info` menunjukkan hit. **Jalankan:** `python 245_functools_cache.py`. **Hasil:** Fibonacci ke-10 adalah 55 dan jumlah hit positif. **Source code:** [245_functools_cache.py](245_functools_cache.py). **Screenshot:** [Lihat hasil eksekusi](output/245_functools_cache.png).

### 246. Abstract Base Classes
**Tujuan:** Mengimplementasikan kontrak iterable. **Konsep dan cara kerja:** `HitungMundur` mewarisi ABC `Iterable` dan mengimplementasikan `__iter__`. **Jalankan:** `python 246_abstract_base_classes.py`. **Hasil:** `[3, 2, 1]`. **Source code:** [246_abstract_base_classes.py](246_abstract_base_classes.py). **Screenshot:** [Lihat hasil eksekusi](output/246_abstract_base_classes.png).

### 247. Reflection dan introspection
**Tujuan:** Memeriksa tipe dan atribut saat runtime. **Konsep dan cara kerja:** `type`, `getattr`, dan `hasattr` mengamati instance Murid. **Jalankan:** `python 247_reflection_introspection.py`. **Hasil:** tipe Murid, nama Ayu, tidak ada atribut nilai. **Source code:** [247_reflection_introspection.py](247_reflection_introspection.py). **Screenshot:** [Lihat hasil eksekusi](output/247_reflection_introspection.png).

## Ringkasan

Anotasi memberi informasi untuk pembaca dan tooling statis; protokol runtime seperti context manager dan iterable justru membutuhkan metode konkret. Fitur memori, cache, dan introspeksi membantu memahami perilaku program pada tingkat lebih lanjut.