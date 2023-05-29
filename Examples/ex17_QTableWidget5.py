## Ex 5-21. QTableWidget.

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        # 기본값: QAbstractItemView.DoubleClicked
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)


        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.tableWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())