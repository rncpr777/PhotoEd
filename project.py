from PIL import Image
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit
from PyQt5.QtGui import QFont, QPainter, QColor, QPen


class Proj(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 960, 540)
        self.setWindowTitle("BrightChange")
        self.label = QLabel(self)
        self.label.resize(350, 100)
        self.label.move(325, 5)
        self.label.setText("BrightChange")
        self.label.setFont(QFont("Times", 27, italic=True))
        self.urlfield = QTextEdit(self)
        self.urlfield.resize(450, 40)
        self.urlfield.move(240, 120)
        self.urlfield.setText("*ссылка на изображение*")
        self.urlfield.setFont(QFont("Arial", 16, italic=True))
        self.url = self.urlfield.toPlainText()

    def change(self):
        delta = int(input())
        delta = 1 + (delta / 100)
        img = Image.open("photo.png")
        pixels = img.load()
        width, height = img.size
        for column in range(width):
            for row in range(height):
                r = pixels[column, row][0]
                g = pixels[column, row][1]
                b = pixels[column, row][2]
                r = round(r * delta)
                g = round(g * delta)
                b = round(b * delta)
                pixels[column, row] = (r, g, b)
        img.save("res.png")
        print("Готово! :)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pr = Proj()
    pr.show()
    sys.exit(app.exec_())
