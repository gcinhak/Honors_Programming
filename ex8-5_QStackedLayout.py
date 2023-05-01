### Example8-5 QStackedLayout ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QStackedLayout, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        vbox = QVBoxLayout()
        self.layout_stack = QStackedLayout()

        label1 = QLabel('label-1')
        label1.setStyleSheet('background-color: #F28444; font-size: 20px; font-weight: bold;')
        label2 = QLabel('label-2')
        label2.setStyleSheet('background-color: #95BFA4; font-size: 20px; font-weight: bold;')
        label3 = QLabel('label-3')
        label3.setStyleSheet('background-color: #F29E38; font-size: 20px; font-weight: bold;')
        label4 = QLabel('label-4')
        label4.setStyleSheet('background-color: #FFF81E; font-size: 20px; font-weight: bold;')

        btn = QPushButton('change layout')
        btn.clicked.connect(self.on_clicked_btn)

        self.layout_stack.addWidget(label1)
        self.layout_stack.addWidget(label2)
        self.layout_stack.addWidget(label3)
        self.layout_stack.addWidget(label4)
        self.layout_stack.setCurrentIndex(0)

        vbox.addLayout(self.layout_stack)
        vbox.addWidget(btn)

        widget.setLayout(vbox)

        self.setCentralWidget(widget)
        self.setWindowTitle("QStacked Layout")

    def on_clicked_btn(self):
        self.count += 1
        self.layout_stack.setCurrentIndex(self.count % 4)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())