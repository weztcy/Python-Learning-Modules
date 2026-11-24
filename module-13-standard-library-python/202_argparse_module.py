import argparse

parser = argparse.ArgumentParser(description="Hitung luas persegi")
parser.add_argument("sisi", type=float, nargs="?", default=4)
# parse_args otomatis menolak masukan yang tidak bisa dikonversi menjadi float.
args = parser.parse_args()
print("Luas:", args.sisi ** 2)