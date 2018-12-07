from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class Sidebar(QWidget):

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        timePanel = QLabel('Time')
        historyPanel = QLabel('History')
        oponentPanel = QLabel('Opponent')
        abadonButton = QPushButton('Vzdát se')

        layout.addWidget(timePanel)
        layout.addWidget(historyPanel)
        layout.addWidget(oponentPanel)
        layout.addWidget(abadonButton)

        self.setLayout(layout)