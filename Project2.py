from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
import urllib.request


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.url = self.textEdit.toPlainText()
        self.soot = self.comboBox.currentText()
        self.chb = self.comboBox_2.currentText()
        self.pushButton.clicked.connect(self.change)
        self.pushButton_2.clicked.connect(self.exit)


    def change(self):
        self.url = self.textEdit.toPlainText()
        self.soot = self.comboBox.currentText()
        self.chb = self.comboBox_2.currentText()
        save_name = "photo.png"
        urllib.request.urlretrieve(self.url, save_name)
        img = Image.open("photo.png")
        pixels = img.load()
        width, height = img.size
        if self.soot == "16:10":
            delen = width // 16
            width = delen * 16
            height = delen * 10
            img = img.resize((width, height))
        elif self.soot == "16:9":
            delen = width // 16
            width = delen * 16
            height = delen * 9
            img = img.resize((width, height))
        elif self.soot == "5:4":
            delen = width // 5
            width = delen * 5
            height = delen * 4
            img = img.resize((width, height))
        elif self.soot == "4:3":
            delen = width // 4
            width = delen * 4
            height = delen * 3
            img = img.resize((width, height))
        elif self.soot == "3:4":
            delen = height // 4
            width = delen * 3
            height = delen * 4
            img = img.resize((width, height))
        elif self.soot == "2:1":
            delen = width // 2
            width = delen * 2
            height = delen
            img = img.resize((width, height))
        elif self.soot == "1:1":
            height = width
            img = img.resize((width, height))
        if self.chb == "Да":
            img = img.convert("L")
        img.save("res.png")
        print("Готово! :)")

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())