import math
import numpy as np
import geopandas
import skimage


def read_polygon(filename, crs):
    # read gis
    gis = geopandas.read_file(filename)
    poly = []

    y_min, x_min, y_max, x_max = gis.total_bounds
    x_size, y_size = math.ceil(abs(x_min - x_max)), math.ceil(abs(y_min - y_max))

    if gis.crs != crs:
        print(f'{gis.crs} != {crs}')
        raise AssertionError

    for index, poi in gis.iterrows():
        # read polygon coords
        c, r = gis.loc[index, 'geometry'].exterior.coords.xy
        r = np.array(r)
        c = np.array(c)
        poly.append((r, c))

    return poly, (x_min, x_max, y_min, y_max), (x_size, y_size)


def view_polygon(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    # limit size of output for preview
    div = 1
    while (x_size/div) * (y_size/div) > 500 * 500:
        div += 1

    polygon_map = np.zeros((math.ceil(x_size/div), math.ceil(y_size/div)), dtype=np.uint8)

    for polygon in data:
        r = polygon[0]
        c = polygon[1]
        # change coords to current area
        r = (r - x_min)
        c = (c - y_min)
        # invert X
        r = r * -1 + x_size
        # preview divider
        r /= div
        c /= div
        # draw polygon
        rr, cc = skimage.draw.polygon(r, c)
        if any(rr < 0) or any(cc < 0) or any(rr >= polygon_map.shape[0]) or any(cc >= polygon_map.shape[1]):
            continue
        polygon_map[rr, cc] = 255

    return polygon_map
