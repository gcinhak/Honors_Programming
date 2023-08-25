### Example1-1 ###

import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
# app생성
# sys.argvs는 파이썬 명령행의 인자값을 받아서 list로 저장한다.
# app = QApplication([])

label = QLabel("Hello World!!!!!")
label.show()

sys.exit(app.exec_())
# app.exec_(): app무한루프, 프로그램 실행, 프로그램 종료시 0 리턴
# sys.exit(0): 파이썬 실행 종료