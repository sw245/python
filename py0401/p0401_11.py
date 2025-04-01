
# score = [0]*3
# print(score)
# score[0] = 100
# print(score)

# 학생성적 프로그램 
# 1. 학생성적 입력 / 2. 출력 / 3. 종료

students = []

# 0. 초기 인터페이스 화면


while True:
    print("[ 학생성적 프로그램 ]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("0. 프로그램 종료")
    choice = int(input("원하는 번호를 선택하세요 >"))

# 1. 학생성적 입력
    count = 1
    if choice == 1:
        print("[ 학생성적 입력 ]")
        while True:
            no = count
            name = input(f"{no}번 학생의 이름을 입력하세요. (0. 이전 화면으로) >")
            if name == "0":
                break
            kor = int(input("국어성적을 입력하세요 >"))
            eng = int(input("영어성적을 입력하세요 >"))
            math = int(input("수학성적을 입력하세요 >"))
            total = kor + eng + math
            avg = total / 3
            rank = 0
            students.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
            count += 1

# 2. 학생성적 출력
    elif choice == 2:
        print("[ 학생성적 출력 ]")
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*students))

