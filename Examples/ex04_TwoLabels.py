### Example4 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

app = QApplication([])

#QMainWindow() 생성
window = QMainWindow()

# QWidget 생성
widget = QWidget()

# QLabel 생성
label1 = QLabel(widget)
label1.setText("Hello World1")
label2 = QLabel(widget)
label2.setText("Hello World2")
label2.move(0,30)

window.setCentralWidget(widget)
window.show()
sys.exit(app.exec_())