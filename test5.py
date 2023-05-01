import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.shot_checkbox = QCheckBox('샷추가', self)
        self.whip_checkbox = QCheckBox('휘핑추가', self)
        self.vanilla_checkbox = QCheckBox('바닐라추가', self)

        self.order_button = QPushButton('주문', self)
        self.order_button.clicked.connect(self.on_order_button_clicked)

        self.order_label = QLabel('주문할 항목:', self)
        self.order_list = QLabel('', self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.shot_checkbox)
        vbox.addWidget(self.whip_checkbox)
        vbox.addWidget(self.vanilla_checkbox)
        vbox.addWidget(self.order_button)
        vbox.addWidget(self.order_label)
        vbox.addWidget(self.order_list)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 200)

    def on_order_button_clicked(self):
        order_items = []
        if self.shot_checkbox.isChecked():
            order_items.append('샷추가')
        if self.whip_checkbox.isChecked():
            order_items.append('휘핑추가')
        if self.vanilla_checkbox.isChecked():
            order_items.append('바닐라추가')
        self.order_list.setText(', '.join(order_items))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
