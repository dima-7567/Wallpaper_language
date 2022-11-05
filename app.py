import os
from ctypes import windll
from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
import sys
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
        self.label.setSizePolicy(size_policy)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.path = 'images/cat_10.png'
        self.label.setPixmap(QPixmap(self.path))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 6)
        self.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 40))
        self.menu_load_local_wallpaper = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_load_local_wallpaper.menuAction())

        self.re_translate()
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Create wallpaper"))
        self.label_2.setText(_translate("MainWindow", "Input the word you would like to learn"))
        self.menu_load_local_wallpaper.setTitle(_translate("MainWindow", "load local wallpaper"))


class Loop(Main):
    def __init__(self):
        super().__init__()
        self.pushButton.clicked.connect(lambda: self.pushed())

    def pushed(self):
        print(os.getcwd() + '\\itog_images\\' + self.path[7:])
        dog_jpg = Image.open(self.path)
        dog_jpg.save('itog_images\\' + self.path[7:])
        wallpaper = bytes(os.getcwd() + '\\itog_images\\' + self.path[7:], 'utf-8')
        windll.user32.SystemParametersInfoA(20, 0, wallpaper, 3)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        pass

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        print(a0.key())
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
открыть локальную картинку
подстройка текста под изображенифе двигаться по курсору мыши до нажатия на клавижу и адаптация цвета
иструкция
базы данных пути к обоям и количество использованных раз
самоликвидация приложения
pep 8
"""