import os
import time
from enum import IntEnum

import numpy as np
import edt
import skimage.morphology
import scipy.signal

from morphology import auto_median
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
        tmp_outputs = {}
        # Map build
        # HEIGHTMAP
        layers_heightmap = self.get_layers_by_type(LayerType.HEIGHTMAP)
        for l in layers_heightmap:
            t0 = time.time()
            data = raster.build(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'HEIGHTMAP_{l:02}'
        # LINE
        layers_path_line = self.get_layers_by_type(LayerType.PATH_LINE)
        for l in layers_path_line:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'PATH_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'PATH_LINE_{l:02}',
        layers_building_line = self.get_layers_by_type(LayerType.BUILDING_LINE)
        for l in layers_building_line:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'BUILDING_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'BUILDING_LINE_{l:02}',
        layers_forest_line = self.get_layers_by_type(LayerType.FOREST_LINE)
        for l in layers_forest_line:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'FOREST_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'FOREST_LINE_{l:02}',
        layers_water_line = self.get_layers_by_type(LayerType.WATER_LINE)
        for l in layers_water_line:
            t0 = time.time()
            data = vector.build_line(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'WATER_LINE_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'WATER_LINE_{l:02}',
        # POLYGON
        layers_building_polygon = self.get_layers_by_type(LayerType.BUILDING_POLYGON)
        for l in layers_building_polygon:
            t0 = time.time()
            data = vector.build_polygon(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'BUILDING_POLYGON_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'BUILDING_POLYGON_{l:02}',
        layers_forest_polygon = self.get_layers_by_type(LayerType.FOREST_POLYGON)
        for l in layers_forest_polygon:
            t0 = time.time()
            data = vector.build_polygon(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'FOREST_POLYGON_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'FOREST_POLYGON_{l:02}',
        layers_water_polygon = self.get_layers_by_type(LayerType.WATER_POLYGON)
        for l in layers_water_polygon:
            t0 = time.time()
            data = vector.build_polygon(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'WATER_POLYGON_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'WATER_POLYGON_{l:02}',
        # POINT
        layers_forest_point = self.get_layers_by_type(LayerType.FOREST_POINT)
        for l in layers_forest_point:
            t0 = time.time()
            data = vector.build_point(self.layers[l][5], bounds, size)
            tmp_outputs[l] = data
            # self.outputs.append((f'FOREST_POINT_{l:02}', data))
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', f'FOREST_POINT_{l:02}',

        # Post process
        # Z Factor
        for l in layers_heightmap:
            z_factor = self.get_layer_option(l)[0]
            z_factor = max(z_factor, 1)
            t0 = time.time()
            data = tmp_outputs[l]

            data = data * z_factor

            tmp_outputs[l] = data
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', 'Z Factor'

        # line, polygon and point layers
        tmp_layers = layers_path_line + layers_building_line + layers_forest_line + layers_water_line +\
                     layers_building_polygon + layers_forest_polygon + layers_water_polygon +\
                     layers_forest_point
        # Dilation
        for l in tmp_layers:
            dilation = self.get_layer_option(l)[2]
            if dilation <= 0:
                continue
            t0 = time.time()
            data = tmp_outputs[l]

            data = skimage.morphology.binary_dilation(data[:, :, 0],
                                                      footprint=skimage.morphology.disk(dilation))
            data = np.clip(edt.edt(data), 0, dilation).astype(np.float32) / dilation
            data = (np.expand_dims(data, -1) * 65535).astype(np.uint16)

            tmp_outputs[l] = data
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', 'Dilation'

        # line and polygon layers
        tmp_layers = layers_path_line + layers_building_line + layers_forest_line + layers_water_line +\
                     layers_building_polygon + layers_forest_polygon + layers_water_polygon
        # Flattening
        for l in tmp_layers:
            flattening = self.get_layer_option(l)[3]
            if flattening <= 0:
                continue
            t0 = time.time()
            data = tmp_outputs[l]

            for hmapl in layers_heightmap:
                heightmap = tmp_outputs[hmapl]
                alternative_height = auto_median(heightmap[:, :, 0], skimage.morphology.disk(flattening))
                alternative_height = np.expand_dims(alternative_height.astype(np.uint16), -1)
                tmp_outputs[hmapl] = np.where(data == 0, heightmap, alternative_height)

            tmp_outputs[l] = data
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', 'Flattening'

        # Elevation difference
        for l in tmp_layers:
            difference = self.get_layer_option(l)[4]
            if difference == 0:
                continue
            t0 = time.time()
            data = tmp_outputs[l]

            for hmapl in layers_heightmap:
                z_factor = self.get_layer_option(hmapl)[0]
                z_factor = max(z_factor, 1)
                heightmap = tmp_outputs[hmapl]
                heightmap += ((data.astype(np.float32) / 65535) * z_factor * difference).astype(np.uint16)
                tmp_outputs[hmapl] = heightmap

            tmp_outputs[l] = data
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', 'Elevation difference'

        # Elevation smoothing
        for l in layers_heightmap:
            elevation_smoothing = self.get_layer_option(l)[1]
            if elevation_smoothing <= 0:
                continue
            t0 = time.time()
            data = tmp_outputs[l]

            kernel = skimage.morphology.disk(elevation_smoothing).astype(np.float64)
            kernel /= np.sum(kernel)
            data = scipy.signal.convolve2d(data[:, :, 0], kernel, mode='same', boundary='symm')
            data = np.expand_dims(data.astype(np.uint16), -1)

            tmp_outputs[l] = data
            t1 = time.time()
            if generator:
                yield f'{round(t1-t0, 2)} s', 'Elevation smoothing', f'HEIGHTMAP_{l:02}'

        # Output
        for l in layers_heightmap:
            self.outputs.append((f'HEIGHTMAP_{l:02}', tmp_outputs[l]))
        for l in layers_path_line:
            self.outputs.append((f'PATH_LINE_{l:02}', tmp_outputs[l]))
        for l in layers_building_line:
            self.outputs.append((f'BUILDING_LINE_{l:02}', tmp_outputs[l]))
        for l in layers_forest_line:
            self.outputs.append((f'FOREST_LINE_{l:02}', tmp_outputs[l]))
        for l in layers_water_line:
            self.outputs.append((f'WATER_LINE_{l:02}', tmp_outputs[l]))
        for l in layers_building_polygon:
            self.outputs.append((f'BUILDING_POLYGON_{l:02}', tmp_outputs[l]))
        for l in layers_forest_polygon:
            self.outputs.append((f'FOREST_POLYGON_{l:02}', tmp_outputs[l]))
        for l in layers_water_polygon:
            self.outputs.append((f'WATER_POLYGON_{l:02}', tmp_outputs[l]))
        for l in layers_forest_point:
            self.outputs.append((f'FOREST_POINT_{l:02}', tmp_outputs[l]))


def geom_type(layer_type):
    return layer_geom_type[layer_type]
