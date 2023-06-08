import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QPushButton, QVBoxLayout, \
    QWidget, QHBoxLayout, QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)

        # 기본값: QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.AnyKeyPressed
        # self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.table_widget.setEditTriggers(QAbstractItemView.CurrentChanged)
        # self.table_widget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.table_widget.setEditTriggers(QAbstractItemView.SelectedClicked)
        # self.table_widget.setEditTriggers(QAbstractItemView.EditKeyPressed)
        # self.table_widget.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        # self.table_widget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        # self.table_widget.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)

        # 기본값: QAbstractItemView.ExtendedSelection
        # self.table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        # self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.table_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.table_widget.setSelectionMode(QAbstractItemView.ContiguousSelection)

        # 기본값: self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        # self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.table_widget.setItem(0, 0, QTableWidgetItem("0"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("3"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("4"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("5"))

        self.setCentralWidget(self.table_widget)
        self.setGeometry(1000, 1000, 600, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()