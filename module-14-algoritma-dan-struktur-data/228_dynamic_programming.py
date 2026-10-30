def fibonacci(n):
    sebelumnya, sekarang = 0, 1
    # Simpan dua hasil terakhir agar submasalah tidak dihitung berulang.
    for _ in range(n):
        sebelumnya, sekarang = sekarang, sebelumnya + sekarang
    return sebelumnya


print("Fibonacci ke-10:", fibonacci(10))