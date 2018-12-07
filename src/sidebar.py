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
    def __init__(self, *args, **kwargs):
        super(TimePanel, self).__init__(*args, **kwargs)

        onTurnLabel = QLabel('Jste na řadě!')
        onTurnLabel.setAlignment(Qt.AlignCenter)

        remainingTimeLabel = QLabel('15 sekund');
        remainingTimeLabel.setAlignment(Qt.AlignCenter)


        self.layout().addWidget(onTurnLabel)
        self.layout().addWidget(remainingTimeLabel)

class HistoryPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(HistoryPanel, self).__init__(*args, **kwargs)

        self.layout().addWidget(QLabel('Historie tahů'))

class OpponentPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(OpponentPanel, self).__init__(*args, **kwargs)

        opponentNameLabel = QLabel('Jan Novák')
        opponentNameLabel.setAlignment(Qt.AlignCenter)

        opponentWinsCountLabel = QLabel('1337 výher');
        opponentWinsCountLabel.setAlignment(Qt.AlignCenter)

        self.layout().addWidget(opponentNameLabel)
        self.layout().addWidget(opponentWinsCountLabel)