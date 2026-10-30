import calendar

# monthrange mengembalikan hari pertama dalam pekan dan jumlah hari bulan.
_, jumlah_hari = calendar.monthrange(2024, 2)
print("Hari pada Februari 2024:", jumlah_hari)
print("Tahun kabisat:", calendar.isleap(2024))