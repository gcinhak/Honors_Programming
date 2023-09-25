### Example5 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

# QMainWindow 상속
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # QLabel 생성
        label1 = QLabel(widget)
        label1.setText("Hello World1")
        label2 = QLabel(widget)
        label2.setText("Hello World2")
        label2.move(0, 30)

        # widget를 QMainWindow의 centralwidget으로 설정
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())