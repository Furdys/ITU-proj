from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from main_window import MainWindow
from menu_window import MenuWindow


if __name__ == '__main__':
    app = QApplication([])
    #window = MainWindow()
    window = MenuWindow()
    sys.exit(app.exec_())