import random


def periksa(tebakan, rahasia):
    if tebakan == rahasia:
        return "Tepat!"
    return "Terlalu kecil" if tebakan < rahasia else "Terlalu besar"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Tebak bilangan 1–10")
    parser.add_argument("tebakan", type=int, nargs="?", default=5)
    args = parser.parse_args()
    # Rahasia dipilih acak, bukan disamarkan sebagai hasil prediksi deterministik.
    rahasia = random.randint(1, 10)
    print("Tebakan:", args.tebakan, periksa(args.tebakan, rahasia), "Jawaban:", rahasia)