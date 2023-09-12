import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QApplication, QCalendarWidget, QWidget, QVBoxLayout
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우 설정
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Canlendar Widget')

        self.init_ui()

    def init_ui(self):
        self.cal = QCalendarWidget()
        self.calendar_label = QLabel()
        self.today_btn = QPushButton('Today')
        self.vbox = QVBoxLayout()

        self.init_widget()

    def init_widget(self):
        self.cal.setGridVisible(True)

        # min max 기간 설정
        # self.cal.setMinimumDate(QDate(2023, 9, 1))
        # self.cal.setMaximumDate(QDate(2023, 9, 27))

        # Calendar 에서 선택한 값을 표시할 QLabel에 font 설정
        self.calendar_label.setFont(QFont("D2Coding", 12))

        # 현재날짜 달력에 표시 버튼
        self.today_btn.clicked.connect(self.select_today)
        # 날짜선택되면 Label에 날짜 표시하는 시그널-슬롯
        self.cal.selectionChanged.connect(self.calendar_change)

        self.vbox.addWidget(self.cal)
        self.vbox.addWidget(self.calendar_label)
        self.vbox.addWidget(self.today_btn)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)

    def calendar_change(self):
        cal_date = self.cal.selectedDate()
        str_date = cal_date.toString('yyyy.MM.dd')  # QDate 를 str 로 변환
        self.calendar_label.setText(str_date)

    def select_today(self):
        self.cal.showToday() # 이번 달 페이지
        # self.cal.showNextMonth() # 다음 달 페이지
        # self.cal.setSelectedDate(QDate(2023, 9, 12)) # 특정 일로 이동

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())