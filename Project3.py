from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
import PIL
import sys
from PIL import Image, ImageEnhance


class Ui_Frame(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(682, 274)
        Frame.setStyleSheet("")
        self.s = 0
        self.chb = False
        self.uluch = False
        self.vibirite_izobraj = QtWidgets.QPushButton(Frame)
        self.vibirite_izobraj.setGeometry(QtCore.QRect(10, 10, 251, 211))
        self.vibirite_izobraj.setObjectName("vibirite_izobraj")
        self.vibirite_izobraj.clicked.connect(self.open_file)

        self.sohranit = QtWidgets.QPushButton(Frame)
        self.sohranit.setGeometry(QtCore.QRect(10, 230, 111, 31))
        self.sohranit.setObjectName("sohranit")
        self.sohranit.clicked.connect(self.sohr)

        self.primenit = QtWidgets.QPushButton(Frame)
        self.primenit.setGeometry(QtCore.QRect(430, 230, 241, 31))
        self.primenit.setObjectName("primenit")
        self.primenit.clicked.connect(self.prim)

        self.sootnosh_storon = QtWidgets.QLabel(Frame)
        self.sootnosh_storon.setGeometry(QtCore.QRect(270, 0, 151, 41))

        font = QtGui.QFont()
        font.setPointSize(11)

        self.sootnosh_storon.setFont(font)
        self.sootnosh_storon.setObjectName("sootnosh_storon")

        self.line1 = QtWidgets.QFrame(Frame)
        self.line1.setGeometry(QtCore.QRect(420, 10, 20, 211))
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")

        self.sootn1 = QtWidgets.QRadioButton(Frame)
        self.sootn1.setGeometry(QtCore.QRect(270, 40, 82, 17))
        self.sootn1.setObjectName("sootn1")
        self.sootn1.toggled.connect(self.s1)

        self.sootn_group = QtWidgets.QButtonGroup(Frame)
        self.sootn_group.setObjectName("sootn_group")
        self.sootn_group.addButton(self.sootn1)

        self.sootn2 = QtWidgets.QRadioButton(Frame)
        self.sootn2.setGeometry(QtCore.QRect(270, 70, 82, 17))
        self.sootn2.setObjectName("sootn2")
        self.sootn_group.addButton(self.sootn2)
        self.sootn2.toggled.connect(self.s2)

        self.sootn3 = QtWidgets.QRadioButton(Frame)
        self.sootn3.setGeometry(QtCore.QRect(270, 100, 82, 17))
        self.sootn3.setObjectName("sootn3")
        self.sootn_group.addButton(self.sootn3)
        self.sootn3.toggled.connect(self.s3)

        self.sootn4 = QtWidgets.QRadioButton(Frame)
        self.sootn4.setGeometry(QtCore.QRect(270, 130, 82, 17))
        self.sootn4.setObjectName("sootn4")
        self.sootn_group.addButton(self.sootn4)
        self.sootn4.toggled.connect(self.s4)

        self.sootn5 = QtWidgets.QRadioButton(Frame)
        self.sootn5.setGeometry(QtCore.QRect(270, 160, 82, 17))
        self.sootn5.setObjectName("sootn5")
        self.sootn_group.addButton(self.sootn5)
        self.sootn5.toggled.connect(self.s5)

        self.cvet_gamma = QtWidgets.QLabel(Frame)
        self.cvet_gamma.setGeometry(QtCore.QRect(440, 0, 131, 41))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.cvet_gamma.setFont(font)
        self.cvet_gamma.setObjectName("cvet_gamma")

        self.cvet1 = QtWidgets.QRadioButton(Frame)
        self.cvet1.setGeometry(QtCore.QRect(440, 40, 101, 17))
        self.cvet1.setObjectName("cvet1")
        self.cvet1.toggled.connect(self.chb1)

        self.line2 = QtWidgets.QFrame(Frame)
        self.line2.setGeometry(QtCore.QRect(553, 10, 20, 211))
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")

        self.ylychshenie = QtWidgets.QLabel(Frame)
        self.ylychshenie.setGeometry(QtCore.QRect(570, 10, 111, 21))

        font = QtGui.QFont()
        font.setPointSize(11)

        self.ylychshenie.setFont(font)
        self.ylychshenie.setObjectName("ylychshenie")

        self.ylych_da = QtWidgets.QRadioButton(Frame)
        self.ylych_da.setGeometry(QtCore.QRect(570, 40, 82, 17))
        self.ylych_da.setObjectName("ylych_da")
        self.ylych_da.toggled.connect(self.uluch1)
        self.uluch_group = QtWidgets.QButtonGroup(Frame)
        self.uluch_group.setObjectName("uluch_group")
        self.uluch_group.addButton(self.ylych_da)

        self.ylych_net = QtWidgets.QRadioButton(Frame)
        self.ylych_net.setGeometry(QtCore.QRect(570, 70, 82, 17))
        self.ylych_net.setObjectName("ylych_net")
        self.ylych_net.toggled.connect(self.uluch2)
        self.uluch_group.addButton(self.ylych_net)

        self.line3 = QtWidgets.QFrame(Frame)
        self.line3.setGeometry(QtCore.QRect(260, 210, 431, 21))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def open_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Проводник", "", "Image (*.jpg)")
        self.img = Image.open(self.file_name[0])
        self.width, self.height = self.img.size
        self.vibirite_izobraj.setText('')
        self.vibirite_izobraj.setIcon(QtGui.QIcon(self.file_name[0]))
        self.vibirite_izobraj.setIconSize(QtCore.QSize(150, 150))

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "PhotoEd"))
        self.vibirite_izobraj.setText(_translate("Frame", "Выберите изображение"))
        self.sohranit.setText(_translate("Frame", "Сохранить"))
        self.primenit.setText(_translate("Frame", "Применить"))
        self.sootnosh_storon.setText(_translate("Frame", "Соотношение сторон"))
        self.sootn1.setText(_translate("Frame", "16:9"))
        self.sootn2.setText(_translate("Frame", "16:10"))
        self.sootn3.setText(_translate("Frame", "4:3"))
        self.sootn4.setText(_translate("Frame", "3:4"))
        self.sootn5.setText(_translate("Frame", "5:4"))
        self.cvet_gamma.setText(_translate("Frame", "Цветовая гамма"))
        self.cvet1.setText(_translate("Frame", "Черно-белая"))
        self.ylychshenie.setText(_translate("Frame", "Улучшение"))
        self.ylych_da.setText(_translate("Frame", "Да"))
        self.ylych_net.setText(_translate("Frame", "Нет"))

    def s1(self):
        self.s = 1

    def s2(self):
        self.s = 2

    def s3(self):
        self.s = 3

    def s4(self):
        self.s = 4

    def s5(self):
        self.s = 5

    def chb1(self):
        self.chb = True

    def uluch1(self):
        self.uluch = True

    def uluch2(self):
        self.uluch = False

    def prim(self):
        if self.s == 1:
            delen = self.width // 16
            self.width = delen * 16
            self.height = delen * 9
            self.img = self.img.resize((self.width, self.height))
        if self.s == 2:
            delen = self.width // 16
            self.width = delen * 16
            self.height = delen * 10
            self.img = self.img.resize((self.width, self.height))
        if self.s == 3:
            delen = self.width // 4
            self.width = delen * 4
            self.height = delen * 3
            self.img = self.img.resize((self.width, self.height))
        if self.s == 4:
            delen = self.width // 3
            self.width = delen * 3
            self.height = delen * 4
            self.img = self.img.resize((self.width, self.height))
        if self.s == 5:
            delen = self.width // 5
            self.width = delen * 5
            self.height = delen * 4
            self.img = self.img.resize((self.width, self.height))
        if self.chb == True:
            self.img = self.img.convert("L")
        if self.uluch == True:
            enhancer = ImageEnhance.Contrast(self.img)
            factor = 1.5
            self.img = enhancer.enhance(factor)
        self.img.save("res.png")
        self.vibirite_izobraj.setText('')
        self.vibirite_izobraj.setIcon(QtGui.QIcon("res.png"))
        self.vibirite_izobraj.setIconSize(QtCore.QSize(150, 150))

    def sohr(self):
        self.img.save("res.png")
        msg = QMessageBox()
        msg.setWindowTitle("Сообщение")
        msg.setText("Сохранено успешно!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())