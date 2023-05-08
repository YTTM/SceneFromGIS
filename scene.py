import os

layer_types = ['heightmap', 'path (line)',
               'building (line)', 'building (polygon)',
               'forest (line)', 'forest (polygon)',
               'forest (point)', 'water (line)',
               'water (polygon)']
layer_symbol = ['🏞️', '🛣️', '🏠', '🧱', '🌳', '🌳', '🌳', '🌊', '🌊']


class Scene:
    def __init__(self):
        self.layers = []
        return

    def add_layer(self, filename, layer_type):
        self.layers.append([filename, layer_type])

    def remove_layer(self, i):
        del self.layers[i]
