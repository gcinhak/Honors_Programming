import sys

from PyQt5.QtWidgets import  QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QTabWidget, \
    QRadioButton, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTabWidget')
        self.setGeometry(200,200,400,300)
        self.init_widget()

    def init_widget(self):
        btn_ok = QPushButton("OK")
        btn_cancel = QPushButton("Cancel")

        tabs = QTabWidget()
        tabs.addTab(self.tab1(), 'Button')
        tabs.addTab(self.tab2(), 'Checkbox')
        tabs.addTab(self.tab3(), 'Radio')

        # 메인윈도우 위젯 설정
        hbox = QHBoxLayout()
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addLayout(hbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def tab1(self):
        # 버튼 객체 만들기
        button1 = QPushButton('버튼1')
        button2 = QPushButton('버튼2')
        button3 = QPushButton('버튼3')

        # 레이아웃 만들기
        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(vbox)
        return tab


    def tab2(self):
        # 버튼 객체 만들기
        check1 = QCheckBox('체크버튼1')
        check2 = QCheckBox('체크버튼2')
        check3 = QCheckBox('체트버튼3')

        # 레이아웃 만들기
        vbox = QVBoxLayout()
        vbox.addWidget(check1)
        vbox.addWidget(check2)
        vbox.addWidget(check3)

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(vbox)
        return tab

    def tab3(self):
        # radio 버튼
        radio1 = QRadioButton('레디오버튼1')
        radio2 = QRadioButton('레디오버튼2')
        radio3 = QRadioButton('레디오버튼3')

        # 레이아웃 만들기
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(vbox)
        return tab

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())