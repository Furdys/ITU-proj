from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_window import MainWindow


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()