import os
import json
import time

import numpy as np
from PIL import Image
import pyvista as pv

import scene

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import mainform
import importform
import logger


class MainWindow(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icons/SfGicon.png'))
        self.setAcceptDrops(True)
        self.view_3d.set_background('E0E0E0')
        self.view_3d.show_axes()

        self.current_scene = scene.Scene()
        logger.default.add_callback((self.listWidget_log.addItem, ''))

    def add_layer(self, filename, type, layer_option=None):
        self.lineEdit_crs.setEnabled(False)
        self.current_scene.add_layer(filename, type, layer_option)

        item = QListWidgetItem(f'{scene.layer_symbols[type]} {os.path.basename(filename)}', self.listWidget_input)
        self.listWidget_input.addItem(item)

    def remove_layer(self, i):
        if i < 0:
            return

        self.listWidget_input.takeItem(i)
        self.current_scene.remove_layer(i)

    def add_layer_dialog(self, filename):
        dlg = DialogImport()
        dlg.set_file_path(filename)
        if dlg.exec():
            self.add_layer(dlg.result['filename'], dlg.result['type'])

    def update_view_2d(self, view):
        if view is None:
            self.graphicsView_2d_input.clear()
            return

        pixmap = qpixmap_from_grayscale_array(view)
        pixmap = pixmap.scaled(self.graphicsView_2d_input.geometry().width() - 25,
                               self.graphicsView_2d_input.geometry().height() - 25,
                               QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2d_input.setPixmap(pixmap)

    def update_view_2d_output(self, view):
        if view is None:
            self.graphicsView_2d_output.clear()
            return

        pixmap = qpixmap_from_grayscale_array(view)
        pixmap = pixmap.scaled(self.graphicsView_2d_output.geometry().width() - 25,
                               self.graphicsView_2d_output.geometry().height() - 25,
                               QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2d_output.setPixmap(pixmap)

    def event_pushbutton_remove_layer_clicked(self):
        self.remove_layer(self.listWidget_input.currentRow())

    def event_pushbutton_gen_clicked(self):
        self.listWidget_output.clear()
        area = self.lineEdit_area.text()
        # todo: this is not safe
        area = eval(area)

        if type(area) != tuple or len(area) != 2 or len(area[0]) != 4 or len(area[1]) != 2:
            QMessageBox.critical(self,
                                 "Invalid area",
                                 f"{area} is not a valid area")
        else:
            if not self.checkBox_gen_2d.isChecked():
                return

            bounds, size = area
            gen = self.current_scene.build(bounds, size, generator=True)
            for info in gen:
                duration, data_name = info
                self.log(f'{"[gui   ][gen]":16} {duration:8} {data_name}')
            builds = self.current_scene.get_builds()
            for b in builds:
                self.listWidget_output.addItem(str(b[0]))

            # 3D view
            if not self.action3D_view.isChecked():
                return
            self.view_3d.clear()
            if len(self.current_scene.get_layers_by_types([scene.LayerType.HEIGHTMAP])) > 0:
                t0 = time.time()
                data = builds[0][1][:, :, 0]
                # heightmap to point list
                points = []
                for x in range(len(data[0])):
                    for y in range(len(data[1])):
                        points.append([y, -x, data[x, y]])
                cloud = pv.PolyData(np.array(points).astype(np.float32))
                cloud['point_color'] = cloud.points[:, 2]
                self.view_3d.add_points(cloud)
                self.view_3d.reset_camera()
                t1 = time.time()
                duration = f'{round(t1 - t0, 2)} s'
                self.log(f'{"[gui   ][3d ]":16} {duration:8} {"3D VIEW"}')

    def event_pushbutton_exp_clicked(self):
        foldername = QFileDialog.getExistingDirectory(self, "Export folder")
        if len(foldername) > 0:
            if os.path.isdir(foldername):
                builds = self.current_scene.get_builds()
                for b in builds:
                    im = Image.fromarray(b[1], 'I;16')
                    im.save(foldername + f'/{b[0]}.png')
            else:
                QMessageBox.critical(self,
                                     "Not a folder",
                                     f"{foldername} is not a valid folder")

    def event_listwidget_input_currentrowchanged(self, i):
        self.label_type.setText('')
        self.spinBox_z_factor.setEnabled(False)
        self.spinBox_elevation_smoothing.setEnabled(False)
        self.spinBox_dilation.setEnabled(False)
        self.spinBox_flattening.setEnabled(False)
        self.spinBox_elevation_diff.setEnabled(False)

        if i < 0:
            return
        self.statusbar.showMessage(self.current_scene.get_layer_filename(i))
        self.update_view_2d(self.current_scene.get_layer_view(i))
        j = self.current_scene.get_layer_type(i)
        self.label_type.setText(f'{scene.layer_symbols[j]} {scene.layer_names[j]}')
        # layer properties
        opt = self.current_scene.get_layer_option(i)

        if scene.geom_type(j) == scene.LayerGeomType.HEIGHTMAP:
            self.spinBox_z_factor.setValue(opt[0])
            self.spinBox_elevation_smoothing.setValue(opt[1])
            self.spinBox_z_factor.setEnabled(True)
            self.spinBox_elevation_smoothing.setEnabled(True)
        elif scene.geom_type(j) == scene.LayerGeomType.LINE:
            self.spinBox_dilation.setValue(opt[2])
            self.spinBox_flattening.setValue(opt[3])
            self.spinBox_elevation_diff.setValue(opt[4])
            self.spinBox_dilation.setEnabled(True)
            self.spinBox_flattening.setEnabled(True)
            self.spinBox_elevation_diff.setEnabled(True)
        elif scene.geom_type(j) == scene.LayerGeomType.POLYGON:
            self.spinBox_dilation.setValue(opt[2])
            self.spinBox_flattening.setValue(opt[3])
            self.spinBox_elevation_diff.setValue(opt[4])
            self.spinBox_dilation.setEnabled(True)
            self.spinBox_flattening.setEnabled(True)
            self.spinBox_elevation_diff.setEnabled(True)
        elif scene.geom_type(j) == scene.LayerGeomType.POINT:
            self.spinBox_dilation.setValue(opt[2])
            self.spinBox_dilation.setEnabled(True)

    def event_set_option(self, option_id, option_val):
        layer = self.listWidget_input.currentRow()
        if layer < 0:
            return
        self.current_scene.set_layer_option(layer, option_id, option_val)

    def event_spinBox_z_factor(self, j):
        self.event_set_option(0, j)

    def event_spinBox_elevation_smoothing(self, j):
        self.event_set_option(1, j)

    def event_spinBox_dilation(self, j):
        self.event_set_option(2, j)

    def event_spinBox_flattening(self, j):
        self.event_set_option(3, j)

    def event_spinBox_elevation_diff(self, j):
        self.event_set_option(4, j)

    def event_listwidget_input_doubleclicked(self, modelindex):
        i = self.listWidget_input.currentRow()
        layer_type = self.current_scene.get_layer_type(i)
        if layer_type == scene.LayerType.HEIGHTMAP:
            self.lineEdit_area.setText(str(self.current_scene.get_layer_info(i)))

    def event_listwidget_output_currentrowchanged(self, i):
        if i < 0:
            return
        self.update_view_2d_output((self.current_scene.get_build_data(i)[:,:,0]/256).astype(np.uint8))

    def event_lineedit_crs_textchanged(self, crs):
        self.current_scene.crs = str(crs)

    def event_action_new(self):
        del self.current_scene
        self.current_scene = scene.Scene()
        self.lineEdit_crs.setEnabled(True)
        self.lineEdit_area.setText('')
        self.label_type.setText('')
        self.listWidget_input.clear()
        self.listWidget_output.clear()

    def event_action_open(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", None, "(*.json)")
        if len(filename[0]) > 0:
            self.event_action_new()
            with open(filename[0], 'r') as outfile:
                data = json.load(outfile)

            self.lineEdit_area.setText(data['area'])
            self.lineEdit_crs.setText(data['crs'])
            self.lineEdit_crs.setEnabled(False)
            self.current_scene.crs = data['crs']

            i = 0
            while str(i) in data:
                x = data[str(i)]
                self.add_layer(x['file'], x['type'], layer_option=x['opts'])
                i += 1

    def event_action_save(self):
        filename = QFileDialog.getSaveFileName(self, "Open file", None, "(*.json)")
        if len(filename[0]) > 0:
            data = dict()
            data['crs'] = self.current_scene.crs
            data['area'] = self.lineEdit_area.text()

            for i in range(len(self.current_scene.layers)):
                data[i] = {'file': self.current_scene.get_layer_filename(i),
                           'type': int(self.current_scene.get_layer_type(i)),
                           'opts': self.current_scene.get_layer_option(i)}

            with open(filename[0], 'w') as outfile:
                json.dump(data, outfile)

    def event_action_add(self):
        self.add_layer_dialog("")

    def event_reset_3d_camera(self):
        self.view_3d.reset_camera()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            if os.path.isfile(f):
                self.add_layer_dialog(f)
            else:
                QMessageBox.critical(self,
                                     "Not a file",
                                     f"{f} is not a valid file")

    def log(self, message):
        logger.default.log(message)
        # self.listWidget_log.addItem(message)
        self.listWidget_log.scrollToBottom()


class DialogImport(QtWidgets.QDialog, importform.Ui_Dialog):
    def __init__(self):
        super(DialogImport, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icons/SfGicon.png'))
        for l in range(len(scene.layer_names)):
            self.comboBox_layer_type.addItem(f'{scene.layer_symbols[l]} {scene.layer_names[l]}')

        self.result = {'filename': None,
                       'type': None}

    def guess_file_type(self):
        filename = os.path.basename(self.lineEdit_file_path.text())
        guess = 0
        if '.tif' in filename:
            guess = 0
        elif 'path' in filename or 'road' in filename:
            guess = 1
        elif 'build' in filename:
            guess = 2
        elif 'forest' in filename or 'flor' in filename:
            guess = 4
        elif 'water' in filename or 'river' in filename:
            guess = 7

        if guess > 0:
            if 'line' in filename:
                guess += 0
            elif 'poly' in filename:
                guess += 1
            elif 'point' in filename:
                guess += 2

        self.comboBox_layer_type.setCurrentIndex(guess)

    def update_file_info(self):
        filename = self.lineEdit_file_path.text()
        basename = os.path.basename(filename)
        if os.path.isfile(filename):
            if os.path.splitext(basename)[-1] in ['.tif', '.shp']:
                result = f'✔️ {basename} seems to be valid'
            else:
                result = f'❓ {basename} has an unusual extension'
        else:
            result = f'❌ {basename} is not a valid file'
        self.label_file_info.setText(result)

    def set_file_path(self, filename):
        self.lineEdit_file_path.setText(filename)
        self.guess_file_type()

    def linedit_file_path_textchanged(self):
        filename = os.path.basename(self.lineEdit_file_path.text())
        self.update_file_info()

    def pushbutton_file_browser_clicked(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", None, None)
        if len(filename[0]) > 0:
            self.lineEdit_file_path.setText(filename[0])
            self.guess_file_type()

    def accept(self):
        self.result['filename'] = self.lineEdit_file_path.text()
        self.result['type'] = self.comboBox_layer_type.currentIndex()
        super(DialogImport, self).accept()


def qpixmap_from_rgb_array(view):
    height, width, channel = view.shape
    bytesPerLine = 3 * width
    qImg = QImage(view.tobytes(), width, height, bytesPerLine, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qImg)
    return pixmap


def qpixmap_from_grayscale_array(view):
    view = np.stack((view,) * 3, axis=-1)
    return qpixmap_from_rgb_array(view)


def start(argv):
    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec()
