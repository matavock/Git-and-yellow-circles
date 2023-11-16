import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git-and-yellow-circles\\UI.ui', self)  # Загрузка интерфейса из файла UI.ui
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.update()  # Обновление окна, вызывает перерисовку и срабатывание paintEvent

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp):
        qp.setBrush(QColor(255, 255, 0))  # Цвет кисти - желтый
        for _ in range(10):
            d = randint(10, 50)  # Случайный диаметр окружности
            # Случайное положение окружности по x
            x = randint(0, self.width() - d)
            # Случайное положение окружности по y
            y = randint(0, self.height() - d)
            qp.drawEllipse(x, y, d, d)  # Рисование окружности


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())