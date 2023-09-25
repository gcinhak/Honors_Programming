import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSpinBox, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.spinbox = QSpinBox()
        self.spinbox.setRange(-25, 25)
        # self.spinbox.setMinimum(-25)
        # self.spinbox.setMaximum(25)
        self.spinbox.setSingleStep(5)
        self.spinbox.setValue(-25)
        self.lbl = QLabel('-25')
        self.spinbox.valueChanged.connect(self.on_spinbox_valuechanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.spinbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 100)

    def on_spinbox_valuechanged(self):
        value = self.spinbox.value()
        self.lbl.setText(str(value))
        print(type(value), value)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())