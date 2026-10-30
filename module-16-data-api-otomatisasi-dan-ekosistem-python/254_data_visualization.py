import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Bar chart membandingkan kategori; gambar belum disimpan dalam tahap uji.
ax.bar(["A", "B", "C"], [80, 90, 75])
ax.set(title="Nilai per Kelas", ylabel="Nilai")
fig.canvas.draw()
print("Diagram batang dirender:", fig.canvas.get_width_height())
plt.close(fig)