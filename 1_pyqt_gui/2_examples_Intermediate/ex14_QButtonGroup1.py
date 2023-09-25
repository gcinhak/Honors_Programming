### Example14. QButtonGroup1 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn_itai = QRadioButton("IT-AI")
        btn_bio = QRadioButton("BIO")
        btn_design = QRadioButton("Design")
        btn_sports = QRadioButton("sports")

        self.btn_group_track = QButtonGroup()
        self.btn_group_track.addButton(btn_itai)
        self.btn_group_track.addButton(btn_bio)
        self.btn_group_track.addButton(btn_design)
        self.btn_group_track.addButton(btn_sports)

        btn_10 = QRadioButton("10th")
        btn_11 = QRadioButton("11th")
        btn_12 = QRadioButton("12th")

        self.btn_group_grade = QButtonGroup()
        self.btn_group_grade.addButton(btn_10)
        self.btn_group_grade.addButton(btn_11)
        self.btn_group_grade.addButton(btn_12)

        #레이아웃 설정
        hbox = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox1.addWidget(btn_itai)
        vbox1.addWidget(btn_bio)
        vbox1.addWidget(btn_design)
        vbox1.addWidget(btn_sports)
        vbox2.addWidget(btn_10)
        vbox2.addWidget(btn_11)
        vbox2.addWidget(btn_12)
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