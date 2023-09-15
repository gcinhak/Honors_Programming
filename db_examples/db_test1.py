import sqlite3

def connection():
    try:
        # SQLite DB 연결
        con = sqlite3.connect("test.db")
        return con
    except Exception as e:
        print(e)

def Insert_Data(con,data1,data2):
    try:
        # Cursor 객체 생성
        cur = con.cursor()
        sql = "INSERT INTO test_table VALUES(?,?)"
        data = (data1,data2)
        cur.execute(sql,data)
    except Exception as e:
        print('error:',e)
    finally:
        con.commit() # sql문을 commit한다

def select_db(con):
    try:
        # Cursor 객체 생성
        cur = con.cursor()
        sql = "SELECT * FROM test_table"
        test_data = cur.execute(sql)
        for i in test_data:
            print(i)
    except Exception as e:
        print('error:',e)

con = connection()
Insert_Data(con, "data1","2")
select_db(con)
con.close()

