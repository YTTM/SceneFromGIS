import argparse
import os

import scene


def parse_layer_option(a):
    parser = argparse.ArgumentParser(a, prefix_chars='*')
    parser.add_argument('filename', type=str)
    parser.add_argument('*dilation', type=integer_range(0, 32), default=0)
    parser.add_argument('*flattening', type=integer_range(0, 32), default=0)
    parser.add_argument('*elevation-difference', type=integer_range(0, 32), default=0)
    return parser.parse_args(a)


def parse_layers_option(args):
    for a in range(len(args)):
        args[a] = parse_layer_option(args[a])


def start(argv):
    parser = argparse.ArgumentParser(argv)
    parser.add_argument('elevation', type=str)
    parser.add_argument('--z-factor', type=integer_range(1, 10000), default=1)
    parser.add_argument('--elevation-smoothing', type=integer_range(0, 32), default=0)
    parser.add_argument('--path-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--building-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--building-polygon', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--forest-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--forest-polygon', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--forest-point', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--water-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--water-polygon', nargs='+', type=str, default=[], action='append')
    args = parser.parse_args()

    parse_layers_option(args.path_line)
    parse_layers_option(args.building_line)
    parse_layers_option(args.building_polygon)
    parse_layers_option(args.forest_line)
    parse_layers_option(args.forest_polygon)
    parse_layers_option(args.forest_point)
    parse_layers_option(args.water_line)
    parse_layers_option(args.water_polygon)

    current_scene = scene.Scene()

    if os.path.isfile(args.elevation):
        current_scene.add_layer(args.elevation, 0)
        current_scene.set_layer_option()
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


# source based on : https://stackoverflow.com/a/64259328
def float_range(mini, maxi):
    def float_range_checker(arg):
        try:
            f = float(arg)
        except ValueError:
            raise argparse.ArgumentTypeError("must be a floating point number")
        if f < mini or f > maxi:
            raise argparse.ArgumentTypeError("must be in range [" + str(mini) + " .. " + str(maxi)+"]")
        return f

    return float_range_checker


def integer_range(mini, maxi):
    def integer_range_checker(arg):
        try:
            i = int(arg)
        except ValueError:
            raise argparse.ArgumentTypeError("must be an integer number")
        if i < mini or i > maxi:
            raise argparse.ArgumentTypeError("must be in range [" + str(mini) + " .. " + str(maxi)+"]")
        return i

    return integer_range_checker
