# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, UiMainWindow):
        UiMainWindow.setObjectName("UiMainWindow")
        UiMainWindow.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(UiMainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.MapImage = QtWidgets.QLabel(UiMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MapImage.sizePolicy().hasHeightForWidth())
        self.MapImage.setSizePolicy(sizePolicy)
        self.MapImage.setScaledContents(True)
        self.MapImage.setObjectName("MapImage")
        self.gridLayout.addWidget(self.MapImage, 0, 0, 1, 1)

        self.retranslateUi(UiMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UiMainWindow)

    def retranslateUi(self, UiMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UiMainWindow.setWindowTitle(_translate("UiMainWindow", "Form"))
        self.MapImage.setText(_translate("UiMainWindow", "TextLabel"))
