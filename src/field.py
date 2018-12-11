#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Field(QWidget):

    clicked = pyqtSignal(int, int)

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.posX = 0
        self.posY = 0
        self.setAutoFillBackground(True)

    # Change color save position
    def setProp(self, posX, posY):
        self.pal = self.palette()
        self.posX = posX
        self.posY = posY
        if ((posX + posY) % 2 != 0):
            self.pal.setColor(self.backgroundRole(), QColor(0,102,204,255))
        else:
            self.pal.setColor(self.backgroundRole(), QColor(179,218,255,255))

        self.setPalette(self.pal)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit(self.posY, self.posX)
        print("Click")
        super(Field, self).mousePressEvent(QMouseEvent)


    def mouseReleaseEvent(self, QMouseEvent):

        pal = self.pal
        pal.setColor(self.backgroundRole(), QColor(204,204,0,255))
        self.setPalette(pal)
        super(Field, self).mouseReleaseEvent(QMouseEvent)

    # def mousePressEvent(self, QMouseEvent):
    #     super(Field, self).mousePressEvent(QMouseEvent)
    #     print ("res: ", QMouseEvent.pos())
    #     pal = self.palette()
    #     pal.setColor(self.backgroundRole(), QColor(0,102,204,255))
    #     self.setAutoFillBackground(True)
    #     self.setPalette(pal)
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     print (QMouseEvent.pos())
    #     pal = self.palette()
    #     pal.setColor(self.backgroundRole(), QColor(179,218,255,255))
    #     self.setAutoFillBackground(True)
    #     self.setPalette(pal)
