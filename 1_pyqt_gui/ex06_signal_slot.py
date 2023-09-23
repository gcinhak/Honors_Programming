### Example6 - Slonal, Slot ###

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
        btn.resize(100,100)
        btn.setCheckable(True)

        # Signal 생성 pressed(), released()
        btn.clicked.connect(self.on_btn_clicked)
        btn.pressed.connect(self.on_btn_pressed)
        btn.released.connect(self.on_btn_released)
        btn.toggled.connect(self.on_btn_toggled)

        # widget를 QMainWindow의 central widget으로 설정
        self.setCentralWidget(widget)

    #Slot 생성
    def on_btn_clicked(self):
        print('on_btn_clicked')

    def on_btn_pressed(self):
        print('on_btn_pressed')

    def on_btn_released(self):
        print('on_btn_released')

    def on_btn_toggled(self):
        print('on_btn_toggled')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())