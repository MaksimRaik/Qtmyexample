from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Button_function import Button

class MenuItem:

    def __init__(self):

        self.items = []

    def getItems(self):

        self.item = Button().openFile()