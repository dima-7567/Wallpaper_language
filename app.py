import os
from ctypes import windll
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QFileDialog
import sys

from translate import Translator

from parser import ImageParsing
import shutil
from PyQt5 import QtGui


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(900, 700)
        self.setStyleSheet("font: 75 14pt \"Palatino Linotype\";\n"
                           "background-color: rgb(241, 183, 255);")
        self.centralWidget = QtWidgets.QWidget()

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 890, 690))

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(size_policy)
        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        size_policy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(size_policy)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        size_policy.setVerticalStretch(5)
        self.label.setSizePolicy(size_policy)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 3)
        self.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 40))
        self.setMenuBar(self.menubar)

        self.re_translate()
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Create wallpaper"))
        self.label_2.setText(_translate("MainWindow", "Input the word you would like to learn"))


class Loop(Main):
    def __init__(self):
        super().__init__()
        self.label.setText("""
        Whenever you write the word or frase in english you are going to learn 
        press 'enter'
        wait 2-3 minutes to load images and add text
        choose wallpaper that you like using right and left arrows 
        press the button to set wallpaper on the desktop
        """)
        self.pushButton.clicked.connect(lambda: self.pushed())

        load_action = QAction('&Load local image', self)
        load_action.triggered.connect(lambda: self.load_local_image())

        delete_action = QAction('&Delete', self)
        delete_action.triggered.connect(lambda: self.delete())

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&Menu')
        file_menu.addAction(load_action)
        file_menu.addAction(delete_action)

    @staticmethod
    def delete():
        shutil.rmtree(os.getcwd())
        exit()

    def load_local_image(self):
        using_image = Image.open(QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0])
        translator = Translator(to_lang="German")
        translation = translator.translate(self.lineEdit.text())
        print(translation)
        font = ImageFont.truetype("arial.ttf", min(using_image.size[0], using_image.size[1]) // 10)
        drawer = ImageDraw.Draw(using_image)
        colour = [0, 0, 0]
        for x in range(using_image.size[1]):
            for y in range(using_image.size[0]):
                try:
                    r, g, b = using_image.getpixel((y, x))
                except Exception:
                    r, g, b, _ = using_image.getpixel((y, x))
                colour[0] += r
                colour[1] += g
                colour[2] += b
        for p in range(3):
            colour[p] = 255 - colour[p] // (using_image.size[1] * using_image.size[0])
        drawer.text(
            (using_image.size[0] // 10, using_image.size[1] // 10), f"{translation}",
            font=font,
            fill="#" + ('{:X}{:X}{:X}').format(*colour)
        )

        using_image.save(f"itog_images/{self.lineEdit.text()}.png", format='PNG')
        using_image.close()
        wallpaper = bytes(f"{os.getcwd()}/itog_images/{self.lineEdit.text()}.png", 'utf-8')
        windll.user32.SystemParametersInfoA(20, 0, wallpaper, 3)

    def pushed(self):
        try:
            dog_jpg = Image.open(self.path)
            dog_jpg.save('itog_images\\' + self.path[7:-6] + '.png')
            wallpaper = bytes(os.getcwd() + '\\itog_images\\' + self.path[7:-6] + '.png', 'utf-8')
            windll.user32.SystemParametersInfoA(20, 0, wallpaper, 3)
        except Exception as ex:
            # user pushed the button without images
            print(ex)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.gridLayoutWidget.resize(a0.size())

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        # print(a0.key())
        if str(a0.key()) == '16777220':
            shutil.rmtree(os.getcwd() + r'\images')
            os.mkdir('images')
            parser_ = ImageParsing(self.lineEdit.text())
            parser_.download_image()
            self.path = os.listdir('images')[0]
            self.label.setPixmap(QPixmap(self.path))
        if str(a0.key()) == "16777234":
            for i in range(len(os.listdir('images'))):
                if os.listdir('images')[i] == self.path[7:]:
                    self.path = os.listdir('images')[(i - 1) % len(os.listdir('images'))]
                    break
            self.path = "images/" + self.path
            self.label.setPixmap(QPixmap(self.path))
        if str(a0.key()) == "16777236":
            for i in range(len(os.listdir('images'))):
                if os.listdir('images')[i] == self.path[7:]:
                    self.path = os.listdir('images')[(i + 1) % len(os.listdir('images'))]
                    break
            self.path = "images/" + self.path
            self.label.setPixmap(QPixmap(self.path))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Loop()
    ex.show()
    app.exec()



"""
базы данных пути к обоям и количество использованных раз
самоликвидация приложения
pep 8
"""