import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
widget = QWidget()
label = QLabel("Hello World", widget)

widget.show()
sys.exit(app.exec_())
