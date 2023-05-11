### Example14. QButtonGroup1 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        t_btn1 = QRadioButton("IT-AI")
        t_btn2 = QRadioButton("BIO")
        t_btn3 = QRadioButton("Design")
        t_btn4 = QRadioButton("sports")

        self.t_btn_group = QButtonGroup()
        self.t_btn_group.addButton(t_btn1)
        self.t_btn_group.addButton(t_btn2)
        self.t_btn_group.addButton(t_btn3)
        self.t_btn_group.addButton(t_btn4)

        g_btn1 = QRadioButton("10th")
        g_btn2 = QRadioButton("11th")
        g_btn3 = QRadioButton("12th")

        self.g_btn_group = QButtonGroup()
        self.g_btn_group.addButton(g_btn1)
        self.g_btn_group.addButton(g_btn2)
        self.g_btn_group.addButton(g_btn3)

        #레이아웃 설정
        hbox = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox1.addWidget(t_btn1)
        vbox1.addWidget(t_btn2)
        vbox1.addWidget(t_btn3)
        vbox1.addWidget(t_btn4)
        vbox2.addWidget(g_btn1)
        vbox2.addWidget(g_btn2)
        vbox2.addWidget(g_btn3)
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        # 윈도우 설정
        widget= QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("GButtonGroup")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())