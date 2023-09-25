import sys

from PyQt5.QtWidgets import *
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DB')
        self.setGeometry(100, 100, 400, 400)
        self.init_ui()

    def init_ui(self):
        global table_widget # tablewidget global로 만들어줘서 클래스 밖의 함수에서 사용할 수 있음.
        table_widget = QTableWidget() # QTableWidget() 객체 만들어서 글로벌로 생성한 변수에 저장
        self.layout_main = QVBoxLayout()
        self.layout_top = QHBoxLayout()
        self.btn_add = QPushButton("추가")
        self.le_name = QLineEdit()
        self.le_age = QLineEdit()
        self.btn_del = QPushButton('삭제')
        self.lb = QLabel("이름과 나이를 입력하세요.")
        self.init_widget()

    def init_widget(self):
        table_widget.setColumnCount(3)

        self.btn_add.clicked.connect(self.on_btn_add)
        self.btn_del.clicked.connect(self.on_btn_del)

        self.layout_top.addWidget(self.le_name)
        self.layout_top.addWidget(self.le_age)
        self.layout_top.addWidget(self.btn_add)
        self.layout_top.addWidget(self.btn_del)

        self.layout_main.addWidget(self.lb)
        self.layout_main.addLayout(self.layout_top)
        self.layout_main.addWidget(table_widget)

        widget = QWidget()
        widget.setLayout(self.layout_main)
        self.setCentralWidget(widget)

        self.set_tablewidget() #TableWidget에 DB 데이터 세팅

    # 테이블 위젯에 DB 데이터 입력
    def set_tablewidget(self):
        con = connection_db() # DB 연결

        select_db(con) # DB 데이터 조회 및 테이블 위젯에 DB 데이터 입력

        con.close() # DB 연결 해제

    # DB에 데이터 추가
    def on_btn_add(self):
        con = connection_db()
        if self.le_name.text() != "":
            insert_db(con, self.le_name.text(), self.le_age.text())
            select_db(con)
        else:
            QMessageBox.about(self, 'Error', '이름은 반드시 입력하셔야 합니다.')

        con.close()

    # DB에 데이터 삭제
    def on_btn_del(self):
        con = connection_db()
        try:
            id = table_widget.item(table_widget.currentRow(),0).text()
            delete_db(con,id)
            select_db(con)
        except Exception as e:
            QMessageBox.about(self, 'Error', '삭제할 데이터가 없습니다.')

        con.close()

# 테이블 위젯에 DB 데이터 입력
def set_table(mem_data):
    cnt = len(mem_data)
    table_widget.setRowCount(cnt)

    for row in range(cnt):
        id, name, age= mem_data[row]
        table_widget.setItem(row,0,QTableWidgetItem(str(id)))
        table_widget.setItem(row,1,QTableWidgetItem(name))
        table_widget.setItem(row,2,QTableWidgetItem(str(age)))

# DB 연결
def connection_db():
    try:
        # SQLite DB 연결
        con = sqlite3.connect("../../2_db/test.db")
        return con
    except Exception as e:
        print(e)

# DB 데이터 입력
def insert_db(con,name,age):
    try:
        # Cursor 객체 생성
        cur = con.cursor()
        sql = "INSERT INTO test_table (test_name, test_age) VALUES(?,?)"
        data = (name,age)
        cur.execute(sql,data)
    except Exception as e:
        print('error:',e)
    finally:
        con.commit() # sql문을 commit한다

# DB 데이터 조회
def select_db(con):
    try:
        # Cursor 객체 생성
        cur = con.cursor()
        sql = "SELECT * FROM test_table"
        cur.execute(sql)
        mem_data = cur.fetchall()
        set_table(mem_data) # 테이블 위젯에 DB 데이터 입력
    except Exception as e:
        print('error:',e)

# DB 데이터 삭제
def delete_db(con,id):
    try:
        # Cursor 객체 생성
        cur = con.cursor()
        sql = "DELETE FROM test_table WHERE test_id =?"
        cur.execute(sql, (id,))
        con.commit()
    except Exception as e:
        print('error:',e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())