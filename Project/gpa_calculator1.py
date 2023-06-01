import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ### widget 생성 ###
        # GP LineEdit 생성
        self.le_gp1 = QLineEdit("0")
        self.le_gp2 = QLineEdit("0")
        self.le_gp3 = QLineEdit("0")
        self.le_gp4 = QLineEdit("0")
        self.le_gp5 = QLineEdit("0")

        # Credit LineEdit 생성
        self.le_credit1 = QLineEdit("0")
        self.le_credit2 = QLineEdit("0")
        self.le_credit3 = QLineEdit("0")
        self.le_credit4 = QLineEdit("0")
        self.le_credit5 = QLineEdit("0")

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
        grid_input.addWidget(self.le_gp1, 0, 0)
        grid_input.addWidget(self.le_gp2, 1, 0)
        grid_input.addWidget(self.le_gp3, 2, 0)
        grid_input.addWidget(self.le_gp4, 3, 0)
        grid_input.addWidget(self.le_gp5, 4, 0)

        grid_input.addWidget(self.le_credit1, 0, 1)
        grid_input.addWidget(self.le_credit2, 1, 1)
        grid_input.addWidget(self.le_credit3, 2, 1)
        grid_input.addWidget(self.le_credit4, 3, 1)
        grid_input.addWidget(self.le_credit5, 4, 1)

        grid_input.addWidget(self.lb_gpa, 5, 0, 1, 2)
        grid_input.addWidget(self.radio_wgpa, 6, 0)
        grid_input.addWidget(self.radio_unwgpa, 6, 1)
        grid_input.addWidget(btn_cal, 7, 0, 1, 2)

        widget = QWidget()
        widget.setLayout(grid_input)
        self.setCentralWidget(widget)

    def on_btn_cal_clicked(self):
        # float으로 변경하여 gp에 저장
        gp1 = float(self.le_gp1.text())
        gp2 = float(self.le_gp2.text())
        gp3 = float(self.le_gp3.text())
        gp4 = float(self.le_gp4.text())
        gp5 = float(self.le_gp5.text())

        # float으로 변경하여 cd에 저장
        cd1 = float(self.le_credit1.text())
        cd2 = float(self.le_credit2.text())
        cd3 = float(self.le_credit3.text())
        cd4 = float(self.le_credit4.text())
        cd5 = float(self.le_credit5.text())

        # wgpa, unwgpa 계산하여 저장
        wgpa = (gp1*cd1+gp2*cd2+gp3*cd3+gp4*cd4+gp5*cd5) / (cd1+cd2+cd3+cd4+cd5)
        unwgpa = (gp1+gp2+gp3+gp4+gp5) / 5

        # 레이블에 출력
        if self.radio_wgpa.isChecked():
            self.lb_gpa.setText(str(wgpa))
        elif self.radio_unwgpa.isChecked():
            self.lb_gpa.setText(str(unwgpa))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
