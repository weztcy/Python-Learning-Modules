# Modul 14 — Algoritma dan Struktur Data

Modul ini mempraktikkan pencarian, pengurutan, struktur linear, tree, heap, hash table, graph, backtracking, dynamic programming, greedy, serta analisis kompleksitas. Tujuannya memahami langkah algoritma, bukan hanya memakai fungsi bawaan. Gunakan Python 3.10+; semua contoh memakai standard library. Jalankan dari folder ini. Screenshot jendela log eksekusi tersedia untuk tiap contoh.

## Daftar materi

1. [Linear search](208_linear_search.py)
2. [Binary search](209_binary_search.py)
3. [Bubble sort](210_bubble_sort.py)
4. [Selection sort](211_selection_sort.py)
5. [Insertion sort](212_insertion_sort.py)
6. [Merge sort](213_merge_sort.py)
7. [Quick sort](214_quick_sort.py)
8. [Stack](215_stack_implementation.py)
9. [Queue](216_queue_implementation.py)
10. [Linked list](217_linked_list.py)
11. [Doubly linked list](218_doubly_linked_list.py)
12. [Binary tree](219_binary_tree.py)
13. [Binary search tree](220_binary_search_tree.py)
14. [Tree traversal](221_tree_traversal.py)
15. [Heap](222_heap_implementation.py)
16. [Hash table](223_hash_table.py)
17. [Graph representation](224_graph_representation.py)
18. [Breadth-First Search](225_graph_bfs.py)
19. [Depth-First Search](226_graph_dfs.py)
20. [Backtracking](227_recursion_backtracking.py)
21. [Dynamic programming](228_dynamic_programming.py)
22. [Greedy algorithm](229_greedy_algorithm.py)
23. [Big O](230_big_o_analysis.py)

### 208. Linear search
**Tujuan:** Mencari dalam data yang tidak perlu terurut. **Konsep dan cara kerja:** setiap elemen diperiksa hingga cocok; jika tidak ada dikembalikan -1. **Jalankan:** `python 208_linear_search.py`. **Hasil:** indeks 7 adalah 1. **Source code:** [208_linear_search.py](208_linear_search.py). **Screenshot:** [Lihat hasil eksekusi](output/208_linear_search.png).

### 209. Binary search
**Tujuan:** Mencari dengan membagi rentang. **Konsep dan cara kerja:** pada data terurut, perbandingan dengan elemen tengah menentukan separuh yang masih mungkin; kompleksitas O(log n). **Jalankan:** `python 209_binary_search.py`. **Hasil:** indeks 7 adalah 3. **Source code:** [209_binary_search.py](209_binary_search.py). **Screenshot:** [Lihat hasil eksekusi](output/209_binary_search.png).

### 210. Bubble sort
**Tujuan:** Mengurutkan dengan pertukaran bertetangga. **Konsep dan cara kerja:** elemen terbesar berpindah ke ujung pada tiap putaran; contoh mengurutkan salinan. **Jalankan:** `python 210_bubble_sort.py`. **Hasil:** `[1, 2, 3, 4]`. **Source code:** [210_bubble_sort.py](210_bubble_sort.py). **Screenshot:** [Lihat hasil eksekusi](output/210_bubble_sort.png).

### 211. Selection sort
**Tujuan:** Memilih nilai minimum dari bagian yang tersisa. **Konsep dan cara kerja:** minimum dipertukarkan ke posisi pertama yang belum terurut pada setiap langkah. **Jalankan:** `python 211_selection_sort.py`. **Hasil:** `[1, 2, 3, 4]`. **Source code:** [211_selection_sort.py](211_selection_sort.py). **Screenshot:** [Lihat hasil eksekusi](output/211_selection_sort.png).

### 212. Insertion sort
**Tujuan:** Menyisipkan nilai ke bagian yang sudah terurut. **Konsep dan cara kerja:** elemen lebih besar digeser, lalu nilai saat ini ditempatkan pada celah. **Jalankan:** `python 212_insertion_sort.py`. **Hasil:** `[1, 2, 3, 4]`. **Source code:** [212_insertion_sort.py](212_insertion_sort.py). **Screenshot:** [Lihat hasil eksekusi](output/212_insertion_sort.png).

