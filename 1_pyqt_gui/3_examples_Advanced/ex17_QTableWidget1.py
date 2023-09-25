import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(2)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["1열", "2열"])
        self.table_widget.setVerticalHeaderLabels(["1행", "2행"])
        # self.table_widget.setVerticalHeaderItem(0, QTableWidgetItem("1행"))
        # self.table_widget.setVerticalHeaderItem(1, QTableWidgetItem("2행"))

        self.table_widget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("(1,1)"))

        self.setCentralWidget(self.table_widget)
        self.setGeometry(1000, 300, 500, 500)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())