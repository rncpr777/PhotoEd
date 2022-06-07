from PIL import Image
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Proj(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("BrightChange")
        self.show()
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
    sys.exit(app.exec_())