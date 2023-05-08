import os

layer_types = ['heightmap', 'path (line)',
               'building (line)', 'building (polygon)',
               'forest (line)', 'forest (polygon)',
               'forest (point)', 'water (line)',
               'water (polygon)']
layer_symbol = ['🏞️', '🛣️', '🏠', '🧱', '🌿', '🌳', '🌲', '💧', '🌊']

import raster

class Scene:
    def __init__(self):
        # layer format : [filename, layer_type, layer_valid, layer_view, layer_data]
        self.layers = []
        return

    def add_layer(self, filename, layer_type):
        self.layers.append([filename, layer_type, None, None, None])

        if layer_type == 0:
            data, (bounds) = raster.read(filename)
            x_min, x_max, y_min, y_max, z_min, z_max = bounds
            view = raster.view(data)

            self.layers[-1][2] = True
            self.layers[-1][3] = view
            self.layers[-1][4] = (data, bounds)
        '''
        else:
            vector.read()
        '''

    def remove_layer(self, i):
        del self.layers[i]
