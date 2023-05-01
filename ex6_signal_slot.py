### Example6 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # QPushButton 생성
        btn = QPushButton('Click me', widget)

        # Signal 생성 pressed(), released()
        btn.clicked.connect(self.on_btn)

        # widget를 QMainWindow의 central widget으로 설정
        self.setCentralWidget(widget)

    #Slot 생성
    def on_btn(self):
        print('Hello World!')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())