import sys, os, requests

sys.path.append(os.path.join(os.getcwd(), 'ui_py'))
from MainWindow import UiMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QPalette, QFont, QBrush, QImage
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

SCREEN_SIZE = ()


class MainWindow(QWidget, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Карты')
        self.map_file = None
        self.setGeometry(0, 10, 620, 450)
        self.MapImage.move(0, 0)
        self.MapImage.resize(620, 455)
        self.pars = [83.780402, 53.345144, 0.02, 0.02]
        self.getImage()
        self.setImage()

    def getImage(self, long=83.780402, lat=53.345144, spn1=0.02, spn2=0.02):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={long},{lat}&spn={spn1},{spn2}&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            raise ValueError

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def setImage(self):
        self.image = QPixmap(self.map_file)
        self.image = self.image.scaled(self.MapImage.size())
        self.MapImage.setPixmap(self.image)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.pars[2] >= 0.000625 and self.pars[3] >= 0.000625:
                self.pars[2] /= 2
                self.pars[3] /= 2
            else:
                self.pars[2] = 0.000625
                self.pars[3] = 0.000625
            self.getImage(*self.pars)
            self.setImage()
        if event.key() == Qt.Key_PageDown:
            try:
                self.pars[2] *= 2
                self.pars[3] *= 2
                self.getImage(*self.pars)
                self.setImage()
            except ValueError:
                self.pars[2], self.pars[3] = 81.92, 81.92


a = QApplication(sys.argv)
b = MainWindow()
b.setFixedSize(650, 500)
b.show()
sys.exit(a.exec_())
