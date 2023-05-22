import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QDoubleSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0.0, 5.5)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.dspinbox.setReadOnly(True)
        self.lbl = QLabel('$ 0.0')
        self.dspinbox.valueChanged.connect(self.on_spinbox_valuechanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl)
        vbox.addStretch()

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 100)

    def on_spinbox_valuechanged(self):
        self.lbl.setText('$ ' + str(self.dspinbox.value()))
        print(type(self.dspinbox.value()))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())