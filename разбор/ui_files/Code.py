from mainwindow import Ui_Mainwindow
from file_add import Ui_file_add
from model_specs import Ui_specs
from model_show import Ui_show
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QPalette, QFont, QBrush, QImage
from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen
import requests
import sys
import os
import sqlite3
import cv2


# import библиотек

class MainWindow(QWidget, Ui_Mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создатель образа')
        self.geolocator = Nominatim(user_agent="my-application")  # создание геолокатора(получение широты и долготы
        self.setStyleSheet("QLabel {color: rgb(255,255,255); font: bold 20px}")
        self.OPENWEATHER_API_KEY = 'd36cbb8582ff58d572c64ba56aaa0f6d'
        self.label.setFont(QFont("Bahnschrift SemiCondensed", 30, QFont.Bold))
        self.temp_city.setFont(QFont("Bahnschrift SemiCondensed", 40, QFont.Bold))
        self.label_4.setFont(QFont("Bahnschrift SemiCondensed", 30, QFont.Bold))
        self.city_name = ''
        self.lat, self.long = 0, 0
        self.change_city.clicked.connect(self.write_city)
        file = open('logs.txt', 'r')  # хранит название последнего использованного города
        self.city_name = file.read()
        file.close()
        self.add_cloth.clicked.connect(self.add_cloth_db)
        if not self.city_name:
            self.city_input.setText('введите название')
        else:
            self.city_input.setText(self.city_name)
            self.get_weather_info(self.city_name)
        self.loadTable()
        self.generate.clicked.connect(self.generator_func)

    def generator_func(self):
        self.gen = ClothSpecs(self.temp_city.text())
        self.gen.show()

    def write_city(self):
        # сохраняет название файла
        self.city_name = self.city_input.text()
        file = open('logs.txt', 'w')
        file.write(self.city_name)
        file.close()
        self.lat, self.long = 0, 0
        self.get_weather_info(self.city_input.text())

    def get_weather_info(self, city_name):
        print(city_name)
        # получение данных о погоде(температура)
        self.geolocator = Nominatim(user_agent="my-application")

        while not self.lat and not self.long:  # получение широты и долготы города
            print('Please wait, collecting data')
            try:  # для обработки возможных ошибок сервера
                location = self.geolocator.geocode(city_name)
                self.lat, self.long = location.latitude, location.longitude
            except:
                pass
        url = f"http://api.openweathermap.org/data/2.5/" \
              f"weather?lat={float(self.lat)}&lon={float(self.long)}&appid={self.OPENWEATHER_API_KEY}"
        # формирование url-ссылки для получения данных с сайта openweather.com
        response = False
        while not response:
            try:
                response = urlopen(url)
            except:
                print('err')
        data = json.loads(response.read())
        temp = (data['main']['temp'] - 273.15)  # перевод температуры из кельвинов в цельсии
        if temp < 0:
            self.temp_city.setText(str(int(temp)) + '°C, одевайтесь теплее!')
        else:
            self.temp_city.setText(str(int(temp)) + '°C, отличный день!')

        # получение изображения погоды
        icon = data['weather'][0]['icon']
        p = requests.get(f'http://openweathermap.org/img/wn/{icon}.png')
        out = open(f'{os.getcwd()}\img.png', "wb")
        out.write(p.content)
        out.close()
        image = QPixmap(f'{os.getcwd()}\img.png')
        self.image_weather.setPixmap(image)
        self.status.setText(self.decode_status(data['weather'][0]['main']))
        self.status.setFont(QFont("Bahnschrift SemiCondensed", 30, QFont.Bold))

    def decode_status(self, status):
        # переводчик статуса погоды на русский язык
        eng_to_rus = {'clear': 'ясно',
                      'clouds': 'облачно',
                      'snow': 'снег',
                      'thunderstorm': 'гроза',
                      'mist': 'туман',
                      'drizzle': 'легкий дождь',
                      'dust': 'пыльно',
                      'fog': 'туман',
                      'rain': 'дождь'}
        return eng_to_rus[status.lower()]

    def add_cloth_db(self):
        # добавление одежды в БД
        self.appender = FileAdd(self)
        self.appender.show()

    def loadTable(self):
        # загрузка таблицы
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        ans = cur.execute('SELECT * FROM clothes').fetchall()
        self.cloth_table.setColumnCount(7)
        self.cloth_table.setHorizontalHeaderLabels(('id', 'name', 'mintemp', 'maxtemp', 'type', 'color', 'style'))
        self.cloth_table.setRowCount(len(ans))
        for i, elem in enumerate(ans):
            for j, elem2 in enumerate(elem):
                self.cloth_table.setItem(i, j, QTableWidgetItem(str(elem2)))
        self.cloth_table.resizeColumnsToContents()

    def resizeEvent(self, QResizeEvent):
        # Файл с задним фоном хранится в background.png, при изменении размеров окна он меняется под него
        width = self.width()
        height = self.height()
        im = cv2.imread('background.png')
        im = cv2.resize(im, (width, height))
        cv2.imwrite('background.png', im)
        brush = QBrush()
        brush.setTextureImage(QImage('background.png'))
        appearance = self.palette()
        appearance.setBrush(QPalette.Background, brush)
        self.setPalette(appearance)


class FileAdd(QWidget, Ui_file_add):
    def __init__(self, other):
        super().__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.append_db)
        self.other = other

    def append_db(self):
        style = self.style.text().lower()
        color = self.color.text().lower()
        cloth_type = self.type.text().lower()
        temperature = self.temperature.text().split(sep=',')
        mintemp, maxtemp = int(temperature[0]), int(temperature[1])
        name = self.name.text()
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        num = len(cur.execute('SELECT id FROM clothes').fetchall())
        cur.execute(
            f"""INSERT INTO clothes
VALUES ({num + 1}, '{name}', {mintemp}, {maxtemp}, '{cloth_type}', '{color}', '{style}')""")
        con.commit()
        cur.close()
        self.other.loadTable()
        self.close()


