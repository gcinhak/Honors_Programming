### Example12. QRadioButton3 - slot 하나 사용 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_btn_1 = QRadioButton('First Button', self)
        self.radio_btn_2 = QRadioButton('Second Button', self)
        self.btn = QPushButton("aa")

        self.radio_btn_1.toggled.connect(self.on_toggled_radio)
        self.radio_btn_2.toggled.connect(self.on_toggled_radio)
        self.btn.clicked.connect(self.on_ck)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.radio_btn_1)
        self.vbox.addWidget(self.radio_btn_2)
        self.vbox.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)

    def on_ck(self):
        self.radio_btn_2.setChecked(True)
        self.radio_btn_2.setChecked(False)

    def on_toggled_radio(self):
        pass
        # self.radio_btn_1.setChecked(True)
        # print("on_toggled_radio")
        # btn_num = 0
        # if state:
        #     if self.radio_btn_1.isChecked():
        #         btn_num = 1
        #     elif self.radio_btn_2.isChecked():
        #         btn_num = 2
        #     print("Selected Button : {}".format(btn_num))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())