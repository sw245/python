
# 가변 + 키워드 

def cal(*a,b=10):          # b값을 변경하려면 b=n 형태로 지정해야 함, 지정하지 않으면 모든 경우에서 b=10 합산 출력
    result = b
    for i in a:
        result += i
    return result



def cal2(b=10,*a):           # cal2() = 10 빼고는 cal2(*a)와 동일
    result = b
    for i in a:
        result += i
    return result

print(cal2(1))
print(cal(1,2,3,4,5))



# # 키워드 매개변수
# def cal(a,b=10,c=12):                # 키워드 매개변수는 뒤쪽부터 채워야 함
#     return a+b+c

# print(cal(3))



# # 가변 매개변수
# # 대표적인 가변 매개변수 사용 함수 >> print()
# print                                                                                            (1)
# print(1,2)
# print(1,2,3,4,5)


# def cal (*num):             # 전개연산자 (*)
#     result = 0
#     for n in num:
#         result += n
#     return result

# print(cal(1,2))
# print(cal(1,2,3))

# def cal(n1,n2):
#     return n1 + n2

# def cal2(n1,n2,n3):
#     return n1 + n2 + n3

# n1 = 10
# n2 = 20
# n3 = 30
# result = cal(n1,n2)
# print(result)

# result2 = cal2(n1,n2,n3)
# print(result2)



# # global 변수: 전역변수

# def func1():
#     global a        # 전역변수 호출
#     a = 20          

# a = 10

# func1()
# print(a)


# s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}

# # 매개변수 >> 일반변수: 리턴으로 값을 돌려줘서 *****입력시켜야 함******

# print("수정 전 국어점수 :",s['kor'])

# def cal(ss):
#     ss['kor'] = int(input("수정할 국어점수를 입력하세요 >"))
#     ss['total']
#     ss['eng']
#     ss['math']
#     # return kor

# # kor = 100
# # eng = 100
# # math = 100

# # 국어점수 변경 함수
# cal(s)          # 리턴값을 꼭 저장해야 함
# print("수정된 국어점수 :",s['kor'])




# def cal():
#     a_list[0] = 100       # 리스트 주소값이 변경됨
#     a_list[1] = 200

# a_list = [0,0]        # 리스트 타입 변수: 주소값
# a_list[0] = 10
# a_list[1] = 20

# print("함수 호출 전 : a_list",a_list[0],a_list[1])


# cal()
# print("함수 호출 후: a_list",a_list[0],a_list[1])


# # 함수 선언

# def cal(a,b):
#     a = 100     # 지역 변수 - 함수를 벗어나면 사라짐(일반 변수-bool, int, float, string일 때)
#     b = 200
#     return a,b

# # 함수 밖

# a = 10          # 전역 변수
# b = 20
# print("함수 호출 전 a,b:",a,b)

# # 함수 호출
# cal(a,b)
# print("함수 호출 후 a,b:",a,b)




# 입력을 5개만 받아, 짝수만 모두 더한 값을 출력

# def cal(n_list):
#     # n_list = [n1,n2,n3,n4,n5]
#     sum = 0
#     for n in n_list:
#         if n % 2 == 0:
#             sum += n
#     return sum



# # n1 = int(input("숫자 입력 >"))
# # n2 = int(input("숫자 입력 >"))
# # n3 = int(input("숫자 입력 >"))
# # n4 = int(input("숫자 입력 >"))
# # n5 = int(input("숫자 입력 >"))

# n_list = [0]*5
# for i in range(5):
#     n_list[i] = int(input("숫자 입력 >"))


# result = cal(n_list)
# print("짝수의 합 :",result)


# # 직사각형 가로, 세로 입력받아 넓이, 둘레 구하기

# x = int(input("직사각형의 가로 길이를 입력하세요 >"))
# y = int(input("직사각형의 세로 길이를 입력하세요 >"))

# def cal(x,y):
#     S = x*y
#     L = 2*x + 2*y
#     return S,L

# result1,result2 = cal(x,y)
# print(f"넓이 : {result1}, 둘레 : {result2}")



# 이름 국어 영어 수학점수 입력 , 합계 평균 출력

# stuS = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":3}
# ]

# def stu_print():
#     for s in stuS:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")

# print("1. 학생성적 입력")
# print("2. 학생성적 출력")
# choice = int(input("원하는 번호를 입력하세요 >"))
# if choice == 2:
#     stu_print()


# def cal(x,y,z):
#     return (x + y + z),(x + y + z) / 3



# no = 1
# name = input("이름을 입력하세요 >")
# kor = int(input("국어점수를 입력하세요 >"))
# eng = int(input("영어점수를 입력하세요 >"))
# math = int(input("수학점수를 입력하세요 >"))
# total,avg = cal(kor,eng,math)
# print(f"이름 : {name}, 국어 : {kor}점, 영어: {eng}점, 수학 : {math}점")
# print("합계 : {}점, 평균 : {:.2f}".format(total,avg))


# print(cal(1,2,0))





# def add(n1,n2):               # 대부분 실제로 함수에 넣을 변수를 함수 정의에서 사용
#     if n1 > n2:
#         n1,n2 = n2,n1
#     sum = 0
#     for i in range(n1,n2+1):
#         sum += i
#     print(f"{n1}부터 {n2}까지의 합계 :",sum)
    

# n1 = int(input("숫자를 입력하세요 >"))
# n2 = int(input("숫자를 입력하세요 >"))
# add(n1,n2)




# 함수 사용 경우
#  1. 중복 코드가 있을 때 >> 프로그램을 모두 구현하고, 중복된 것을 함수로 사용
#  2. 소스가 너무 복잡할 때

# def add():
#     return kor + eng + math


# kor = int(input("점수를 입력하세요 >"))
# eng = int(input("점수를 입력하세요 >"))
# math = int(input("점수를 입력하세요 >"))
# total = add()
# avg = total / 3

# print(kor,eng,math,total,avg)