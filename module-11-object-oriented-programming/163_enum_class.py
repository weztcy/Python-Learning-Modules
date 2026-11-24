from enum import Enum


class Status(Enum):
    BARU = "baru"
    SELESAI = "selesai"


# Enum membuat anggota bernama yang bisa dibandingkan tanpa string bebas.
status = Status.BARU
print("Nama:", status.name, "Nilai:", status.value)