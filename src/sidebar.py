from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import math
import os


class Sidebar(QWidget):

    def __init__(self, *args, **kwargs):
        super(Sidebar, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        # Create widgets for the sidebar
        timePanel = TimePanel()
        historyPanel = HistoryPanel()
        oponentPanel = OpponentPanel()
        abandonButton = AbandonButton()

        # Put the widgets into the layout
        layout = QVBoxLayout(self)
        layout.addWidget(timePanel, 3)
        layout.addWidget(historyPanel, 3)
        layout.addWidget(oponentPanel, 3)
        layout.addWidget(abandonButton, 1)
        self.setLayout(layout)

        # Set sidebar settings
        self.setMinimumWidth(180)


class InfoPanel(QFrame):    # QFrame instead of QWidget to fill content margin with bg color
    """ Widget uniting apperance style of panels in the sidebar """
    def __init__(self, *args, **kwargs):
        super(InfoPanel, self).__init__(*args, **kwargs)

        self.setStyleSheet("background-color: #1F232D")

        # Prepare the layout for panel
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        self.setLayout(layout)


class TimePanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(TimePanel, self).__init__(*args, **kwargs)

        # Settings
        self.roundLength = 15000

        # Create timer indicating end of the round
        self.roundTimer = QTimer(self)
        self.roundTimer.timeout.connect(self.resetRound)

        # Create widgets used in the panel
        self.labelTimeIndicator = LabelTimeIndicator(self)
        self.circularTimeIndicator = CircularTimeIndicator(self)
        self.onTurnLabel = OnTurnLabel(self)

        # Init the playing state
        self.resetRound()

        # Put the widgets into the layout
        self.layout().addWidget(self.onTurnLabel)
        self.layout().addWidget(self.circularTimeIndicator, 1)
        self.layout().addWidget(self.labelTimeIndicator)

    def resetRound(self):
        # Reset timer indicating end of the round
        self.roundTimer.start(self.roundLength)

        # Reset time indicators
        self.labelTimeIndicator.reset()
        self.circularTimeIndicator.reset()
        self.onTurnLabel.switchPlayer()


class OnTurnLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(OnTurnLabel, self).__init__(*args, **kwargs)

        # Label settings
        self.setAlignment(Qt.AlignCenter)

        # Texts used in label
        self.texts = ['Jste na řadě!', 'Protihráč je na řadě']
        self.textIndex = 0

        # Init the text
        self.switchPlayer()

    def switchPlayer(self):
        # Switch the text indicating who is on turn
        self.textIndex = (self.textIndex + 1) % 2
        self.setText(self.texts[self.textIndex])


class LabelTimeIndicator(QLabel):
    def __init__(self, *args, **kwargs):
        super(LabelTimeIndicator, self).__init__(*args, **kwargs)

        # Label settings
        self.setAlignment(Qt.AlignCenter)

        # Create seconds timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.subSecond)

        # Init the timer
        self.secondsRemaining = 0
        self.reset()

    def subSecond(self):
        # Decrease remaining time
        if self.secondsRemaining > 0:
            self.secondsRemaining -= 1

        # Redraw text shown
        self.updateText()

    def updateText(self):
        # Find out how to say it in czech
        if self.secondsRemaining > 4 or self.secondsRemaining == 0:
            self.setText('{0} sekund'.format(self.secondsRemaining))
        elif self.secondsRemaining > 1:
            self.setText('{0} sekundy'.format(self.secondsRemaining))
        else:
            self.setText('{0} sekunda'.format(self.secondsRemaining))

    def reset(self):
        # Start new round
        self.secondsRemaining = int(self.parent().roundLength / 1000)

        # Redraw text shown
        self.updateText()

        # Resart the timer
        self.timer.start(1000)


class CircularTimeIndicator(QWidget):
    def __init__(self, *args, **kwargs):
        super(CircularTimeIndicator, self).__init__(*args, **kwargs)

        # Widget settings
        self.setMinimumSize(40, 40)
        self.sampling = 10

        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.repaint)
        self.timer.start(self.sampling)

    def paintEvent(self, event):
        # Settings
        margin = 10

        # Calculate line width
        lineWidth = 1 + round(min(self.width(), self.height()) / 30)
        lineWidthHalf = math.ceil(lineWidth/2)

        # Setup drawing
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setWidth(lineWidth)
        pen.setColor(Qt.white)
        painter.setPen(pen)

        # Calculate size and angle
        diameter = min(self.width(), self.height()) - lineWidthHalf*2 - margin*2
        xPosStart = math.floor((self.width() - diameter) / 2)
        rectangle = QRectF(xPosStart, lineWidthHalf + margin, diameter, diameter)
        angle = self.parent().roundTimer.remainingTime() / self.parent().roundLength * 360

        # Draw
        painter.drawArc(rectangle, 90*16, angle*16)

    def reset(self):
        # Restart the timer
        self.timer.start(self.sampling)


class HistoryPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(HistoryPanel, self).__init__(*args, **kwargs)

        # Create table and list for items
        self.table = QTableWidget(self)
        self.moves = []

        # Table settings
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Stretch to 100% width available

        # Add widgets to the layout
        self.layout().addWidget(QLabel('Historie tahů'))
        self.layout().addWidget(self.table)

        # @todo Dummy data
        self.storeMove('aa', 'bb')
        self.storeMove('cc', 'dd')

    @pyqtSlot(str, str)
    def storeMove(self, arg1, arg2):
        # Store new data
        self.moves = [(arg1, arg2)] + self.moves

        # Update table settings
        self.table.setRowCount(self.table.rowCount() + 1)

        # Repopulate the table
        row = 0
        for move in self.moves:
            self.table.setItem(row, 0, QTableWidgetItem(move[0]))
            self.table.setItem(row, 1, QTableWidgetItem(move[1]))
            row += 1


class OpponentPanel(InfoPanel):
    def __init__(self, *args, **kwargs):
        super(OpponentPanel, self).__init__(*args, **kwargs)

        # Create widget for opponent's name
        opponentNameLabel = QLabel('Jan Novák', self)
        opponentNameLabel.setAlignment(Qt.AlignCenter)

        # Create widget for opponent's avatar
        opponentAvatarLabel = OpponentAvatarLabel(self)

        # Create widget for opponent's wins count
        opponentWinsCountLabel = QLabel('1337 výher', self)
        opponentWinsCountLabel.setAlignment(Qt.AlignCenter)

        # Add widgets to the layout
        self.layout().addWidget(opponentNameLabel)
        self.layout().addWidget(opponentAvatarLabel, 1)
        self.layout().addWidget(opponentWinsCountLabel)


class OpponentAvatarLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(OpponentAvatarLabel, self).__init__(*args, **kwargs)

        # Image settings
        self.margin = 10
        self.setMinimumSize(50 + self.margin, 50 + self.margin)
        self.originalPixmap = QPixmap(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img/avatar.png')))
        self.setAlignment(Qt.AlignCenter)

    def resizeEvent(self, event):
        # Resize with the window
        self.setPixmap(self.originalPixmap.scaled(self.width() - self.margin*2, self.height() - self.margin*2, Qt.KeepAspectRatio | Qt.SmoothTransformation))


class AbandonButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(AbandonButton, self).__init__(*args, **kwargs)

        # Button settings
        self.setText('Vzdát se')
        self.released.connect(self.showDialog)

    def showDialog(self):
        # Are you sure dialog
        if QMessageBox.Yes == QMessageBox.question(self, 'Vzdát se', 'Opravdu se chcete vzdát?'):
            # Show menu
            from menu_window import MenuWindow
            self.cams = MenuWindow()
            self.cams.show()

            # Close this game window
            self.window().close()