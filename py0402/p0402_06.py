

### 기본 변수 ###

stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":3}
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']




### 함수 모아놓기 ###

# 국/영/수 점수 입력
def score_cal(i,score):
    while True:
        score[i] = input(f"{title[i+2]}점수를 입력하세요 >")
        if score[i].isdigit(): 
            score[i] = int(score[i])
            if 0 <= score[i] <= 100:
                break
            else: print("0부터 100까지의 숫자만 가능합니다.")
        else: print("숫자(정수)만 가능합니다.")

# 학생성적 입력

def stu_input(count):
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
    return count


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
        count = stu_input(count)
        
        
        

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