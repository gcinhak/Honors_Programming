import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)

        tabs = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tabs.addTab(tab1, "tab1")
        tabs.addTab(tab2, "tab2")
        tabs.addTab(tab3, "tab3")

        # tab1
        label1 = QLabel("tab1 widget", tab1)
        btn1 = QPushButton("tab1 btn", tab1)
        btn1.move(10,50)
        label1.move(10, 10)

        # tab2
        label2 = QLabel("tab2 widget", tab2)
        btn2 = QPushButton("tab1 btn", tab2)
        btn2.move(10,50)
        label2.move(10, 10)

        # tab3
        label3 = QLabel("tab3 widget", tab3)
        btn3 = QPushButton("tab1 btn", tab3)
        btn3.move(10,50)
        label3.move(10, 10)

        self.setCentralWidget(tabs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    def dark_mode():
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        return palette

    app.setPalette(dark_mode())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())