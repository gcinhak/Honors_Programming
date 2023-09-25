import sys

from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget')
        self.setGeometry(100, 100, 800, 400)
        self.init_ui()

    def init_ui(self):
        self.list_widget = QListWidget()
        self.list_widget_remove = QListWidget()
        self.btn_add_item = QPushButton("add")
        self.btn_insert_item = QPushButton("insert")
        self.btn_print_item = QPushButton("Print")
        self.btn_print_multi_items = QPushButton("Print_Multi")
        self.btn_remove_item = QPushButton("Remove")
        self.btn_clear_item = QPushButton("Clear")
        self.le_add_item = QLineEdit()
        self.le_insert_item = QLineEdit()
        self.spin_insert_row = QSpinBox()

        self.layout_main = QVBoxLayout()
        self.hbox_listwidget = QHBoxLayout()
        self.hbox_add = QHBoxLayout()
        self.hbox_insert = QHBoxLayout()
        self.hbox_btn = QHBoxLayout()

        self.init_widget()

    def init_widget(self):
        # ListWidget의 시그널
        self.list_widget.itemClicked.connect(self.chkItemClicked)
        self.list_widget.itemDoubleClicked.connect(self.chkItemDoubleClicked)
        self.list_widget.currentItemChanged.connect(self.chkCurrentItemChanged)
        self.list_widget_remove.itemClicked.connect(self.removeListchkItemClicked)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)

        # 버튼에 기능 연결
        self.btn_add_item.clicked.connect(self.addListWidget)
        self.btn_insert_item.clicked.connect(self.insertListWidget)

        self.btn_print_item.clicked.connect(self.printCurrentItem)
        self.btn_print_multi_items.clicked.connect(self.printMultiItems)
        self.btn_remove_item.clicked.connect(self.removeCurrentItem)
        self.btn_clear_item.clicked.connect(self.clearItem)

        self.hbox_listwidget.addWidget(self.list_widget)
        self.hbox_listwidget.addWidget(self.list_widget_remove)

        self.hbox_add.addWidget(self.le_add_item)
        self.hbox_add.addWidget(self.btn_add_item)

        self.hbox_insert.addWidget(self.le_insert_item)
        self.hbox_insert.addWidget(self.spin_insert_row)
        self.hbox_insert.addWidget(self.btn_insert_item)

        self.hbox_btn.addWidget(self.btn_print_item)
        self.hbox_btn.addWidget(self.btn_print_multi_items)
        self.hbox_btn.addWidget(self.btn_remove_item)
        self.hbox_btn.addWidget(self.btn_clear_item)

        self.layout_main.addLayout(self.hbox_listwidget)
        self.layout_main.addLayout(self.hbox_add)
        self.layout_main.addLayout(self.hbox_insert)
        self.layout_main.addLayout(self.hbox_btn)

        widget = QWidget()
        widget.setLayout(self.layout_main)
        self.setCentralWidget(widget)

    def chkItemClicked(self):
        print(self.list_widget.currentItem().text())

        self.btn_remove_item.setDisabled(False)
        self.btn_clear_item.setDisabled(False)
        self.btn_print_item.setDisabled(False)
        self.btn_print_multi_items.setDisabled(False)

    def chkItemDoubleClicked(self):
        print(str(self.list_widget.currentRow()) + " : " + self.list_widget.currentItem().text())

    def chkCurrentItemChanged(self):
        print("Current Row : " + str(self.list_widget.currentRow()))

    def addListWidget(self):
        self.addItemText = self.le_add_item.text()
        self.list_widget.addItem(self.addItemText)

    def insertListWidget(self):
        self.insertRow = self.spin_insert_row.value()
        self.insertText = self.le_insert_item.text()
        self.list_widget.insertItem(self.insertRow, self.insertText)

    def printCurrentItem(self):
        if self.list_widget.count() != 0:
            print(self.list_widget.currentItem().text())

    def printMultiItems(self):
        # 여러개를 선택했을 때, selectedItems()를 이용하여 선택한 항목을 List의 형태로 반환받습니다.
        # 그 후, for문을 이용하여 선택된 항목을 출력합니다.
        # 출력할 때, List안에는 QListWidgetItem객체가 저장되어 있으므로, .text()함수를 이용하여 문자열로 변환해야 합니다.
        if self.list_widget.count() != 0:
            self.selectedList = self.list_widget.selectedItems()
            for i in self.selectedList:
                print(i.text())

    def removeCurrentItem(self):
        # ListWidget에서 현재 선택한 항목을 삭제할 때는 선택한 항목의 줄을 반환한 후, takeItem함수를 이용해 삭제합니다.
        self.removeItemRow = self.list_widget.currentRow()
        if self.removeItemRow != -1:
            self.list_widget_remove.addItem(self.list_widget.currentItem().text())
        self.list_widget.takeItem(self.removeItemRow)

    def removeListchkItemClicked(self):
        # ListWidget에서 현재 선택한 항목을 삭제할 때는 선택한 항목의 줄을 반환한 후, takeItem함수를 이용해 삭제합니다.
        self.btn_remove_item.setDisabled(True)
        self.btn_clear_item.setDisabled(True)
        self.btn_print_item.setDisabled(True)
        self.btn_print_multi_items.setDisabled(True)

    def clearItem(self):
        self.list_widget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())