import argparse
import os

import scene


def start(argv):
    parser = argparse.ArgumentParser(argv)

    parser.add_argument('elevation', type=str)
    parser.add_argument('--path-line', nargs='+', type=str, default=[])
    parser.add_argument('--building-line', nargs='+', type=str, default=[])
    parser.add_argument('--building-polygon', nargs='+', type=str, default=[])
    parser.add_argument('--forest-line', nargs='+', type=str, default=[])
    parser.add_argument('--forest-polygon', nargs='+', type=str, default=[])
    parser.add_argument('--forest-point', nargs='+', type=str, default=[])
    parser.add_argument('--water-line', nargs='+', type=str, default=[])
    parser.add_argument('--water-polygon', nargs='+', type=str, default=[])

    args = parser.parse_args()

    current_scene = scene.Scene()
    if os.path.isfile(args.elevation):
        current_scene.add_layer(args.elevation, 0)
    else:
        raise FileNotFoundError

    for f in args.path_line:
        if os.path.isfile(f):
            current_scene.add_layer(f, 1)
        else:
            raise FileNotFoundError
    for f in args.building_line:
        if os.path.isfile(f):
            current_scene.add_layer(f, 2)
        else:
            raise FileNotFoundError
    for f in args.building_polygon:
        if os.path.isfile(f):
            current_scene.add_layer(f, 3)
        else:
            raise FileNotFoundError
    for f in args.forest_line:
        if os.path.isfile(f):
            current_scene.add_layer(f, 4)
        else:
            raise FileNotFoundError
    for f in args.forest_polygon:
        if os.path.isfile(f):
            current_scene.add_layer(f, 5)
        else:
            raise FileNotFoundError
    for f in args.forest_point:
        if os.path.isfile(f):
            current_scene.add_layer(f, 6)
        else:
            raise FileNotFoundError
    for f in args.water_line:
        if os.path.isfile(f):
            current_scene.add_layer(f, 7)
        else:
            raise FileNotFoundError
    for f in args.water_polygon:
        if os.path.isfile(f):
            current_scene.add_layer(f, 8)
        else:
            raise FileNotFoundError
