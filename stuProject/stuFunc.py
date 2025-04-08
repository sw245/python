
from stuModule import *


# Students 객체선언

students = Students()           # 객체 선언 / students >> 객체 변수
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


# 타이틀메뉴 함수 선언
def tmenu_print():
    print()
    print(" "*20,end="")
    print("[ 학생성적처리 프로그램 ]")
    print("-"*60)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
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
        stu = Student(name,*score)
        students.add(stu)
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
        
        
# 과목성적수정 함수 선언

def stu_renew(sub,ch_r):        
    print(f"[ {title[ch_r+1]}성적 수정 ]")
    print(f"현재 {title[ch_r+1]}점수 : {sub}")
    sub = int(input("새로운 점수를 입력하세요 >"))
    print(f"{title[ch_r+1]}점수가 {sub}점으로 변경되었습니다.")
    return sub


# 성적수정 함수 선언

def stu_modify():
    print("[ 학생성적 수정 ]")
    name_r = input("수정하려는 학생의 이름을 입력하세요 >")
    temp = 0                        # 찾지 못한 경우 구분
    for stu in students.students:
        if name_r == stu.name:
            temp = 1
            print(f"{name_r} 학생을 찾았습니다. 성적을 수정합니다.")
            print("[ 수정과목 선택 ]")
            print("1. 국어")
            print("2. 영어")
            print("3. 수학")
            print("-"*20)
            try:
                ch_r = int(input("원하는 번호를 입력하세요 >"))
            except Exception as e:
                print(e)
                continue
            if ch_r == 1:
                stu.kor = stu_renew(stu.kor,ch_r)
            elif ch_r == 2:
                stu.eng = stu_renew(stu.eng,ch_r)
            elif ch_r == 3:
                stu.math = stu_renew(stu.math,ch_r)
            stu.stu_total()             # 합계 수정
            stu.stu_avg()               # 평균 수정
    if temp == 0:
        print(f"{name_r} 학생을 찾지 못했습니다.")