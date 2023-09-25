import sys

from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.btn1 = QPushButton("시작")
        self.btn2 = QPushButton("종료")
        self.slider_volume = QSlider(Qt.Horizontal)
        self.bell = QSoundEffect()
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.init_widget()

    def init_widget(self):
        self.slider_volume.setRange(0, 100)
        self.bell.setSource(QUrl.fromLocalFile("../../sounds/bell.wav"))

        self.btn1.clicked.connect(self.on_btn1)
        self.btn2.clicked.connect(self.on_btn2)
        self.slider_volume.valueChanged.connect(self.volume_changed)


        self.vbox.addWidget(self.slider_volume)
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.vbox.addLayout(self.hbox)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)
        self.setGeometry(500,500,300,100)

    def volume_changed(self):
        self.bell.setVolume(self.slider_volume.value() / 100) # 0 ~ 1

    def on_btn1(self):
        self.bell.play()

    def on_btn2(self):
        self.bell.stop()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())