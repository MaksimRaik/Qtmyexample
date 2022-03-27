from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Button:

    def __init__(self):

        self.filename = ''

    def getFileName(self):

        self.filename = QFileDialog.getOpenFileName()[0]



