# 콘솔에 입력
# pip install oracledb

import dbconn

    
print("------------db연결------------")
# db접속
conn = dbconn.connections()    # sql dev 프로그램 오픈
cursor = conn.cursor()  # sql 창이 오픈
# employees 월급이 4000~6000 사이의 사번,이름,월급
# name = input("검색하려는 이름을 입력하세요 >")

name = '%'+name+'%'
query = "select employee_id,emp_name,salary from employees where salary between 4000 and 6000"
query2 = "select employee_id,emp_name,salary from employees where emp_name like :name"
cursor.execute(query2,name=name)
# cursor.execute("select * from stuscore")    #sql구문 실행 - f9
# rows = cursor.fetchall()    # 데이터를 가져옴.

    
for r in rows:
    print(r[0],r[1],r[2])
    
# title = ['번호','이름','국어','영어','수학','합계','평균','등수']    
# print("[ 학생성적 출력 ]")
# print("-"*70)
# print("{}\t{}\t\t\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
# for r in rows:
#     print(f"{r[0]}\t{r[1]}\t\t\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}")
