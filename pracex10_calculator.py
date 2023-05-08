### Practice Exercise 10. Calculator ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QGridLayout, \
    QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label1 = QLabel()
        self.label1.setStyleSheet("border-style: solid; border-width: 1px; font-size: 22px; background-color: #FFFFFF;")
        self.label1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label1.setFixedHeight(50)
        self.label2 = QLabel()
        self.label2.setStyleSheet("border-style: solid; border-width: 1px; font-size: 22px; background-color: #FFFFFF;")
        self.label2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label2.setFixedHeight(50)

        self.btn_list = []
        for number in range(10):
            self.btn_list.append(QPushButton(str(number)))
            self.btn_list[number].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.btn_list[number].clicked.connect(self.on_clicked_number_btn)
            self.btn_list[number].setStyleSheet("font-size: 20px;")

        operations = ["+","-","*","/",".","=","inhak"]
        self.operation_list = {}
        for operation in operations:
            self.operation_list[operation] = QPushButton(operation)
            self.operation_list[operation].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.operation_list[operation].clicked.connect(self.on_clicked_operation_btn)

        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.on_clicked_clear_btn)
        self.btn_clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_del = QPushButton("del")
        self.btn_del.clicked.connect(self.on_clicked_del_btn)
        self.btn_del.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_empty = QPushButton()
        self.btn_empty.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_empty.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btn_clear,0,0,1,1)
        grid_layout.addWidget(self.btn_del,0,1,1,1)
        grid_layout.addWidget(self.btn_empty,0,2,1,1)
        grid_layout.addWidget(self.operation_list["/"],0,3,1,1)
        grid_layout.addWidget(self.operation_list["*"],1,3,1,1)
        grid_layout.addWidget(self.operation_list["-"],2,3,1,1)
        grid_layout.addWidget(self.operation_list["+"],3,3,1,1)
        grid_layout.addWidget(self.operation_list["="],4,3,1,1)
        grid_layout.addWidget(self.operation_list["."],4,2,1,1)
        grid_layout.addWidget(self.operation_list["inhak"],4,0,1,1)
        grid_layout.addWidget(self.btn_list[7],1,0,1,1)
        grid_layout.addWidget(self.btn_list[8],1,1,1,1)
        grid_layout.addWidget(self.btn_list[9],1,2,1,1)
        grid_layout.addWidget(self.btn_list[4],2,0,1,1)
        grid_layout.addWidget(self.btn_list[5],2,1,1,1)
        grid_layout.addWidget(self.btn_list[6],2,2,1,1)
        grid_layout.addWidget(self.btn_list[1],3,0,1,1)
        grid_layout.addWidget(self.btn_list[2],3,1,1,1)
        grid_layout.addWidget(self.btn_list[3],3,2,1,1)
        grid_layout.addWidget(self.btn_list[0],4,1,1,1)
        vbox.addLayout(grid_layout)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(500, 500, 400, 500)
        self.setWindowTitle('Calculator')
        self.statusBar().showMessage('Developed by Teacher')

    def on_clicked_number_btn(self):
        sender = self.sender()
        number = sender.text()
        self.label2.setText(self.label2.text()+number)

    def on_clicked_operation_btn(self):
        sender = self.sender()
        operation = sender.text()
        if operation in ["+","-","/","*","."]:
            if self.label2.text() and self.label2.text()[-1] not in ["+","-","/","*","."]:
                self.label2.setText(self.label2.text() + operation)
        elif operation == "inhak":
            self.label1.setText("Hello World!!")
        elif operation == "=":
            try:
                self.label1.setText(str(eval(self.label2.text())))
                self.label2.clear()
            except:
                QMessageBox.warning(self, "Close", "계산할 수 없습니다.")

    def on_clicked_del_btn(self):
        self.label2.setText(self.label2.text()[:-1])

    def on_clicked_clear_btn(self):
        self.label2.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())