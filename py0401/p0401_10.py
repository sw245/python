
stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":3}
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


while True:
    print(" "*5,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 >"))
    
    # 입력번호 확인
    if choice == 1:
        while True:
            print("[ 학생성적 입력 ]")
            no = count
            name = input(f"{no}번 학생의 이름을 입력하세요. (0.이전화면 이동) >")
            if name == "0" : break
            kor = int(input("국어점수를 입력하세요 >"))
            eng = int(input("영어점수를 입력하세요 >"))
            math = int(input("수학점수를 입력하세요 >"))
            total = kor + eng + math
            avg = total / 3     # 나눗셈 >> float타입으로 생성(n.00)
            rank = 0
        
            stuS.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            print(f"{name} 학생의 성적이 등록되었습니다.")
            print()
            count += 1
    
        ## for문으로 입력받기
        # score = [0]*3      # kor, eng, math
        # for i in range(3):
        #     score[i] = int(input(f"{title[i+2]}점수를 입력하세요."))
    
    elif choice == 2:
        print(" "*20,end="")
        print("[ 학생성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*title))
        print("-"*60)
        for s in stuS:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")
        print()
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        print()
        break
    


