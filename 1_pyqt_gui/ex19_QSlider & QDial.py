import sys

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QHBoxLayout, QSlider, \
    QVBoxLayout, QLabel, QDial, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # slider 설정
        self.slider_horizontal = QSlider(Qt.Horizontal)
        self.slider_horizontal.setRange(0, 50)
        self.slider_horizontal.setSingleStep(1)
        self.slider_horizontal.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.slider_horizontal.setTickPosition(3)

        # slider 설정
        self.slider_vertical = QSlider(Qt.Vertical)
        self.slider_vertical.setRange(0, 100)
        self.slider_vertical.setSingleStep(2)
        self.slider_vertical.setValue(50)
        self.slider_vertical.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.slider_vertical.setTickPosition(QSlider.TicksLeft or QSlider.TicksRight)

        # dail 설정
        self.dial = QDial(self)
        self.dial.setRange(0, 50)
        self.dial.setSingleStep(1)
        self.dial.setNotchesVisible(True)
        self.dial.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Label, Button 설정
        self.label_silder_horizontal = QLabel("Horizontal Value")
        self.label_silder_horizontal.setFixedWidth(150)
        self.label_silder_horizontal.setAlignment(Qt.AlignCenter)

        self.label_silder_vertical = QLabel("Vertical Value")
        self.label_silder_vertical.setFixedWidth(100)
        self.label_silder_vertical.setAlignment(Qt.AlignCenter)

        self.label_dial = QLabel("Dial Value")
        self.label_dial.setFixedWidth(100)
        self.label_dial.setAlignment(Qt.AlignCenter)

        btn_reset = QPushButton('reset')
        btn_reset.setFixedHeight(50)

        # 시그널 사용
        self.slider_horizontal.valueChanged.connect(self.hslider_changed)
        self.slider_vertical.valueChanged.connect(self.vslider_changed)
        self.dial.valueChanged.connect(self.dail_changed)
        btn_reset.clicked.connect(self.on_btn_reset_clicked)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.slider_horizontal)
        hbox.addWidget(self.label_silder_horizontal)
        hbox.addWidget(self.slider_vertical)
        hbox.addWidget(self.label_silder_vertical)
        hbox.addWidget(self.dial)
        hbox.addWidget(self.label_dial)
        vbox.addLayout(hbox)
        vbox.addWidget(btn_reset)

        datetime = QDateTime.currentDateTime()
        self.statusBar().showMessage(datetime.toString('yyyy-MM-dd, hh:mm:ss'))

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle('QSlider & QDial')
        self.setGeometry(1000, 300, 800, 400)


    def on_btn_reset_clicked(self):
        print(self.slider_horizontal.value())
        print(self.slider_vertical.value())
        print(self.dial.value())
        self.slider_horizontal.setValue(10)
        self.slider_vertical.setValue(50)
        self.dial.setValue(30)

    def hslider_changed(self):
        self.label_silder_horizontal.setText(str(self.slider_horizontal.value()))

    def vslider_changed(self):
        self.label_silder_vertical.setText(str(self.slider_vertical.value()))

    def dail_changed(self):
        self.label_dial.setText(str(self.dial.value()))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())