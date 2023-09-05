import sys
import urllib.request
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.lb = QLabel()
        self.btn1 = QPushButton("웹")
        self.btn1.clicked.connect(self.on_btn1)
        self.btn2 = QPushButton("파일")
        self.btn2.clicked.connect(self.on_btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def on_btn1(self):
        pixmap_web = QPixmap()
        url_string="https://petnolza.com/wp-content/uploads/2021/11/dog-smart7.jpg"
        image_from_web = urllib.request.urlopen(url_string).read()
        pixmap_web.loadFromData(image_from_web)
        pixmap_web = pixmap_web.scaledToWidth(600)
        self.lb.setPixmap(pixmap_web)

    def on_btn2(self):
        pixmap_file = QPixmap()
        pixmap_file.load("../cat.jpg")
        pixmap_file = pixmap_file.scaledToWidth(600)
        self.lb.setPixmap(pixmap_file)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())