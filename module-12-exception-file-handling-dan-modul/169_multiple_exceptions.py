def bagi(teks, pembagi):
    try:
        return int(teks) / pembagi
    # Exception berbeda diberi penanganan berbeda sesuai sumber kesalahannya.
    except ValueError:
        return "Bukan bilangan bulat"
    except ZeroDivisionError:
        return "Pembagi tidak boleh nol"


print(bagi("salah", 2))
print(bagi("4", 0))