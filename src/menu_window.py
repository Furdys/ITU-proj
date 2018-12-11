from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
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
        self.stacked_layout = QStackedLayout()
        self.centralWidget().setLayout(self.stacked_layout)

        self.setStyleSheet("background-color: #272C38")
        self.createMenuLayout()
        self.createSettingsLayout()

        #self.stacked_layout = QStackedLayout()
        #self.stacked_layout.addWidget(self.selectMenuWidget)

        #self.setCentralWidget(QWidget())
        #self.centralWidget().setLayout(self.stacked_layout)

        self.show()


    def createMenuLayout(self):
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
        grid.setSpacing(25)
        playButton = QPushButton('Hrát', self)
        playButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/playIcon.png')))))
        playButton.setIconSize(QSize(40,40))
        playButton.clicked.connect(self.chessboardWindow_onClick)

        settingsButton = QPushButton('Nastavení', self)
        settingsButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/settingsIcon.png')))))
        settingsButton.setIconSize(QSize(40,40))
        settingsButton.clicked.connect(self.showSettings)

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

        self.selectMenuWidget = QWidget()
        self.selectMenuWidget.setLayout(vbox)
        self.centralWidget().layout().addWidget(self.selectMenuWidget)
        #self.centralWidget().setLayout(vbox)

        testbutton2.released.connect(self.testSound)

    def testSound(self):
        QSound.play(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sound/piecePlaced.wav')))

    @pyqtSlot()
    def chessboardWindow_onClick(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def showSettings(self):
        self.stacked_layout.setCurrentIndex(1)

    def createSettingsLayout(self):
        settings = QWidget()
        settings.setStyleSheet("""
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
        grid.setSpacing(25)


        returnButton = QPushButton('Zpět', self)
        returnButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/returnIcon.png')))))
        returnButton.setIconSize(QSize(40,40))
        returnButton.clicked.connect(self.returnToMenu)
        grid.addWidget(returnButton, 0,1)
        settings.setLayout(grid)

        hbox = QHBoxLayout()
        hbox.addWidget(QWidget(), 1)
        hbox.addWidget(settings, 1)
        hbox.addWidget(QWidget(), 1)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch()

        self.selectSettingsWidget = QWidget()
        self.selectSettingsWidget.setLayout(vbox)
        self.centralWidget().layout().addWidget(self.selectSettingsWidget)

    @pyqtSlot()
    def returnToMenu(self):
        self.stacked_layout.setCurrentIndex(0)




