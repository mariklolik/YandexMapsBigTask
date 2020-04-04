import sys, os, requests

from ui_py.MainWindow import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QPalette, QFont, QBrush, QImage
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

SCREEN_SIZE = ()


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Карты')
        self.map_file = None
        self.types = ['map', 'sat', 'trf', 'map,trf']
        self.type_now = 0
        self.setGeometry(100, 100, 620, 450)
        self.MapImage.move(0, 0)
        self.MapImage.resize(620, 455)
        self.pars = [83.780402, 53.345144, 0.02, 0.02, 'map', False]
        self.mc = [83.780402, 53.345144]
        self.ButtonSearch.clicked.connect(self.searchCity)
        self.ButtonChange.clicked.connect(self.changeType)
        self.getImage(*self.pars)
        self.setImage()
        self.dischangeButton.clicked.connect(self.dischange)

    def dischange(self):
        self.pars[-1] = False
        self.InputSearch.setText("")
        self.getImage(*self.pars)
        self.setImage()

    def toFixed(numObj, digits=3):
        return f"{numObj:.{digits}f}"

    def searchCity(self):
        self.pars[-1] = True
        CityName = self.InputSearch.text()
        self.setCoordinates_setSpn(CityName)
        self.getImage(*self.pars)
        self.setImage()
        self.disable_buttons(True)

    def setCoordinates_setSpn(self, city_name):
        toponym_to_find = city_name
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        size1 = toponym["boundedBy"]['Envelope']['lowerCorner'].split()
        size2 = toponym["boundedBy"]['Envelope']['upperCorner'].split()
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
        spn1 = str(abs(float(size1[0]) - float(size2[0])))
        spn2 = str(abs(float(size1[1]) - float(size2[1])))
        self.pars[0] = float(toponym_longitude)
        self.pars[1] = float(toponym_lattitude)
        self.mc = [self.pars[0], self.pars[1]]
        self.pars[2], self.pars[3] = float(spn1), float(spn2)

    def changeType(self):
        self.type_now = (self.type_now + 1) % 4
        self.pars[4] = self.types[self.type_now]
        self.getImage(*self.pars)
        self.setImage()

    def getImage(self, long=83.780402, lat=53.345144, spn1=0.02, spn2=0.02, typ='map', pt=None):
        map_api_server = 'http://static-maps.yandex.ru/1.x/'
        map_params = {"ll": f'{long},{lat}',
                      "spn": f"{spn1},{spn2}",
                      "l": typ}
        if pt:
            map_params['pt'] = f'{self.mc[0]},{self.mc[1]},pm2dgl'
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={long},{lat}&spn={spn1},{spn2}&l={typ}"
        response = requests.get(map_api_server, params=map_params)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            raise ValueError

        # Запишем полученное изображение в файл.
        if self.pars[4] != 'sat':
            self.map_file = "map.png"
        else:
            self.map_file = 'map.jpg'
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def setImage(self):
        self.image = QPixmap(self.map_file)
        self.image = self.image.scaled(self.MapImage.size())
        self.MapImage.setPixmap(self.image)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def disable_buttons(self, disabler=True):
        self.InputSearch.setDisabled(disabler)
        self.ButtonChange.setDisabled(disabler)
        self.ButtonSearch.setDisabled(disabler)
        self.dischangeButton.setDisabled(disabler)

    def keyPressEvent(self, event):
        if event.key() in [16777234, 16777235, 16777236, 16777237]:
            self.disable_buttons()
        if event.key() == Qt.Key_PageUp:
            if self.pars[2] >= 0.000625 and self.pars[3] >= 0.000625:
                self.pars[2] /= 2
                self.pars[3] /= 2
            else:
                self.pars[2] = 0.000625
                self.pars[3] = 0.000625
            self.getImage(*self.pars)
            self.setImage()
            self.disable_buttons(False)
        if event.key() == Qt.Key_PageDown:
            try:
                self.pars[2] *= 2
                self.pars[3] *= 2
                self.getImage(*self.pars)
                self.setImage()
            except ValueError:
                self.pars[2], self.pars[3] = 81.92, 81.92
            self.disable_buttons(False)
        if event.key() == Qt.Key_Up:

            try:
                self.pars[1] += self.pars[3]

                self.getImage(*self.pars)
                self.setImage()
            except ValueError:
                self.pars[1] -= self.pars[3]
            self.disable_buttons(False)
        if event.key() == Qt.Key_Down:
            try:
                self.pars[1] -= self.pars[3]

                self.getImage(*self.pars)
                self.setImage()
            except ValueError:
                self.pars[1] += self.pars[3]
            self.disable_buttons(False)
        if event.key() == Qt.Key_Left:
            self.InputSearch.setDisabled(True)
            try:
                self.pars[0] -= self.pars[2]

                self.getImage(*self.pars)
                self.setImage()
            except ValueError:
                self.pars[0] += self.pars[2]
            self.disable_buttons(False)
        if event.key() == Qt.Key_Right:
            try:
                self.pars[0] += self.pars[2]

                self.getImage(*self.pars)
                self.setImage()
            except ValueError:
                self.pars[0] -= self.pars[2]
            self.disable_buttons(False)


a = QApplication(sys.argv)
b = MainWindow()
b.setFixedSize(650, 500)
b.show()
sys.exit(a.exec_())
