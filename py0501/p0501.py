# 오라클 db연결

from dbconn import *

# 오라클 접속 - 외부연결이므로 에러에 대한 예외처리를 하는 게 좋음

conn = connections()

cursor = conn.cursor()  # sql dev 페이지 오픈



# ## 데이터 하나만 가져오기
# query1 = 'select count(*) from stuscore'
# cursor.execute(query1)
# cnt = cursor.fetchone()     # 실행결과 - 한 개
# print("학생수 : ",cnt[0])


while True:
    print("[ 학생성적 프로그램 ]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 검색")
    print("5. 학생성적 정렬 - 이름 순차정렬")
    print("-"*30)
    choice = input("원하는 번호를 선택하세요 >")

    if choice == '1':
        ## 직접입력
        name = input("이름을 입력하세요 >")
        kor = int(input("국어점수를 입력하세요 >"))
        eng = int(input("영어점수를 입력하세요 >"))
        math = int(input("수학점수를 입력하세요 >"))
        total = kor+eng+math
        avg = total/3


        ## insert - 1개 저장
        query = "insert into stuscore values(stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0)"
        cursor.execute(query,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
        conn.commit()
        
        
    elif choice == '2':
        query = 'select * from stuscore'
        cursor.execute(query)   # f5 쿼리문 실행
        rows = cursor.fetchall()       # 실행 결과 가져옴 - 여러 개
        # print(type(rows))

        for r in rows:
            print(r)
    
    elif choice == '3':
        # 학생 검색 > 현재 점수 출력 > 수정 점수 입력 > total avg 계산 업데이트
        # r_name = input("수정할 학생의 이름을 입력하세요 >")
        
        r_kor = int(input("새로운 국어점수를 입력하세요 >"))
        query = "update stuscore set kor=:r_kor,total=:r_kor+eng+math,avg=(:r_kor+eng+math)/3 where sno=103"
        cursor.execute(query,r_kor=r_kor)
        conn.commit()
        print("수정이 완료되었습니다.")
    
    elif choice == '4':
        # 이름을 검색해서 해당 학생 출력
        name_s = input("검색할 학생의 이름을 입력하세요 >")
        # name = '%'+name_s+'%'
        # like = '%'||:name_s||'%'      ## || >> concat 명령어
        query = "select * from stuscore where name like '%'||:name_s||'%'"   # 직접 넣으려면 '%||:name_s||%' 같은 형태로 써야 함 ?
        cursor.execute(query,name_s=name_s)
        rows = cursor.fetchall()
        if len(rows) <= 0:
            print("학생을 찾지 못했습니다.")
            continue
        
        for r in rows:
            print(r)
        print()
    
    elif choice == '5':
        print("[ 이름으로 정렬 ]")
        query = "select * from stuscore order by name"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        for r in rows:
            print(r)
    
    
    else:
        break




# 종료
cursor.close()
conn.close()
print("[ 프로그램 종료 ]")

# ## db접속정보
# def connections():
#     conn = ora.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
#     return conn