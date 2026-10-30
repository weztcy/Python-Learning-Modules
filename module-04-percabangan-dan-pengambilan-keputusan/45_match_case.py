perintah = "mulai"

# match-case memilih pola yang cocok; pola _ menjadi pilihan default.
match perintah:
    case "mulai":
        print("Program dimulai")
    case "berhenti":
        print("Program berhenti")
    case _:
        print("Perintah tidak dikenal")