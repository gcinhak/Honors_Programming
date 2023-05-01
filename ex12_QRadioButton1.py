### Example12. QRadioButton1 - clicked ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_btn_1 = QRadioButton('First Button', self)
        self.radio_btn_2 = QRadioButton('Second Button', self)

        self.radio_btn_1.clicked.connect(self.on_radio1_btn_1)
        self.radio_btn_2.clicked.connect(self.on_radio1_btn_2)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.radio_btn_1)
        self.vbox.addWidget(self.radio_btn_2)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)

    def on_radio1_btn_1(self):
        print("button 1 clicked")

    def on_radio1_btn_2(self):
        print("button 2 clicked")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())