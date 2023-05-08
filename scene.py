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
        # layer format : [filename, layer_type, layer_valid, layer_view, layer_data]
        self.layers = []
        self.crs = crs
        return

    def add_layer(self, filename, layer_type):
        self.layers.append([filename, layer_type, None, None, None])

        if layer_types_id[layer_type] == 0: # heightmap
            data, (bounds) = raster.read(filename, crs=self.crs)
            x_min, x_max, y_min, y_max, z_min, z_max = bounds
            view = raster.view(data)

            self.layers[-1][2] = True
            self.layers[-1][3] = view
            self.layers[-1][4] = (data, bounds)
            return bounds
        '''
        elif layer_types_id[layer_type] == 2: # polygon
            data = vector.read_polygon(filename, self.crs)
        '''
        '''
        else:
            vector.read()
        '''
        return

    def remove_layer(self, i):
        del self.layers[i]
