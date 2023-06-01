import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ### widget 생성 ###
        self.gp_list = []
        self.cd_list = []
        for i in range(5):
            self.gp_list.append(QLineEdit("0"))
            self.cd_list.append(QLineEdit("0"))

        # 라디오버튼 생성
        self.radio_unwgpa = QRadioButton("UNWGPA")
        self.radio_wgpa = QRadioButton("WGPA")
        self.radio_wgpa.setChecked(True)

        # GPA 출력 레이블 생성
        self.lb_gpa = QLabel("GPA 출력")

        # GPA 계산 버튼 생성
        btn_cal = QPushButton("GPA 계산")
        btn_cal.clicked.connect(self.on_btn_cal_clicked)

        ### layout 생성 ###
        grid_input = QGridLayout()
        for i in range(5):
            grid_input.addWidget(self.gp_list[i], i, 0)
            grid_input.addWidget(self.cd_list[i], i, 1)

        grid_input.addWidget(self.lb_gpa, 5, 0, 1, 2)
        grid_input.addWidget(self.radio_wgpa, 6, 0)
        grid_input.addWidget(self.radio_unwgpa, 6, 1)
        grid_input.addWidget(btn_cal, 7, 0, 1, 2)

        widget = QWidget()
        widget.setLayout(grid_input)
        self.setCentralWidget(widget)

    def on_btn_cal_clicked(self):
        wgpa = 0
        unwgpa = 0
        total_credit = 0

        for i in range(5):
            wgpa += float(self.gp_list[i].text()) * float(self.cd_list[i].text())
            unwgpa += float(self.gp_list[i].text())
            total_credit += float(self.cd_list[i].text())

        # 레이블에 출력
        if self.radio_wgpa.isChecked():
            self.lb_gpa.setText(str(wgpa / total_credit))
        elif self.radio_unwgpa.isChecked():
            self.lb_gpa.setText(str(unwgpa / 5))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
