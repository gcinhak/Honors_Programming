### Example13. QRadioButton ###

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

        vbox = QVBoxLayout()
        vbox.addWidget(self.checkbox_1)
        vbox.addWidget(self.checkbox_2)
        vbox.addWidget(self.checkbox_3)

        widget = QWidget()
        widget.setLayout(vbox)

        # 윈도우 설정
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("CheckBox")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())