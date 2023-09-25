import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QVBoxLayout, QWidget

# 체크 박스 state 활용
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox1 = QCheckBox('그림자 표시', self)
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(self.on_state_changed)

        self.checkbox2 = QCheckBox('자동 저장', self)
        self.checkbox2.setChecked(False)
        self.checkbox2.stateChanged.connect(self.on_state_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.checkbox1)
        vbox.addWidget(self.checkbox2)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)
        self.setGeometry(300, 300, 250, 200)

    def on_state_changed(self, state):
        sender = self.sender()
        if sender == self.checkbox1:
            print('그림자 표시:', state)
        elif sender == self.checkbox2:
            print('자동 저장:', state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())