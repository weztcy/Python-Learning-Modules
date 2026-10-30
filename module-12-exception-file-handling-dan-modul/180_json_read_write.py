import json
from pathlib import Path
from tempfile import TemporaryDirectory

data = {"nama": "Ayu", "nilai": 90}
with TemporaryDirectory() as folder:
    path = Path(folder) / "murid.json"
    # JSON menyimpan dictionary dalam format teks yang dapat dibaca aplikasi lain.
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Dibaca kembali:", json.loads(path.read_text(encoding="utf-8")))