import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

# # Import an image from ms paint

# img = Image.open('cspace.png')
# img = ImageOps.grayscale(img)

# np_img = np.array(img)
# np_img = ~np_img        # invert B&W
# np_img[np_img > 0] = 1

# plt.set_cmap('binary')
# plt.imshow(img)

# # Save image
# np.save('cspace.npy', np_img)

# Read image
grid = np.load('cspace.npy')
plt.imshow(grid, cmap='binary')
plt.tight_layout()
plt.show()