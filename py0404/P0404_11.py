
# 1 파일 불러오기
stuS = []

with open("py0404/stu_list.txt","r",encoding="utf-8") as f:
    stu_list = f.readlines()
    for s in stu_list:
        splist = s.split(",")
        stuS.append({'no':int(splist[0]),'name':splist[1],'kor':int(splist[2]),'eng':int(splist[3]),
                     'math':int(splist[4]),'total':int(splist[5]),'avg':float(splist[6]),'rank':int(splist[7])})
        
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
        
        
# b = "1,2,3,4,5"
# a = b.split(",")
# print(a)
        

# print(stuS)



#초기화면
while True:
    print()
    print("[ 학생성적 프로그램 ]")
    print("-"*25)
    print("1. 학생성적 입력")   # 4
    print("2. 학생성적 출력")   # 2
    print("3. 학생성적 수정")
    print("4. 등수 처리")
    print("5. 학생성적 정렬")
    print("6. 학생성적 삭제")
    print("7. 학생성적 저장")   # 3
    print("0. 프로그램 종료")   # 5
    print("-"*25)
    choice = int(input("원하는 번호를 입력하세요 >"))

    if choice == 1:
        print("[ 학생성적 입력 ]")
        no = max()

    elif choice == 2:
        print(" "*20,end="")
        print("[ 학생성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for s in stuS:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        input("(아무 키를 눌러 이전으로 이동)")
        
    elif choice == 7:
        print("[ 학생성적 저장 ]")
        with open("py0404/stu_test.txt","w",encoding="utf-8") as f:
            for s in stuS:
                stu_line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(stu_line)
        print("[ 저장이 완료되었습니다. ]")
        
    
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
    
    
    
    
    
    # count = max(students,key=lambda x:x['no'])['no']+1  >> 딕셔너리에서 max를 쓰기 위해 람다 사용