import math
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


def build(data, bounds, size, block_size=1, z_factor=1):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    x_blocks = math.ceil(x_size / block_size)
    y_blocks = math.ceil(y_size / block_size)
    x_diff = x_blocks * block_size - x_size
    y_diff = y_blocks * block_size - y_size

    arr = np.zeros((x_blocks * block_size, y_blocks * block_size, 1), dtype=np.uint16)
    arr[0:data.shape[0], 0:data.shape[1], 0] = data * int(z_factor)

    logger.default.log(f'{"[raster][out]":16} {"output size":16} : {x_blocks * block_size} x {y_blocks * block_size}')
    logger.default.log(f'{"[raster][out]":16} {"block size":16} : {x_blocks} x {y_blocks}')

    return arr
