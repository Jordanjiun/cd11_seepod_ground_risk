# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textDialog.ui',
# licensing of 'textDialog.ui' applies.
#
# Created: Mon Nov 30 23:06:15 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets


class Ui_TextAboutDialog(object):
    def setupUi(self, TextAboutDialog):
        TextAboutDialog.setObjectName("TextAboutDialog")
        TextAboutDialog.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TextAboutDialog.sizePolicy().hasHeightForWidth())
        TextAboutDialog.setSizePolicy(sizePolicy)
        TextAboutDialog.setMinimumSize(QtCore.QSize(500, 400))
        TextAboutDialog.setSizeGripEnabled(False)
        TextAboutDialog.setModal(True)
        self.textEdit = QtWidgets.QTextEdit(TextAboutDialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 500, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 400))
        self.textEdit.setMaximumSize(QtCore.QSize(0, 0))
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(TextAboutDialog)
        QtCore.QMetaObject.connectSlotsByName(TextAboutDialog)

    def retranslateUi(self, TextAboutDialog):
        TextAboutDialog.setWindowTitle(QtWidgets.QApplication.translate("TextAboutDialog", "Dialog", None, -1))
