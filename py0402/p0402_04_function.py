
## 함수
print()     # 변수 뒤에 ()가 있는 형태

# # 함수 정의
# def cal(x,y):
#     result = x + y
#     print(result)
#     result2 = x - y
#     print(result2)
#     result3 = x * y
#     print(result3)
#     result4 = x / y
#     print(result4)

# a,b = 10,20
# cal(a,b)

# c,d = 100,200
# cal(c,d)

# e,f = 50,100
# cal(e,f)


# def add():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
    

# print("인사")
# add()               # 함수 호출


# def add(x,y):
#     print("x :",x)
#     print("y :",y)
#     print("x + y :",x+y)

# a = 10
# b = 20
# c = 30
# d = 40

# add(a,b)
# add(a,c)
# add(c,d)
# add(b,c)

# 두 수를 입력받아 사칙연산을 출력하시오.

def cal(x,y):
    print("더하기",x+y)
    print("빼기",x-y)
    print("곱하기",x*y)
    print("나누기",x/y)
    return x+y
    
    
num1 = int(input("첫 번째 숫자를 입력하세요 >"))
num2 = int(input("두 번째 숫자를 입력하세요 >"))

num3 = int(input("첫 번째 숫자를 입력하세요 >"))
num4 = int(input("두 번째 숫자를 입력하세요 >"))

num5 = int(input("첫 번째 숫자를 입력하세요 >"))
num6 = int(input("두 번째 숫자를 입력하세요 >"))

result1 = cal(num1,num2)
result2 = cal(num3,num4)
result3 = cal(num5,num6)

result = result1 + result2 + result3
print(result)










# dic = {"no":1,"name":"홍길동"}

# if "홍길동" in dic:     # 키 비교
#     print("있다.")
# else: print("없다.")

# if "홍길동" in dic["name"]:     # 값 비교
#     print("있다.")
# else: print("없다.")