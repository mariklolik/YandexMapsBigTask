# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'city_get.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_city(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(356, 96)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.city_name = QtWidgets.QLineEdit(Form)
        self.city_name.setObjectName("city_name")
        self.verticalLayout.addWidget(self.city_name)
        self.city_name_button = QtWidgets.QPushButton(Form)
        self.city_name_button.setObjectName("city_name_button")
        self.verticalLayout.addWidget(self.city_name_button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Введите название вашего города:</span></p></body></html>"))
        self.city_name_button.setText(_translate("Form", "Подтвердить"))
