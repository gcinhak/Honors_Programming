import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # Button 새성
        btn1 = QPushButton('&Button1')
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton('Button2')
        btn2.setShortcut('Alt+2')

        btn3 = QPushButton()
        btn3.setText('Button3')
        btn3.setEnabled(False)

        # 레이아웃 생성
        vbox = QVBoxLayout()

        # 레이아웃에 위젯 추가
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        # widget에 레이아웃 추가
        widget.setLayout(vbox)

        # central widget에 widget 추가
        self.setCentralWidget(widget)
        self.setWindowTitle('QPushButton')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())