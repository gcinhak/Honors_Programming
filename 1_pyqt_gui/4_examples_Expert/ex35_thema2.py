import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
import qdarkstyle
import qtmodern.styles
import qtmodern.windows
from qt_material import apply_stylesheet


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

        font_defult = QFont()
        font_defult.setPointSize(20)

        # tab1
        label1 = QLabel("tab1 widget", tab1)
        label1.setFont(font_defult)
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
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # qtmodern.styles.dark(app)
    # mw = qtmodern.windows.ModernWindow(window)
    # mw.show()
    # sys.exit(app.exec_())
    #
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    # app.setStyleSheet(dark_stylesheet)
    # window.show()
    # sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # window = MainWindow()
    # apply_stylesheet(app, theme='dark_teal.xml')
    # window.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme = 'light_red.xml', invert_secondary = True)
    window.show()
    sys.exit(app.exec_())