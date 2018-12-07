from PyQt5.QtWidgets import QLabel, QMainWindow, QGridLayout, QPushButton, QHBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUI()




    def initUI(self):
        self.setWindowTitle('Chess')
        self.resize(500, 400)

        '''
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.setLayout(layout)
        '''

        layout = QHBoxLayout()
        layout.addWidget(QPushButton('1'))
        layout.addWidget(QPushButton('2'))

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

        self.show()