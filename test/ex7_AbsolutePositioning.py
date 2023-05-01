import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # QLabel 생성
        label1 = QLabel('Label1', widget)
        label1.move(20, 20)
        label2 = QLabel('Label2', widget)
        label2.move(20, 60)

        # widget를 QMainWindow의 central widget으로 설정
        self.setCentralWidget(widget)

        # window의 타이틀 생성
        self.setWindowTitle('Absolute Positioning')

        # window의 위치와 크기 변경
        self.setGeometry(300, 300, 400, 200)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())