### 213. Merge sort
**Tujuan:** Mengurutkan dengan divide-and-conquer. **Konsep dan cara kerja:** list dibelah rekursif dan dua bagian terurut digabung memakai dua indeks; waktu O(n log n). **Jalankan:** `python 213_merge_sort.py`. **Hasil:** `[1, 2, 3, 4]`. **Source code:** [213_merge_sort.py](213_merge_sort.py). **Screenshot:** [Lihat hasil eksekusi](output/213_merge_sort.png).

### 214. Quick sort
**Tujuan:** Mengurutkan dengan partisi pivot. **Konsep dan cara kerja:** elemen lebih kecil dan besar diurutkan rekursif; kelompok sama mempertahankan duplikat. Implementasi contoh membuat list tambahan. **Jalankan:** `python 214_quick_sort.py`. **Hasil:** `[1, 2, 3, 3, 4]`. **Source code:** [214_quick_sort.py](214_quick_sort.py). **Screenshot:** [Lihat hasil eksekusi](output/214_quick_sort.png).

### 215. Stack
**Tujuan:** Menggunakan perilaku LIFO. **Konsep dan cara kerja:** `push` menaruh data di ujung list, `pop` mengambil yang terakhir masuk. **Jalankan:** `python 215_stack_implementation.py`. **Hasil:** B lalu A. **Source code:** [215_stack_implementation.py](215_stack_implementation.py). **Screenshot:** [Lihat hasil eksekusi](output/215_stack_implementation.png).

### 216. Queue
**Tujuan:** Menggunakan perilaku FIFO. **Konsep dan cara kerja:** `deque.append` menambah belakang dan `popleft` melayani bagian depan. **Jalankan:** `python 216_queue_implementation.py`. **Hasil:** Ayu lalu Budi. **Source code:** [216_queue_implementation.py](216_queue_implementation.py). **Screenshot:** [Lihat hasil eksekusi](output/216_queue_implementation.png).

### 217. Linked list
**Tujuan:** Menyusuri node satu arah. **Konsep dan cara kerja:** tiap Node menunjuk node berikutnya sampai bertemu None. **Jalankan:** `python 217_linked_list.py`. **Hasil:** A, B, C. **Source code:** [217_linked_list.py](217_linked_list.py). **Screenshot:** [Lihat hasil eksekusi](output/217_linked_list.png).

### 218. Doubly linked list
**Tujuan:** Menyusuri node dua arah. **Konsep dan cara kerja:** tautan `berikutnya` dan `sebelumnya` menghubungkan dua node. **Jalankan:** `python 218_doubly_linked_list.py`. **Hasil:** maju B, mundur A. **Source code:** [218_doubly_linked_list.py](218_doubly_linked_list.py). **Screenshot:** [Lihat hasil eksekusi](output/218_doubly_linked_list.png).

### 219. Binary tree
**Tujuan:** Menyimpan hierarki node dengan maksimal dua anak. **Konsep dan cara kerja:** akar A mempunyai anak kiri B dan kanan C. **Jalankan:** `python 219_binary_tree.py`. **Hasil:** akar A, anak B dan C. **Source code:** [219_binary_tree.py](219_binary_tree.py). **Screenshot:** [Lihat hasil eksekusi](output/219_binary_tree.png).

### 220. Binary search tree
**Tujuan:** Menjaga aturan nilai kiri lebih kecil dari akar dan kanan lebih besar. **Konsep dan cara kerja:** `sisip` rekursif memasukkan 5, 3, 7 dan mengabaikan duplikat. **Jalankan:** `python 220_binary_search_tree.py`. **Hasil:** akar 5 dengan anak 3 dan 7. **Source code:** [220_binary_search_tree.py](220_binary_search_tree.py). **Screenshot:** [Lihat hasil eksekusi](output/220_binary_search_tree.png).

### 221. Tree traversal
**Tujuan:** Menjelajahi node berurutan. **Konsep dan cara kerja:** generator in-order mengunjungi kiri, akar, kanan. **Jalankan:** `python 221_tree_traversal.py`. **Hasil:** `[1, 2, 3]`. **Source code:** [221_tree_traversal.py](221_tree_traversal.py). **Screenshot:** [Lihat hasil eksekusi](output/221_tree_traversal.png).

### 222. Heap
**Tujuan:** Mengambil elemen prioritas minimum. **Konsep dan cara kerja:** `heappush` menambahkan nilai, `heappop` mengeluarkannya mulai dari terkecil. **Jalankan:** `python 222_heap_implementation.py`. **Hasil:** `[1, 3, 5]`. **Source code:** [222_heap_implementation.py](222_heap_implementation.py). **Screenshot:** [Lihat hasil eksekusi](output/222_heap_implementation.png).

