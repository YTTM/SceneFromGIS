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


layer_geom_type = [LayerGeomType.HEIGHTMAP, LayerGeomType.LINE,
                   LayerGeomType.LINE, LayerGeomType.POLYGON,
                   LayerGeomType.LINE, LayerGeomType.POLYGON, LayerGeomType.POINT,
                   LayerGeomType.LINE, LayerGeomType.POLYGON]

layer_names = ['heightmap', 'path (line)',
               'building (line)', 'building (polygon)',
               'forest (line)', 'forest (polygon)',
               'forest (point)', 'water (line)',
               'water (polygon)']
layer_symbols = ['🏞️', '🛣️', '🧱', '🏠', '🌿', '🌳', '🌲', '💧', '🌊']
layer_names_ = [str(s).upper().replace(' ', '_').replace('(', '').replace(')', '') for s in layer_names]


class Scene:
    def __init__(self, crs='EPSG:2154'):
        # layer format : [filename, type, valid, info, view, data, option]
        self.layers = []
        self.crs = crs
        self.outputs = []
        return

    def last_layer_setup(self, valid=False, info=None, view=None, data=None, option=None):
        self.layers[-1][2] = valid
        self.layers[-1][3] = info
        self.layers[-1][4] = view
        self.layers[-1][5] = data
        self.layers[-1][6] = option

    def add_layer(self, filename, layer_type, layer_option=None, create_view=True):
        self.layers.append([filename, LayerType(layer_type), None, None, None, None, None])
        view = None
        if layer_geom_type[layer_type] == LayerGeomType.HEIGHTMAP:
            data, (bounds), (size) = raster.read(filename, crs=self.crs)
            if create_view:
                view = raster.view(data)
            if layer_option is None:
                layer_option = [1, 0, None, None, None]
            self.last_layer_setup(True, (bounds, size), view, data, layer_option)
        elif layer_geom_type[layer_type] == LayerGeomType.POLYGON:
            data, (bounds), (size) = vector.read_polygon(filename, self.crs)
            if create_view:
                view = vector.view_polygon(data, bounds, size)
            if layer_option is None:
                layer_option = [None, None, 0, 0, 0]
            self.last_layer_setup(True, (bounds, size), view, data, layer_option)
        elif layer_geom_type[layer_type] == LayerGeomType.LINE:
            data, (bounds), (size) = vector.read_line(filename, self.crs)
            if create_view:
                view = vector.view_line(data, bounds, size)
            if layer_option is None:
                layer_option = [None, None, 0, 0, 0]
            self.last_layer_setup(True, (bounds, size), view, data, layer_option)
        elif layer_geom_type[layer_type] == LayerGeomType.POINT:
            data, (bounds), (size) = vector.read_point(filename, self.crs)
            if create_view:
                view = vector.view_point(data, bounds, size)
            if layer_option is None:
                layer_option = [None, None, 0, None, None]
            self.last_layer_setup(True, (bounds, size), view, data, layer_option)

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

    def get_layers_by_types(self, type):
        layers = []
        for i in range(len(self.layers)):
            if self.layers[i][1] in type:
                layers.append(i)
        return layers

    def get_builds(self):
        return self.outputs

    def get_build_data(self, i):
        return self.outputs[i][1]

    def build_layer_initial(self, layer, bounds, size):
        t0 = time.time()
        layer_type = self.get_layer_type(layer)

        # check layer type to handle result
        if geom_type(layer_type) == LayerGeomType.HEIGHTMAP:
            data = raster.build(self.get_layer_data(layer), bounds, size)
        elif geom_type(layer_type) == LayerGeomType.LINE:
            data = vector.build_line(self.get_layer_data(layer), bounds, size)
        elif geom_type(layer_type) == LayerGeomType.POLYGON:
            data = vector.build_polygon(self.get_layer_data(layer), bounds, size)
        elif geom_type(layer_type) == LayerGeomType.POINT:
            data = vector.build_point(self.get_layer_data(layer), bounds, size)
        else:
            raise NotImplementedError

        t1 = time.time()
        return data, (f'{round(t1-t0, 2)} s', f'{str(layer_names_[layer_type])}_{layer:02}')

    def build_postprocess_z_factor(self, layer, data):
        t0 = time.time()

        z_factor = self.get_layer_option(layer)[0]
        z_factor = max(z_factor, 1)
        data = data * z_factor

        t1 = time.time()
        return data, (f'{round(t1-t0, 2)} s', f'{str(layer_names_[self.get_layer_type(layer)])}_{layer:02} Z Factor')

    def build_postprocess_dilation(self, layer, data, dilation):
        t0 = time.time()

        data = skimage.morphology.binary_dilation(data[:, :, 0], footprint=skimage.morphology.disk(dilation))
        data = np.clip(edt.edt(data), 0, dilation).astype(np.float32) / dilation
        data = (np.expand_dims(data, -1) * 65535).astype(np.uint16)

        t1 = time.time()
        return data, (f'{round(t1-t0, 2)} s', f'{str(layer_names_[self.get_layer_type(layer)])}_{layer:02} Dilation')

    def build_postprocess_flattening(self, layer, data_vector, data_map, flattening):
        t0 = time.time()

        alternative_height = auto_median(data_map[:, :, 0], skimage.morphology.disk(flattening))
        alternative_height = np.expand_dims(alternative_height.astype(np.uint16), -1)
        data_map = np.where(data_vector == 0, data_map, alternative_height)

        t1 = time.time()
        return data_map, (f'{round(t1-t0, 2)} s', f'{str(layer_names_[self.get_layer_type(layer)])}_{layer:02} Flattening')

    def build_postprocess_elevation_difference(self, layer, data_vector, data_map, difference, ):
        t0 = time.time()

        z_factor = self.get_layer_option(layer)[0]
        z_factor = max(z_factor, 1)

        heightmap = data_map
        data_map += ((data_vector.astype(np.float32) / 65535) * z_factor * difference).astype(np.uint16)

        t1 = time.time()
        return data_map, (f'{round(t1-t0, 2)} s', f'{str(layer_names_[self.get_layer_type(layer)])}_{layer:02} Elevation Difference')

    def build_postprocess_elevation_smoothing(self, layer, data, elevation_smoothing):
        t0 = time.time()

        kernel = skimage.morphology.disk(elevation_smoothing).astype(np.float64)
        kernel /= np.sum(kernel)
        data = scipy.signal.convolve2d(data[:, :, 0], kernel, mode='same', boundary='symm')
        data = np.expand_dims(data.astype(np.uint16), -1)

        t1 = time.time()
        return data, (f'{round(t1-t0, 2)} s', f'{str(layer_names_[self.get_layer_type(layer)])}_{layer:02} Elevation Smoothing')

    def build(self, bounds, size, generator=False):
        self.outputs = []
        tmp_outputs = {}

        # Map initial build
        for l_type in LayerType:
            layers = self.get_layers_by_types([l_type])
            for l in layers:
                data, info = self.build_layer_initial(l, bounds, size)
                tmp_outputs[l] = data
                if generator:
                    yield info

        # Post process
        # Layers collections
        layers_heightmap = self.get_layers_by_types([LayerType.HEIGHTMAP])
        layers_non_forest = self.get_layers_by_types([LayerType.PATH_LINE,
                                                      LayerType.BUILDING_LINE,
                                                      LayerType.BUILDING_POLYGON,
                                                      LayerType.WATER_LINE,
                                                      LayerType.WATER_POLYGON])
        layers_vectors_ = layers_non_forest + self.get_layers_by_types([LayerType.FOREST_LINE,
                                                                        LayerType.FOREST_POLYGON])
        layers_vectors = layers_vectors_ + self.get_layers_by_types([LayerType.FOREST_POINT])
        layers_forest = self.get_layers_by_types([LayerType.FOREST_LINE,
                                                  LayerType.FOREST_POLYGON,
                                                  LayerType.FOREST_POINT])

        # Z Factor
        for l in layers_heightmap:
            tmp_outputs[l], info = self.build_postprocess_z_factor(l, tmp_outputs[l])
            if generator:
                yield info

        # Dilation
        for l in layers_vectors:
            dilation = self.get_layer_option(l)[2]
            if dilation <= 0:
                continue
            tmp_outputs[l], info = self.build_postprocess_dilation(l, tmp_outputs[l], dilation)
            if generator:
                yield info

        # Flattening
        for l in layers_vectors_:
            flattening = self.get_layer_option(l)[3]
            if flattening <= 0:
                continue
            for hmapl in layers_heightmap:
                tmp_outputs[hmapl], info = self.build_postprocess_flattening(l, tmp_outputs[l], tmp_outputs[hmapl], flattening)
                if generator:
                    yield info

        # Elevation difference
        for l in layers_vectors_:
            difference = self.get_layer_option(l)[4]
            if difference == 0:
                continue
            for hmapl in layers_heightmap:
                tmp_outputs[hmapl], info = self.build_postprocess_elevation_difference(hmapl, tmp_outputs[l], tmp_outputs[hmapl], difference)
                if generator:
                    yield info

        # Elevation smoothing
        for l in layers_heightmap:
            elevation_smoothing = self.get_layer_option(l)[1]
            if elevation_smoothing <= 0:
                continue
            tmp_outputs[l], info = self.build_postprocess_elevation_smoothing(l, tmp_outputs[l], elevation_smoothing)
            if generator:
                yield info

        # Output
        for type in LayerType:
            layers = self.get_layers_by_types([type])
            for l in layers:
                self.outputs.append((f'{str(layer_names_[self.get_layer_type(l)])}_{l:02}', tmp_outputs[l]))

        # Heightmap edges
        for l in layers_heightmap:
            data = tmp_outputs[l]
            data = skimage.filters.sobel(data)
            data = ((np.clip(data, 0, 0.0005) / 0.0005) * 65535).astype(np.uint16)
            self.outputs.append((f'HEIGHTMAP_EDGES_{l:02}', data))

        # Remove forest from non forest layers
        for l in layers_forest:
            data = tmp_outputs[l]
            for l_neg in layers_non_forest:
                data = np.logical_and(data > 0, tmp_outputs[l_neg] <= 0)
            data = skimage.morphology.binary_erosion(data[:, :, 0], footprint=skimage.morphology.disk(2))
            data = (np.expand_dims(data, -1).astype(np.uint16) * 65535)
            tmp_outputs[l] = data
        for l in layers_forest:
            self.outputs.append((f'FOREST_CLEAN_{l:02}', tmp_outputs[l]))

        # Grass : negative of all non forest layers
        data = np.zeros((size[0], size[1], 1), dtype=np.uint16)
        for layer in layers_non_forest:
            data = np.logical_or(data, tmp_outputs[layer] > 0)
        data = (1 - data.astype(np.uint16))*65535
        self.outputs.append((f'GRASS', data))


def geom_type(layer_type):
    return layer_geom_type[layer_type]
