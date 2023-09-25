### Example9. QPushButton3 ###

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()

        vbox = QVBoxLayout()

        self.btn1 = QPushButton('&Button1')
        self.btn1.resize(300,300)
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn2 = QPushButton('Button2')
        self.btn2.setShortcut('Alt+2')
        self.btn3 = QPushButton('Button3')
        self.btn3.setEnabled(False)

        self.btn1.clicked.connect(lambda state, btn = self.btn1: self.on_clicked_btn(state, btn))
        self.btn2.clicked.connect(lambda state, btn = self.btn2: self.on_clicked_btn(state, btn))
        self.btn3.clicked.connect(lambda state, btn = self.btn3: self.on_clicked_btn(state, btn))

        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        widget.setLayout(vbox)

        self.setCentralWidget(widget)
        self.setWindowTitle('QPushButton')

    def on_clicked_btn(self, state, btn):
        print(btn.text(), state)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())