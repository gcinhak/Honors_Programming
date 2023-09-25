### Example3 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

app = QApplication([])
window = QMainWindow()
widget = QWidget()

label = QLabel()
label.setText("Hello World")
label.setParent(widget)

window.setCentralWidget(widget)
window.show()
sys.exit(app.exec_())