def heightmap_to_point_list(data):
    # todo: performance improvement
    points = []
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            points.append([y, -x, data[x, y]])
    return points
