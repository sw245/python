
# import stu_func

# import stu_func as stu                                      # 호출에 별칭 사용
# from stu_func import stu_input,stu_output,stu_print         # 각각의 함수명을 미리 불러옴
from stu_func import *                                      # 모든 함수 불러오기

stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":0}
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


# def stu_renew():


while True:
    choice = stu_print()                               # 초기화면 출력
    if choice == 1:
        count = stu_input(count,stuS)                  # 성적입력
    elif choice == 2:
        stu_output(stuS,title)                         # 성적출력
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        name_r = input("수정하려는 학생의 이름을 입력하세요 >")
        temp = 0
        print()
        for s in stuS:
            if name_r == s['name']:
                temp = 1
                print(f"{name_r} 학생의 성적을 수정합니다.")
                print("[ 수정과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                ch_r = int(input("원하는 번호를 입력하세요 >"))
                sub_list = ['','kor','eng','math']
                if ch_r == 1:
                    pre_score = s[sub_list[ch_r]]
                    print(f"현재 {title[ch_r+1]}점수 : {pre_score}")
                    s[sub_list[ch_r]] = int(input("새로운 점수를 입력하세요 >"))
                    print(f"{pre_score}점에서 {s[sub_list[ch_r]]}점으로 변경되었습니다.")
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                elif ch_r == 2:
                    pre_score = s[sub_list[ch_r]]
                    print(f"현재 {title[ch_r+1]}점수 : {pre_score}")
                    s[sub_list[ch_r]] = int(input("새로운 점수를 입력하세요 >"))
                    print(f"{pre_score}점에서 {s[sub_list[ch_r]]}점으로 변경되었습니다.")
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                elif ch_r == 3:
                    pre_score = s[sub_list[ch_r]]
                    print(f"현재 {title[ch_r+1]}점수 : {pre_score}")
                    s[sub_list[ch_r]] = int(input("새로운 점수를 입력하세요 >"))
                    print(f"{pre_score}점에서 {s[sub_list[ch_r]]}점으로 변경되었습니다.")
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
        if temp == 0:
            print(f"{name_r} 학생을 찾지 못했습니다.")
    elif choice == 4:
        stu_rank(stuS)                                 # 등수처리
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break