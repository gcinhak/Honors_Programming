import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, \
    QGridLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setPointSize(10)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["v", "학번", "이름", "성적"])
        btn_add = QPushButton("추가")
        btn_del = QPushButton("삭제")
        le_id = QLabel("학번")
        le_name = QLabel("이름")
        le_score = QLabel("성적")
        btn_add.setFont(font)
        btn_del.setFont(font)

        self.btn_wgpa.clicked.connect(self.on_btn_wgpa_clicked)
        self.btn_unwgpa.clicked.connect(self.on_btn_unwgpa_clicked)

        vbox = QVBoxLayout()
        gbox = QGridLayout()
        gbox.addWidget(le_id, 0,0)
        gbox.addWidget(QLineEdit(), 1,0)
        gbox.addWidget(le_name, 0,1)
        gbox.addWidget(QLineEdit(), 1,1)
        gbox.addWidget(le_score, 0,2)
        gbox.addWidget(QLineEdit(), 1,2)
        gbox.addWidget(btn_add,2,0,1,2)
        gbox.addWidget(btn_del,2,2,1,1)

        vbox.addWidget(self.tableWidget)
        vbox.addLayout(gbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 1000, 1000, 600)

    def on_btn_unwgpa_clicked(self):
        sum_score = 0
        cnt_subject = 0
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row,0)
            if item != None:
                sum_score += float(item.text())
                cnt_subject += 1
        if cnt_subject != 0:
            self.lb_unwgpa.setText(str(sum_score/cnt_subject))

    def on_btn_wgpa_clicked(self):
        sum_gp_cd = 0
        sum_cd = 0
        for row in range(self.tableWidget.rowCount()):
            gp = self.tableWidget.item(row, 0)
            cd = self.tableWidget.item(row, 1)
            if gp != None and cd != None:
                sum_gp_cd += float(gp.text()) * float(cd.text())
                sum_cd += float(cd.text())
        if sum_cd > 0:
            self.lb_wgpa.setText(str(sum_gp_cd / sum_cd))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()