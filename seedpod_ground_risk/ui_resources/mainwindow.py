# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .maplayerslistwidget import MapLayersListWidget
from .plot_webview import PlotWebview


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 857)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 836))
        MainWindow.setBaseSize(QSize(1200, 800))
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionAbout_Static_Sources = QAction(MainWindow)
        self.actionAbout_Static_Sources.setObjectName(u"actionAbout_Static_Sources")
        self.actionAbout_App = QAction(MainWindow)
        self.actionAbout_App.setObjectName(u"actionAbout_App")
        self.actionRasterise = QAction(MainWindow)
        self.actionRasterise.setObjectName(u"actionRasterise")
        self.actionRasterise.setCheckable(True)
        self.actionGenerate = QAction(MainWindow)
        self.actionGenerate.setObjectName(u"actionGenerate")
        self.actionAdd_Aircraft = QAction(MainWindow)
        self.actionAdd_Aircraft.setObjectName(u"actionAdd_Aircraft")
        self.actionView_Risk_vs_Distance_Graph = QAction(MainWindow)
        self.actionView_Risk_vs_Distance_Graph.setObjectName(u"actionView_Risk_vs_Distance_Graph")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1200, 757))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.listWidget = MapLayersListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMinimumSize(QSize(405, 490))

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.addLayerButton = QPushButton(self.centralwidget)
        self.addLayerButton.setObjectName(u"addLayerButton")

        self.horizontalLayout.addWidget(self.addLayerButton)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")

        self.horizontalLayout.addWidget(self.generateButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.plotWebview = PlotWebview(self.centralwidget)
        self.plotWebview.setObjectName(u"plotWebview")
        self.plotWebview.setEnabled(True)
        sizePolicy.setHeightForWidth(self.plotWebview.sizePolicy().hasHeightForWidth())
        self.plotWebview.setSizePolicy(sizePolicy)
        self.plotWebview.setMinimumSize(QSize(800, 700))

        self.horizontalLayout_4.addWidget(self.plotWebview)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1200, 21))
        self.menu_File = QMenu(self.menuBar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menu_Aircraft = QMenu(self.menuBar)
        self.menu_Aircraft.setObjectName(u"menu_Aircraft")
        self.menu_Help = QMenu(self.menuBar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menu_Aircraft.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.actionImport)
        self.menu_File.addAction(self.actionExport)
        self.menu_Aircraft.addAction(self.actionAdd_Aircraft)
        self.menu_Help.addAction(self.actionAbout_Static_Sources)
        self.menu_Help.addAction(self.actionAbout_App)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SEEDPOD Ground Risk", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export .png", None))
        self.actionAbout_Static_Sources.setText(QCoreApplication.translate("MainWindow", u"About Static Data", None))
        self.actionAbout_App.setText(QCoreApplication.translate("MainWindow", u"About App", None))
        self.actionRasterise.setText(QCoreApplication.translate("MainWindow", u"Rasterise", None))
        self.actionGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        # if QT_CONFIG(tooltip)
        self.actionGenerate.setToolTip(QCoreApplication.translate("MainWindow", u"Generate Map for current view", None))
        # endif // QT_CONFIG(tooltip)
        self.actionAdd_Aircraft.setText(QCoreApplication.translate("MainWindow", u"Add Aircraft", None))
        # if QT_CONFIG(tooltip)
        self.actionAdd_Aircraft.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add a custom aircraft to the database", None))
        # endif // QT_CONFIG(tooltip)
        self.actionView_Risk_vs_Distance_Graph.setText(
            QCoreApplication.translate("MainWindow", u"Risk vs Distance Graph", None))
        self.addLayerButton.setText(QCoreApplication.translate("MainWindow", u"Add Layer", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menu_Aircraft.setTitle(QCoreApplication.translate("MainWindow", u"&Aircraft", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

