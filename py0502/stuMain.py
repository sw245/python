
from stuConn import *
conn = connections()
cursor = conn.cursor()

while True:
    print("[ 학생성적 프로그램 ]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 프로그램 종료")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요 >"))
    
    if choice == 1:
        name = input("이름을 입력하세요 >")
        kor = int(input("수학성적을 입력하세요 >"))
        eng = int(input("영어성적을 입력하세요 >"))
        math = int(input("국어성적을 입력하세요 >"))
        total = kor+eng+math
        avg = total / 3
        query = "insert into stuscore values (stuscore_seq.nextval,:sname,:skor,:seng,:smath,:stotal,:savg,0)"
        cursor.execute(query,sname=name,skor=kor,seng=eng,smath=math,stotal=total,savg=avg)
        conn.commit()
        print("성적이 입력되었습니다.")
        print()
        