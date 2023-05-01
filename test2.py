import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel


class 체크박스(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.cbox = QCheckBox('체크박스1', self)
        self.cbox.move(40, 30)

        self.cbox.stateChanged.connect(self.changeBox1)

        self.cbox2 = QCheckBox('체크박스2', self)
        self.cbox2.move(150, 30)

        self.cbox2.stateChanged.connect(self.changeBox2)

        self.result = QLabel('체크 박스를 선택해주세요.', self)
        self.result.setFixedWidth(300)
        self.result.move(40, 100)

        self.cbox2.toggle()

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeBox1(self, state):
        print(state)
        if state == Qt.Checked:
            self.result.setText('체크박스1이 선택되었습니다.')
        else:
            self.result.setText('체크박스를 선택해주세요.')

    def changeBox2(self, state):
        if state == Qt.Checked:
            self.result.setText('체크박스2이 선택되었습니다.')
        else:
            self.result.setText('체크박스를 선택해주세요.')


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 체크박스()
프로그램무한반복.exec_()