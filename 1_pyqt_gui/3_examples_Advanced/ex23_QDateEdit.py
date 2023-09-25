import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        datetimeedit = QDateTimeEdit()
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        dateedit = QDateEdit()
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))

        timeedit = QTimeEdit()
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(00, 00, 00), QTime(24, 00, 00))
        timeedit.setDisplayFormat('hh:mm:ss')


        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(dateedit)
        vbox.addWidget(timeedit)
        vbox.addWidget(datetimeedit)

        # 윈도우 설정
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(500,500,300,100)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())