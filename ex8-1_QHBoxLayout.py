### Example8-1. QHBoxLayout ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()

        hbox = QHBoxLayout()

        label1 = QLabel('1')
        label1.setStyleSheet('background-color: #F23D3D; font-size: 20px; font-weight: bold;')
        # label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('2')
        label2.setStyleSheet('background-color: #A65526; font-size: 20px; font-weight: bold;')
        # label2.setAlignment(Qt.AlignLeft)

        label3 = QLabel('3')
        label3.setStyleSheet('background-color: #BF9B7A; font-size: 20px; font-weight: bold;')
        # label3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        label4 = QLabel('4')
        label4.setStyleSheet('background-color: #F2BD1D; font-size: 20px; font-weight: bold;')
        # label4.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)

        # QWidget 객체에 레이아웃은 하나의 레이아웃만 가짐
        widget.setLayout(hbox)

        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 700, 100)
        self.setWindowTitle('QHBoxLayout')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())