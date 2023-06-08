import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget,QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.mark = "O"

    def init_ui(self):
        ### Button 생성 ###
        self.btn_list = []
        for i in range(9):
            self.btn_list.append(QPushButton(""))
            self.btn_list[i].clicked.connect(self.on_btn_clicked)
            self.btn_list[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_reset = QPushButton("Reset")
        btn_reset.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_reset.clicked.connect(self.on_btn_reset_clicked)

        grid_board = QGridLayout()
        for i in range(3):
            for j in range(3):
                grid_board.addWidget(self.btn_list[i*3+j], i , j)

        grid_board.addWidget(btn_reset,3,0,1,3)

        widget = QWidget()
        widget.setLayout(grid_board)
        self.setCentralWidget(widget)
        self.setGeometry(1000, 500, 500, 500)

    def on_btn_reset_clicked(self):
        print("on reset")
        self.mark = "O"
        for i in range(3):
            for j in range(3):
                self.btn_list[i * 3 + j].setText("")

    def on_btn_clicked(self):
        e = self.sender()
        print(self.mark)
        if e.text() == "":
            e.setText(self.mark)
            if self.mark == "O":
                self.mark = "X"
            elif self.mark == "X":
                self.mark = "O"
        else:
            return

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())