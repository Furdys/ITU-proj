#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

class Field(QWidget):

    clickedInField = pyqtSignal(int, int, int)
    

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.posX = 0
        self.posY = 0
        self.setAutoFillBackground(True)
        self.hasPawn = False

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
        if self.hasPawn == True:
            self.clickedInField.emit(self.posY, self.posX, 2)
        else:
            self.clickedInField.emit(self.posY, self.posX, 3)
        super(Field, self).mousePressEvent(QMouseEvent)


    def mouseReleaseEvent(self, QMouseEvent):
        super(Field, self).mouseReleaseEvent(QMouseEvent)

    @pyqtSlot(int, int)
    def fieldClicked(self, posY, posX):
        if (posY == self.posY and posX == self.posX):
            self.pal.setColor(self.backgroundRole(), QColor(204,204,0,124))
        else:
            if ((self.posX + self.posY) % 2 != 0):
                self.pal.setColor(self.backgroundRole(), QColor(0,102,204,255))
            else:
                self.pal.setColor(self.backgroundRole(), QColor(179,218,255,255))

        self.setPalette(self.pal)
