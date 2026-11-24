from dataclasses import dataclass


# dataclass menghasilkan __init__, __repr__, dan pembandingan nilai otomatis.
@dataclass
class Titik:
    x: int
    y: int


print(Titik(2, 3))
print("Setara:", Titik(2, 3) == Titik(2, 3))