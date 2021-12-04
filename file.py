import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Окружность')
        self.btn = QPushButton('Нарисовать', self)
        self.btn.move(200, 400)
        self.btn.resize(100, 50)
        self.btn.clicked.connect(self.press)
        self.fl = False

    def press(self):
        self.fl = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.fl:
            self.draw(qp)
        qp.end()

    def draw(self, qp):
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c3 = random.randint(0, 255)
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        qp.setBrush(QColor(c1, c2, c3))
        qp.drawEllipse((500 - x) // 2, ((500 - x) // 2) - 80, x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())