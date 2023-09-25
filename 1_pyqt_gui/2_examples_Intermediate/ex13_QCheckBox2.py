import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox_1 = QCheckBox("CheckBox 1")
        self.checkbox_2 = QCheckBox("CheckBox 2")
        self.checkbox_3 = QCheckBox("CheckBox 3")

        self.checkbox_1.setTristate(True)
        self.checkbox_2.setTristate(True)
        self.checkbox_3.setTristate(True)

        # connect the signal to the slot
        self.checkbox_1.clicked.connect(self.on_clicked_checkbox_1)
        self.checkbox_2.toggled.connect(self.on_toggled_checkbox_2)
        self.checkbox_3.stateChanged.connect(self.on_stateChanged_checkbox_3)

        #레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.checkbox_1)
        vbox.addWidget(self.checkbox_2)
        vbox.addWidget(self.checkbox_3)
        print(self.checkbox_1.text(), self.checkbox_2.text(), self.checkbox_3.text())

        # 윈도우 설정
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("CheckBox")

    def on_clicked_checkbox_1(self, state):
        print(self.checkbox_1.checkState(), state)

    def on_toggled_checkbox_2(self, state):
        print(self.checkbox_2.checkState(), state)

    def on_stateChanged_checkbox_3(self, state):
        print(self.checkbox_3.checkState(), state)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())