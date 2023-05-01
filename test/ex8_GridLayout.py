import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # QLabel 생성
        label1 = QLabel('Label1')
        label1.setStyleSheet('background-color: red')
        label2 = QLabel('Label2')
        label2.setStyleSheet('background-color: blue')
        label3 = QLabel('Label3')
        label3.setStyleSheet('background-color: yellow')
        label4 = QLabel('Label4')
        label4.setStyleSheet('background-color: pink')

        # 레이아웃 생성
        grid = QGridLayout()

        # 레이아웃에 위젯 추가
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)

        # widget에 레이아웃 추가
        widget.setLayout(grid)

        # central widget에 widget 추가
        self.setCentralWidget(widget)

        self.setWindowTitle('QGridLayout')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())