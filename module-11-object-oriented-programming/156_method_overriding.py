class Hewan:
    def bersuara(self):
        return "Suara hewan"


class Kucing(Hewan):
    def bersuara(self):
        # Override mengganti perilaku parent ketika dipanggil lewat instance anak.
        return "Meong"


print(Hewan().bersuara(), Kucing().bersuara())