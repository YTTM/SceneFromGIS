import numpy as np
import rasterio


def read(filename, crs):
    elevation_gis = rasterio.open(filename)
    elevation_arr = elevation_gis.read()[0]

    y_min, x_min, y_max, x_max = elevation_gis.bounds
    x_size = elevation_gis.height
    y_size = elevation_gis.width

    if elevation_gis.crs != crs:
        print(f'{elevation_gis.crs} != {crs}')
        raise AssertionError

    return elevation_arr, (x_min, x_max, y_min, y_max), (x_size, y_size)


def view(data):
    mini, maxi = data.min(), data.max()
    # normalize 0 - 255
    return (((data - mini) / (maxi - mini))*255.0).astype(np.uint8)
