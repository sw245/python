# 1. sModule.py - class 2개
# 2. sMain.py
#   sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수를 옮겨봄.



from sModule import *

title = ['번호','이름','국어','영어','수학','합계','평균','등수']


students = Students()

while True:    
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("0. 프로그램 종료")
    try:
        choice = int(input("원하는 숫자를 입력하세요 >"))
    except Exception as e:
        print(e)
        continue

    if choice == 1:
        print("[ 학생성적 입력 ]")
        s.name = input(f"{s.no}번 학생의 이름을 입력하세요 >")
        score = [s.kor,s.eng,s.math]
        for i in range(len(score)):
            try:
                score[i] = int(input(f"{title[i+2]}성적을 입력하세요 >"))
            except Exception as e:
                print(e)
                continue
        s = Student(s.name,s.kor,s.eng,s.math)
        students.add(str(s))
        print("성적 입력이 완료되었습니다.")
        
        
    if choice == 2:
        print("[ 학생성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for s in students.stuS:
            print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg}\t{s.rank}")
        
            
            
    if choice == 0:
        pass