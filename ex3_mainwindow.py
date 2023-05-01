### Example3 ###

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

app = QApplication([])

window = QMainWindow()

widget = QWidget()

label = QLabel(parent=widget)
label.setText("Hello World")

window.setCentralWidget(widget)

window.show()

sys.exit(app.exec_())