from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import math


class Sidebar(QWidget):

    def __init__(self, *args, **kwargs):
        super(Sidebar, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        layout = QVBoxLayout(self)

        timePanel = TimePanel()
        historyPanel = HistoryPanel()
        oponentPanel = OpponentPanel()
        abandonButton = AbandonButton()

        layout.addWidget(timePanel, 3)
        layout.addWidget(historyPanel, 3)
        layout.addWidget(oponentPanel, 3)
        layout.addWidget(abandonButton, 1)

        self.setLayout(layout)


class InfoPanel(QFrame):    # QFrame instead of QWidget to fill content margin with bg color
    def __init__(self, *args, **kwargs):
        super(InfoPanel, self).__init__(*args, **kwargs)
        self.setStyleSheet("background-color: #1F232D")

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        self.setLayout(layout)


class TimePanel(InfoPanel):

    def __init__(self, *args, **kwargs):
        super(TimePanel, self).__init__(*args, **kwargs)

        self.roundLength = 15000

        self.roundTimer = QTimer(self)
        self.roundTimer.timeout.connect(self.resetRound)

        self.labelTimeIndicator = LabelTimeIndicator(self)
        self.circularTimeIndicator = CircularTimeIndicator(self)
        self.onTurnLabel = OnTurnLabel(self)

        self.resetRound()

        self.layout().addWidget(self.onTurnLabel)
        self.layout().addWidget(self.circularTimeIndicator)
        self.layout().addWidget(self.labelTimeIndicator)

    def resetRound(self):
        self.roundTimer.start(self.roundLength)

        self.labelTimeIndicator.reset()
        self.circularTimeIndicator.reset()
        self.onTurnLabel.switchPlayer()


class OnTurnLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(OnTurnLabel, self).__init__(*args, **kwargs)

        self.texts = ['Jste na řadě!', 'Protihráč je na řadě']
        self.textIndex = 0

        self.setAlignment(Qt.AlignCenter)

        self.switchPlayer()

    def switchPlayer(self):
        self.textIndex = (self.textIndex + 1) % 2
        self.setText(self.texts[self.textIndex])


class LabelTimeIndicator(QLabel):
    def __init__(self, *args, **kwargs):
        super(LabelTimeIndicator, self).__init__(*args, **kwargs)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.subSecond)

        self.secondsRemaining = 0
        self.reset()


        self.setAlignment(Qt.AlignCenter)

        self.updateText()

    def subSecond(self):
        if self.secondsRemaining > 0:
            self.secondsRemaining -= 1

        self.updateText()

    def updateText(self):
        if self.secondsRemaining > 4 or self.secondsRemaining == 0:
            self.setText('{0} sekund'.format(self.secondsRemaining))
        elif self.secondsRemaining > 1:
            self.setText('{0} sekundy'.format(self.secondsRemaining))
        else:
            self.setText('{0} sekunda'.format(self.secondsRemaining))

    def reset(self):
        self.secondsRemaining = int(self.parent().roundLength / 1000)
        self.updateText()

        self.timer.start(1000)


class CircularTimeIndicator(QWidget):
    def __init__(self, *args, **kwargs):
        super(CircularTimeIndicator, self).__init__(*args, **kwargs)

        self.sampling = 100

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.repaint)
        self.timer.start(self.sampling)


    def paintEvent(self, event):
        lineWidth = 2
        lineWidthHalf = math.ceil(lineWidth/2)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen()
        pen.setWidth(lineWidth)
        pen.setColor(Qt.white)
        painter.setPen(pen)

        diameter = min(self.width(), self.height()) - lineWidthHalf*2
        xPosStart = math.floor((self.width() - diameter) / 2)

        rectangle = QRectF(xPosStart, lineWidthHalf, diameter, diameter)
        angle = self.parent().roundTimer.remainingTime() / self.parent().roundLength * 360


        painter.drawArc(rectangle, 90*16, angle*16)

    def reset(self):
        self.timer.start(self.sampling)

class HistoryPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(HistoryPanel, self).__init__(*args, **kwargs)

        table = QTableWidget(self)

        moves = [
            ('g3', 'e5'),
            ('Bg2', 'f5'),
            ('Nh3', 'c5'),
            ('O-O', 'Ne7'),
        ]

        table.setColumnCount(2)
        table.setRowCount(len(moves))
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        row = 0
        for move in moves:
            table.setItem(row, 0, QTableWidgetItem(move[0]))
            table.setItem(row, 1, QTableWidgetItem(move[1]))
            row += 1

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Stretch to 100% width available

        self.layout().addWidget(QLabel('Historie tahů'))
        self.layout().addWidget(table)


class OpponentPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(OpponentPanel, self).__init__(*args, **kwargs)

        opponentNameLabel = QLabel('Jan Novák', self)
        opponentNameLabel.setAlignment(Qt.AlignCenter)

        opponentWinsCountLabel = QLabel('1337 výher', self)
        opponentWinsCountLabel.setAlignment(Qt.AlignCenter)

        self.layout().addWidget(opponentNameLabel)
        self.layout().addWidget(opponentWinsCountLabel)


class AbandonButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(AbandonButton, self).__init__(*args, **kwargs)

        self.setText('Vzdát se')
        self.released.connect(self.showDialog)

    def showDialog(self):
        if QMessageBox.Yes == QMessageBox.question(self, 'Vzdát se', 'Opravdu se chcete vzdát?'):
            from menu_window import MenuWindow
            self.cams = MenuWindow()
            self.cams.show()
            self.window().close()