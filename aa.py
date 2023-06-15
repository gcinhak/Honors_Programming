from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()



# =====================================================================================
# =====================================================================================

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()

    sys.exit(app.exec_())