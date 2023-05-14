import math
import numpy as np
import geopandas
import skimage

import logger


def read_gis(filename, crs):
    # read gis
    gis = geopandas.read_file(filename)

    y_min, x_min, y_max, x_max = gis.total_bounds
    x_size, y_size = math.ceil(abs(x_min - x_max)), math.ceil(abs(y_min - y_max))

    if gis.crs != crs:
        logger.default.log(f'{"[vector][crs]":16} {gis.crs} != {crs}')
        raise AssertionError

    return gis, (x_min, x_max, y_min, y_max), (x_size, y_size)


def read_polygon(filename, crs):
    gis, bounds, size = read_gis(filename, crs)
    poly = []

    for index, poi in gis.iterrows():
        # read polygon coords
        c, r = gis.loc[index, 'geometry'].exterior.coords.xy
        r = np.array(r)
        c = np.array(c)
        poly.append((r, c))

    return poly, bounds, size


def read_line(filename, crs):
    gis, bounds, size = read_gis(filename, crs)
    lines = []

    # read all lines
    for index, poi in gis.iterrows():
        line = []
        # read line coords
        coords = gis.loc[index, 'geometry'].coords
        for c in range(len(coords)):
            if len(coords[c]) == 2:
                y0, x0 = coords[c]
                z0 = 0
            else:
                y0, x0, z0 = coords[c]
            line.append((x0, y0, z0))
        lines.append(line)

    return lines, bounds, size


def read_point(filename, crs):
    gis, bounds, size = read_gis(filename, crs)
    points = []

    # read all points
    for index, poi in gis.iterrows():
        coords = gis.loc[index, 'geometry'].coords
        for c in range(len(coords)):
            if len(coords[c]) == 2:
                y0, x0 = coords[c]
                z0 = 0
            else:
                y0, x0, z0 = coords[c]
            points.append((x0, y0, z0))

    return points, bounds, size


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


def view_line(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    # limit size of output for preview
    div = 1
    while (x_size/div) * (y_size/div) > 500 * 500:
        div += 1

    line_map = np.zeros((math.ceil(x_size/div), math.ceil(y_size/div)), dtype=np.uint8)

    for line in data:
        for c in range(len(line) -1):
            # read coords
            x0, y0, z0 = line[c]
            x1, y1, z1 = line[c + 1]
            # change coords to current area
            x0 = (x0 - x_min)
            y0 = (y0 - y_min)
            x1 = (x1 - x_min)
            y1 = (y1 - y_min)
            # invert X
            x0 = x0 * -1 + x_size
            x1 = x1 * -1 + x_size
            # preview divider
            x0 /= div
            x1 /= div
            y0 /= div
            y1 /= div
            # draw line
            rr, cc = skimage.draw.line(round(x0), round(y0), round(x1), round(y1))
            if any(rr < 0) or any(cc < 0) or any(rr >= line_map.shape[0]) or any(cc >= line_map.shape[1]):
                continue
            line_map[rr, cc] = 255

    return line_map


def view_point(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    # limit size of output for preview
    div = 1
    while (x_size/div) * (y_size/div) > 500 * 500:
        div += 1

    point_map = np.zeros((math.ceil(x_size/div), math.ceil(y_size/div)), dtype=np.uint8)

    for point in data:
        # read coords
        x0, y0, z0 = point
        # change coords to current area
        x0 = (x0 - x_min)
        y0 = (y0 - y_min)
        # invert X
        x0 = x0 * -1 + x_size
        # preview divider
        x0 /= div
        y0 /= div
        # draw point
        x0 = round(x0)
        y0 = round(y0)
        if x0 < 0 or y0 < 0 or x0 >= point_map.shape[0] or y0 >= point_map.shape[1]:
            continue
        point_map[x0, y0] = 255

    return point_map


def build_polygon(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    # create empty map
    polygon_map = np.zeros((x_size, y_size, 1), dtype=np.uint16)

    for polygon in data:
        r = polygon[0]
        c = polygon[1]
        # change coords to current area
        r = (r - x_min)
        c = (c - y_min)
        # invert X
        r = r * -1 + x_size
        # draw polygon
        rr, cc = skimage.draw.polygon(r, c)
        if any(rr < 0) or any(cc < 0) or any(rr >= polygon_map.shape[0]) or any(cc >= polygon_map.shape[1]):
            continue
        polygon_map[rr, cc] = 65535

    return polygon_map


def build_line(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    # create empty map
    line_map = np.zeros((x_size, y_size, 1), dtype=np.uint16)

    for line in data:
        for c in range(len(line) -1):
            # read coords
            x0, y0, z0 = line[c]
            x1, y1, z1 = line[c + 1]
            # change coords to current area
            x0 = (x0 - x_min)
            y0 = (y0 - y_min)
            x1 = (x1 - x_min)
            y1 = (y1 - y_min)
            # invert X
            x0 = x0 * -1 + x_size
            x1 = x1 * -1 + x_size
            # draw line
            rr, cc = skimage.draw.line(round(x0), round(y0), round(x1), round(y1))
            if any(rr < 0) or any(cc < 0) or any(rr >= line_map.shape[0]) or any(cc >= line_map.shape[1]):
                continue
            line_map[rr, cc] = 65535

    return line_map


def build_point(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    # create empty map
    point_map = np.zeros((x_size, y_size, 1), dtype=np.uint16)

    for point in data:
        # read coords
        x0, y0, z0 = point
        # change coords to current area
        x0 = (x0 - x_min)
        y0 = (y0 - y_min)
        # invert X
        x0 = x0 * -1 + x_size
        # draw point
        x0 = round(x0)
        y0 = round(y0)
        if x0 < 0 or y0 < 0 or x0 >= point_map.shape[0] or y0 >= point_map.shape[1]:
            continue
        point_map[x0, y0] = 65535

    return point_map


def build_line_path(data, bounds, size):
    x_min, x_max, y_min, y_max = bounds
    x_size, y_size = size

    paths = []
    paths_dir = []

    # path point
    for line in data:
        path = []
        for c in range(len(line)):
            # read coords
            x0, y0, z0 = line[c]
            # change coords to current area
            x0 = (x0 - x_min)
            y0 = (y0 - y_min)
            # invert X
            x0 = x0 * -1 + x_size
            # x0 += x_diff
            # ignore output points
            if x0 < 0 or x0 > x_size or y0 < 0 or y0 > y_size:
                continue
            path.append((y0, x0, z0))
        if len(path) < 2:
            continue
        paths.append(path)

    # path directional vector
    for path in paths:
        path_dir = []
        for p_ in range(len(path)):
            p0 = np.array(path[p_])
            if p_ == 0:
                d1 = np.array(path[p_+1] - p0) / 2
                d2 = -d1
            elif p_ == len(path) - 1:
                d2 = np.array(p0 - path[p_-1]) / 2
                d1 = -d2
            else:
                d1 = np.array(path[p_+1] - p0) / 2
                d2 = np.array(p0 - path[p_-1]) / 2
            path_dir.append((d1, d2))
        paths_dir.append(path_dir)

    return paths, paths_dir
