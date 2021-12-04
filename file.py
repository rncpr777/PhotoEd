import sys
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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(125, 80, 250, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())