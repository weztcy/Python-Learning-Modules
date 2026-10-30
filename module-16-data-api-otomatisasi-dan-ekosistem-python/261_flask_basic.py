from flask import Flask

app = Flask(__name__)


@app.get("/")
def beranda():
    return "Halo dari Flask!"


if __name__ == "__main__":
    # Test client menjalankan route tanpa membuka port jaringan.
    with app.test_client() as klien:
        print("GET /:", klien.get("/").get_data(as_text=True))