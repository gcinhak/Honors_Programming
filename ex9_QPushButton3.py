### Example9. QPushButton3 ###

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        # 레이아웃 생성
        vbox = QVBoxLayout()

        # Button 새성
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

        # 레이아웃에 위젯 추가
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        # widget에 레이아웃 추가
        widget.setLayout(vbox)

        # central widget에 widget 추가
        self.setCentralWidget(widget)
        self.setWindowTitle('QPushButton')

    def on_clicked_btn(self, state, btn):
        print(btn.text(), state)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())