import os
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
        return

    def add_layer(self, filename, layer_type):
        self.layers.append([filename, LayerType(layer_type), None, None, None, None, None])

        if layer_geom_type[layer_type] == LayerGeomType.HEIGHTMAP:
            data, (bounds), (size) = raster.read(filename, crs=self.crs)
            view = raster.view(data)

            self.layers[-1][2] = True
            self.layers[-1][3] = bounds, size
            self.layers[-1][4] = view
            self.layers[-1][5] = data
        '''
        elif layer_geom_type[layer_type] == LayerGeomType.POLYGON:
            data = vector.read_polygon(filename, self.crs)
        else:
            vector.read()
        '''

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

    def remove_layer(self, i):
        del self.layers[i]
