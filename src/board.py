from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import math
import os
from field import Field
from pawn import Pawn

class Board(QWidget):

    passClickToField = pyqtSignal(int, int)

    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)

        self.playerPlaying = 1
        self.pawnSelected = False
        self.selectedPosition = [0,0]
        self.oldPosition = [0,0]

        # Position for pawns
        self.cornersPositions = [[[0, 0] for x in range(8)] for y in range(8)]

    @pyqtSlot()
    def AnimFinish(self):
        print("Fuk", self.oldPosition)
        #Hide enemy pawn -> was deleted
        if (self.Matrix[self.selectedPosition[1]][self.selectedPosition[0]].hasPawn == True):
            j = 0
            for j in range(len(self.pawns)):
                if self.pawns[j].position[0] == self.selectedPosition[0] and self.pawns[j].position[1] == self.selectedPosition[1]:
                    print("Co do", self.pawns[j].position[0], self.pawns[j].position[1])
                    break
            self.pawns[j].hide()
            self.pawns[j].deleted = True

        for i in range(len(self.pawns)):
            if self.pawns[i].position[0] == self.oldPosition[0] and self.pawns[i].position[1] == self.oldPosition[1]:
                print(self.pawns[i].position[0],self.pawns[i].position[1])
                self.pawns[i].position[0] = self.selectedPosition[0]
                self.pawns[i].position[1] = self.selectedPosition[1]
                print(self.pawns[i].position[0],self.pawns[i].position[1])


    # To resolve when pas was clicked
    @pyqtSlot(int, int, int)
    def fieldWasClickedBoard(self, posY, posX, player): # pass signal to field
        if player == 2:
            print("Klikol na pole nie panaka")
            return

        if (self.pawnSelected and player == 3):
            print("Klikol na volne pole, skontroluj ci tam moze ist")
            self.doAnimation(posY, posX) # X is row Y is column
            return


        if (self.pawnSelected == True and self.playerPlaying != player):
            print("Skusit ci sa da vyhodit")
            self.doAnimation(posY, posX)
            return


        if (self.pawnSelected == False and self.playerPlaying != player):
            print("Klikol na superoveho panaka hned na zaciatku")
            return

        else:
            self.selectedPosition[0] = posY
            self.selectedPosition[1] = posX
            self.passClickToField.emit(posY, posX)
            self.pawnSelected = True
            print("Tu to ide: ", posY, posX)




    def mousePressEvent(self, event):
        super(Board, self).mousePressEvent(event)

    # newX, new Y represents index in self.cornersPositions, newX -> col, newY -> row
    def doAnimation(self, newX, newY):
        print(self.selectedPosition)

        index = self.selectedPosition # Position which X is X and Y is Y

        oldXY = self.cornersPositions[index[1]][index[0]] # Get old position of
        newXY = self.cornersPositions[newY][newX] # Get new position

        #Find pawn which should be moved
        i = 0
        for i in range(len(self.pawns)):
            if self.pawns[i].position == index:
                break

        distance = math.sqrt((oldXY[0] - newXY[0]) * (oldXY[0] - newXY[0]) + (oldXY[1] - newXY[1]) * (oldXY[1] - newXY[1]))
        self.anim = QPropertyAnimation(self.pawns[i], b"geometry")
        self.anim.setDuration(distance * 5)
        self.anim.setStartValue(QRect(oldXY[0], oldXY[1], self.pawns[i].width(), self.pawns[i].height()))
        self.anim.setEndValue(QRect(newXY[0], newXY[1], self.pawns[i].width(),self.pawns[i].height()))
        self.anim.start()

        self.anim.finished.connect(self.AnimFinish) # When animation is finished signal is emited

        self.Matrix[index[1]][index[0]].hasPawn = False
        self.pawnSelected = False
        self.Matrix[newY][newX].hasPawn = True

        print("V:", index)
        self.oldPosition[0] = index[0]
        self.oldPosition[0] = index[1]
        self.selectedPosition[0] = newX
        self.selectedPosition[1] = newY

        print("E:", self.oldPosition)


    def createBord(self):

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
                self.passClickToField.connect(self.Matrix[i][j-1].fieldClicked)
                self.Matrix[i][j-1].clickedInField.connect(self.fieldWasClickedBoard)

        self.setLayout(layout)

        self.importPawns()

    # Import pawns
    def importPawns(self):
        self.pawns = []

        for i in range(8):
            self.pawns.append(Pawn(self))
            self.pawns[i].initUI("Pawn", [i,6], self.cornersPositions[6][i], 0)
            self.pawns[i].move(self.cornersPositions[6][i][0], self.cornersPositions[6][i][1])


        for i in range(8,16):
            self.pawns.append(Pawn(self))
            self.pawns[i].initUI("PawnWhite", [i-8,1], self.cornersPositions[1][i-8], 1)
            self.pawns[i].move(self.cornersPositions[1][i-8][0], self.cornersPositions[1][i-8][1])


        # Rooks
        self.pawns.append(Pawn(self))
        self.pawns[16].initUI("RookWhite", [0,0], self.cornersPositions[0][0], 1)
        self.pawns[16].move(self.cornersPositions[0][0][0], self.cornersPositions[0][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[17].initUI("RookWhite", [7,0], self.cornersPositions[7][0], 1)
        self.pawns[17].move(self.cornersPositions[7][0][0], self.cornersPositions[7][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[18].initUI("Rook", [7,7], self.cornersPositions[7][7], 0)
        self.pawns[18].move(self.cornersPositions[7][7][0], self.cornersPositions[7][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[19].initUI("Rook", [0,7], self.cornersPositions[0][7], 0)
        self.pawns[19].move(self.cornersPositions[7][7][0], self.cornersPositions[7][7][1])

        #Horses
        self.pawns.append(Pawn(self))
        self.pawns[20].initUI("Horse", [1,7], self.cornersPositions[1][7], 0)
        self.pawns[20].move(self.cornersPositions[1][7][0], self.cornersPositions[1][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[21].initUI("Horse", [6,7], self.cornersPositions[6][7], 0)
        self.pawns[21].move(self.cornersPositions[6][7][0], self.cornersPositions[6][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[22].initUI("HorseWhite", [1,0], self.cornersPositions[1][0], 1)
        self.pawns[22].move(self.cornersPositions[1][0][0], self.cornersPositions[1][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[23].initUI("HorseWhite", [6,0], self.cornersPositions[6][0], 1)
        self.pawns[23].move(self.cornersPositions[6][0][0], self.cornersPositions[6][0][1])

        #Bishops
        self.pawns.append(Pawn(self))
        self.pawns[24].initUI("Bishop", [2,7], self.cornersPositions[2][7], 0)
        self.pawns[24].move(self.cornersPositions[2][7][0], self.cornersPositions[2][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[25].initUI("Bishop", [5,7], self.cornersPositions[5][7], 0)
        self.pawns[25].move(self.cornersPositions[5][7][0], self.cornersPositions[5][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[26].initUI("BishopWhite", [2,0], self.cornersPositions[2][0], 1)
        self.pawns[26].move(self.cornersPositions[2][0][0], self.cornersPositions[2][0][1])

        self.pawns.append(Pawn(self))
        self.pawns[27].initUI("BishopWhite", [5,0], self.cornersPositions[5][0], 1)
        self.pawns[27].move(self.cornersPositions[5][0][0], self.cornersPositions[5][0][1])

        #Queens
        self.pawns.append(Pawn(self))
        self.pawns[28].initUI("Queen", [4,7], self.cornersPositions[4][7], 0)
        self.pawns[28].move(self.cornersPositions[4][7][0], self.cornersPositions[4][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[29].initUI("QueenWhite", [3,0], self.cornersPositions[3][0], 1)
        self.pawns[29].move(self.cornersPositions[3][0][0], self.cornersPositions[3][0][1])

        #Kings
        self.pawns.append(Pawn(self))
        self.pawns[30].initUI("King", [3,7], self.cornersPositions[3][7], 0)
        self.pawns[30].move(self.cornersPositions[3][7][0], self.cornersPositions[3][7][1])

        self.pawns.append(Pawn(self))
        self.pawns[31].initUI("KingWhite", [4,0], self.cornersPositions[4][0], 1)
        self.pawns[31].move(self.cornersPositions[4][0][0], self.cornersPositions[4][0][1])

        # Connect to slot, to know when clicked
        for pawn in self.pawns:
            pawn.clicked.connect(self.fieldWasClickedBoard)
            self.Matrix[pawn.position[1]][pawn.position[0]].hasPawn = True

    # Resizing
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
