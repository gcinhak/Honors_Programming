import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, \
    QGridLayout, QLineEdit, QSpinBox, QComboBox, QTableWidgetItem, QAbstractItemView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["학년도","학기", "과목", "GP", "CREDIT"])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        btn_add = QPushButton("추가")
        btn_add.setShortcut("Return")
        btn_del = QPushButton("선택한 행 삭제")
        btn_wgpa = QPushButton("&WGPA")
        btn_unwgpa = QPushButton("&UNWGPA")
        self.lb_year = QLabel("학년도")
        self.lb_semester = QLabel("학기")
        self.lb_subject = QLabel("과목")
        self.lb_gp = QLabel("GP")
        self.lb_credit = QLabel("CREDIT")
        self.lb_wgpa = QLabel("")
        self.lb_unwgpa = QLabel("")
        self.sbox_year = QComboBox()
        self.sbox_year.addItem("2022")
        self.sbox_year.addItem("2023")
        self.sbox_year.setCurrentIndex(1)
        self.sbox_semester = QComboBox()
        self.sbox_semester.addItem("1 학기")
        self.sbox_semester.addItem("2 학기")
        self.le_subject = QLineEdit()
        self.le_gp = QLineEdit()
        self.le_credit = QLineEdit()

        btn_wgpa.clicked.connect(self.on_btn_wgpa_clicked)
        btn_unwgpa.clicked.connect(self.on_btn_unwgpa_clicked)
        btn_add.clicked.connect(self.on_btn_add_clicked)
        btn_del.clicked.connect(self.on_btn_del_clicked)

        vbox = QVBoxLayout()
        gbox = QGridLayout()
        gbox.addWidget(self.lb_year, 0,0)
        gbox.addWidget(self.lb_semester, 0,1)
        gbox.addWidget(self.lb_subject, 0,2)
        gbox.addWidget(self.lb_gp,0,3)
        gbox.addWidget(self.lb_credit,0,4)

        gbox.addWidget(self.sbox_year, 1,0)
        gbox.addWidget(self.sbox_semester, 1,1)
        gbox.addWidget(self.le_subject, 1,2)
        gbox.addWidget(self.le_gp, 1,3)
        gbox.addWidget(self.le_credit, 1,4)

        gbox.addWidget(btn_del,0,5)
        gbox.addWidget(btn_add,1,5)

        vbox.addLayout(gbox)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(btn_wgpa)
        vbox.addWidget(self.lb_wgpa)
        vbox.addWidget(btn_unwgpa)
        vbox.addWidget(self.lb_unwgpa)


        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 1000, 1100, 800)

    def on_btn_unwgpa_clicked(self):
        sum_score = 0
        cnt_subject = 0
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row,3)
            if item is not None and item.text():
                sum_score += float(item.text())
                cnt_subject += 1
        if cnt_subject != 0:
            self.lb_unwgpa.setText(str(sum_score/cnt_subject))

    def on_btn_wgpa_clicked(self):
        sum_gp_cd = 0
        sum_cd = 0
        for row in range(self.tableWidget.rowCount()):
            gp = self.tableWidget.item(row, 3)
            cd = self.tableWidget.item(row, 4)
            if gp is not None and cd is not None and gp.text() and cd.text():
                sum_gp_cd += float(gp.text()) * float(cd.text())
                sum_cd += float(cd.text())
        if sum_cd > 0:
            self.lb_wgpa.setText(str(sum_gp_cd / sum_cd))

    def on_btn_add_clicked(self):
        items = [self.sbox_year.currentText(), self.sbox_semester.currentText(), self.le_subject.text()\
                 , self.le_gp.text(), self.le_credit.text()]
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        for i in range(len(items)):
            self.tableWidget.setItem(row_count, i, QTableWidgetItem(items[i]))

        self.le_subject.clear()
        self.le_gp.clear()
        self.le_credit.clear()

        self.le_subject.setFocus()

    def on_btn_del_clicked(self):
        current_row_count = self.tableWidget.currentRow()
        self.tableWidget.removeRow(current_row_count)

if __name__ == "__main__":
    font = QFont()
    font.setPointSize(10)
    app = QApplication(sys.argv)
    app.setFont(font)
    window = MainWindow()
    window.show()
    app.exec_()