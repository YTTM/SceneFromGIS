from PyQt5 import QtCore, QtGui, QtWidgets
import mainform


class MainWindow(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


def start(argv):
    app = QtWidgets.QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec()
