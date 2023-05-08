### Practice Exercise 13 ###

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QRadioButton, QHBoxLayout, QWidget, QLabel, \
    QVBoxLayout, QPushButton, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_btn_1 = QRadioButton('1')
        self.radio_btn_2 = QRadioButton('2')
        self.radio_btn_3 = QRadioButton('3')
        self.btn_up = QPushButton('Up')
        self.btn_up.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_up.clicked.connect(self.on_btn_up)
        self.btn_up.setAutoRepeat(True)
        self.btn_up.setAutoRepeatInterval(100)
        self.btn_down = QPushButton('Down')
        self.btn_down.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_down.clicked.connect(self.on_btn_down)
        self.btn_down.setAutoRepeat(True)
        self.btn_down.setAutoRepeatInterval(100)
        self.label = QLabel('0')
        self.label.setStyleSheet('background-color: #FFFFFF; font-size: 40px; font-weight: bold;')
        self.label.setAlignment(Qt.AlignCenter)


        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.hbox2.addWidget(self.radio_btn_1)
        self.hbox2.addWidget(self.radio_btn_2)
        self.hbox2.addWidget(self.radio_btn_3)

        self.hbox1.addWidget(self.btn_up)
        self.hbox1.addWidget(self.btn_down)

        self.vbox.addWidget(self.label,stretch = 1)
        self.vbox.addLayout(self.hbox2,stretch = 1)
        self.vbox.addLayout(self.hbox1,stretch = 1)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 250, 200)

    def on_btn_up(self):
        score = int(self.label.text())
        if self.radio_btn_1.isChecked():
            score += 1
        elif self.radio_btn_2.isChecked():
            score += 2
        elif self.radio_btn_3.isChecked():
            score += 3
        self.label.setText(str(score))

    def on_btn_down(self):
        score = int(self.label.text())
        if self.radio_btn_1.isChecked():
            score -= 1
        elif self.radio_btn_2.isChecked():
            score -= 2
        elif self.radio_btn_3.isChecked():
            score -= 3
        self.label.setText(str(score))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())