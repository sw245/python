

stuS = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99.67,2],
    [3,'이순신',90,99,98,287,95.67,3],
]

# stuS = list()
count = 3
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    # 화면 출력
    print("-"*30)
    print(" "*5,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("5. 학생성적 정렬")
    print("6. 학생성적 검색")
    print("7. 등수 처리")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 >"))
    
    if choice == 1:
        print("[ 학생성적 입력 ]")
        count += 1
        name = input("학생의 이름을 입력하세요 >")
        kor = int(input("국어성적을 입력하세요 >"))
        eng = int(input("영어성적을 입력하세요 >"))
        math = int(input("수학성적을 입력하세요 >"))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        stuS.append([count,name,kor,eng,math,total,avg,rank])
        print(f"{name} 학생의 성적 입력이 완료되었습니다.")
                
    elif choice == 2:
        print("[ 학생성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))      # *는 리스트 전개 연산자
        print("-"*60)
        for s in stuS:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))
        print()
        
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        name_r = input("수정할 학생의 이름을 입력하세요 >")
        temp = 0
        for s in stuS:
            if name_r in s:
                temp = 1
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                ch_r = int(input("수정할 과목의 번호를 입력하세요 >"))
                if ch_r == 1:
                    print(f"현재 입력된 {name_r} 학생의 국어성적은 {s[2]}입니다.")
                    s[2] = int(input("수정할 국어성적을 입력하세요 >"))
                    s[5] = s[2] + s[3] + s[4]
                    s[6] = s[5] / 3
                    print("수정이 완료되었습니다.")
                elif ch_r == 2:
                    print(f"현재 입력된 {name_r} 학생의 영어성적은 {s[3]}입니다.")
                    s[3] = int(input("수정할 영어성적을 입력하세요 >"))
                    s[5] = s[2] + s[3] + s[4]
                    s[6] = s[5] / 3
                    print("수정이 완료되었습니다.")
                elif ch_r == 3: 
                    print(f"현재 입력된 {name_r} 학생의 수학성적은 {s[4]}입니다.")
                    s[4] = int(input("수정할 수학성적을 입력하세요 >"))
                    s[5] = s[2] + s[3] + s[4]
                    s[6] = s[5] / 3
                    print("수정이 완료되었습니다.")
        if temp == 0:
            print(f"{name_r} 학생을 찾지 못했습니다.")
                            
    elif choice == 4:
        print("[ 학생성적 삭제 ]")
        name_d = input("삭제할 학생의 이름을 입력하세요 >")
        for s in stuS:
            if name_d in s:
                print(f"{name_d} 학생을 찾았습니다.")
                print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
                ch_d = int(input(f"{name_d} 학생의 정보를 삭제하시겠습니까? 1. 예 / 2. 아니오 >"))
                if ch_d == 1:
                    del s           # 작동 안함 다시 작성
                    print(f"{name_d} 학생의 정보가 삭제되었습니다.")
                
        
        
        
    elif choice == 0:
        pass
        