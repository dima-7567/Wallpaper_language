from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(872, 661)
        self.setStyleSheet("font: 75 14pt \"Palatino Linotype\";\n"
                           "background-color: rgb(241, 183, 255);")
        self.centralWidget = QtWidgets.QWidget()

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 841, 601))

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(size_policy)
        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.gridLayout_3.addWidget(self.textEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(size_policy)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 3)
        self.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 37))
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Loop()
    ex.show()
    app.exec()
