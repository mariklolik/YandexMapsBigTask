# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main456.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 536)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MapImage = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MapImage.sizePolicy().hasHeightForWidth())
        self.MapImage.setSizePolicy(sizePolicy)
        self.MapImage.setMinimumSize(QtCore.QSize(620, 450))
        self.MapImage.setObjectName("MapImage")
        self.verticalLayout.addWidget(self.MapImage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonChange = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonChange.sizePolicy().hasHeightForWidth())
        self.ButtonChange.setSizePolicy(sizePolicy)
        self.ButtonChange.setObjectName("ButtonChange")
        self.horizontalLayout.addWidget(self.ButtonChange)
        self.dischangeButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dischangeButton.sizePolicy().hasHeightForWidth())
        self.dischangeButton.setSizePolicy(sizePolicy)
        self.dischangeButton.setObjectName("dischangeButton")
        self.horizontalLayout.addWidget(self.dischangeButton)
        self.InputSearch = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputSearch.sizePolicy().hasHeightForWidth())
        self.InputSearch.setSizePolicy(sizePolicy)
        self.InputSearch.setObjectName("InputSearch")
        self.horizontalLayout.addWidget(self.InputSearch)
        self.ButtonSearch = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonSearch.sizePolicy().hasHeightForWidth())
        self.ButtonSearch.setSizePolicy(sizePolicy)
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.horizontalLayout.addWidget(self.ButtonSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MapImage.setText(_translate("Form", "Барнаааууууууууууул"))
        self.ButtonChange.setText(_translate("Form", "Поменять вид"))
        self.dischangeButton.setText(_translate("Form", "сброс"))
        self.ButtonSearch.setText(_translate("Form", "Поиск"))
