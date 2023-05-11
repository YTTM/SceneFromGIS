import os
import time
from enum import IntEnum

import raster
import vector


class LayerType(IntEnum):
    HEIGHTMAP = 0
    PATH_LINE = 1
    BUILDING_LINE = 2
    BUILDING_POLYGON = 3
    FOREST_LINE = 4
    FOREST_POLYGON = 5
    FOREST_POINT = 6
    WATER_LINE = 7
    WATER_POLYGON = 8


class LayerGeomType(IntEnum):
    HEIGHTMAP = 0xA
    LINE = 0
    POLYGON = 1
    POINT = 2


layer_names = ['heightmap', 'path (line)',
               'building (line)', 'building (polygon)',
               'forest (line)', 'forest (polygon)',
               'forest (point)', 'water (line)',
               'water (polygon)']
layer_symbols = ['🏞️', '🛣️', '🧱', '🏠', '🌿', '🌳', '🌲', '💧', '🌊']
layer_geom_type = [LayerGeomType.HEIGHTMAP, LayerGeomType.LINE,
                   LayerGeomType.LINE, LayerGeomType.POLYGON,
                   LayerGeomType.LINE, LayerGeomType.POLYGON, LayerGeomType.POINT,
                   LayerGeomType.LINE, LayerGeomType.POLYGON]


class Scene:
    def __init__(self, crs='EPSG:2154'):
        # layer format : [filename, type, valid, info, view, data, option]
        self.layers = []
        self.crs = crs
        self.outputs = []
        return

    def add_layer(self, filename, layer_type, layer_option=None, create_view=True):
        self.layers.append([filename, LayerType(layer_type), None, None, None, None, None])

        if layer_geom_type[layer_type] == LayerGeomType.HEIGHTMAP:
            data, (bounds), (size) = raster.read(filename, crs=self.crs)
            view = raster.view(data)
            self.layers[-1][2] = True
            self.layers[-1][3] = bounds, size
            if create_view:
                self.layers[-1][4] = view
            self.layers[-1][5] = data
            if layer_option is None:
                layer_option = [1, 0, None, None, None]
            self.layers[-1][6] = layer_option
        elif layer_geom_type[layer_type] == LayerGeomType.POLYGON:
            data, (bounds), (size) = vector.read_polygon(filename, self.crs)
            view = vector.view_polygon(data, bounds, size)
            self.layers[-1][2] = True
            self.layers[-1][3] = bounds, size
            if create_view:
                self.layers[-1][4] = view
            self.layers[-1][5] = data
            if layer_option is None:
                layer_option = [None, None, 0, 0, 0]
            self.layers[-1][6] = layer_option
        elif layer_geom_type[layer_type] == LayerGeomType.LINE:
            data, (bounds), (size) = vector.read_line(filename, self.crs)
            view = vector.view_line(data, bounds, size)
            self.layers[-1][2] = True
            self.layers[-1][3] = bounds, size
            if create_view:
                self.layers[-1][4] = view
            self.layers[-1][5] = data
            if layer_option is None:
                layer_option = [None, None, 0, 0, 0]
            self.layers[-1][6] = layer_option
        elif layer_geom_type[layer_type] == LayerGeomType.POINT:
            data, (bounds), (size) = vector.read_point(filename, self.crs)
            view = vector.view_point(data, bounds, size)
            self.layers[-1][2] = True
            self.layers[-1][3] = bounds, size
            if create_view:
                self.layers[-1][4] = view
            self.layers[-1][5] = data
            if layer_option is None:
                layer_option = [None, None, 0, None, None]
            self.layers[-1][6] = layer_option

    def get_layer(self, i):
        return self.layers[i]

    def get_layer_filename(self, i):
        return self.layers[i][0]

    def get_layer_type(self, i):
        return self.layers[i][1]

    def get_layer_valid(self, i):
        return self.layers[i][2]

    def get_layer_info(self, i):
        return self.layers[i][3]

    def get_layer_view(self, i):
        return self.layers[i][4]

    def get_layer_data(self, i):
        return self.layers[i][5]

    def get_layer_option(self, i):
        return self.layers[i][6]

    def set_layer_option(self, layer, option_id, option_val):
        self.layers[layer][6][option_id] = option_val

    def remove_layer(self, i):
        del self.layers[i]

    def get_layers_by_type(self, type):
        layers = []
        for i in range(len(self.layers)):
            if self.layers[i][1] == type:
                layers.append(i)
        return layers

    def get_builds(self):
        return self.outputs

    def get_build_data(self, i):
        return self.outputs[i][1]

    def build(self, bounds, size, generator=False):
        self.outputs = []
        # HEIGHTMAP
        layers = self.get_layers_by_type(LayerType.HEIGHTMAP)
        for l in layers:
            t0 = time.time()
            data = raster.build(self.layers[l][5], bounds, size)
            self.outputs.append((f'HEIGHTMAP_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'HEIGHTMAP_{l:02}'
        # LINE
        layers = self.get_layers_by_type(LayerType.PATH_LINE)
        for l in layers:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            self.outputs.append((f'PATH_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'PATH_LINE_{l:02}',
        layers = self.get_layers_by_type(LayerType.BUILDING_LINE)
        for l in layers:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            self.outputs.append((f'BUILDING_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'BUILDING_LINE_{l:02}',
        layers = self.get_layers_by_type(LayerType.FOREST_LINE)
        for l in layers:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            self.outputs.append((f'FOREST_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'FOREST_LINE_{l:02}',
        layers = self.get_layers_by_type(LayerType.WATER_LINE)
        for l in layers:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            self.outputs.append((f'WATER_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'WATER_LINE_{l:02}',
        # POLYGON
        layers = self.get_layers_by_type(LayerType.BUILDING_POLYGON)
        for l in layers:
            t0 = time.time()
            data = vector.build_polygon(self.layers[l][5], bounds, size)
            self.outputs.append((f'BUILDING_POLYGON_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'BUILDING_POLYGON_{l:02}',
        layers = self.get_layers_by_type(LayerType.FOREST_POLYGON)
        for l in layers:
            t0 = time.time()
            data = vector.build_polygon(self.layers[l][5], bounds, size)
            self.outputs.append((f'FOREST_POLYGON_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'FOREST_POLYGON_{l:02}',
        layers = self.get_layers_by_type(LayerType.WATER_POLYGON)
        for l in layers:
            t0 = time.time()
            data = vector.build_polygon(self.layers[l][5], bounds, size)
            self.outputs.append((f'WATER_POLYGON_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'WATER_POLYGON_{l:02}',
        # POINT
        layers = self.get_layers_by_type(LayerType.FOREST_POINT)
        for l in layers:
            t0 = time.time()
            data = vector.build_point(self.layers[l][5], bounds, size)
            self.outputs.append((f'FOREST_POINT_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'FOREST_POINT_{l:02}',


def geom_type(layer_type):
    return layer_geom_type[layer_type]
