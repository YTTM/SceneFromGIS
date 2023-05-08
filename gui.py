from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import mainform
import importform

from scene import Scene


class DialogImport(QtWidgets.QDialog, importform.Ui_Dialog):
    def __init__(self):
        super(DialogImport, self).__init__()
        self.setupUi(self)
        self.result = {'filename': None,
                       'type': None}

    def set_file_path(self, filename):
        self.lineEdit_file_path.setText(filename)

    def pushbutton_file_browser_clicked(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", None, None)
        if len(filename[0]) > 0:
            self.lineEdit_file_path.setText(filename[0])

    def accept(self):
        self.result['filename'] = self.lineEdit_file_path.text()
        self.result['type'] = self.comboBox_layer_type.currentIndex()
        super(DialogImport, self).accept()


class MainWindow(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.scene = Scene()

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


def start(argv):
    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec()
