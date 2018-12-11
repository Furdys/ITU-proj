from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from sidebar import Sidebar
from board import Board


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        self.setWindowTitle('Chess')
        self.resize(700, 500)

        layout = QHBoxLayout()

        playingFiled = Board()
        playingFiled.setObjectName("boardPlayer")
        playingFiled.createBord()
        sidebar = Sidebar()

        layout.addWidget(playingFiled, 3)   # Takes 3 times more space than sidebar
        layout.addWidget(sidebar, 1)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

        playingFiled.playerChanged.connect(sidebar.TimePanel.boardSays)
        self.show()
