from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QMainWindow
import sys

# 체크박스 클릭 갯수 제한 2개까지
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.cb1 = QCheckBox("Option 1")
        self.cb2 = QCheckBox("Option 2")
        self.cb3 = QCheckBox("Option 3")
        self.cb4 = QCheckBox("Option 4")

        self.cb1.stateChanged.connect(self.on_state_changed)
        self.cb2.stateChanged.connect(self.on_state_changed)
        self.cb3.stateChanged.connect(self.on_state_changed)
        self.cb4.stateChanged.connect(self.on_state_changed)

        vbox.addWidget(self.cb1)
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.cb3)
        vbox.addWidget(self.cb4)

        # 윈도우 설정
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("CheckBox")

    def on_state_changed(self, state):
        print("checekbox number:", state)
        checkboxes = [self.cb1, self.cb2, self.cb3, self.cb4]
        checked_boxes = [cb for cb in checkboxes if cb.isChecked()]
        print("number of checked:", len(checked_boxes))
        if len(checked_boxes) >= 2:
            for cb in checkboxes:
                if not cb.isChecked():
                    cb.setEnabled(False)
        else:
            for cb in checkboxes:
                cb.setEnabled(True)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())