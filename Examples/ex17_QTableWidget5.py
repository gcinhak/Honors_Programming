import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)

        self.table_widget.setItem(0, 0, QTableWidgetItem("0"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("3"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("4"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("5"))

        self.table_widget.cellChanged.connect(self.on_cell_changed)
        self.table_widget.currentCellChanged.connect(self.on_current_cell_changed)
        self.table_widget.cellClicked.connect(self.on_cell_clicked)
        self.table_widget.cellDoubleClicked.connect(self.on_cell_double_clicked)

        # self.table_widget.itemChanged.connect(self.on_item_changed)
        # self.table_widget.currentItemChanged.connect(self.on_current_item_changed)
        # self.table_widget.itemClicked.connect(self.on_item_clicked)
        # self.table_widget.itemDoubleClicked.connect(self.on_item_double_clicked)

        self.setCentralWidget(self.table_widget)
        self.setGeometry(1000, 1000, 600, 600)

    def on_cell_changed(self, row, col):
        print("cellChanged", row, col)
    def on_current_cell_changed(self, row, col,prow,pcol):
        print("currentCellChanged", prow, pcol, row, col)
    def on_cell_clicked(self, row, col):
        print("cellClicked", row, col)
    def on_cell_double_clicked(self, row, col):
        print("cellDoubleClicked", row, col)

    # def on_item_changed(self, item):
    #     print("itemChanged", item.text())
    # def on_current_item_changed(self, item, pitem):
    #     if pitem != None:
    #         print("currentItemChanged", pitem.text(), item.text())
    # def on_item_clicked(self, item):
    #     print("itemClicked", item.text())
    # def on_item_double_clicked(self, item):
    #     print("itemDoubleClicked", item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())