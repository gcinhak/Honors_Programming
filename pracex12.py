### Practice Exercise 12 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QHBoxLayout, QWidget, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_btn_1 = QRadioButton('red', self)
        self.radio_btn_2 = QRadioButton('green', self)
        self.radio_btn_3 = QRadioButton('blue', self)
        self.radio_btn_1.setChecked(True)

        self.label = QLabel()
        self.label.setStyleSheet('background-color: #FF0000;')

        self.radio_btn_1.toggled.connect(self.on_toggled_radio)
        self.radio_btn_2.toggled.connect(self.on_toggled_radio)
        self.radio_btn_3.toggled.connect(self.on_toggled_radio)

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.hbox.addWidget(self.radio_btn_1)
        self.hbox.addWidget(self.radio_btn_2)
        self.hbox.addWidget(self.radio_btn_3)

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.label)


        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 250, 100)

    def on_toggled_radio(self, checked):
        if checked:
            if self.radio_btn_1.isChecked():
                self.label.setStyleSheet('background-color: #FF0000;')
            elif self.radio_btn_2.isChecked():
                self.label.setStyleSheet('background-color: #00FF00;')
            elif self.radio_btn_3.isChecked():
                self.label.setStyleSheet('background-color: #0000FF;')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())