### Example5 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    ### ui 설정 ###
    def init_ui(self):
        # widget 생성
        self.label = QLabel()
        btn_yes = QPushButton("YES")
        btn_no = QPushButton("NO")

        # connect the signal to the slot
        btn_yes.clicked.connect(self.on_clicked_btn_ok)
        btn_no.clicked.connect(self.on_clicked_btn_no)

        # layout 생성, widget 배치
        hbox = QHBoxLayout()
        hbox.addWidget(btn_yes)
        hbox.addWidget(btn_no)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        # QWidget 생성과 layout 배치
        widget = QWidget()
        widget.setLayout(vbox)

        # widget를 QMainWindow의 centralwidget으로 설정
        self.setCentralWidget(widget)

    ### slot 설정 ###
    def on_clicked_btn_ok(self):
        self.label.setText("YES")

    def on_clicked_btn_no(self):
        self.label.setText("NO")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())