def faktorial(n):
    # Base case menghentikan pemanggilan berulang sebelum stack bertambah terus.
    if n <= 1:
        return 1
    return n * faktorial(n - 1)


print("5! =", faktorial(5))