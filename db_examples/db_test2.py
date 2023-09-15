import sqlite3

class test_db:
    # SQLite DB 연결
    con = sqlite3.connect("test.db")

    #Cursor 객체 생성
    cur = con.cursor()

    def Insert_Data(self,data1,data2):
        try:
            sql = "INSERT INTO test_table VALUES(?,?)"
            data = (data1,data2)
            self.cur.execute(sql,data)
        except Exception as e:
            print('error:',e)
        finally:
            self.con.commit() # sql문을 commit한다

    def select_db(self):
        try:
            sql = "SELECT string_test FROM test_table"
            test_data = self.cur.execute(sql)
            for i in test_data:
                print(i[0])
        except Exception as e:
            print('error:',e)
        finally:
            self.con.close()

if __name__ == '__main__':
    SQL = test_db()
    SQL.Insert_Data("data1","1")
    SQL.select_db()
    SQL.con.close()