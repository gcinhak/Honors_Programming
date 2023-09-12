import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit')
        self.init_ui()

    def init_ui(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.lbl2 = QLabel('The number of words is 0')
        self.vbox = QVBoxLayout()
        self.init_widget()

    def init_widget(self):
        # TextEdit 설정
        self.te.setTextColor(QColor(250, 127, 8,255))
        self.te.setFontItalic(True)
        # self.te.setFontUnderline(False)
        self.te.setFontPointSize(20)
        self.te.setText("Hello World")

        # layout 설정
        self.vbox.addWidget(self.lbl1)
        self.vbox.addWidget(self.te)
        self.vbox.addWidget(self.lbl2)

        # 시그널 설정
        self.te.textChanged.connect(self.text_changed)

        # 메인윈도우 위젯 설정
        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())