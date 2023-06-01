### Example14. QButtonGroup1 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QHBoxLayout, QWidget, QLabel, QSpinBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label1 =QLabel("생년월일")
        self.spinbox_year = QSpinBox()
        self.spinbox_year.setRange(1990, 2023)
        self.spinbox_month = QSpinBox()
        self.spinbox_month.setRange(1,12)
        self.spinbox_day = QSpinBox()
        self.spinbox_day.setRange(1,31)
        btn = QPushButton("저장")
        btn.clicked.connect(self.on_btn)

        #레이아웃 설정
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(self.spinbox_year)
        hbox.addWidget(self.spinbox_month)
        hbox.addWidget(self.spinbox_day)
        hbox.addWidget(btn)

        # 윈도우 설정
        widget= QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)

    def on_btn(self):
        print("{}년 {}월 {}일".format(self.spinbox_year.value(),self.spinbox_month.value(),self.spinbox_day.value()))


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())