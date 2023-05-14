import numpy as np
import rasterio

import logger


def read(filename, crs):
    gis = rasterio.open(filename)
    arr = gis.read()[0]

    y_min, x_min, y_max, x_max = gis.bounds
    x_size = gis.height
    y_size = gis.width

    if gis.crs != crs:
        logger.default.log(f'{"[raster][crs]":16} {gis.crs} != {crs}')
        raise AssertionError

    return arr, (x_min, x_max, y_min, y_max), (x_size, y_size)


def view(data):
    mini, maxi = data.min(), data.max()
    # normalize 0 - 255
    return (((data - mini) / (maxi - mini))*255.0).astype(np.uint8)


def build(data, bounds, size, z_factor=1):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    z_min, z_max = data.min(), data.max()
    z_size = abs(z_max - z_min)
    data -= z_min

    arr = np.zeros((x_size, y_size, 1), dtype=np.uint16)
    arr[0:data.shape[0], 0:data.shape[1], 0] = data * float(z_factor)
    arr += 100 * z_factor

    return arr
