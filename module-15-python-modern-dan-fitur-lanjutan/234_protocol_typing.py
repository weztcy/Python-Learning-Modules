from typing import Protocol


class BisaBersuara(Protocol):
    def bersuara(self) -> str: ...


class Kucing:
    def bersuara(self) -> str:
        return "Meong"


def dengar(hewan: BisaBersuara) -> str:
    # Structural typing tidak memerlukan inheritance dari Protocol.
    return hewan.bersuara()


print(dengar(Kucing()))