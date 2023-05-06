### Practice Exercise 11. QStatusBar ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QLineEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        vbox = QVBoxLayout()

        self.label = QLabel("label")
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("line edit")
        btn_clear = QPushButton("clear statusbar")
        btn_set_message = QPushButton("set statusbar")
        btn_return_message = QPushButton("return message")

        btn_clear.clicked.connect(self.on_clicked_btn_clear)
        btn_set_message.clicked.connect(self.on_clicked_btn_set_message)
        btn_return_message.clicked.connect(self.on_clicked_btn_return_message)

        vbox.addWidget(self.label)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(btn_clear)
        vbox.addWidget(btn_set_message)
        vbox.addWidget(btn_return_message)

        widget.setLayout(vbox)

        self.statusBar().showMessage('Developed by students in the IT-AI track')

        self.setCentralWidget(widget)
        self.setGeometry(500, 500, 350, 200)
        self.setWindowTitle('QStatusBar')

    def on_clicked_btn_clear(self):
        self.statusBar().clearMessage()

    def on_clicked_btn_set_message(self):
        self.statusBar().showMessage(self.line_edit.text())

    def on_clicked_btn_return_message(self):
        print(self.statusBar().currentMessage())
        self.label.setText(self.statusBar().currentMessage())

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())