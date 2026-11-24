from collections import Counter, deque

# Counter menghitung frekuensi; deque memudahkan ambil data dari depan.
print("Frekuensi:", Counter("banana"))
antrian = deque(["Ayu", "Budi"])
print("Dilayani:", antrian.popleft())