# 1. 숫자 두 개를 입력받아서 사칙연산 값을 출력 (수식까지) format 함수 사용
# 2. 국어 영어 수학 점수 입력받아 출력, 합계 평균 값 출력 (합계 : 221)

a = int(input("숫자를 입력하세요 >"))
b = int(input("숫자를 하나 더 입력하세요 >"))

str_print1 = f"{a} + {b} = {a+b}"
str_print2 = f"{a} - {b} = {a-b}"
str_print3 = f"{a} * {b} = {a*b}"
str_print4 = f"{a} / {b} = {a/b}"

#1.
print(str_print1)
print(str_print2)
print(str_print3)
print(str_print4)


kor = int(input("국어점수를 입력하세요 >"))
eng = int(input("영어점수를 입력하세요 >"))
math = int(input("수학점수를 입력하세요 >"))

sum = kor+eng+math

# str_print5 = f"국어 : {kor}"            
# str_print6 = f"영어 : {eng}"           
# str_print7 = f"수학 : {math}"
# str_print8 = f"합계 : {sum}"
# str_print9 = f"평균 : {(sum/3):.2f}"

str_print5 = "국어 : {}".format(kor)
str_print6 = "영어 : {}".format(eng)
str_print7 = "수학 : {}".format(math)
str_print8 = "합계 : {}".format(sum)
str_print9 = "평균 : {:.2f}".format(sum/3)


#2.
print(str_print5)
print(str_print6) 
print(str_print7)
print(str_print8)
print(str_print9)


