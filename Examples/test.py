import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QVBoxLayout, QPushButton, QTableWidgetItem

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell 1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell 2"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell 3"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell 4"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell 5"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell 6"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell 7"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell 8"))

        self.button = QPushButton('Set Current Item')
        self.button.clicked.connect(self.setCurrentItem)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Set Current Item Example')
        self.show()

    def setCurrentItem(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.tableWidget.setCurrentItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())