from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file.ui', self)
        self.answer = ''
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.answer = self.lineEdit.text()

