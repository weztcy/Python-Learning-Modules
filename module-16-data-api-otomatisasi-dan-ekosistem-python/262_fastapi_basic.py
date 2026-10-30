from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/halo/{nama}")
def halo(nama: str):
    return {"pesan": f"Halo, {nama}!"}


if __name__ == "__main__":
    # TestClient memanggil route tanpa server eksternal.
    with TestClient(app) as klien:
        print("Respons:", klien.get("/halo/Ayu").json())