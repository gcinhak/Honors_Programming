import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setPointSize(10)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["GP", "CREDIT"])
        self.btn_wgpa = QPushButton("WGPA")
        self.btn_wgpa.setFont(font)
        self.lb_wgpa = QLabel("WGPA")
        self.lb_wgpa.setFont(font)
        self.lb_wgpa.setAlignment(Qt.AlignVCenter)
        self.btn_unwgpa = QPushButton("UNWGPA")
        self.btn_unwgpa.setFont(font)
        self.lb_unwgpa = QLabel("UNWGPA")
        self.lb_unwgpa.setFont(font)
        self.lb_unwgpa.setAlignment(Qt.AlignVCenter)

        self.btn_wgpa.clicked.connect(self.on_btn_wgpa_clicked)
        self.btn_unwgpa.clicked.connect(self.on_btn_unwgpa_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.lb_unwgpa)
        vbox.addWidget(self.btn_unwgpa)
        vbox.addWidget(self.lb_wgpa)
        vbox.addWidget(self.btn_wgpa)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 1000, 500, 600)

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