import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.te_1 = QTextEdit()
        self.te_2 = QTextEdit()
        self.te_3 = QTextEdit()
        self.split_1 = QSplitter()
        self.split_2 = QSplitter()
        self.vbox = QVBoxLayout()

        self.init_widget()

    def init_widget(self):
        # self.split_1.setStyleSheet('background-color:red')
        # self.split_2.setStyleSheet('background-color:blue')
        self.split_1.addWidget(self.te_1)
        self.split_1.addWidget(self.te_2)
        self.split_1.setOrientation(Qt.Vertical)
        self.split_1.setStretchFactor(0,1)
        self.split_1.setStretchFactor(1,5)

        self.split_2.setOrientation(Qt.Horizontal)
        self.split_2.addWidget(self.split_1)
        self.split_2.addWidget(self.te_3)

        self.vbox.addWidget(self.split_2)
        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())