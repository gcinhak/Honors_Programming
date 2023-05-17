### Example1-2 ###

import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Hello World")
label.show()

print("Before event loop")
# 시스템을 바로 종료
# sys.exit(app.exec_())

# 이벤트 루프를 종료 하고, 코드 진행
app.exec_()
print("After event loop")