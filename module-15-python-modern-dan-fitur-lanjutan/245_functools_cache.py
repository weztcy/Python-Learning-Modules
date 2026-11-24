from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# cache_info menunjukkan pemanggilan ulang yang tidak perlu dihitung lagi.
print("Fibonacci ke-10:", fib(10))
print("Cache hit:", fib.cache_info().hits)