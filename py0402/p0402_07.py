
# 나중에 할 것
## 파일 - 저장해서 불러오기
## DB에서 불러오기

stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":3}
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


## 함수 ##

def score_cal(i,score):
    while True:
                score[i] = input(f"{title[i+2]}점수를 입력하세요 >")
                if score[i].isdigit(): 
                    score[i] = int(score[i])
                    if 0 <= score[i] <= 100:
                        break
                    else: print("0부터 100까지의 숫자만 가능합니다.")
                else: print("숫자(정수)만 가능합니다.")


while True:
    print()
    print(" "*5,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 >"))
    
# 번호선택
    if choice == 1:
        print()
        print("[ 학생성적 입력 ]")
        while True:
            no = count
            name = input(f"{no}번 학생의 이름을 입력하세요. (0. 이전화면으로) >")
            # 이전화면 이동 확인
            if name == '0': break
            score = [0]*3
            # 점수 입력
            for i in range(3):
                score_cal(i,score)
            total = score[0] + score[1] + score[2]
            avg = total / 3
            rank = 0
            stuS.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
            print(f"{no}번 학생의 성적이 입력되었습니다.")
            count += 1
            print()
                
    elif choice == 2:
        print()
        print(" "*20,end="")
        print("[ 학생성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in stuS:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        
    elif choice == 3:
        print()
        print("[ 학생성적 수정 ]")
        while True:
            name_r = input("수정하려고 하는 학생 이름을 입력하세요. (0. 이전화면으로) >")
            if name_r == "0":
                break
            temp = 0            # 찾는 학생이 없을 경우에 활용
            for s in stuS:
                if name_r in s['name']:
                    temp = 1
                    print("[ 수정할 과목 선택 ]")
                    print("1. 국어")
                    print("2. 영어")
                    print("3. 수학")
                    print("-"*10)
                    choice = int(input("수정할 과목의 번호를 입력하세요 >"))
                    if choice == 1:
                        pr_kor = s['kor']
                        print(f"현재 입력된 국어점수는 {pr_kor}입니다.")
                        s['kor'] = int(input("변경할 점수를 입력하세요 >"))
                        print(f"{pr_kor}에서 {s['kor']}으로 변경되었습니다.")
                        s['total'] = s['kor'] + s['eng'] + s['math']
                        s['avg'] = s['total'] / 3
                    
                    elif choice == 2:
                        pr_eng = s['eng']
                        print(f"현재 입력된 영어점수는 {pr_eng}입니다.")
                        s['eng'] = int(input("변경할 점수를 입력하세요 >"))
                        print(f"{pr_eng}에서 {s['eng']}으로 변경되었습니다.")
                        s['total'] = s['kor'] + s['eng'] + s['math']
                        s['avg'] = s['total'] / 3
                        
                    elif choice == 3:
                        pr_math = s['math']
                        print(f"현재 입력된 수학점수는 {pr_math}입니다.")
                        s['math'] = int(input("변경할 점수를 입력하세요 >"))
                        print(f"{pr_math}에서 {s['math']}으로 변경되었습니다.")
                        s['total'] = s['kor'] + s['eng'] + s['math']
                        s['avg'] = s['total'] / 3
                    
                        
            if temp == 0:
                print(f"{name_r} 학생을 찾지 못했습니다.")
        
                
    
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break