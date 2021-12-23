from skimage.transform import probabilistic_hough_line
from skimage.feature import canny
from skimage.draw import line
from skimage import data
from pathlib import Path
import os
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import open3d as o3d


# Constructing test image
image = np.zeros((255, 255))

# image[0][2]=255
# image[1][2]=255
image[25][25]=255
image[100][100]=255
image[174][174]=255

# idx = np.arange(25, 175)
#first line
# image[idx, idx] = 255
# #2nd line
# image[line(45, 25, 25, 175)] = 255
lines = probabilistic_hough_line(image, threshold=10, line_length=5,
                                 line_gap=3)

# Generating figure 2
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap=cm.gray)
ax[0].set_title('Input image')

ax[2].imshow(image * 0)
for line in lines:
    p0, p1 = line
    ax[2].plot((p0[0], p1[0]), (p0[1], p1[1]))
ax[2].set_xlim((0, image.shape[1]))
ax[2].set_ylim((image.shape[0], 0))
ax[2].set_title('Probabilistic Hough')
for a in ax:
    a.set_axis_off()

plt.tight_layout()
plt.show()



    