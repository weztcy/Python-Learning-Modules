import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def ringkasan(data):
    return data.groupby("kategori")["nilai"].sum()


if __name__ == "__main__":
    data = pd.DataFrame({"kategori": ["A", "A", "B"], "nilai": [10, 20, 15]})
    hasil = ringkasan(data)
    fig, ax = plt.subplots()
    hasil.plot.bar(ax=ax, title="Ringkasan Kategori")
    # Render dalam memori; belum mengambil screenshot atau membuka jendela.
    fig.canvas.draw()
    print("Total kategori:", hasil.to_dict())
    plt.close(fig)