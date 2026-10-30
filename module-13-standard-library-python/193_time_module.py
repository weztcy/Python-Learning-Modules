import time

# monotonic cocok untuk mengukur durasi karena tidak mengikuti perubahan jam sistem.
mulai = time.monotonic()
total = sum(range(1000))
print("Jumlah:", total)
print("Durasi (detik):", round(time.monotonic() - mulai, 6))