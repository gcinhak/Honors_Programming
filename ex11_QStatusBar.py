### Example11. QStatusBar ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # StatusBar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Developed by students in the IT-AI track")


        # self.statusBar().showMessage('Developed by students in the IT-AI track')

        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('QHBoxLayout')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())