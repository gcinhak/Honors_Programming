import sqlite3

def connection():
    try:
        con = sqlite3.connect("test.db") # SQLite DB 연결
        return con
    except Exception as e:
        print(e)

def insert_db(con):
    name = input("이름 입력>>> ")
    age = input("나이 입력>>> ")
    try:
        cur = con.cursor() # Cursor 객체 생성
        sql = "INSERT INTO test_table(test_name,test_age) VALUES(?,?)"
        data = (name,age)
        cur.execute(sql,data)
    except Exception as e:
        print('error:',e)
    finally:
        con.commit() # sql문을 commit한다

def select_db(con):
    try:
        cur = con.cursor() # Cursor 객체 생성
        sql = "SELECT * FROM test_table"
        cur.execute(sql)
        test_data = cur.fetchall() # 모든 자료를 row 단위 묶어서 리스트로 리턴
        print(test_data)
        print("id\t이름\t나이")
        for i in test_data:
            print("{}\t{}\t{}".format(i[0], i[1], i[2]))
    except Exception as e:
        print('error:',e)

con = connection()
insert_db(con)
select_db(con)
con.close() # DB 연결 해제

