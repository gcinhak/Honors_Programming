import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.btn = QPushButton("click")
        self.btn.setStyleSheet("font-size:28px;")
        self.btn.clicked.connect(self.on_btn_clicked)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("0"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("2"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("3"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("4"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("5"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 1000, 500, 400)

    def on_btn_clicked(self):
        print("rowCount():{} columnCount():{}".format(self.tableWidget.rowCount(), self.tableWidget.columnCount()))
        print("currentRow():{} currentColumn():{}".format(self.tableWidget.currentRow(), self.tableWidget.currentColumn()))
        print("--------------------------------")
        print("item(0,0):{} item(1,1):{}".format(self.tableWidget.item(0,0).text(), self.tableWidget.item(1,1).text()))
        print("currentItem():{}".format(self.tableWidget.currentItem().text()))
        print("--------------------------------")
        for item_obj in self.tableWidget.selectedItems():
            if self.tableWidget.selectedItems()[0] == item_obj:
                print("selectedItems():{}".format(item_obj.text()), end=" ")
            else:
                print("{}".format(item_obj.text()), end=" ")
        print("\n--------------------------------")
        for item_range in self.tableWidget.selectedRanges():
            print("rowCount():{} columnCount():{}\ntopRow():{} bottomRow():{}\nleftColumn():{} rightColumn(): {}".format
                  (item_range.rowCount(), item_range.columnCount(), item_range.topRow(), item_range.bottomRow(),
                   item_range.leftColumn(), item_range.rightColumn()))
            print("--------------------------------")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()