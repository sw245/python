
# a_list = ["52","273","32","파이썬","103"]

# list_number = []
# # 숫자로 변환되는 것만 list_number에 저장하시오.

# # if문
# for a in a_list:
#     if a.isdigit():
#         list_number.append(a)
        
# print(list_number)

# # 예외처리
# for a in a_list:
#     try:
#         a = int(a)
#         list_number.append(a)
#     except:
#         pass
    
# print(list_number)


# try:
#     num = int(input("원의 반지름을 입력하세요 >"))
# except Exception as e:
#     print(e)
# else:               # try 구문에서 에러가 발생하지 않으면 실행
#     print("원의 넓이 :",3.14 * ( num ** 2))         # try 구문에 넣어도 됨
    
    
    
# try:            # 프로그램 구현
#     print(1)
#     print(2)
#     # raise NotImplementedError       # 예외를 강제로 발생시킴
#     raise ZeroDivisionError
#     choice = int(input("숫자를 입력하세요 >"))
#     print(3)
#     print(4)
    
# except Exception as e:         # 에러가 났을 때 실행
#     print(e)
#     print(5)
# else:           # 에러가 나지 않았을 때 실행
#     print(6)
# finally:        # 무조건 실행
#     print(7)


print(1)
print(2)
raise NotImplementedError       # 프로그램이 아직 구현되지 않았음
print(3)