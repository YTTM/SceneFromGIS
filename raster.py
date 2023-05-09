import numpy as np
import rasterio


def read(filename, crs):
    gis = rasterio.open(filename)
    arr = gis.read()[0]

    y_min, x_min, y_max, x_max = gis.bounds
    x_size = gis.height
    y_size = gis.width

    if gis.crs != crs:
        print(f'{gis.crs} != {crs}')
        raise AssertionError

    return arr, (x_min, x_max, y_min, y_max), (x_size, y_size)


def view(data):
    mini, maxi = data.min(), data.max()
    # normalize 0 - 255
    return (((data - mini) / (maxi - mini))*255.0).astype(np.uint8)
