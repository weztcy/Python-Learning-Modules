import gc

# gc.collect meminta pembersihan siklus referensi yang tidak terjangkau.
data = []
data.append(data)
del data
print("Objek siklik terkumpul:", gc.collect() >= 1)