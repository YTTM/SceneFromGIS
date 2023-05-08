import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import mainform
import importform

from scene import Scene


class DialogImport(QtWidgets.QDialog, importform.Ui_Dialog):
    def __init__(self):
        super(DialogImport, self).__init__()
        self.setupUi(self)
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


class MainWindow(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAcceptDrops(True)

    def add_layer_dialog(self, filename):
        dlg = DialogImport()
        dlg.set_file_path(filename)
        if dlg.exec():
            print(dlg.result)

    def event_pushbutton_remove_layer_clicked(self):
        print("event_pushButton_remove_layer_clicked")

    def event_pushbutton_gen_clicked(self):
        print("event_pushButton_gen_clicked")

    def event_pushbutton_exp_clicked(self):
        print("event_pushButton_exp_clicked")

    def event_listwidget_input_currentRowChanged(self, i):
        print(i)

    def event_action_new(self):
        print("event_action_new")

    def event_action_open(self):
        print("event_action_open")

    def event_action_save(self):
        print("event_action_save")

    def event_action_add(self):
        print("event_action_add")
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


def start(argv):
    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec()
