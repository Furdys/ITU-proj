from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
from field import Field
from pawn import Pawn

class Board(QWidget):

    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)

        print (self.width())
        print (self.height())

        # Position for pawns
        self.cornersPositions = [[[0, 0] for x in range(8)] for y in range(8)]


    @pyqtSlot(int, int)
    def fieldWasClicked(self, posY, posX):
        print("Field: ", posY, posX)

    def mousePressEvent(self, event):
        super(Board, self).mousePressEvent(event)
        print (event.pos())

    def createBord(self):

        # pal = self.palette()
        # pal.setColor(self.backgroundRole(), QColor(205,205,205,255))
        # self.setAutoFillBackground(True)
        # self.setPalette(pal)
        self.sizeOfField()
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)

        # Field sizes
        for i in range(0,8):
            layout.setColumnStretch(i+1, 1)
            layout.setRowStretch(i, 1)

        # Number and letter row and column
        for i in range(1, 9):
            layout.addWidget(QLabel(str(i)), 8-i,0)

        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(1, 9):
            label = QLabel(letters[i-1])
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label, 8, i)

        # Matrix to store all objects in grid
        self.Matrix = []

        for i in range(0,8):
            self.Matrix.append([])
            for j in range(1,9):
                self.Matrix[i].append(Field())
                layout.addWidget(self.Matrix[i][j-1], i, j)
                self.Matrix[i][j-1].setProp(i,(j-1))
                self.Matrix[i][j-1].clicked.connect(self.fieldWasClicked)

        self.setLayout(layout)

        self.importPawns()

    # Import pawns
    def importPawns(self):
        self.pawns = []
        # Create pawns
        for i in range(8):
            self.pawns.append(Pawn(self))
            self.pawns[i].initUI("Pawn", [i,6], self.cornersPositions[6][i])
            self.pawns[i].move(self.cornersPositions[6][i][0], self.cornersPositions[6][i][1])

        for i in range(8,16):
            self.pawns.append(Pawn(self))
            self.pawns[i].initUI("PawnWhite", [i-8,1], self.cornersPositions[1][i-8])
            self.pawns[i].move(self.cornersPositions[1][i-8][0], self.cornersPositions[1][i-8][1])


        # Rooks
        self.pawns.append(Pawn(self))
        self.pawns[16].initUI("RookWhite", [0,0], self.cornersPositions[0][0])
        self.pawns[16].move(self.cornersPositions[0][0][0], self.cornersPositions[0][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[17].initUI("RookWhite", [7,0], self.cornersPositions[7][0])
        self.pawns[17].move(self.cornersPositions[7][0][0], self.cornersPositions[7][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[18].initUI("Rook", [7,7], self.cornersPositions[7][7])
        self.pawns[18].move(self.cornersPositions[7][7][0], self.cornersPositions[7][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[19].initUI("Rook", [0,7], self.cornersPositions[0][7])
        self.pawns[19].move(self.cornersPositions[7][7][0], self.cornersPositions[7][7][1])

        #Horses
        self.pawns.append(Pawn(self))
        self.pawns[20].initUI("Horse", [1,7], self.cornersPositions[1][7])
        self.pawns[20].move(self.cornersPositions[1][7][0], self.cornersPositions[1][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[21].initUI("Horse", [6,7], self.cornersPositions[6][7])
        self.pawns[21].move(self.cornersPositions[6][7][0], self.cornersPositions[6][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[22].initUI("HorseWhite", [1,0], self.cornersPositions[1][0])
        self.pawns[22].move(self.cornersPositions[1][0][0], self.cornersPositions[1][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[23].initUI("HorseWhite", [6,0], self.cornersPositions[6][0])
        self.pawns[23].move(self.cornersPositions[6][0][0], self.cornersPositions[6][0][1])

        #Bishops
        self.pawns.append(Pawn(self))
        self.pawns[24].initUI("Bishop", [2,7], self.cornersPositions[2][7])
        self.pawns[24].move(self.cornersPositions[2][7][0], self.cornersPositions[2][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[25].initUI("Bishop", [5,7], self.cornersPositions[5][7])
        self.pawns[25].move(self.cornersPositions[5][7][0], self.cornersPositions[5][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[26].initUI("BishopWhite", [2,0], self.cornersPositions[2][0])
        self.pawns[26].move(self.cornersPositions[2][0][0], self.cornersPositions[2][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[27].initUI("BishopWhite", [5,0], self.cornersPositions[5][0])
        self.pawns[27].move(self.cornersPositions[5][0][0], self.cornersPositions[5][0][1])

        #Queens
        self.pawns.append(Pawn(self))
        self.pawns[28].initUI("Queen", [4,7], self.cornersPositions[4][7])
        self.pawns[28].move(self.cornersPositions[4][7][0], self.cornersPositions[4][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[29].initUI("QueenWhite", [3,0], self.cornersPositions[3][0])
        self.pawns[29].move(self.cornersPositions[3][0][0], self.cornersPositions[3][0][1])

        #Kings
        self.pawns.append(Pawn(self))
        self.pawns[30].initUI("King", [3,7], self.cornersPositions[3][7])
        self.pawns[30].move(self.cornersPositions[3][7][0], self.cornersPositions[3][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[31].initUI("KingWhite", [4,0], self.cornersPositions[4][0])
        self.pawns[31].move(self.cornersPositions[4][0][0], self.cornersPositions[4][0][1])


    def resizeEvent(self, event):
        super(Board, self).resizeEvent(event)

        self.sizeOfField()
        self.resizePawnsMove()

    # Resize TODO
    def resizePawnsMove(self):
        for pawn in self.pawns:
            fieldPos = pawn.position
            pawn.move(self.cornersPositions[fieldPos[1]][fieldPos[0]][0], self.cornersPositions[fieldPos[1]][fieldPos[0]][1])
            pawn.windowPos = [self.cornersPositions[fieldPos[1]][fieldPos[0]][0], self.cornersPositions[fieldPos[1]][fieldPos[0]][1]]

    # Create Matrix of field corner Positions
    def sizeOfField(self):
        self.oldCornersPositions = self.cornersPositions
        # Size of the step 13 - width of first col , 18 height of las row
        self.xStep = (self.width() - 13) // 8
        self.yStep = (self.height() - 18) // 8

        #Reduce gab created after //
        self.xStep+= 1 if ((self.width() - 13) % 8) >= 4 else 0
        self.yStep+= 1 if ((self.height() - 18) % 8) >= 4 else 0

        for i in range(8):
            for j in range(8):
                self.cornersPositions[i][j] = [j*self.xStep+13, i*self.yStep]
