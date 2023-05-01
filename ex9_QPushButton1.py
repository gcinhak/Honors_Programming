### Example9. QPushButton1 ###

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        vbox = QVBoxLayout()

        btn1 = QPushButton('&Button1')
        btn1.setCheckable(True)
        btn1.toggle()
        btn2 = QPushButton('Button2')
        btn2.setShortcut('Alt+2')
        btn3 = QPushButton('Button3')
        btn3.setEnabled(False)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        widget.setLayout(vbox)

        self.setCentralWidget(widget)
        self.setWindowTitle('QPushButton')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())