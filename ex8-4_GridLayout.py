### Example8-4. GridLayout ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        layout_grid = QGridLayout()

        label1 = QLabel('1')
        label1.setStyleSheet('background-color: #F28444; font-size: 20px; font-weight: bold;')
        label2 = QLabel('2')
        label2.setStyleSheet('background-color: #95BFA4; font-size: 20px; font-weight: bold;')
        label3 = QLabel('3')
        label3.setStyleSheet('background-color: #F29E38; font-size: 20px; font-weight: bold;')
        label4 = QLabel('4')
        label4.setStyleSheet('background-color: #FFF8EE; font-size: 20px; font-weight: bold;')
        label5 = QLabel('5')
        label5.setStyleSheet('background-color: #FFF8EE; font-size: 20px; font-weight: bold;')

        layout_grid.addWidget(label1, 0, 3)
        layout_grid.addWidget(label2, 1, 0)
        layout_grid.addWidget(label3, 2, 2)
        layout_grid.addWidget(label4, 3, 1)
        layout_grid.addWidget(label5, 0, 4)

        widget.setLayout(layout_grid)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Grid Layout")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())