from datetime import date, timedelta

# date menyimpan tanggal; timedelta menyatakan selisih waktu.
hari_ini = date.today()
print("Hari ini:", hari_ini.isoformat())
print("Besok:", (hari_ini + timedelta(days=1)).isoformat())