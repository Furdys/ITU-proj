from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_window import MainWindow
import os

class MenuWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chess Menu')
        self.resize(700, 500)
        self.setCentralWidget(QWidget())

        self.setStyleSheet("background-color: #272C38")
        self.createLayout()
        self.show()


    def createLayout(self):
        menu = QWidget()
        menu.setStyleSheet("""
            QWidget {
                background-color: #1F232D;
            }
                      
            QPushButton {
                background-color: #3C6478;
                font-weight: bold;
                color: #FFF;
                height: 48px;
                width: 200px;
            }
                           """)

        grid = QGridLayout()

        print(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/playIcon.png')))
        grid.setSpacing(25)
        playButton = QPushButton('Hrát', self)
        playButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/playIcon.png')))))
        playButton.setIconSize(QSize(40,40))
        playButton.clicked.connect(self.chessboardWindow_onClick)

        settingsButton = QPushButton('Nastavení', self)
        testbutton2 = QPushButton('Test 2', self)
        testbutton3 = QPushButton('Test 3', self)
        testbutton4 = QPushButton('Test 4', self)

        grid.addWidget(playButton, 0,1)
        grid.addWidget(settingsButton, 1,1)
        grid.addWidget(testbutton2, 2,1)
        grid.addWidget(testbutton3, 3,1)
        grid.addWidget(testbutton4, 4,1)
        menu.setLayout(grid)

        hbox = QHBoxLayout()
        hbox.addWidget(QWidget(), 1)
        hbox.addWidget(menu, 1)
        hbox.addWidget(QWidget(), 1)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch()

        self.centralWidget().setLayout(vbox)

    @pyqtSlot()
    def chessboardWindow_onClick(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close()





