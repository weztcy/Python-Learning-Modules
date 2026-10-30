import pandas as pd

data = pd.DataFrame({"nama": [" Ayu ", "Budi", "Cici"], "nilai": [90, None, 75]})
# strip membersihkan spasi; fillna mengganti nilai hilang.
data["nama"] = data["nama"].str.strip()
data["nilai"] = data["nilai"].fillna(0)
print(data.to_string(index=False))