class ClothSpecs(QWidget, Ui_specs):
    def __init__(self, temperature):
        super().__init__()
        self.setupUi(self)
        self.loadtypes()
        self.ok.clicked.connect(self.ok_but)
        self.type = ''
        self.temperature = temperature

    def loadtypes(self):
        # получение видов одежды
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        data = cur.execute('SELECT DISTINCT style FROM clothes').fetchall()
        for i, elem in enumerate(data):
            self.types.addItem(str(elem[0]))

    def ok_but(self):
        self.type = self.types.currentItem().text()
        self.showdata = Show(self.type, self.temperature)
        self.showdata.show()
        self.close()


class Show(QWidget, Ui_show):
    def __init__(self, style, temperature):
        super().__init__()
        temperature = int(temperature[:temperature.find('°')])

        self.setupUi(self)
        self.chosen_style = style
        self.temperature = temperature
        self.data = []
        self.get_data()

        self.counter_hat = 0
        self.counter_body = 0
        self.counter_pants = 0
        self.counter_shoes = 0

        self.hat_left.clicked.connect(self.hat_left_click)
        self.hat_right.clicked.connect(self.hat_right_click)
        self.body_left.clicked.connect(self.body_left_click)
        self.body_right.clicked.connect(self.body_right_click)
        self.pants_left.clicked.connect(self.pants_left_click)
        self.pants_right.clicked.connect(self.pants_right_click)
        self.shoes_left.clicked.connect(self.shoes_left_click)
        self.shoes_right.clicked.connect(self.shoes_right_click)

    def get_data(self):
        # получение одежды из БД
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        self.setStyleSheet("QLabel {color: rgb(44,7,108); font: bold 30px}")
        names = ['шапка', 'одежда на тело', 'штаны', 'обувь']
        data = []
        for curr_type in names:
            data.append(cur.execute(
                f'SELECT name FROM clothes WHERE type="{curr_type}" AND mintemp <= {self.temperature} AND maxtemp >= {self.temperature} AND style="{self.chosen_style}"').fetchall())

        self.counter_hat = 0
        self.counter_body = 0
        self.counter_pants = 0
        self.counter_shoes = 0

        self.data = data

        labels = [self.hat, self.body, self.pants, self.shoes]
        for label in labels:
            label.setFont(QFont("Bahnschrift SemiCondensed", 30, QFont.Bold))

        self.show_data()

    def hat_left_click(self):
        self.counter_hat += 1
        self.show_data()

    def hat_right_click(self):
        self.counter_hat -= 1
        self.show_data()

    def body_left_click(self):
        self.counter_body += 1
        self.show_data()

    def body_right_click(self):
        self.counter_body -= 1
        self.show_data()

    def pants_left_click(self):
        self.counter_pants += 1
        self.show_data()

    def pants_right_click(self):
        self.counter_pants -= 1
        self.show_data()

    def shoes_left_click(self):
        self.counter_shoes += 1
        self.show_data()

    def shoes_right_click(self):
        self.counter_shoes -= 1
        self.show_data()

    def resizeEvent(self, QResizeEvent):
        # Файл с задним фоном хранится в background.png, при изменении размеров окна он меняется под него
        width = self.width()
        height = self.height()
        im = cv2.imread('background2.png')
        im = cv2.resize(im, (width, height))
        cv2.imwrite('background2.png', im)
        brush = QBrush()
        brush.setTextureImage(QImage('background2.png'))
        appearance = self.palette()
        appearance.setBrush(QPalette.Background, brush)
        self.setPalette(appearance)

    def show_data(self):
        item_labels = [self.hat, self.body, self.pants, self.shoes]
        item_num = [self.counter_hat, self.counter_body, self.counter_pants, self.counter_shoes]
        for i in range(4):
            if self.data[i]:
                try:
                    item_labels[i].setText(self.data[i][item_num[i] % len(self.data[i])][0])
                    item_labels[i].setFont(QFont("Times", 20, QFont.Bold))
                    item_labels[i].adjustSize()
                except Exception as err:
                    print(self.data[i][item_num[i] % len(self.data[i])][0])
                    print(f'ошибка {err}')
            else:
                item_labels[i].setText('Нет подходящей вещи!')
                item_labels[i].setFont(QFont("Times", 20, QFont.Bold))
                item_labels[i].adjustSize()


a = QApplication(sys.argv)
b = MainWindow()
b.show()
sys.exit(a.exec_())
