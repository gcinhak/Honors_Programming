import sys
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QPushButton, QVBoxLayout, \
    QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["1열", "2열"])
        self.table_widget.setVerticalHeaderLabels(["1행", "2행", "3행"])

        self.btn_add_row = QPushButton("행 추가")
        self.btn_add_col = QPushButton("열 추가")
        self.btn_del_row = QPushButton("행 삭제")
        self.btn_del_col = QPushButton("열 삭제")
        self.btn_del = QPushButton("삭제")
        self.btn_clear_contents = QPushButton("모든 내용 삭제")
        self.btn_clear = QPushButton("모두 삭제")

        self.btn_add_row.clicked.connect(self.on_btn_add_row_clicked)
        self.btn_add_col.clicked.connect(self.on_btn_add_col_clicked)
        self.btn_del_row.clicked.connect(self.on_btn_del_row_clicked)
        self.btn_del_col.clicked.connect(self.on_btn_del_col_clicked)
        self.btn_del.clicked.connect(self.on_btn_del_clicked)
        self.btn_clear_contents.clicked.connect(self.on_btn_clear_contents_clicked)
        self.btn_clear.clicked.connect(self.on_btn_clear_clicked)

        self.table_widget.setItem(0, 0, QTableWidgetItem("0"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("3"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("4"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("5"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.table_widget)
        hbox_row = QHBoxLayout()
        hbox_row.addWidget(self.btn_add_row)
        hbox_row.addWidget(self.btn_del_row)
        hbox_col = QHBoxLayout()
        hbox_col.addWidget(self.btn_add_col)
        hbox_col.addWidget(self.btn_del_col)
        hbox_delete = QHBoxLayout()
        hbox_delete.addWidget(self.btn_del)
        hbox_delete.addWidget(self.btn_clear_contents)
        hbox_delete.addWidget(self.btn_clear)
        vbox.addLayout(hbox_row)
        vbox.addLayout(hbox_col)
        vbox.addLayout(hbox_delete)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 500, 400, 300)

    def on_btn_add_row_clicked(self):
        self.table_widget.insertRow(self.table_widget.rowCount())
    def on_btn_add_col_clicked(self):
        self.table_widget.insertColumn(self.table_widget.columnCount())
    def on_btn_del_row_clicked(self):
        self.table_widget.removeRow(self.table_widget.rowCount()-1)
    def on_btn_del_col_clicked(self):
        self.table_widget.removeColumn(self.table_widget.columnCount()-1)
    def on_btn_del_clicked(self):
        self.table_widget.takeItem(self.table_widget.currentRow(), self.table_widget.currentColumn())
    def on_btn_clear_clicked(self):
        self.table_widget.clear()
    def on_btn_clear_contents_clicked(self):
        self.table_widget.clearContents()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())