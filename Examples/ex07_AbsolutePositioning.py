### Example7. AbsolutePositioning ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()

        label1 = QLabel('Label1', widget)
        label1.move(20, 20)
        label2 = QLabel('Label2', widget)
        label2.move(20, 60)
        label3 = QLabel('Label3', widget)
        label3.move(80, 20)
        label4 = QLabel('Label4', widget)
        label4.move(80, 60)

        self.setCentralWidget(widget)
        self.setWindowTitle('Absolute Positioning')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())