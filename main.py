import sys

from PyQt5 import QtWidgets

from app import Main, Loop
from parser import *
import asyncio


class App:
    def __init__(self):
        super().__init__()
        app = QtWidgets.QApplication(sys.argv)
        ex = Loop()
        ex.show()
        app.exec()
