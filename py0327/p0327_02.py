# 달러 입력 후 원화로 환산 출력
# 1$ >> 1467won

# money = int(input("환산할 금액(달러)을 입력하세요 >"))
# won = money*1467
# print("입력한 금액 : {:,d}달러 / 한화 : {:,d}원".format(money,won))


# 임의의 금액을 동전으로 표현했을 때, 동전의 개수 세기

# money2 = int(input("동전의 개수로 변환할 금액을 입력하세요 >"))
# ch500 = money2//500
# ch100 = (money2%500)//100
# ch50 = ((money2%500)%100)//50
# ch10 = (((money2%500)%100)%50)//10
# ch1 = ((((money2%500)%100)%50)%10)//1
# print(f"""\
#       500원 : {ch500}개
#       100원 : {ch100}개
#       50원 : {ch50}개
#       10원 : {ch10}개
#       1원 : {ch1}개""")

# 원의 넓이 : pi*r**2
# 원의 둘레 : 2*pi*r
# 반지름을 입력받고 원의 넓이와 둘레를 구해서 출력하기

# r = float(input("넓이와 둘레를 구할 원의 반지름을 입력하세요 >"))
# print(f"""\
#     입력한 원의 반지름 : {r}
#     원의 넓이 : {(3.14*(r**2)):.2f}
#     원의 둘레 : {((2*r)*3.14):.2f}""")

# 직사각형의 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오.

# a = float(input("직사각형의 가로 길이를 입력하시오 >"))
# b = float(input("직사각형의 세로 길이를 입력하시오 >"))
# print(f"""\
#     직사각형의 넓이 : {(a*b):.2f}
#     직사각형의 둘레 : {(2*a)+(2*b):.2f}""")

# 직각삼각형

t = float(input("직각삼각형의 밑변의 길이를 입력하시오 >"))
h = float(input("직각삼각형의 높이의 길이를 입력하시오 >"))
S = (0.5*t)*h
l = t+h+((t**2)+(h**2))**(1/2)

print("""
직각삼각형의 넓이 : {:.2f}
직각삼각형의 둘레 : {:.2f}""".format(S,l))

print(((t**2)+(h**2))**(1/2))

