import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, \
    QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 콤보박스 생성 및 세팅
        self.cb = QComboBox()
        self.cb.addItem('Option1')
        self.cb.addItem('Option3')
        self.cb.addItems(['Option4','Option5'])
        self.cb.insertItem(1, 'Option2')
        # self.cb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 버튼, 라벨 생성 및 세팅
        self.lb = QLabel()
        btn = QPushButton("btn1")
        # btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 콤보박스 시그널 설정
        # self.cb.activated.connect(self.changed_item)
        # self.cb.currentIndexChanged.connect(self.changed_item)
        # self.cb.currentTextChanged.connect(self.changed_item)
        # self.cb.highlighted.connect(self.changed_item)

        # 버튼 시그널 설정
        btn.clicked.connect(self.on_clicked_btn)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.cb)
        vbox.addWidget(btn)

        # 윈도우 설정
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle('ComboBox')
        self.setGeometry(800, 300, 150, 100)

    # 슬롯
    def changed_item(self, i):
        print("changed item:",i)

    def on_clicked_btn(self):
        # self.lb.setText("현재 index: "+str(self.cb.currentIndex()))
        self.lb.setText("현재 text: "+self.cb.currentText())
        # self.lb.setText("항목 개수: "+str(self.cb.count()))
        # self.lb.setText("2번째 항목은: "+str(self.cb.itemText(1)))
        # self.cb.removeItem(self.cb.currentIndex())
        # self.cb.clear()

        # self.cb.setCurrentIndex(1)
        # self.cb.setCurrentText('Option4')

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())