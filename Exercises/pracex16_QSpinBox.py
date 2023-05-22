### Example14. QButtonGroup1 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QHBoxLayout, QWidget, QLabel, QSpinBox, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label1 =QLabel("생년월일")
        spinbox_year = QSpinBox()
        spinbox_year.setRange(1990, 2023)
        spinbox_month = QSpinBox()
        spinbox_month.setRange(1,12)
        spinbox_day = QSpinBox()
        spinbox_day.setRange(1,31)

        #레이아웃 설정
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(spinbox_year)
        hbox.addWidget(spinbox_month)
        hbox.addWidget(spinbox_day)

        # 윈도우 설정
        widget= QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())