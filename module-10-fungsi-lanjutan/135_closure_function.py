def buat_pengali(faktor):
    def kalikan(angka):
        # Fungsi dalam tetap mengingat faktor sesudah pemanggilan luar selesai.
        return angka * faktor

    return kalikan


dua_kali = buat_pengali(2)
print("Hasil:", dua_kali(5))