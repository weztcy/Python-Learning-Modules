import pandas as pd

# DataFrame menyatukan kolom dengan label untuk data tabular.
data = pd.DataFrame({"nama": ["Ayu", "Budi"], "nilai": [90, 80]})
print(data.to_string(index=False))