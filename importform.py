# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importform.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.lineEdit_file_path = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.gridLayout.addWidget(self.lineEdit_file_path, 0, 1, 1, 1)
        self.pushButton_file_browser = QtWidgets.QPushButton(Dialog)
        self.pushButton_file_browser.setObjectName("pushButton_file_browser")
        self.gridLayout.addWidget(self.pushButton_file_browser, 0, 2, 1, 1)
        self.comboBox_layer_type = QtWidgets.QComboBox(Dialog)
        self.comboBox_layer_type.setObjectName("comboBox_layer_type")
        self.gridLayout.addWidget(self.comboBox_layer_type, 1, 1, 1, 2)
        self.label_file_info = QtWidgets.QLabel(Dialog)
        self.label_file_info.setText("")
        self.label_file_info.setObjectName("label_file_info")
        self.gridLayout.addWidget(self.label_file_info, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        self.pushButton_file_browser.clicked.connect(Dialog.pushbutton_file_browser_clicked) # type: ignore
        self.lineEdit_file_path.textChanged['QString'].connect(Dialog.linedit_file_path_textchanged) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Layer add"))
        self.label_2.setText(_translate("Dialog", "Layer type"))
        self.label_3.setText(_translate("Dialog", "File info"))
        self.label_1.setText(_translate("Dialog", "File path"))
        self.pushButton_file_browser.setText(_translate("Dialog", "📁"))
