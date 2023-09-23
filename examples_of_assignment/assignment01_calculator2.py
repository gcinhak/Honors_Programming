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
        self.label_equation = QLabel()
        self.label_equation.setStyleSheet("border-style: solid; border-width: 1px; font-size: 18px; background-color: #FBFBFB; border-radius: 7%; border-color: #BDBDBD;")
        self.label_equation.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_equation.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.label_equation.setFixedHeight(40)

        self.label_solution = QLabel()
        self.label_solution.setStyleSheet("border-style: solid; border-width: 1px; font-size: 26px; background-color: #FBFBFB; border-radius: 7%; border-color: #BDBDBD; font-weight: 400;")
        self.label_solution.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_solution.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.label_solution.setFixedHeight(50)

        self.btn_list = []
        for number in range(10):
            self.btn_list.append(QPushButton(str(number)))
            self.btn_list[number].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.btn_list[number].clicked.connect(self.on_clicked_number_btn)
            self.btn_list[number].setStyleSheet("font-size: 20px;")

        operations = ["/","*","-","+","=",".","inhak"]
        self.operation_btn_list = {}
        for operation in operations:
            self.operation_btn_list[operation] = QPushButton(operation)
            self.operation_btn_list[operation].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.operation_btn_list[operation].clicked.connect(self.on_clicked_operation_btn)

        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.on_clicked_clear_btn)
        # self.btn_clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_del = QPushButton("Del")
        self.btn_del.clicked.connect(self.on_clicked_del_btn)
        # self.btn_del.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btn_empty = QPushButton()
        # self.btn_empty.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_empty.setEnabled(False)

        vbox = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btn_clear,0,0,1,1)
        grid_layout.addWidget(self.btn_del,0,1,1,1)
        grid_layout.addWidget(self.btn_empty,0,2,1,1)

        for row, value in enumerate(operations):
            if value == ".":
                grid_layout.addWidget(self.operation_btn_list["."],4,2,1,1)
            elif value == "inhak":
                grid_layout.addWidget(self.operation_btn_list["inhak"],4,0,1,1)
            else:
                grid_layout.addWidget(self.operation_btn_list[value],row,3,1,1)

        for num in range(0,10):
            row = (9 - num) // 3 + 1
            col = (num - 1) % 3
            if num == 0:
                grid_layout.addWidget(self.btn_list[num],4,1,1,1)
            else:
                grid_layout.addWidget(self.btn_list[num],row,col,1,1)

        vbox.addWidget(self.label_equation, stretch = 2)
        vbox.addWidget(self.label_solution, stretch = 3)
        vbox.addLayout(grid_layout, stretch = 10)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(screen_width//2, 200, 400, 600)
        self.setWindowTitle('Calculator')
        self.statusBar().showMessage('Developed by GVCSMG')

    def on_clicked_number_btn(self):
        if self.label_solution.text():
            self.label_equation.clear()
            self.label_solution.clear()

        sender = self.sender()
        number = sender.text()
        self.label_equation.setText(self.label_equation.text()+number)

    def on_clicked_operation_btn(self):
        sender = self.sender()
        operation = sender.text()
        if operation in ["+","-","/","*","."]:
            if self.label_equation.text() and self.label_equation.text()[-1] in "0123456789":
                self.label_equation.setText(self.label_equation.text() + operation)
            if self.label_solution.text():
                self.label_equation.setText(self.label_solution.text() + operation)
                self.label_solution.clear()
        elif operation == "inhak":
            self.label_equation.clear()
            self.label_solution.setText("Hello World!!")
        elif operation == "=":
            if self.label_equation.text():
                try:
                    self.label_solution.setText(str(format(eval(self.label_equation.text().replace(",","")),",")))
                    self.label_equation.setText(self.label_equation.text() + '=')
                except:
                    QMessageBox.warning(self, "Close", "계산할 수 없습니다.")

    def on_clicked_del_btn(self):
        if not self.label_solution.text():
            self.label_equation.setText(self.label_equation.text()[:-1])

    def on_clicked_clear_btn(self):
        self.label_solution.clear()
        self.label_equation.clear()

if __name__ == '__main__':
    app = QApplication([])
    screen_rect = app.desktop().screenGeometry()
    screen_width = screen_rect.width()
    screen_height = screen_rect.height()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())