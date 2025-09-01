import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("lee.jpg")
img_rgb = img.convert("RGB")

img_array = np.array(img_rgb)

rows, cols, _ = img_array.shape
fig, ax = plt.subplots(figsize=(cols/4, rows/4)) 
ax.imshow(img_array)

for i in range(rows):
    for j in range(cols):
        r, g, b = img_array[i, j]
        ax.text(j, i, f"{r},{g},{b}",
                ha="center", va="center",
                fontsize=5, color="white",
                bbox=dict(facecolor="black", alpha=0.5, boxstyle="round,pad=0.2"))

ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
ax.grid(which="minor", color="gray", linewidth=0.5)
ax.tick_params(which="minor", size=0)

plt.title("Visualisasi Matriks Pixel RGB")
plt.show()

