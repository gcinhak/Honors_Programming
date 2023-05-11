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
        ### widget 생성 ###
        # Label 생성
        self.label_equation = QLabel()
        self.label_equation.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        print(Qt.AlignRight)
        print(Qt.AlignVCenter)
        print(Qt.AlignRight | Qt.AlignVCenter)
        self.label_equation.setStyleSheet("""border-style: solid; border-width: 1px; 
                                          font-size: 18px; background-color: #FBFBFB;
                                          border-radius: 7%; border-color: #BCBCBC;""")

        self.label_solution = QLabel()
        self.label_solution.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_solution.setStyleSheet("""border-style: solid; border-width: 1px;
                                          font-size: 26px; background-color: #FBFBFB;
                                          border-radius: 7%; border-color: #BCBCBC;
                                          font-weight: 400;""")
        # 숫자 버튼 생성
        self.btn_list = []
        for number in range(10):
            self.btn_list.append(QPushButton(str(number)))
            self.btn_list[number].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.btn_list[number].setStyleSheet("font-size: 20px;")
            # signal, slot 연결
            self.btn_list[number].clicked.connect(self.on_clicked_number_btn)


        # 연산자 버튼 생성
        operations = ["/","*","-","+","=",".","inhak"]
        self.operation_btn_list = {}
        for operation in operations:
            self.operation_btn_list[operation] = QPushButton(operation)
            self.operation_btn_list[operation].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # signal, slot 연결
            self.operation_btn_list[operation].clicked.connect(self.on_clicked_operation_btn)

        # Clear, Del, Empty 버튼 생성
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # signal, slot 연결
        self.btn_clear.clicked.connect(self.on_clicked_clear_btn)

        self.btn_del = QPushButton("Del")
        self.btn_del.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # signal, slot 연결
        self.btn_del.clicked.connect(self.on_clicked_del_btn)

        self.btn_empty = QPushButton()
        self.btn_empty.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_empty.setEnabled(False)

        ### widget 배치 ###
        # Grid Layout 생성 -> 버튼 배치
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

        # Vertical Layout 생성 -> label 2개, 버튼이 배치된 gridlayout을 배치
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_equation, stretch = 2)
        vbox.addWidget(self.label_solution, stretch = 3)
        vbox.addLayout(grid_layout, stretch = 12)

        ### 윈도우 설정 ###
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(800, 200, 350, 550)
        self.setWindowTitle('Calculator')
        self.statusBar().showMessage('Developed by GVCSMG')

    ### slot 생성 ###
    # 버튼 클릭시 작동할 slot
    def on_clicked_number_btn(self):
        if self.label_solution.text():
            self.label_equation.clear()
            self.label_solution.clear()

        sender = self.sender()
        number = sender.text()
        self.label_equation.setText(self.label_equation.text()+number)

    # 연산자 클릭시 작동할 slot
    def on_clicked_operation_btn(self):
        sender = self.sender()
        operation = sender.text()
        if operation in ["+","-","/","*","."]:
            if self.label_equation.text() and self.label_equation.text()[-1] in "0123456789":
                self.label_equation.setText(self.label_equation.text() + operation)
            if self.label_solution.text() and self.label_solution.text()[-1] in "0123456789":
                self.label_equation.setText(self.label_solution.text() + operation)
                self.label_solution.clear()
        elif operation == "inhak":
            self.label_equation.clear()
            self.label_solution.setText("Hello World!!")
        elif operation == "=":
            if self.label_equation.text() and self.label_equation.text()[-1] in "=":
                try:
                    self.label_solution.setText(str(format(eval(self.label_equation.text().replace(",","")),",")))
                    self.label_equation.setText(self.label_equation.text() + '=')
                except:
                    QMessageBox.warning(self, "Close", "계산할 수 없습니다.")

    # del 버튼 slot
    def on_clicked_del_btn(self):
        if not self.label_solution.text():
            self.label_equation.setText(self.label_equation.text()[:-1])

    # clear 버튼 slot
    def on_clicked_clear_btn(self):
        self.label_solution.clear()
        self.label_equation.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())