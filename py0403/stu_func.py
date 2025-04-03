
# 초기화면 출력 함수
def stu_print():
    print()
    print("[ 학생성적 프로그램 ]")
    print("-"*25)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 등수 처리")
    print("5. 학생성적 검색")
    print("6. ")
    print("0. 프로그램 종료")
    print("-"*25)
    choice = int(input("원하는 번호를 입력하세요 >"))
    return choice
    
# 성적입력 함수
def stu_input(count,stuS):
    no = count
    name = input(f"{no}번 학생의 이름을 입력하세요 >")
    kor = int(input("국어점수를 입력하세요 >"))
    eng = int(input("영어점수를 입력하세요 >"))
    math = int(input("수학점수를 입력하세요 >"))
    total = kor + eng + math
    avg = total / 3
    rank = 0
    stuS.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
    print(f"{no}번 {name} 학생이 입력되었습니다.")
    count += 1
    return count
    
# 성적출력 함수
def stu_output(stuS,title):
    print(" "*20,end="")
    print("[ 학생성적 출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in stuS:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
    input("(아무 키나 입력해 이전 화면으로) >")
    
# 등수처리 함수
def stu_rank(stuS):
    print("[ 등수처리 ]")
    for s in stuS:
        num = 1
        for ss in stuS:
            if s['total'] < ss['total']:
                num += 1
        s['rank'] = num
    print("등수처리가 완료되었습니다.") 