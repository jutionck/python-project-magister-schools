import numpy as np
# fungsi ini sudah deprecated, sebagai gantinya menggunakan Pillow
# from scipy.misc import imread, imresize
from PIL import Image
import matplotlib.pyplot as plt

# Membaca gambar menggunakan Pillow
img = np.array(Image.open('image.jpg'))

# Menerapkan tint = red
img_tinted = img * [1, 0, 0]
# green
# img_tinted = img * [0, 1, 0]

# Menampilkan gambar asli dan gambar yang telah di-tint
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))
plt.title("Tinted Image")

plt.show()