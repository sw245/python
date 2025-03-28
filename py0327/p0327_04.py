# a,b = 100,200
# c = 300; d = 400
# e = 500
# f = 600


# print(a==b)
# print(a!=b)
# print(a>b,a<b,a>=b,a<=b)

# # 조건식
# a = int(input("숫자를 입력하세요 >"))
# if a<100:   # True
#     print("입력한 값은 100보다 작습니다.")
# else:       # False
#     print("입력한 값은 100보다 큽니다.")

# 양수/음수 판별

# input_num = int(input("숫자를 입력하세요 >"))
# if input_num>=0: 
#     print("양수 또는 0입니다.")
# else:
#     print("음수입니다.")
    
# 짝수, 홀수 판별

num = int(input("숫자를 입력하세요 >"))
if num % 2 == 0:
    print("짝수입니다.")
else: 
    print("홀수입니다.")
    
# 3의 배수 판별
    
num3 = int(input("숫자를 입력하세요 >"))
if num3 % 3 == 0:
    print("3의 배수입니다.")
else: 
    print("3의 배수가 아닙니다.")