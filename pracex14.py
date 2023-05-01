### Example13. QRadioButton ###

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QCheckBox, QRadioButton, QHBoxLayout, \
    QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_hot = QRadioButton("Hot")
        self.radio_ice = QRadioButton("Ice")
        self.checkbox_decaffein = QCheckBox("디카페인")
        self.checkbox_shot = QCheckBox("샷 추가")
        self.checkbox_cream = QCheckBox("휘핑 추가")
        self.checkbox_vanilla = QCheckBox("바닐라 추가")
        self.checkbox_hazelnut = QCheckBox("헤이즐넛 추가")
        self.checkbox_syrup = QCheckBox("슈가시럽 추가")
        self.order_label = QLabel("주문 내역:")
        self.order_list = QLabel('')
        self.order_btn = QPushButton("주문")

        self.order_btn.clicked.connect(self.on_order_button_clicked)

        # 레이아웃 선언 및 Widget 설정
        vbox = QVBoxLayout()
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.radio_hot)
        hbox_1.addWidget(self.radio_ice)

        vbox.addLayout(hbox_1)
        vbox.addWidget(self.checkbox_decaffein)
        vbox.addWidget(self.checkbox_shot)
        vbox.addWidget(self.checkbox_cream)
        vbox.addWidget(self.checkbox_vanilla)
        vbox.addWidget(self.checkbox_hazelnut)
        vbox.addWidget(self.checkbox_syrup)
        vbox.addWidget(self.order_btn)
        vbox.addWidget(self.order_label)
        vbox.addWidget(self.order_list)

        widget = QWidget()
        widget.setLayout(vbox)

        # 윈도우 설정
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("CheckBox")

    def on_order_button_clicked(self):
        order_items = []
        if self.radio_hot.isChecked():
            order_items.append(self.radio_hot.text())
        elif self.radio_ice.isChecked():
            order_items.append(self.radio_ice.text())
        if self.checkbox_decaffein.isChecked():
            order_items.append(self.checkbox_decaffein.text())
        if self.checkbox_shot.isChecked():
            order_items.append(self.checkbox_shot.text())
        if self.checkbox_cream.isChecked():
            order_items.append(self.checkbox_cream.text())
        if self.checkbox_vanilla.isChecked():
            order_items.append(self.checkbox_vanilla.text())
        if self.checkbox_hazelnut.isChecked():
            order_items.append(self.checkbox_hazelnut.text())
        if self.checkbox_syrup.isChecked():
            order_items.append(self.checkbox_syrup.text())
        self.order_list.setText(', '.join(order_items))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())