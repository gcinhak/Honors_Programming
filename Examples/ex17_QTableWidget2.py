import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)
        self.btn = QPushButton("click")
        self.btn.setStyleSheet("font-size:28px;")
        self.btn.clicked.connect(self.on_btn_clicked)

        self.table_widget.setItem(0, 0, QTableWidgetItem("0"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("3"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("4"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("5"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.table_widget)
        vbox.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 300, 500, 400)

    def on_btn_clicked(self):
        print("rowCount():{} columnCount():{}".format(self.table_widget.rowCount(), self.table_widget.columnCount()))
        print("currentRow():{} currentColumn():{}".format(self.table_widget.currentRow(), self.table_widget.currentColumn()))
        print("--------------------------------")
        print("item(0,0):{} item(2,0):{}".format(self.table_widget.item(0,0).text(), self.table_widget.item(2,0).text()))
        print("currentItem():{}".format(self.table_widget.currentItem().text()))
        print("--------------------------------")
        for item_obj in self.table_widget.selectedItems():
            print(item_obj.text())

            if self.table_widget.selectedItems()[0] == item_obj:
                print("selectedItems():{}".format(item_obj.text()), end=" ")
            else:
                print("{}".format(item_obj.text()), end=" ")
        print("\n--------------------------------")
        for item_range in self.table_widget.selectedRanges():
            print("rowCount():{} columnCount():{}\ntopRow():{} bottomRow():{}\nleftColumn():{} rightColumn(): {}".format
                  (item_range.rowCount(), item_range.columnCount(), item_range.topRow(), item_range.bottomRow(),
                   item_range.leftColumn(), item_range.rightColumn()))
            print("--------------------------------")
        index_list = self.table_widget.selectedIndexes()
        for index in index_list:
            print("row:{} column:{}".format(index.row(), index.column()))
            print(type(index))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()