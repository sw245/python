#학생성적 프로그램 국영수 합계 평균

name1 = input("이름을 입력하세요 >")
kor = int(input("국어성적을 입력하세요 >"))
eng = int(input("영어성적을 입력하세요 >"))
math = int(input("수학성적을 입력하세요 >"))
print()
print("-"*85)
print("\t\t\t\t학생 성적 프로그램")
print("-"*85)
print()
print("이름\t\t국어\t\t영어\t\t수학\t\t합계\t\t평균")
print("-"*85)
print(f"{name1}\t\t{kor}\t\t{eng}\t\t{math}\t\t{kor+eng+math}\t\t{((kor+eng+math)/3):.2f}")

