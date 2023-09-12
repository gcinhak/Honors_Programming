import sys

from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QGroupBox, \
    QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QGroupBox')
        self.init_ui()

    def init_ui(self):
        self.button_1 = QPushButton("button_1")
        self.button_2 = QPushButton("button_2")
        self.button_3 = QPushButton("button_3")
        self.button_4 = QPushButton("button_4")

        self.layout_top = QVBoxLayout()
        self.layout_bottom = QVBoxLayout()
        self.layout_main = QHBoxLayout()

        self.groupbox_1 = QGroupBox("group_1")
        self.groupbox_2 = QGroupBox("group_2")

        self.init_widget()

    def init_widget(self):
        # layout 설정
        self.layout_top.addWidget(self.button_1)
        self.layout_top.addWidget(self.button_2)
        self.layout_bottom.addWidget(self.button_3)
        self.layout_bottom.addWidget(self.button_4)

        self.groupbox_1.setLayout(self.layout_top)
        self.groupbox_1.setCheckable(True)
        self.groupbox_2.setLayout(self.layout_bottom)
        self.groupbox_2.setCheckable(True)
        self.groupbox_2.setChecked(False)

        self.layout_main.addWidget(self.groupbox_1)
        self.layout_main.addWidget(self.groupbox_2)

        # 메인윈도우 위젯 설정
        widget = QWidget()
        widget.setLayout(self.layout_main)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())