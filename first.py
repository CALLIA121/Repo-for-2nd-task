import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.draw_circles)

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
            self.circles.append((x, y, diameter))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor("yellow"))
        painter.setPen(Qt.PenStyle.NoPen)

        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

        super().paintEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
