from PyQt5.QtWidgets import QLabel, QMainWindow, QGridLayout, QPushButton, QHBoxLayout, QWidget
from sidebar import Sidebar


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        self.setWindowTitle('Chess')
        self.resize(500, 400)

        layout = QHBoxLayout()

        playingFiled = QLabel('Playing field')
        sidebar = Sidebar()

        layout.addWidget(playingFiled)
        layout.addWidget(sidebar)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

        self.show()