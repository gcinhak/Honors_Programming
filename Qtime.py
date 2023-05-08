import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.label1 = QLabel()
        self.label2 = QLabel()
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle("Test")
        self.setGeometry(1000, 200, 300, 300)

        # timer 1
        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.timeout_fun)
        self.time_cnt = 0

        # timer 2
        self.timer2 = QTimer(self)
        self.timer2.start(500)
        self.timer2.timeout.connect(self.timeout_fun2)
        self.time_cnt2 = 0

    def timeout_fun(self):
        self.time_cnt += 1
        self.label1.setText(str(self.time_cnt))
        print("time cnt is %d" % self.time_cnt)

    def timeout_fun2(self):
        self.time_cnt2 += 1
        self.label2.setText(str(self.time_cnt2))
        print("time cnt2 is %d" % self.time_cnt2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    app.exec_()