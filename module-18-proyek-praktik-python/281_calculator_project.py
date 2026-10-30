def hitung(a, operator, b):
    operasi = {"+": lambda: a + b, "-": lambda: a - b, "*": lambda: a * b, "/": lambda: a / b}
    if operator not in operasi:
        raise ValueError("Operator tidak dikenal")
    if operator == "/" and b == 0:
        raise ValueError("Pembagi tidak boleh nol")
    return operasi[operator]()


if __name__ == "__main__":
    # Opsi argumen memungkinkan demo teruji tanpa input interaktif tanpa akhir.
    import argparse

    parser = argparse.ArgumentParser(description="Kalkulator konsol")
    parser.add_argument("a", type=float, nargs="?", default=8)
    parser.add_argument("operator", nargs="?", default="+")
    parser.add_argument("b", type=float, nargs="?", default=2)
    args = parser.parse_args()
    try:
        print("Hasil:", hitung(args.a, args.operator, args.b))
    except ValueError as kesalahan:
        parser.error(str(kesalahan))