### Example11. QRadioButton ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QRadioButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_btn_1 = QRadioButton('First Button', self)
        self.radio_btn_2 = QRadioButton('Second Button', self)

        self.btnGroup = QButtonGroup()
        self.btnGroup.addButton(self.radio_btn_1)
        self.btnGroup.addButton(self.radio_btn_2)
        # self.btnGroup.setExclusive(False)
        self.btnGroup.buttonClicked.connect(self.fnc_radio)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.radio_btn_1)
        self.vbox.addWidget(self.radio_btn_2)

        widget = QWidget()
        widget.setLayout(self.vbox)

        # 윈도우 설정
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("GButtonGroup")

    # ===============================  Slot 부분   =========================================
    def fnc_radio(self, button):
        print(button.text(),'toggled')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())