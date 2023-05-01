import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # 레이블 생성
        label1 = QLabel('Label1')
        label1.setStyleSheet('background-color: #ff0000')
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Label2')
        label2.setStyleSheet('background-color: #ffff00')
        label2.setAlignment(Qt.AlignHCenter)


        # 레이아웃 생성
        layout = QVBoxLayout()
        # 레이아웃에 위젯 추가
        layout.addWidget(label1)
        layout.addWidget(label2)

        # widget에 레이아웃 추가
        widget.setLayout(layout)

        # central widget에 widget 추가
        self.setCentralWidget(widget)
        self.setWindowTitle('QLabel')
        # self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())