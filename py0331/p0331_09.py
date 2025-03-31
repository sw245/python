
# 초기화 선언
stuS = list()
count = 1

# 프로그램 시작
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
    print("0. 프로그램 종료")
    print("-"*30)
    
    # 번호 입력
    choice = int(input("원하는 번호를 입력하세요 >"))
    print()
    
    # 원하는 프로그램 실행
    if choice == 1:
        print("[ 학생성적 입력 ]")
        name = input("이름을 입력하세요 >>")
        kor = int(input("국어성적을 입력하세요 >"))
        eng = int(input("영어성적을 입력하세요 >"))
        math = int(input("수학성적을 입력하세요 >"))
        sum = kor + eng + math
        avg = sum / 3
        rank = 0
        stu = [count,name,kor,eng,math,sum,avg,rank]
        stuS.append(stu)
        count += 1
        
    elif choice == 2:
        print(" "*30,end="")
        print("[ 학생성적 출력 ]")
        print("-"*65)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*65)
        for stu in stuS:
            for i,s in enumerate(stu): 
                if i != 6:
                    print(s,end="\t")
                else:
                    print(f"{s:.2f}",end="\t")
            print()
    elif choice == 3:
        print("[ 학생성적 수정 ]")
    elif choice == 4:
        print("[ 학생성적 삭제 ]")
    elif choice == 5:
        print("[ 학생성적 정렬 ]")
    elif choice == 6:
        print("[ 학생성적 검색 ]")
    elif choice == 0: break
    else: print("잘못된 입력입니다.")
    
