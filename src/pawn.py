import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os

class Pawn(QLabel):

    def __init__(self, *args, **kwargs):
        super(Pawn, self).__init__(*args, **kwargs)

    def initUI(self, name, fieldPos, windowPos):
        self.windowPosition = windowPos
        self.type = name
        self.position = fieldPos
        self.pixmap = QPixmap('../img/'+ name + '.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap.scaled(50,50))

        self.resize(self.pixmap.width(),self.pixmap.height())


        # self.show()
