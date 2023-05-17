### Example5 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # QLabel 생성
        label1 = QLabel(self)
        label1.setText("First Label")
        label2 = QLabel(self)
        label2.setText("Second Label")
        label2.move(0, 30)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())