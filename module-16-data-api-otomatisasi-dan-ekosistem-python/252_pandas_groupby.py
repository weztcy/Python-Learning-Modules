import pandas as pd

data = pd.DataFrame({"kelas": ["A", "A", "B"], "nilai": [80, 90, 70]})
# groupby menghitung rata-rata untuk tiap kelas secara terpisah.
print(data.groupby("kelas")["nilai"].mean().to_string())