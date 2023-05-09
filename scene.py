import os

import raster
import vector

layer_types = ['heightmap', 'path (line)',
               'building (line)', 'building (polygon)',
               'forest (line)', 'forest (polygon)',
               'forest (point)', 'water (line)',
               'water (polygon)']
layer_types_id = [0, 1, 1, 2, 1, 2, 3, 1, 2]
layer_symbol = ['🏞️', '🛣️', '🏠', '🧱', '🌿', '🌳', '🌲', '💧', '🌊']


class Scene:
    def __init__(self, crs='EPSG:2154'):
        # layer format : [filename, layer_type_id, layer_valid, layer_info, layer_view]
        self.layers = []
        self.layers_data = []
        self.crs = crs
        return

    def add_layer(self, filename, layer_type):
        self.layers.append([filename, layer_type, None, None, None])
        self.layers_data.append(None)

        if layer_types_id[layer_type] == 0:  # heightmap
            data, (bounds), (size) = raster.read(filename, crs=self.crs)
            view = raster.view(data)

            self.layers[-1][2] = True
            self.layers[-1][3] = bounds, size
            self.layers[-1][4] = view
            self.layers_data[-1] = data
        '''
        elif layer_types_id[layer_type] == 2: # polygon
            data = vector.read_polygon(filename, self.crs)
        '''
        '''
        else:
            vector.read()
        '''

    def get_layer(self, i):
        return self.layers[i]

    def get_layer_data(self, i):
        return self.layers_data[i]

    def remove_layer(self, i):
        del self.layers[i]
        del self.layers_data[i]
