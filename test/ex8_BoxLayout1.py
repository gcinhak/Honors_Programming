import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # QLabel 생성
        label1 = QLabel('Label1')
        label1.setStyleSheet('background-color: #ff0000')
        label2 = QLabel('Label2')
        label2.setStyleSheet('background-color: #ffff00')

        # QHBoxLayout 생성, horizontal(수평)
        hbox = QHBoxLayout()
        # Layout에 위젯 추가
        hbox.addWidget(label1)
        hbox.addWidget(label2)

        # QWidget 객체에 레이아웃 ( 하나의 레이아웃만 가짐 )
        widget.setLayout(hbox)

        # widget를 QMainWindow의 central widget으로 설정
        self.setCentralWidget(widget)
        # window의 타이틀 생성
        self.setWindowTitle('Box Layout')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())