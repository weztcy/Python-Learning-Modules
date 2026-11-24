import tracemalloc

# tracemalloc mengukur alokasi Python, bukan seluruh memori proses sistem.
tracemalloc.start()
angka = list(range(10_000))
saat_ini, puncak = tracemalloc.get_traced_memory()
print("Item:", len(angka))
print("Memori terlacak (byte):", saat_ini, "Puncak:", puncak)
tracemalloc.stop()