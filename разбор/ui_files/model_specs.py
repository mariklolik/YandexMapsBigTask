# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_specs2ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_specs(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(286, 207)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.types = QtWidgets.QListWidget(Form)
        self.types.setObjectName("types")
        self.gridLayout.addWidget(self.types, 2, 0, 1, 1)

        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#141414;\">Желаемые характеристики</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Вид одежды</span></p></body></html>"))

        self.ok.setText(_translate("Form", "Подтвердить"))
