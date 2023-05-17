### Example1-2 ###

import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Hello World")
label.show()

print("Before event loop")
sys.exit(app.exec_())
print("After event loop")