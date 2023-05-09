import os

import numpy as np

import scene

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import mainform
import importform


class MainWindow(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('SfGicon.png'))
        self.setAcceptDrops(True)

        self.current_scene = scene.Scene()

    def add_layer(self, filename, type):
        self.lineEdit_crs.setEnabled(False)
        self.current_scene.add_layer(filename, type)

        item = QListWidgetItem(f'{scene.layer_symbol[type]} {os.path.basename(filename)}', self.listWidget_input)
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
            self.graphicsView_2d.clear()
            return

        pixmap = qpixmap_from_grayscale_array(view)
        pixmap = pixmap.scaled(self.graphicsView_2d.geometry().width() - 25,
                               self.graphicsView_2d.geometry().height() - 25,
                               QtCore.Qt.KeepAspectRatio)
        self.graphicsView_2d.setPixmap(pixmap)

    def event_pushbutton_remove_layer_clicked(self):
        self.remove_layer(self.listWidget_input.currentRow())

    def event_pushbutton_gen_clicked(self):
        print("event_pushButton_gen_clicked")
        # todo: generate output

    def event_pushbutton_exp_clicked(self):
        print("event_pushButton_exp_clicked")
        # todo: export output

    def event_listwidget_input_currentrowchanged(self, i):
        # print("event_listwidget_input_currentRowChanged", i)
        if i < 0:
            return

        layer = self.current_scene.get_layer(i)
        self.statusbar.showMessage(layer[0])
        self.update_view_2d(layer[4])
        j = layer[1]
        self.label_type.setText(f'{scene.layer_symbol[j]} {scene.layer_types[j]}')

    def event_listwidget_input_doubleclicked(self, modelindex):
        i = self.listWidget_input.currentRow()
        layer = self.current_scene.get_layer(i)
        if layer[1] == 0:
            self.lineEdit_area.setText(str(layer[3][0]))

    def event_lineedit_crs_textchanged(self, crs):
        # print("event_lineedit_crs_textchanged")
        self.current_scene.crs = str(crs)

    def event_action_new(self):
        # todo: new project
        print("event_action_new")

    def event_action_open(self):
        # todo: load project (json)
        print("event_action_open")

    def event_action_save(self):
        # todo: save project (json)
        print("event_action_save")

    def event_action_add(self):
        # print("event_action_add")
        self.add_layer_dialog("")

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


class DialogImport(QtWidgets.QDialog, importform.Ui_Dialog):
    def __init__(self):
        super(DialogImport, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('SfGicon.png'))
        for l in range(len(scene.layer_types)):
            self.comboBox_layer_type.addItem(f'{scene.layer_symbol[l]} {scene.layer_types[l]}')

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
