a = {1, 2, 3}
b = {3, 4, 5}

# sorted membuat tampilan konsisten tanpa mengubah sifat set yang tak berurutan.
print("Gabungan:", sorted(a | b))
print("Irisan:", sorted(a & b))
print("Selisih a-b:", sorted(a - b))