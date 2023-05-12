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
        self.graphicsView_2d_output = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.graphicsView_2d_output.sizePolicy().hasHeightForWidth())
        self.graphicsView_2d_output.setSizePolicy(sizePolicy)
        self.graphicsView_2d_output.setText("")
        self.graphicsView_2d_output.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView_2d_output.setObjectName("graphicsView_2d_output")
        self.gridLayout.addWidget(self.graphicsView_2d_output, 0, 2, 1, 1)
        self.graphicsView_2d_input = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.graphicsView_2d_input.sizePolicy().hasHeightForWidth())
        self.graphicsView_2d_input.setSizePolicy(sizePolicy)
        self.graphicsView_2d_input.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView_2d_input.setObjectName("graphicsView_2d_input")
        self.gridLayout.addWidget(self.graphicsView_2d_input, 0, 1, 1, 1)
        self.gridLayout_left = QtWidgets.QGridLayout()
        self.gridLayout_left.setObjectName("gridLayout_left")
        self.label_layers = QtWidgets.QLabel(self.centralwidget)
        self.label_layers.setAlignment(QtCore.Qt.AlignCenter)
        self.label_layers.setObjectName("label_layers")
        self.gridLayout_left.addWidget(self.label_layers, 2, 0, 1, 1)
        self.label_layer_properties = QtWidgets.QLabel(self.centralwidget)
        self.label_layer_properties.setAlignment(QtCore.Qt.AlignCenter)
        self.label_layer_properties.setObjectName("label_layer_properties")
        self.gridLayout_left.addWidget(self.label_layer_properties, 5, 0, 1, 1)
        self.pushButton_remove_layer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove_layer.setObjectName("pushButton_remove_layer")
        self.gridLayout_left.addWidget(self.pushButton_remove_layer, 4, 0, 1, 1)
        self.gridLayout_properties = QtWidgets.QGridLayout()
        self.gridLayout_properties.setObjectName("gridLayout_properties")
        self.label_z_factor = QtWidgets.QLabel(self.centralwidget)
        self.label_z_factor.setObjectName("label_z_factor")
        self.gridLayout_properties.addWidget(self.label_z_factor, 1, 0, 1, 1)
        self.label_elevation_smoothing = QtWidgets.QLabel(self.centralwidget)
        self.label_elevation_smoothing.setObjectName("label_elevation_smoothing")
        self.gridLayout_properties.addWidget(self.label_elevation_smoothing, 2, 0, 1, 1)
        self.spinBox_flattening = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_flattening.setEnabled(False)
        self.spinBox_flattening.setMaximum(100)
        self.spinBox_flattening.setObjectName("spinBox_flattening")
        self.gridLayout_properties.addWidget(self.spinBox_flattening, 4, 1, 1, 1)
        self.spinBox_z_factor = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_z_factor.setEnabled(False)
        self.spinBox_z_factor.setMinimum(1)
        self.spinBox_z_factor.setMaximum(10000)
        self.spinBox_z_factor.setObjectName("spinBox_z_factor")
        self.gridLayout_properties.addWidget(self.spinBox_z_factor, 1, 1, 1, 1)
        self.label_flattening = QtWidgets.QLabel(self.centralwidget)
        self.label_flattening.setObjectName("label_flattening")
        self.gridLayout_properties.addWidget(self.label_flattening, 4, 0, 1, 1)
        self.label_dilation = QtWidgets.QLabel(self.centralwidget)
        self.label_dilation.setObjectName("label_dilation")
        self.gridLayout_properties.addWidget(self.label_dilation, 3, 0, 1, 1)
        self.spinBox_dilation = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_dilation.setEnabled(False)
        self.spinBox_dilation.setMaximum(100)
        self.spinBox_dilation.setObjectName("spinBox_dilation")
        self.gridLayout_properties.addWidget(self.spinBox_dilation, 3, 1, 1, 1)
        self.label_type_ = QtWidgets.QLabel(self.centralwidget)
        self.label_type_.setObjectName("label_type_")
        self.gridLayout_properties.addWidget(self.label_type_, 0, 0, 1, 1)
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setMinimumSize(QtCore.QSize(0, 20))
        self.label_type.setText("")
        self.label_type.setObjectName("label_type")
        self.gridLayout_properties.addWidget(self.label_type, 0, 1, 1, 1)
        self.spinBox_elevation_smoothing = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_elevation_smoothing.setEnabled(False)
        self.spinBox_elevation_smoothing.setMaximum(100)
        self.spinBox_elevation_smoothing.setObjectName("spinBox_elevation_smoothing")
        self.gridLayout_properties.addWidget(self.spinBox_elevation_smoothing, 2, 1, 1, 1)
        self.label_elevation_diff = QtWidgets.QLabel(self.centralwidget)
        self.label_elevation_diff.setObjectName("label_elevation_diff")
        self.gridLayout_properties.addWidget(self.label_elevation_diff, 5, 0, 1, 1)
        self.spinBox_elevation_diff = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_elevation_diff.setEnabled(False)
        self.spinBox_elevation_diff.setMinimum(-1000)
        self.spinBox_elevation_diff.setMaximum(1000)
        self.spinBox_elevation_diff.setObjectName("spinBox_elevation_diff")
        self.gridLayout_properties.addWidget(self.spinBox_elevation_diff, 5, 1, 1, 1)
        self.gridLayout_left.addLayout(self.gridLayout_properties, 6, 0, 1, 1)
        self.gridLayout_project_setup = QtWidgets.QGridLayout()
        self.gridLayout_project_setup.setObjectName("gridLayout_project_setup")
        self.lineEdit_area = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_area.setObjectName("lineEdit_area")
        self.gridLayout_project_setup.addWidget(self.lineEdit_area, 1, 1, 1, 1)
        self.lineEdit_crs = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_crs.setObjectName("lineEdit_crs")
        self.gridLayout_project_setup.addWidget(self.lineEdit_crs, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_project_setup.addWidget(self.label, 1, 0, 1, 1)
        self.label_crs = QtWidgets.QLabel(self.centralwidget)
        self.label_crs.setObjectName("label_crs")
        self.gridLayout_project_setup.addWidget(self.label_crs, 0, 0, 1, 1)
        self.gridLayout_left.addLayout(self.gridLayout_project_setup, 1, 0, 1, 1)
        self.listWidget_input = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_input.setObjectName("listWidget_input")
        self.gridLayout_left.addWidget(self.listWidget_input, 3, 0, 1, 1)
        self.label_project = QtWidgets.QLabel(self.centralwidget)
        self.label_project.setAlignment(QtCore.Qt.AlignCenter)
        self.label_project.setObjectName("label_project")
        self.gridLayout_left.addWidget(self.label_project, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_left, 0, 0, 2, 1)
        self.gridLayout_right = QtWidgets.QGridLayout()
        self.gridLayout_right.setObjectName("gridLayout_right")
        self.checkBox_gen_2d = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gen_2d.setChecked(True)
        self.checkBox_gen_2d.setObjectName("checkBox_gen_2d")
        self.gridLayout_right.addWidget(self.checkBox_gen_2d, 1, 0, 1, 1)
        self.checkBox_gen_3d = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gen_3d.setEnabled(False)
        self.checkBox_gen_3d.setObjectName("checkBox_gen_3d")
        self.gridLayout_right.addWidget(self.checkBox_gen_3d, 2, 0, 1, 1)
        self.listWidget_output = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_output.setObjectName("listWidget_output")
        self.gridLayout_right.addWidget(self.listWidget_output, 0, 0, 1, 1)
        self.pushButton_gen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gen.setObjectName("pushButton_gen")
        self.gridLayout_right.addWidget(self.pushButton_gen, 3, 0, 1, 1)
        self.pushButton_exp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exp.setObjectName("pushButton_exp")
        self.gridLayout_right.addWidget(self.pushButton_exp, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_right, 0, 3, 2, 1)
        self.view_3d = QtInteractor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.view_3d.sizePolicy().hasHeightForWidth())
        self.view_3d.setSizePolicy(sizePolicy)
        self.view_3d.setObjectName("view_3d")
        self.gridLayout.addWidget(self.view_3d, 1, 1, 1, 2)
        self.listWidget_log = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_log.setMaximumSize(QtCore.QSize(16777215, 80))
        self.listWidget_log.setObjectName("listWidget_log")
        self.gridLayout.addWidget(self.listWidget_log, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuLayer = QtWidgets.QMenu(self.menubar)
        self.menuLayer.setObjectName("menuLayer")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
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
        self.actionShow_log = QtWidgets.QAction(MainWindow)
        self.actionShow_log.setCheckable(True)
        self.actionShow_log.setChecked(True)
        self.actionShow_log.setObjectName("actionShow_log")
        self.menuProject.addAction(self.actionNew)
        self.menuProject.addAction(self.actionOpen)
        self.menuProject.addAction(self.actionSave)
        self.menuLayer.addAction(self.actionAdd)
        self.menuView.addAction(self.actionShow_log)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuLayer.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_remove_layer.clicked.connect(MainWindow.event_pushbutton_remove_layer_clicked) # type: ignore
        self.pushButton_gen.clicked.connect(MainWindow.event_pushbutton_gen_clicked) # type: ignore
        self.pushButton_exp.clicked.connect(MainWindow.event_pushbutton_exp_clicked) # type: ignore
        self.listWidget_input.currentRowChanged['int'].connect(MainWindow.event_listwidget_input_currentrowchanged) # type: ignore
        self.actionNew.triggered.connect(MainWindow.event_action_new) # type: ignore
        self.actionOpen.triggered.connect(MainWindow.event_action_open) # type: ignore
        self.actionSave.triggered.connect(MainWindow.event_action_save) # type: ignore
        self.actionAdd.triggered.connect(MainWindow.event_action_add) # type: ignore
        self.listWidget_input.doubleClicked['QModelIndex'].connect(MainWindow.event_listwidget_input_doubleclicked) # type: ignore
        self.lineEdit_crs.textChanged['QString'].connect(MainWindow.event_lineedit_crs_textchanged) # type: ignore
        self.listWidget_output.currentRowChanged['int'].connect(MainWindow.event_listwidget_output_currentrowchanged) # type: ignore
        self.spinBox_z_factor.valueChanged['int'].connect(MainWindow.event_spinBox_z_factor) # type: ignore
        self.spinBox_elevation_smoothing.valueChanged['int'].connect(MainWindow.event_spinBox_elevation_smoothing) # type: ignore
        self.spinBox_dilation.valueChanged['int'].connect(MainWindow.event_spinBox_dilation) # type: ignore
        self.spinBox_flattening.valueChanged['int'].connect(MainWindow.event_spinBox_flattening) # type: ignore
        self.spinBox_elevation_diff.valueChanged['int'].connect(MainWindow.event_spinBox_elevation_diff) # type: ignore
        self.actionShow_log.toggled['bool'].connect(self.listWidget_log.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_crs, self.lineEdit_area)
        MainWindow.setTabOrder(self.lineEdit_area, self.listWidget_input)
        MainWindow.setTabOrder(self.listWidget_input, self.pushButton_remove_layer)
        MainWindow.setTabOrder(self.pushButton_remove_layer, self.spinBox_z_factor)
        MainWindow.setTabOrder(self.spinBox_z_factor, self.spinBox_elevation_smoothing)
        MainWindow.setTabOrder(self.spinBox_elevation_smoothing, self.spinBox_dilation)
        MainWindow.setTabOrder(self.spinBox_dilation, self.spinBox_flattening)
        MainWindow.setTabOrder(self.spinBox_flattening, self.listWidget_output)
        MainWindow.setTabOrder(self.listWidget_output, self.checkBox_gen_2d)
        MainWindow.setTabOrder(self.checkBox_gen_2d, self.checkBox_gen_3d)
        MainWindow.setTabOrder(self.checkBox_gen_3d, self.pushButton_gen)
        MainWindow.setTabOrder(self.pushButton_gen, self.pushButton_exp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SceneFromGIS"))
        self.label_layers.setText(_translate("MainWindow", "Layers"))
        self.label_layer_properties.setText(_translate("MainWindow", "Layer properties"))
        self.pushButton_remove_layer.setText(_translate("MainWindow", "Remove layer"))
        self.label_z_factor.setText(_translate("MainWindow", "Z Factor"))
        self.label_elevation_smoothing.setText(_translate("MainWindow", "Elevation smoothing"))
        self.label_flattening.setText(_translate("MainWindow", "Flattening"))
        self.label_dilation.setText(_translate("MainWindow", "Dilation"))
        self.label_type_.setText(_translate("MainWindow", "Type"))
        self.label_elevation_diff.setText(_translate("MainWindow", "Elevation difference"))
        self.lineEdit_crs.setText(_translate("MainWindow", "EPSG:2154"))
        self.label.setText(_translate("MainWindow", "Area"))
        self.label_crs.setText(_translate("MainWindow", "CRS"))
        self.label_project.setText(_translate("MainWindow", "Project"))
        self.checkBox_gen_2d.setText(_translate("MainWindow", "Generate 2D maps"))
        self.checkBox_gen_3d.setText(_translate("MainWindow", "Generate 3D obj"))
        self.pushButton_gen.setText(_translate("MainWindow", "Generate"))
        self.pushButton_exp.setText(_translate("MainWindow", "Export"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuLayer.setTitle(_translate("MainWindow", "Layer"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionShow_log.setText(_translate("MainWindow", "Show log"))
from pyvistaqt import QtInteractor
