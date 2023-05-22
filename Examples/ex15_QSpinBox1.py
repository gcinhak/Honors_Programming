import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.on_spinbox_valuechanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.spinbox)

        widget_central = QWidget()
        widget_central.setLayout(vbox)
        self.setCentralWidget(widget_central)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("QSpinBox")

    def on_spinbox_valuechanged(self):
        value = self.spinbox.value()
        print(type(value), value)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())