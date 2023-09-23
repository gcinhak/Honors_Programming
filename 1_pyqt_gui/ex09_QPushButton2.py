### Example9. QPushButton2 ###

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.btn1 = QPushButton('&Button1')
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn2 = QPushButton('Button2')
        self.btn2.setShortcut('Alt+2')
        self.btn3 = QPushButton('Button3')
        self.btn3.setEnabled(False)

        self.btn1.toggled.connect(self.on_clicked_btn1)
        self.btn2.clicked.connect(self.on_clicked_btn2)
        self.btn3.clicked.connect(self.on_clicked_btn3)

        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)

        self.widget.setLayout(self.vbox)

        self.setCentralWidget(self.widget)
        self.setWindowTitle('QPushButton')

    def on_clicked_btn1(self,state):
        print(self.btn1.text(), state)

    def on_clicked_btn2(self, state):
        print(self.btn2.text(), state)

    def on_clicked_btn3(self, state):
        print(self.btn3.text(), state)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())