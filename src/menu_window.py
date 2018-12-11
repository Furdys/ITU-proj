from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from main_window import MainWindow
import os
import time
import webbrowser

class MenuWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Šachy')
       # self.resize(200, 400)
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
        playAIButton = QPushButton('Hrát proti A.I.', self)
        playAIButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/playIcon.png')))))
        playAIButton.setIconSize(QSize(40,40))
        playAIButton.clicked.connect(self.chessboardWindow_onClick)

        playOfflineButton = QPushButton('Hrát offline.', self)
        playOfflineButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/playIcon.png')))))
        playOfflineButton.setIconSize(QSize(40,40))
        playOfflineButton.clicked.connect(self.chessboardWindow_onClick)

        playOnlineButton = QPushButton('Hrát online.', self)
        playOnlineButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/playIcon.png')))))
        playOnlineButton.setIconSize(QSize(40,40))
        playOnlineButton.clicked.connect(self.inviteDialog_onClick)

        settingsButton = QPushButton('Nastavení', self)
        settingsButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/settingsIcon.png')))))
        settingsButton.setIconSize(QSize(40,40))
        settingsButton.clicked.connect(self.showSettings)

        infoButton = QPushButton('Napověda', self)
        infoButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/infoIcon.png')))))
        infoButton.setIconSize(QSize(40,40))
        infoButton.clicked.connect(self.infoBrowser)

        grid.addWidget(playAIButton, 0,1)
        grid.addWidget(playOfflineButton, 1,1)
        grid.addWidget(playOnlineButton, 2,1)
        grid.addWidget(infoButton, 3,1)
        grid.addWidget(settingsButton, 4,1)
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

    @pyqtSlot()
    def chessboardWindow_onClick(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def showSettings(self):
        self.stacked_layout.setCurrentIndex(1)

    @pyqtSlot()
    def inviteDialog_onClick(self):
        inviteDialog = InviteDialog()
        inviteDialog.exec()

        if (inviteDialog.playerFound()):
            QSound.play(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sound/foundSound.wav')))
            self.chessboardWindow_onClick()

    @pyqtSlot()
    def infoBrowser(self):
        webbrowser.open('https://www.chess.com/cs/learn-how-to-play-chess')

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
            
            QComboBox {
                background-color: #3C6478;
                font: bold 16px;
                color: #FFF;
                height: 48px;
                width: 200px;
                text-align: center;           
            
            }
            
            QListView {
                color: white;
            }
                           
            QLabel {
                color:  #FFF;
                font: bold 14px;
                min-width: 2em;
                text - align: center;
                }
                
                    """)

        grid = QGridLayout()
        grid.setSpacing(25)
        grid.setHorizontalSpacing(5)

        grid.addWidget(QLabel("Mód: "),0,0)

        comboBox = QComboBox()
        comboBox.setEditable(True)
        comboBox.lineEdit().setAlignment(Qt.AlignCenter)
        comboBox.lineEdit().setReadOnly(True)
        comboBox.addItem("Classic (15+15)")
        comboBox.addItem("Rapid (10+0)")
        comboBox.addItem("Blitz (5+3)")
        comboBox.addItem("Bullet (2+1)")

        returnButton = QPushButton('Zpět', self)
        returnButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/returnIcon.png')))))
        returnButton.setIconSize(QSize(40,40))
        returnButton.clicked.connect(self.returnToMenu)
        grid.addWidget(comboBox, 0, 1)
        grid.addWidget(returnButton, 1, 0, 2, Qt.AlignHCenter)
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

class InviteDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setFixedSize(250,100)
        self.found = False
        self.setStyleSheet("""
            QDialog {
                background-color: #1F232D;
            }
            QLabel {
                color: #FFF;
                background-color: #3C6478;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                font: bold 14px;
                min-width: 10em;
                text-align: center;
            }

    
                        """)

        inviteLink = QLabel('Odkaz na hru')
        inviteLink.setAlignment(Qt.AlignCenter)
        inviteLink.setTextInteractionFlags(Qt.TextSelectableByMouse)
        cancelButton = QPushButton("Zrušiť")
        cancelButton.setStyleSheet("""
            QPushButton {
                background-color: darkred;
                font-weight: bold;
                color: #FFF;
                height: 48px;
                width: 200px;
        }
        
                            """)

        cancelButton.clicked.connect(self.close)
        clipboardButton = QPushButton()
        clipboardButton.setIcon(QIcon(QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/clipboardIcon.png')))))
        clipboardButton.setIconSize(QSize(25, 25))
        clipboardButton.clicked.connect(self.copyToClipboard)

        hbox = QHBoxLayout()
        hbox.stretch(1)
        hbox.addWidget(inviteLink)
        hbox.addWidget(clipboardButton)
        self.dialogLayout = QVBoxLayout()
        self.dialogLayout.addLayout(hbox)
        #self.dialogLayout.addWidget(inviteLink)
        self.dialogLayout.addWidget(cancelButton)
        self.setLayout(self.dialogLayout)

    @pyqtSlot()
    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("Odkaz na hru")
        time.sleep(10)
        self.found = True
        self.close()

    def playerFound(self):
        return self.found





