import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os

class Pawn(QLabel):

    clicked = pyqtSignal(int, int, int)

    def __init__(self, *args, **kwargs):
        super(Pawn, self).__init__(*args, **kwargs)
        self.deleted = False

    def initUI(self, name, fieldPos, windowPos, player):
        self.player = player
        self.windowPosition = windowPos
        self.type = name
        self.position = fieldPos
        self.pixmap = QPixmap('../img/'+ name + '.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap.scaled(50,50))

        self.resize(50,50)

    def mousePressEvent(self, event):
        self.clicked.emit(self.position[0], self.position[1], self.player)
        super(Pawn, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(Pawn, self).mousePressEvent(event)