### 223. Hash table
**Tujuan:** Menyimpan pasangan kunci-nilai melalui hash. **Konsep dan cara kerja:** indeks bucket ditentukan hash modulo ukuran; beberapa pasangan dalam satu bucket menangani collision. **Jalankan:** `python 223_hash_table.py`. **Hasil:** apel 3. **Source code:** [223_hash_table.py](223_hash_table.py). **Screenshot:** [Lihat hasil eksekusi](output/223_hash_table.png).

### 224. Graph representation
**Tujuan:** Merepresentasikan koneksi antarsimpul. **Konsep dan cara kerja:** adjacency list memetakan simpul A, B, C ke tetangganya; sisi dua arah dicatat dua kali. **Jalankan:** `python 224_graph_representation.py`. **Hasil:** daftar tetangga tiga simpul. **Source code:** [224_graph_representation.py](224_graph_representation.py). **Screenshot:** [Lihat hasil eksekusi](output/224_graph_representation.png).

### 225. Breadth-First Search
**Tujuan:** Menjelajah graph per tingkat. **Konsep dan cara kerja:** antrian FIFO dan himpunan dikunjungi mencegah node berulang. **Jalankan:** `python 225_graph_bfs.py`. **Hasil:** A, B, C, D. **Source code:** [225_graph_bfs.py](225_graph_bfs.py). **Screenshot:** [Lihat hasil eksekusi](output/225_graph_bfs.png).

### 226. Depth-First Search
**Tujuan:** Menjelajah satu cabang sedalam mungkin. **Konsep dan cara kerja:** rekursi mengunjungi tetangga sebelum kembali ke simpul sebelumnya. **Jalankan:** `python 226_graph_dfs.py`. **Hasil:** A B D C. **Source code:** [226_graph_dfs.py](226_graph_dfs.py). **Screenshot:** [Lihat hasil eksekusi](output/226_graph_dfs.png).

### 227. Backtracking
**Tujuan:** Mencoba kemungkinan dan kembali untuk pilihan lain. **Konsep dan cara kerja:** satu angka dipilih dari sisa untuk setiap posisi hingga semua permutasi terbentuk. **Jalankan:** `python 227_recursion_backtracking.py`. **Hasil:** enam susunan dari 1, 2, 3. **Source code:** [227_recursion_backtracking.py](227_recursion_backtracking.py). **Screenshot:** [Lihat hasil eksekusi](output/227_recursion_backtracking.png).

### 228. Dynamic programming
**Tujuan:** Menghindari perhitungan submasalah berulang. **Konsep dan cara kerja:** dua nilai Fibonacci terakhir disimpan pada setiap iterasi. **Jalankan:** `python 228_dynamic_programming.py`. **Hasil:** Fibonacci ke-10 = 55. **Source code:** [228_dynamic_programming.py](228_dynamic_programming.py). **Screenshot:** [Lihat hasil eksekusi](output/228_dynamic_programming.png).

### 229. Greedy algorithm
**Tujuan:** Memilih aktivitas tanpa jadwal bertabrakan. **Konsep dan cara kerja:** interval diurutkan menurut akhir; pilih yang mulai setelah aktivitas terakhir selesai. **Jalankan:** `python 229_greedy_algorithm.py`. **Hasil:** `(1,4), (4,6), (6,8)`. **Source code:** [229_greedy_algorithm.py](229_greedy_algorithm.py). **Screenshot:** [Lihat hasil eksekusi](output/229_greedy_algorithm.png).

### 230. Big O
**Tujuan:** Mengamati pertumbuhan langkah saat input membesar. **Konsep dan cara kerja:** target yang tidak ada memaksa pencarian linear memeriksa semua elemen. **Jalankan:** `python 230_big_o_analysis.py`. **Hasil:** 10, 100, 1000 langkah untuk n sama; pola O(n). **Source code:** [230_big_o_analysis.py](230_big_o_analysis.py). **Screenshot:** [Lihat hasil eksekusi](output/230_big_o_analysis.png).

## Ringkasan

Pencarian, pengurutan, dan traversal memiliki prasyarat serta biaya berbeda. Contoh kecil memperlihatkan operasi inti sebelum digunakan pada data berskala lebih besar.