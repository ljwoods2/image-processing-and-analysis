import matplotlib.pyplot as plt
from PIL import Image
import argparse
import numpy as np


# parser = argparse.ArgumentParser(description="Otsu thresholding")
# parser.add_argument("image", type=str, help="Path to the image")
# args = parser.parse_args()

# image = Image.open(args.image)
image = Image.open("otsu/sudoku4.jpg")

# convert to grayscale
if image.mode != "L":
    image = image.convert("L")

image_np = np.array(image)

flat = image_np.ravel()
freq, _ = np.histogram(flat, bins=256, range=(0, 256))

p = freq / len(flat)

# must do intensity + 1 bc min intensity is 1 but min index is 0
mu_k = np.array([(i + 1) * (prob) for i, prob in enumerate(p)])
mu_k = np.cumsum(mu_k)

omega_k = np.cumsum(p)

mu_t = mu_k[-1]

max_var_b = 0
threshold = 0
for k in range(0, 256):
    if omega_k[k] == 0 or omega_k[k] == 1:
        pass
    var_b = (mu_t * omega_k[k] - mu_k[k]) ** 2
    var_b /= omega_k[k] * (1 - omega_k[k])

    if var_b > max_var_b:
        threshold = k
        max_var_b = var_b

image_otsu_np = image_np.copy()

mask = image_np < (threshold + 1)
image_otsu_np[mask] = 0
image_otsu_np[~mask] = 255

print(threshold)
print(image_np)
print(image_otsu_np)

image_otsu = Image.fromarray(image_otsu_np, mode="L")

image_otsu.save("grayscale_image.png")
