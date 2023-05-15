import argparse
import os

from PIL import Image

import scene
import logger


def parse_layer_option(a):
    parser = argparse.ArgumentParser(a, prefix_chars='*')
    parser.add_argument('filename', type=str)
    parser.add_argument('*dilation', type=integer_range(0, 32), default=0)
    parser.add_argument('*flattening', type=integer_range(0, 32), default=0)
    parser.add_argument('*elevation-difference', type=integer_range(-100, 100), default=0)
    return parser.parse_args(a)


def parse_layers_option(args):
    for a in range(len(args)):
        args[a] = parse_layer_option(args[a])


def add_layer_with_options(args, scene_object, layer_type):
    for layer_args in args:
        f = layer_args.filename
        if os.path.isfile(f):
            opt = [None, None, layer_args.dilation, layer_args.flattening, layer_args.elevation_difference]
            scene_object.add_layer(f, layer_type, layer_option=opt, create_view=False)
        else:
            raise FileNotFoundError


def start(argv):
    parser = argparse.ArgumentParser(argv)
    parser.add_argument('elevation', type=str)
    parser.add_argument('output', type=str)
    parser.add_argument('--block-size', type=integer_range(1, 16384), default=256)
    parser.add_argument('--crs', type=str, default='EPSG:2154')
    parser.add_argument('--z-factor', type=integer_range(1, 10000), default=1)
    parser.add_argument('--elevation-smoothing', type=integer_range(0, 32), default=0)
    parser.add_argument('--path-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--building-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--building-polygon', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--forest-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--forest-polygon', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--forest-point', type=str, action='append')
    parser.add_argument('--water-line', nargs='+', type=str, default=[], action='append')
    parser.add_argument('--water-polygon', nargs='+', type=str, default=[], action='append')
    args = parser.parse_args()

    parse_layers_option(args.path_line)
    parse_layers_option(args.building_line)
    parse_layers_option(args.building_polygon)
    parse_layers_option(args.forest_line)
    parse_layers_option(args.forest_polygon)
    # parse_layers_option(args.forest_point)
    parse_layers_option(args.water_line)
    parse_layers_option(args.water_polygon)

    if not os.path.isdir(args.output):
        os.makedirs(args.output)
    if not os.path.isdir(args.output):
        raise NotADirectoryError

    cli_logger = logger.Logger(os.path.abspath(args.output) + f'/logs.txt')

    current_scene = scene.Scene(crs=args.crs, enable_build_cache=False)

    if os.path.isfile(args.elevation):
        opt = [args.z_factor, args.elevation_smoothing, None, None, None]
        current_scene.add_layer(args.elevation, scene.LayerType.HEIGHTMAP, layer_option=opt)
    else:
        raise FileNotFoundError

    add_layer_with_options(args.path_line, current_scene, scene.LayerType.PATH_LINE)
    add_layer_with_options(args.building_line, current_scene, scene.LayerType.BUILDING_LINE)
    add_layer_with_options(args.building_polygon, current_scene, scene.LayerType.BUILDING_POLYGON)
    add_layer_with_options(args.forest_line, current_scene, scene.LayerType.FOREST_LINE)
    add_layer_with_options(args.forest_polygon, current_scene, scene.LayerType.FOREST_POLYGON)
    for f in args.forest_point:
        if os.path.isfile(f):
            current_scene.add_layer(f, scene.LayerType.FOREST_POINT, create_view=False)
        else:
            raise FileNotFoundError
    add_layer_with_options(args.water_line, current_scene, scene.LayerType.WATER_LINE)
    add_layer_with_options(args.water_polygon, current_scene, scene.LayerType.WATER_POLYGON)

    gen = current_scene.build(0, args.block_size, generator=True, current_logger=cli_logger)
    for info in gen:
        duration, data_name = info
        cli_logger.log(f'{"[gui   ][gen]":16} {duration:8} {data_name}')

    if os.path.isdir(args.output):
        builds = current_scene.get_builds()
        for b in builds:
            im = Image.fromarray(b[1], 'I;16')
            im.save(os.path.abspath(args.output) + f'/{b[0]}.png')


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
