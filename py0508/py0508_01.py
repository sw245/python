import oracledb
from math import *

## db연결
def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn

def stuPrintAll():
    conn = connections()
    cursor = conn.cursor()
    query1 = "select * from stuscore"
    cursor.execute(query1)
    rows = cursor.fetchall()
    conn.close()
    return rows
    
    

while True:
    print("[ db ]")
    print("1. stuscore_학생 전체출력")
    print("2. stuscore_반 별 1등 학생 출력")
    print("3. stuscore_반 별 최하등 학생 출력")
    print("4. employees_부서별 최고연봉 출력")
    print("5. stuscore2_반(sclass) 부여")
    print("6. member_rownum 사용, 11-20번 출력")
    print("0. 종료")
    print("-"*20)
    choice = input("번호를 입력하세요 >")
    
    # 1-2-5-6
    if choice == '1':
        rows = stuPrintAll()
        for r in rows:
            print(r)
        print()
    
    elif choice == '2':
        conn = connections()
        cursor = conn.cursor()
        query2 = """select * from stuscore where (sclass,total) in (select sclass,max(total) from stuscore group by sclass)
                order by sclass"""
        cursor.execute(query2)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
        conn.close()
    
    elif choice == '3':
        pass
    
    elif choice == '4':
        pass
    
    elif choice == '5':
        conn = connections()
        cursor = conn.cursor()
        query5= """update stuscore2 set sclass = case when sno between :mm and :nn then :n end
                    where sno between :mm and :nn"""
        rows = stuPrintAll()
        for r in range(1,ceil(len(rows)/10)+1):
            cursor.execute(query5,mm=(r*10)-9,nn=r*10,n=r)
        print("반 부여 완료")
        conn.commit()
        conn.close()

    
    elif choice == '6':
        conn = connections()
        cursor = conn.cursor()
        query6 = """select * from (select rownum rnum,m.* from member m)
                where rnum between 11 and 20"""
        cursor.execute(query6)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        conn.close()
    
    elif choice == '0':
        break