import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.btn = QPushButton("실행")
        self.btn.clicked.connect(self.on_btn)

        labels_horizontal_header = ["과목", "성적"]
        self.tableWidget.setHorizontalHeaderLabels(labels_horizontal_header)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("국어"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("영어"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("수학"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("과학"))

        self.tableWidget.setItem(0, 1, QTableWidgetItem("100"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("90"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("80"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("50"))


        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(1500, 500, 500, 500)

    def on_btn(self):
        # self.tableWidget.setRowCount(6)
        # print(self.tableWidget.currentRow())
        # self.tableWidget.setCurrentCell(1,1)
        # self.tableWidget.setCurrentItem(QTableWidgetItem("(100,100)"))
        # for i in self.tableWidget.selectedItems():
        #     print(i.text())
        # for i in self.tableWidget.selectedRanges():
        #     print(i.bottomRow())
        #     print(i.columnCount())
        #     print(i.leftColumn())
        #     print(i.rightColumn())
        #     print(i.rowCount())
        #     print(i.topRow())
        # print(self.tableWidget.rowCount())
        # print(self.tableWidget.currentRow())
        # print(self.tableWidget.selectedItems())
        result = 0
        for i in self.tableWidget.selectedItems():
            result += int(i.text())
            # print(i.text())
        print(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()