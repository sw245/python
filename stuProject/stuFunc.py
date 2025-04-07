
from stuModule import *


# Students 객체선언

students = Students()
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


# 타이틀메뉴 함수 선언
def tmenu_print():
    print(" "*20,end="")
    print("[ 학생성적처리 프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("0. 프로그램 종료")
    choice = 0
    try:
        choice = int(input("원하는 번호를 입력하세요 >"))
    except Exception as e:  
        print(e)

    return choice



# 성적입력 함수 선언
def stu_input():
    try:
        print("[ 학생성적 입력 ]")
        name = input(f"{Student.count}번째 학생의 이름을 입력하세요 >")
        score = [0]*3
        for i in range(len(score)):
            score[i] = int(input(f"{title[i+2]} 점수를 입력하세요 >"))
        students.add(Student(name,*score))
        print(f"{name} 학생이 등록되었습니다.")
    except Exception as e:
        print(e)
        
        
# 성적출력 함수 선언

def stu_print():
    print("[ 학생성적 출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students:     # 참조변수명.리스트변수
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}")