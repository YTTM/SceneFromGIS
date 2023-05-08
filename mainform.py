# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_right = QtWidgets.QGridLayout()
        self.gridLayout_right.setObjectName("gridLayout_right")
        self.checkBox_gen_2d = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gen_2d.setObjectName("checkBox_gen_2d")
        self.gridLayout_right.addWidget(self.checkBox_gen_2d, 1, 0, 1, 1)
        self.checkBox_gen_3d = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gen_3d.setObjectName("checkBox_gen_3d")
        self.gridLayout_right.addWidget(self.checkBox_gen_3d, 2, 0, 1, 1)
        self.listView_output = QtWidgets.QListView(self.centralwidget)
        self.listView_output.setObjectName("listView_output")
        self.gridLayout_right.addWidget(self.listView_output, 0, 0, 1, 1)
        self.pushButton_gen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gen.setObjectName("pushButton_gen")
        self.gridLayout_right.addWidget(self.pushButton_gen, 3, 0, 1, 1)
        self.pushButton_exp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exp.setObjectName("pushButton_exp")
        self.gridLayout_right.addWidget(self.pushButton_exp, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_right, 0, 2, 2, 1)
        self.graphicsView_2d = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.graphicsView_2d.sizePolicy().hasHeightForWidth())
        self.graphicsView_2d.setSizePolicy(sizePolicy)
        self.graphicsView_2d.setObjectName("graphicsView_2d")
        self.gridLayout.addWidget(self.graphicsView_2d, 0, 1, 1, 1)
        self.view_3d = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.view_3d.sizePolicy().hasHeightForWidth())
        self.view_3d.setSizePolicy(sizePolicy)
        self.view_3d.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_3d.setFrameShadow(QtWidgets.QFrame.Raised)
        self.view_3d.setObjectName("view_3d")
        self.gridLayout.addWidget(self.view_3d, 1, 1, 1, 1)
        self.gridLayout_left = QtWidgets.QGridLayout()
        self.gridLayout_left.setObjectName("gridLayout_left")
        self.pushButton_remove_layer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove_layer.setObjectName("pushButton_remove_layer")
        self.gridLayout_left.addWidget(self.pushButton_remove_layer, 1, 0, 1, 1)
        self.listWidget_input = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_input.setObjectName("listWidget_input")
        self.gridLayout_left.addWidget(self.listWidget_input, 0, 0, 1, 1)
        self.gridLayout_properties = QtWidgets.QGridLayout()
        self.gridLayout_properties.setObjectName("gridLayout_properties")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName("comboBox_1")
        self.gridLayout_properties.addWidget(self.comboBox_1, 0, 1, 1, 1)
        self.label_id_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_id_1.setObjectName("label_id_1")
        self.gridLayout_properties.addWidget(self.label_id_1, 0, 0, 1, 1)
        self.label_uint_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_uint_2.setText("")
        self.label_uint_2.setObjectName("label_uint_2")
        self.gridLayout_properties.addWidget(self.label_uint_2, 1, 0, 1, 1)
        self.spinBox_uint_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_uint_2.setMaximum(10000)
        self.spinBox_uint_2.setObjectName("spinBox_uint_2")
        self.gridLayout_properties.addWidget(self.spinBox_uint_2, 1, 1, 1, 1)
        self.label_ushort_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_ushort_3.setText("")
        self.label_ushort_3.setObjectName("label_ushort_3")
        self.gridLayout_properties.addWidget(self.label_ushort_3, 2, 0, 1, 1)
        self.spinBox_ushort_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ushort_3.setMaximum(100)
        self.spinBox_ushort_3.setObjectName("spinBox_ushort_3")
        self.gridLayout_properties.addWidget(self.spinBox_ushort_3, 2, 1, 1, 1)
        self.label_ushort_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_ushort_4.setText("")
        self.label_ushort_4.setObjectName("label_ushort_4")
        self.gridLayout_properties.addWidget(self.label_ushort_4, 3, 0, 1, 1)
        self.spinBox_ushort_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ushort_4.setMaximum(100)
        self.spinBox_ushort_4.setObjectName("spinBox_ushort_4")
        self.gridLayout_properties.addWidget(self.spinBox_ushort_4, 3, 1, 1, 1)
        self.label_ushort_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_ushort_5.setText("")
        self.label_ushort_5.setObjectName("label_ushort_5")
        self.gridLayout_properties.addWidget(self.label_ushort_5, 4, 0, 1, 1)
        self.spinBox_ushort_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ushort_5.setMaximum(100)
        self.spinBox_ushort_5.setObjectName("spinBox_ushort_5")
        self.gridLayout_properties.addWidget(self.spinBox_ushort_5, 4, 1, 1, 1)
        self.gridLayout_left.addLayout(self.gridLayout_properties, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_left, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuLayer = QtWidgets.QMenu(self.menubar)
        self.menuLayer.setObjectName("menuLayer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.menuProject.addAction(self.actionNew)
        self.menuProject.addAction(self.actionOpen)
        self.menuProject.addAction(self.actionSave)
        self.menuLayer.addAction(self.actionAdd)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuLayer.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_remove_layer.clicked.connect(MainWindow.event_pushbutton_remove_layer_clicked) # type: ignore
        self.pushButton_gen.clicked.connect(MainWindow.event_pushbutton_gen_clicked) # type: ignore
        self.pushButton_exp.clicked.connect(MainWindow.event_pushbutton_exp_clicked) # type: ignore
        self.listWidget_input.currentRowChanged['int'].connect(MainWindow.event_listwidget_input_currentrowchanged) # type: ignore
        self.actionNew.triggered.connect(MainWindow.event_action_new) # type: ignore
        self.actionOpen.triggered.connect(MainWindow.event_action_open) # type: ignore
        self.actionSave.triggered.connect(MainWindow.event_action_save) # type: ignore
        self.actionAdd.triggered.connect(MainWindow.event_action_add) # type: ignore
        self.comboBox_1.activated['int'].connect(MainWindow.event_comboBox_1_activated) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listWidget_input, self.pushButton_remove_layer)
        MainWindow.setTabOrder(self.pushButton_remove_layer, self.comboBox_1)
        MainWindow.setTabOrder(self.comboBox_1, self.spinBox_uint_2)
        MainWindow.setTabOrder(self.spinBox_uint_2, self.spinBox_ushort_3)
        MainWindow.setTabOrder(self.spinBox_ushort_3, self.spinBox_ushort_4)
        MainWindow.setTabOrder(self.spinBox_ushort_4, self.spinBox_ushort_5)
        MainWindow.setTabOrder(self.spinBox_ushort_5, self.graphicsView_2d)
        MainWindow.setTabOrder(self.graphicsView_2d, self.listView_output)
        MainWindow.setTabOrder(self.listView_output, self.checkBox_gen_2d)
        MainWindow.setTabOrder(self.checkBox_gen_2d, self.checkBox_gen_3d)
        MainWindow.setTabOrder(self.checkBox_gen_3d, self.pushButton_gen)
        MainWindow.setTabOrder(self.pushButton_gen, self.pushButton_exp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SceneFromGIS"))
        self.checkBox_gen_2d.setText(_translate("MainWindow", "Generate 2D maps"))
        self.checkBox_gen_3d.setText(_translate("MainWindow", "Generate 3D obj"))
        self.pushButton_gen.setText(_translate("MainWindow", "Generate"))
        self.pushButton_exp.setText(_translate("MainWindow", "Export"))
        self.pushButton_remove_layer.setText(_translate("MainWindow", "Remove layer"))
        self.label_id_1.setText(_translate("MainWindow", "Type"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuLayer.setTitle(_translate("MainWindow", "Layer"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
