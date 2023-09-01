import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 위젯 생성
        self.bar = QProgressBar()
        self.btn_start = QPushButton("Start")
        self.timer = QTimer()

        # ProgressBar 설정
        self.bar.setMaximum(120)
        self.bar.setValue(50)
        self.bar.setAlignment(Qt.AlignCenter)
        self.bar.setFixedHeight(30)
        # self.bar.setFormat("%p %v %m")
        # self.bar.resetFormat()
        # self.bar.setTextVisible(False)

        self.btn_start.clicked.connect(self.start_process)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.bar)
        vbox.addWidget(self.btn_start)

        # 윈도우 설정
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(500,500,300,100)

    # 슬롯
    def start_process(self):
        self.btn_start.setEnabled(False)

        self.timer.setInterval(50)
        self.timer.timeout.connect(self.timer_progress)
        self.timer.start()

    def timer_progress(self):
        count = self.bar.value()
        count += 1
        self.bar.setValue(count)

        if count >= self.bar.maximum():
            self.btn_start.setEnabled(True)
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())