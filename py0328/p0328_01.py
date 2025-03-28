# 파이썬 타입
# bool타입, 숫자-- int타입, float타입, str타입

# if True:
#     print("참입니다.")
    
# if False:
#     print("거짓입니다.")
#  >> 출력되지 않음

# print("안녕" + 1)     >> 에러, 타입이 다름

# print("%s : %.2f" % ("소수점 둘째 자리까지 나타나는 실수",10/3))

# 실수형을 정수형으로 타입 변경 시 소수점 사라짐(버림) 
# print(int(1.9)) >> 1

# list타입 : 여러 값을 한 군데(같은 공간은 아님)에 모아 둠

# listA = [1,2,3,4]

# print(listA)
# print(listA[0],listA[3])

# input() : 데이터를 입력받는 함수 --str타입!!!!
# 두 수를 입력받아 합계, 평균을 출력

# num1 = int(input("숫자를 입력하세요 >"))
# num2 = int(input("숫자를 하나 더 입력하세요 >"))

# print(f"합계 : {num1+num2}")
# print(f"평균 : {(num1+num2)/2}")

# # if
score = int(input("점수를 입력하세요 >"))
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")

