# 파이썬 변수타입
# 불 bool, 숫자 int, float, 문자열 str

# 출력 print()
# 변수 선언  a = 10

#  print("%d : %s" % (5,"a"))
#  print("{} : {}".format(5,7))
#  print(f"a : {5}")
#  print("a :",5)

# 입력 input() >> 입력받은 데이터는 문자열str 타입
# a = input() 입력받은 데이터를 변수에 저장
# b = input()
# print("입력된 숫자 : a, b")
# a = int(a); b = int(b)
# print("합계 :",a+b)


# a = input("dd")
# b = input("aa")
# print("입력된 숫자 :",a,",",b)

# num1 = int(input("숫자1>"))
# num2 = int(input("숫자2>"))
# print("입력된 숫자 : {}, {} / 합계 : {}".format(num1,num2,num1+num2))


# 학생성적 프로그램
# 이름, 국어점수, 영어점수, 수학점수, 합계, 평균 출력

name1 = input("이름 >")
kor = int(input("국어점수 >"))
eng = int(input("영어점수 >"))
math = int(input("수학점수 >"))
print()
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t{}\t{}\t{}\t{}\t{:.1f}".format(name1,kor,eng,math,kor+eng+math,(kor+eng+math)/3))
print("-"*50)