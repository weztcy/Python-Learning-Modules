from functools import lru_cache, reduce

@lru_cache(maxsize=None)
def fibonacci(n):
    # Cache menghindari hitung ulang cabang rekursi dengan argumen sama.
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci ke-10:", fibonacci(10))
print("Jumlah:", reduce(lambda a, b: a + b, [1, 2, 3], 0))