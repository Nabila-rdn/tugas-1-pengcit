from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"D:\TUGAS SEMESTER 3\PengCit\lee.jpg")

mode = img.mode
if mode == "RGB":
    jenis = "Citra RGB (3 channel warna: Red, Green, Blue)"
elif mode == "L":
    jenis = "Citra Grayscale (1 channel, intensitas 0-255)"
elif mode == "1":
    jenis = "Citra Biner (1 channel, hanya 0 atau 1)"
else:
    jenis = f"Citra dengan mode lain: {mode}"

print("=== Informasi Citra ===")
print("Jenis citra   :", jenis)
print("Resolusi      :", img.size[0], "x", img.size[1], "pixel (lebar x tinggi)")
print("Jumlah pixel  :", img.size[0] * img.size[1])

new_size = (20, 20)
img_resized = img.resize(new_size)

matrix = np.array(img_resized)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img_resized, cmap="gray" if mode != "RGB" else None)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if mode == "RGB":
            text = str(tuple(matrix[i, j]))
            color = "white" if np.mean(matrix[i, j]) < 128 else "black"
        else:
            text = str(matrix[i, j])
            color = "red" if matrix[i, j] < 128 else "black"

        ax.text(j, i, text, ha="center", va="center", color=color, fontsize=6)

ax.set_title(f"Visualisasi Matriks Pixel ({jenis})")
ax.axis("off")
plt.show()

