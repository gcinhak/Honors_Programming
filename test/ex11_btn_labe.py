import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QWidget 생성
        widget = QWidget()

        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)

        # QPushButton 생성
        btn = QPushButton('+')
        btn.clicked.connect(self.on_click_btn)

        # QVBoxLayout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(btn)

        # widget에 레이아웃 추가
        widget.setLayout(layout)

        # central widget에 widget 추가
        self.setCentralWidget(widget)

    def on_click_btn(self):
        count = int(self.label.text())
        self.label.setText(str(count + 1))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())