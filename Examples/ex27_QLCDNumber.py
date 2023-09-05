import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("시계")
        self.setFixedSize(450, 200)
        self.init_ui()

    def init_ui(self):
        self.lcd = QLCDNumber()
        self.timer = QTimer()
        self.vbox = QVBoxLayout()

        self.init_widget()

    def init_widget(self):
        self.lcd.setSegmentStyle(2)
        self.lcd.setDigitCount(8)
        self.lcd.setFrameStyle(QFrame.NoFrame)

        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()

        self.vbox.addWidget(self.lcd)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)

    def show_time(self):
        time = QTime.currentTime()
        self.currentTime = time.toString('hh:mm:ss')
        self.lcd.display(self.currentTime)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.mouseClick = True
            self.oldPos = e.globalPos()

    def mouseReleaseEvent(self, e):
        self.mouseClick = False

    def mouseMoveEvent(self, e):
        if self.mouseClick:
            delta = QPoint(e.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = e.globalPos()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())