### Example14. QButtonGroup1 ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, \
    QLabel,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label1 =QLabel("샐러드 선택")
        label2 =QLabel("드레싱 선택")
        label3 = QLabel("음료 선택")
        label4 = QLabel("HOT/ICED")
        order_btn = QPushButton("주문")
        order_label = QLabel("주문 내역:")

        t_btn1 = QRadioButton("베이직 샐러드")
        t_btn2 = QRadioButton("에그마요 샐러드")
        t_btn3 = QRadioButton("햄 샐러드")

        self.t_btn_group = QButtonGroup()
        self.t_btn_group.addButton(t_btn1, 1)
        self.t_btn_group.addButton(t_btn2, 2)
        self.t_btn_group.addButton(t_btn3, 3)

        g_btn1 = QRadioButton("발사믹")
        g_btn2 = QRadioButton("오리엔탈")
        g_btn3 = QRadioButton("허니머스타드")

        self.g_btn_group = QButtonGroup()
        self.g_btn_group.addButton(g_btn1, 1)
        self.g_btn_group.addButton(g_btn2, 2)
        self.g_btn_group.addButton(g_btn3, 3)

        d_btn1 = QRadioButton("아메리카노")
        d_btn2 = QRadioButton("카페라떼")
        d_btn3 = QRadioButton("바닐라라떼")

        self.d_btn_group = QButtonGroup()
        self.d_btn_group.addButton(d_btn1, 1)
        self.d_btn_group.addButton(d_btn2, 2)
        self.d_btn_group.addButton(d_btn3, 3)

        h_btn1 = QRadioButton("HOT")
        h_btn2 = QRadioButton("ICED")

        self.h_btn_group = QButtonGroup()
        self.h_btn_group.addButton(h_btn1, 1)
        self.h_btn_group.addButton(h_btn2, 2)

        # connect the signal to the slot
        self.t_btn_group.buttonClicked.connect(self.on_clicked_t_btn)
        self.g_btn_group.buttonClicked.connect(self.on_clicked_g_btn)

        #레이아웃 설정
        hbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        vbox4 = QVBoxLayout()
        vbox1.addWidget(t_btn1)
        vbox1.addWidget(t_btn2)
        vbox1.addWidget(t_btn3)
        vbox2.addWidget(g_btn1)
        vbox2.addWidget(g_btn2)
        vbox2.addWidget(g_btn3)
        vbox3.addWidget(d_btn1)
        vbox3.addWidget(d_btn2)
        vbox3.addWidget(d_btn3)
        vbox4.addWidget(h_btn1)
        vbox4.addWidget(h_btn2)
        hbox.addWidget(label1)
        hbox.addLayout(vbox1)
        hbox.addWidget(label2)
        hbox.addLayout(vbox2)
        hbox.addWidget(label3)
        hbox.addLayout(vbox3)
        hbox.addWidget(label4)
        hbox.addLayout(vbox4)
        hbox.addWidget(order_btn)

        # 윈도우 설정
        widget= QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("GButtonGroup")

    def on_clicked_t_btn(self):
        print("Button Label is", self.t_btn_group.checkedButton().text(), \
              ", id is:", self.t_btn_group.id(self.t_btn_group.checkedButton()))

    def on_clicked_g_btn(self, obj):
        print("Button Label is", obj.text(), ", id is:", self.g_btn_group.id(obj))



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())