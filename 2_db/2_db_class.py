import sqlite3

class test_db:
    # SQLite DB 연결
    con = sqlite3.connect("test.db")

    #Cursor 객체 생성
    cur = con.cursor()

    def insert_data(self, name, age):
        try:
            cur = self.con.cursor()  # Cursor 객체 생성
            sql = "INSERT INTO test_table(test_name,test_age) VALUES(?,?)"
            data = (name, age)
            cur.execute(sql, data)
        except Exception as e:
            print('error:', e)
        finally:
            self.con.commit()  # sql문을 commit한다

    def select_db(self):
        try:
            cur = self.con.cursor()  # Cursor 객체 생성
            sql = "SELECT * FROM test_table"
            cur.execute(sql)
            test_data = cur.fetchall()  # 모든 자료를 row 단위 묶어서 리스트로 리턴
            print("id\t이름\t나이")
            for i in test_data:
                print("{}\t{}\t{}".format(i[0], i[1], i[2]))
        except Exception as e:
            print('error:', e)

if __name__ == '__main__':
    SQL = test_db()
    name = input("이름입력>>> ")
    age = input("나이 입력>>> ")
    SQL.insert_data(name,age)
    SQL.select_db()
    SQL.con.close()