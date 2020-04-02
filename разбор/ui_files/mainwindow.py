# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mainwindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 355)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cloth_table = QtWidgets.QTableWidget(Form)
        self.cloth_table.setObjectName("cloth_table")
        self.cloth_table.setColumnCount(0)
        self.cloth_table.setRowCount(0)
        self.gridLayout.addWidget(self.cloth_table, 2, 0, 3, 2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.temp_city = QtWidgets.QLabel(Form)
        self.temp_city.setObjectName("temp_city")
        self.gridLayout.addWidget(self.temp_city, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_weather = QtWidgets.QLabel(Form)
        self.image_weather.setObjectName("image_weather")
        self.horizontalLayout.addWidget(self.image_weather)
        self.status = QtWidgets.QLabel(Form)
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.add_cloth = QtWidgets.QPushButton(Form)
        self.add_cloth.setObjectName("add_cloth")
        self.gridLayout.addWidget(self.add_cloth, 5, 0, 1, 1)
        self.change_city = QtWidgets.QPushButton(Form)
        self.change_city.setObjectName("change_city")
        self.gridLayout.addWidget(self.change_city, 6, 0, 1, 1)
        self.city_input = QtWidgets.QLineEdit(Form)
        self.city_input.setObjectName("city_input")
        self.gridLayout.addWidget(self.city_input, 6, 1, 1, 1)
        self.generate = QtWidgets.QPushButton(Form)
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 6, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:25pt; font-weight:600; text-decoration: none; color:#050D2C; text-shadow:-0   -3px 1px #000000, 0   -3px 1px #000000,-0    3px 1px #000000, 0    3px 1px #000000,-3px -0   1px #000000, 3px -0   1px #000000,-3px  0   1px #000000, 3px  0   1px #000000,-1px -3px 1px #000000, 1px -3px 1px #000000,-1px  3px 1px #000000, 1px  3px 1px #000000,-3px -1px 1px #000000, 3px -1px 1px #000000,-3px  1px 1px #000000, 3px  1px 1px #000000,-2px -3px 1px #000000, 2px -3px 1px #000000,-2px  3px 1px #000000, 2px  3px 1px #000000,-3px -2px 1px #000000, 3px -2px 1px #000000,-3px  2px 1px #000000, 3px  2px 1px #000000,-3px -3px 1px #000000, 3px -3px 1px #000000,-3px  3px 1px #000000, 3px  3px 1px #000000,-3px -3px 1px #000000, 3px -3px 1px #000000,-3px  3px 1px #000000, 3px  3px 1px #000000;\">ПОДБОР ОДЕЖДЫ</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Ваша одежда</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Температура сегодня:</span></p></body></html>"))
        self.temp_city.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">температура</span></p></body></html>"))
        self.image_weather.setText(_translate("Form", "not_availiable"))
        self.status.setText(_translate("Form", "Статус"))
        self.add_cloth.setText(_translate("Form", "Добавить одежду"))
        self.change_city.setText(_translate("Form", "Изменить город"))
        self.generate.setText(_translate("Form", "Сгенерировать образ"))
