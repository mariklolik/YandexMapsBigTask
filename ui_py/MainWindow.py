# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main456.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 536)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.adress = QtWidgets.QLabel(Form)
        self.adress.setText("")
        self.adress.setObjectName("adress")
        self.horizontalLayout_2.addWidget(self.adress)
        self.showindex = QtWidgets.QCheckBox(Form)
        self.showindex.setObjectName("showindex")
        self.horizontalLayout_2.addWidget(self.showindex)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
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
        self.showindex.setText(_translate("Form", "показывать почтовый индекс"))
        self.ButtonChange.setText(_translate("Form", "Поменять вид"))
        self.dischangeButton.setText(_translate("Form", "сброс"))
        self.ButtonSearch.setText(_translate("Form", "Поиск"))

