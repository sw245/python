

stuS = list()

count = 1
while True:
    name = input("이름을 입력하세요 >>")
    kor = int(input("국어성적을 입력하세요 >"))
    eng = int(input("영어성적을 입력하세요 >"))
    math = int(input("수학성적을 입력하세요 >"))
    sum = kor + eng + math
    avg = sum / 3
    rank = 0
    stu = [no,name,kor,eng,math,sum,avg,rank]
    stuS.append(stu)
    count += 1


    print("                    [ 학생 성적 프로그램 ]")
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



# stuS = [
#     [1,'홍길동',100,100,100,300,100.0,0],
#     [2,'유관순',100,100,100,300,100.0,0],
#     [3,'이순신',100,100,100,300,100.0,0],
# ]

# # stu = [1,'홍길동',100,100,100,300,100.0,0]

# print("                    [ 학생 성적 프로그램 ]")
# print("-"*65)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
# print("-"*65)
# for stu in stuS:
#     for s in stu: 
#         print(s,end="\t")
#     print()