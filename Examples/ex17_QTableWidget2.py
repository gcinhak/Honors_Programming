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
        self.btn = QPushButton("행 추가")
        self.btn.clicked.connect(self.on_btn)

        labels_horizontal_header = ["종목명", "종목코드"]
        self.tableWidget.setHorizontalHeaderLabels(labels_horizontal_header)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

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
        print(self.tableWidget.selectedRanges().bottomRow())
        print(self.tableWidget.selectedRanges().columnCount())
        print(self.tableWidget.selectedRanges().leftColumn())
        print(self.tableWidget.selectedRanges().rightColumn())
        print(self.tableWidget.selectedRanges().rowCount())
        print(self.tableWidget.selectedRanges().topRow())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()