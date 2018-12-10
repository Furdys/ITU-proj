from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Sidebar(QWidget):

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        timePanel = TimePanel()
        historyPanel = HistoryPanel()
        oponentPanel = OpponentPanel()
        abadonButton = QPushButton('Vzdát se')

        layout.addWidget(timePanel, 3)
        layout.addWidget(historyPanel, 3)
        layout.addWidget(oponentPanel, 3)
        layout.addWidget(abadonButton, 1)

        self.setLayout(layout)


class InfoPanel(QFrame):
    def __init__(self, *args, **kwargs):
        super(InfoPanel, self).__init__(*args, **kwargs)

        self.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.setLineWidth(2)
        self.setLayout(QVBoxLayout())


class TimePanel(InfoPanel):
    secondsRemaining = 15

    def __init__(self, *args, **kwargs):
        super(TimePanel, self).__init__(*args, **kwargs)

        onTurnLabel = QLabel('Jste na řadě!')
        onTurnLabel.setAlignment(Qt.AlignCenter)

        timer = QTimer(self)
        timer.timeout.connect(self.subSecond)
        timer.start(1000)

        self.secondsRemaining = 15
        self.remainingTimeLabel = QLabel()
        self.remainingTimeLabel.setAlignment(Qt.AlignCenter)
        self.redrawTime()

        self.layout().addWidget(onTurnLabel)
        self.layout().addWidget(self.remainingTimeLabel)

    def subSecond(self):
        if self.secondsRemaining > 0:
            self.secondsRemaining -= 1

        self.redrawTime()

    def redrawTime(self):
        if self.secondsRemaining > 4 or self.secondsRemaining == 0:
            self.remainingTimeLabel.setText('{0} sekund'.format(self.secondsRemaining))
        elif self.secondsRemaining > 1:
            self.remainingTimeLabel.setText('{0} sekundy'.format(self.secondsRemaining))
        else:
            self.remainingTimeLabel.setText('{0} sekunda'.format(self.secondsRemaining))


class HistoryPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(HistoryPanel, self).__init__(*args, **kwargs)

        table = QTableWidget()

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

        opponentNameLabel = QLabel('Jan Novák')
        opponentNameLabel.setAlignment(Qt.AlignCenter)

        opponentWinsCountLabel = QLabel('1337 výher');
        opponentWinsCountLabel.setAlignment(Qt.AlignCenter)

        self.layout().addWidget(opponentNameLabel)
        self.layout().addWidget(opponentWinsCountLabel)