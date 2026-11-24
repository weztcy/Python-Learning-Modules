import heapq

data = []
# Min-heap selalu menempatkan nilai terkecil sebagai yang berikutnya diambil.
for nilai in (5, 1, 3):
    heapq.heappush(data, nilai)
print("Urutan keluar:", [heapq.heappop(data) for _ in range(3)])