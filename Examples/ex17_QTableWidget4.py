import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QPushButton, QVBoxLayout, \
    QWidget, QHBoxLayout, QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)

        # 기본값: QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.AnyKeyPressed
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.SelectedClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.EditKeyPressed)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)

        # 기본값: QAbstractItemView.ExtendedSelection
        # self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)

        # 기본값: self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("0"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("2"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("3"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("4"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("5"))

        self.setCentralWidget(self.tableWidget)
        self.setGeometry(1000, 1000, 600, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()