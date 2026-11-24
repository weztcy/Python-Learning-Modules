def set_usia(usia):
    if usia < 0:
        # raise menolak nilai tidak valid dengan exception yang sesuai.
        raise ValueError("Usia tidak boleh negatif")
    return usia


try:
    set_usia(-1)
except ValueError as kesalahan:
    print(kesalahan)