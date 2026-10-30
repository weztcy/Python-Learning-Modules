from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class Produk(BaseModel):
    nama: str
    harga: int = Field(gt=0)


app = FastAPI()


@app.post("/produk")
def tambah(produk: Produk):
    return produk.model_dump()


if __name__ == "__main__":
    # Pydantic menolak harga tidak positif sebelum endpoint dipanggil.
    with TestClient(app) as klien:
        print("Valid:", klien.post("/produk", json={"nama": "Buku", "harga": 100}).json())
        print("Status tidak valid:", klien.post("/produk", json={"nama": "Buku", "harga": 0}).status_code)