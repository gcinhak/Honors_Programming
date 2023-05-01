### Example8-3 NestedLayout ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()

        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        label1 = QLabel('1')
        label1.setStyleSheet('background-color: #F28444; font-size: 20px;')
        label2 = QLabel('2')
        label2.setStyleSheet('background-color: #95BFA4; font-size: 20px; font-weight: bold;')
        label3 = QLabel('3')
        label3.setStyleSheet('background-color: #F29E38; font-size: 20px; font-weight: bold;')
        label4 = QLabel('4')
        label4.setStyleSheet('background-color: #FFF8EE; font-size: 20px; font-weight: bold;')
        label5 = QLabel('5')
        label5.setStyleSheet('background-color: #F2889B; font-size: 20px; font-weight: bold;')

        hbox1.addWidget(label1)
        hbox1.addWidget(label2)
        hbox2.addWidget(label3)
        hbox2.addWidget(label4)
        hbox2.addWidget(label5)

        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)

        widget.setLayout(vbox1)
        self.setCentralWidget(widget)
        self.setWindowTitle("Nested Layout")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())