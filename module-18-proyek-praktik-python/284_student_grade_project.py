def rapor(nama, nilai):
    if not nilai or any(not 0 <= angka <= 100 for angka in nilai):
        raise ValueError("Nilai harus tersedia dalam rentang 0–100")
    rata = sum(nilai) / len(nilai)
    return {"nama": nama, "rata_rata": rata, "lulus": rata >= 75}


if __name__ == "__main__":
    # Data demo dapat diganti ketika fungsi di-import untuk pengujian.
    print("Rapor:", rapor("Ayu", [80, 90, 85]))