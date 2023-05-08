import numpy as np
import rasterio


def read(filename, crs='EPSG:2154'):
    elevation_gis = rasterio.open(filename)
    elevation_arr = elevation_gis.read()[0]

    y_min, x_min, y_max, x_max = elevation_gis.bounds
    z_min, z_max = elevation_arr.min(), elevation_arr.max()

    if elevation_gis.crs != crs:
        print(f'{elevation_gis.crs} != {crs}')
        raise AssertionError

    return elevation_arr, (x_min, x_max, y_min, y_max, z_min, z_max)


def view(data):
    mini, maxi = data.min(), data.max()
    # normalize 0 - 255
    return (((data - mini) / (maxi - mini))*255.0).astype(np.uint8)
