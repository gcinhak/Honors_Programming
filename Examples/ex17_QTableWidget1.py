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
        self.tableWidget.insertRow
        # self.tableWidget.horizontalHeader().setVisible(False)
        # self.tableWidget.verticalHeader().setVisible(False)

        labels_horizontal_header = ["종목명", "종목코드"]
        self.tableWidget.setHorizontalHeaderLabels(labels_horizontal_header)


        self.btn = QPushButton("행 추가")
        self.btn.clicked.connect(self.on_btn)

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
        # print(self.tableWidget.item(2, 1))
        # self.tableWidget.clear()
        # self.tableWidget.clearContents()
        self.tableWidget.setCurrentItem(QTableWidgetItem("0000"))
        # self.tableWidget.takeItem(0,0)
        # row = self.tableWidget.rowCount()
        # print(row)
        # self.tableWidget.insertRow(row)
        # self.tableWidget.setItem(row, 0, QTableWidgetItem("---"))
        # col = self.tableWidget.columnCount()
        # print(col)
        # self.tableWidget.insertColumn(col)
        # self.tableWidget.setItem(0, col, QTableWidgetItem("---"))
        #
        # print(self.tableWidget.item(row,0))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()