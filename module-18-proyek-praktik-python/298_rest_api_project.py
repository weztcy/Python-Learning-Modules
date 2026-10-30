from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel


class Tugas(BaseModel):
    judul: str


app = FastAPI()
data = {}


@app.post("/tugas/{nomor}")
def simpan(nomor: int, tugas: Tugas):
    data[nomor] = tugas.judul
    return {"id": nomor, "judul": tugas.judul}


@app.get("/tugas/{nomor}")
def ambil(nomor: int):
    if nomor not in data:
        raise HTTPException(status_code=404, detail="Tidak ditemukan")
    return {"id": nomor, "judul": data[nomor]}


if __name__ == "__main__":
    # TestClient menjalankan API tanpa server publik; data hanya di memori proses.
    with TestClient(app) as klien:
        print("POST:", klien.post("/tugas/1", json={"judul": "Belajar"}).json())
        print("GET:", klien.get("/tugas/1").json())