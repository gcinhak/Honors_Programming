### Example2 ###

import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

server_ip = None
port = None

for arg in sys.argv:
    if arg.startswith('--server-ip'):
        server_ip = arg.split("=")[1]
    elif arg.startswith('--port='):
        port = arg.split("=")[1]

# 서버 주소와 포트 번호를 사용하여 QLabel 객체 생성
label = QLabel(f"Server: {server_ip}, Port: {port}")

label.show()
sys.exit(app.exec_())