import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from osgeo import gdal
from scipy.signal import fftconvolve
from seedpod_ground_risk.data import geotiff_test_filepath


def gaussian_blur(in_array, size):
    # expand in_array to fit edge of kernel
    padded_array = np.pad(in_array, size, 'symmetric')
    # build kernel
    x, y = np.mgrid[-size:size + 1, -size:size + 1]
    g = np.exp(-(x**2 / float(size) + y**2 / float(size)))
    g = (g / g.sum()).astype(in_array.dtype)
    # do the Gaussian blur
    return fftconvolve(padded_array, g, mode='valid')


colours = ['#ffffff', '#fee9a6', '#f1a729', '#af5428', '#6a0c0d', '#6a0c0d']
bins = [0, 10, 150, 450, 900, 2000]
assert len(bins) == len(colours)
cmap = mpl.colors.ListedColormap(colours)
norm = mpl.colors.BoundaryNorm(boundaries=bins, ncolors=len(cmap.colors)-1)

dataset = gdal.Open(geotiff_test_filepath(), gdal.GA_ReadOnly)
band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()
arr_new = gaussian_blur(arr, 1)
plt.imshow(arr, cmap=cmap, norm=norm)
# plt.imshow(arr_new, cmap=cmap, norm=norm)
plt.title('SurfaceBuilder247 Output')
plt.colorbar()
plt.show()
