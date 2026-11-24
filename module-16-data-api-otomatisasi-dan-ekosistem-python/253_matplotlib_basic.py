import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Backend Agg merender di memori tanpa membuat screenshot sebelum tahap akhir.
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 3], marker="o")
ax.set(title="Grafik Garis", xlabel="Hari", ylabel="Nilai")
fig.canvas.draw()
print("Grafik garis dirender:", fig.canvas.get_width_height())
plt.close(fig)