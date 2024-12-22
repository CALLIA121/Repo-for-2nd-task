import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Draw Circles")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.draw_circles)

        self.circles = []

    def draw_circles(self):
        # Очищаем предыдущие окружности
        self.circles.clear()

        # Добавляем от 1 до 10 новых окружностей
        num_circles = random.randint(1, 10)
        for _ in range(num_circles):
            diameter = random.randint(10, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            color = QColor(random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            self.circles.append((x, y, diameter, color))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)

        super().paintEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
