### Example11. QStatusBar ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # StatusBar 예제1
        # self.statusbar = QStatusBar()
        # self.setStatusBar(self.statusbar)
        # self.statusbar.showMessage("Developed by students in the IT-AI track")

        # StatusBar 예제2
        self.statusBar().showMessage('Developed by students in the IT-AI track')

        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('QStatusBar')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())