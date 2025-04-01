

stuS = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99.67,2],
    [3,'이순신',90,99,98,287,95.67,3]
]

# stuS = list()
count = 4
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
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요. (0.이전화면 이동) >")
        # 이전화면 이동 로직 구현
        kor = int(input("국어 점수를 입력하세요 >"))
        eng = int(input("영어 점수를 입력하세요 >"))
        math = int(input("수학 점수를 입력하세요 >"))
        total = kor + eng + math 
        avg = total / 3
        rank = 0    # 등수는 나중에
        stuS.append([no,name,kor,eng,math,total,avg,rank])
        count += 1
        print(f"{no}번 {name} 학생성적이 등록되었습니다.")
        print()
    elif choice == 2:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in stuS:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        name_r = input("수정하려는 학생의 이름을 입력하세요 >")
        temp = 0
        for i,s in enumerate(stuS):
            if name_r in s:
                temp = 1
                print(f"{name_r} 학생을 찾았습니다.")
                print("[ 수정하려는 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                print("-"*20)
                ch_r = int(input("수정할 과목의 번호를 입력하세요 >"))
                if choice == 1: 
                    print("[ 국어성적 수정 ]")
                    print(f"현재 입력된 국어점수 : {s[2]}")
                    s[2] = int(input("수정할 국어점수를 입력하세요 >"))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5] / 3
                    print(f"{name_r} 학생의 성적이 수정되었습니다.")
                elif choice == 2:
                    print("[ 영어성적 수정 ]")
                    print(f"현재 입력된 영어점수 : {s[3]}")
                    s[3] = int(input("수정할 영어점수를 입력하세요 >"))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5] / 3
                    print(f"{name_r} 학생의 성적이 수정되었습니다.")
                elif choice == 3:
                    print("[ 수학성적 수정 ]")
                    print(f"현재 입력된 수학점수 : {s[4]}")
                    s[4] = int(input("수정할 수학점수를 입력하세요 >"))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5] / 3
                    print(f"{name_r} 학생의 성적이 수정되었습니다.")
        if temp == 0:
            print(f"{name_r} 학생을 찾지 못했습니다.")
    #     renew = input("수정할 학생의 이름을 입력하세요 >")
    #     for s in stuS:
    #         if renew in s:
    #             renew_n = s
    #             print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))
    #             print("수정할 정보를 선택하세요.")
    elif choice == 4:
        print("[ 학생성적 삭제 ]")
        name_d = input("삭제하려는 학생의 이름을 입력하세요 >")
        for i,s in enumerate(stuS):
            temp = 0
            if name_d in s:
                temp = 1
                print(f"{name_d} 학생을 찾았습니다.")
                ch_d = int(input(f"{name_d} 학생의 성적을 삭제하시겠습니까? 0.취소 / 1.삭제 >"))
                if ch_d == 1:
                    del stuS[i]
                    print(f"{name_d} 학생의 성적을 삭제했습니다.")
                else: print("삭제를 취소했습니다.")
                break       # 반복문을 중지함
        if temp == 0: 
            print(f"{name_d} 학생을 찾지 못했습니다. 다시 입력해주세요.")
        print()
            
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    