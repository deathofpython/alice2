from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file.ui', self)
        self.answer = ''
        self.flag = False
        self.pushButton.clicked.connect(self.click)
        self.pushButton_2.clicked.connect(self.reset)

    def click(self):
        self.answer = self.lineEdit.text()

    def reset(self):
        self.flag = True
