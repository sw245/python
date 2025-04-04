

stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":0}
]


# 리스트 >> sort()로 정렬됨. 기존의 리스트 변경
a_list = [20,50,10,40,90]
a_list.sort()               # 순차 정렬
print(a_list)
a_list.sort(reverse=True)
print(a_list)


# dict타입은 sort() 단독으로 사용 불가
# stuS.sort()
# print(stuS)

# print(stuS)
# print("-"*60)
# stuS.sort(key=lambda x:x['name'])               # 이름으로 순차 정렬
# print(stuS)
# print("-"*60)
# stuS.sort(key=lambda x:x['name'],reverse=True)  # 이름으로 역순 정렬
# print(stuS)

# stuS.sort(key=lambda x:x['total'])              # 합계로 순차 정렬 (점수가 낮은 순)
# print(stuS)
# print("-"*60)
# stuS.sort(key=lambda x:x['total'],reverse=True) # 합계로 역순 정렬 (점수가 높은 순)
# print(stuS)

# # sorted는 기존의 리스트는 유지, 새로운 리스트 생성
# s_list = sorted(stuS,key=lambda x:x['name'])
# print(s_list)
# print("-"*60)
# print(stuS)







# def add(a,b):
#     return a+b

# print(add(10,20))

# def func(a,b,c):
#     return max(a,b,c)              # max() 가장 큰 수 출력


# def 함수명(매개변수) : 
#       return 값

# def func2(a,b):
#     return a+b




### 람다식 lambda: 함수 축약형

# lambda 매개변수:리턴값
# lambda a:a*20

# aList = [1,2,3,4,5]         # list의 모든 값에 제곱해서 다시 리스트 생성하려 함

# # for문 사용
# aaList = []
# for i in aList:
#     aaList.append(i**2)
    
# # 함수 정의
# def func(x):
#     return x**2
# print(list(map(func,aList)))

# # map 함수 : 리스트의 값을 함수에 넣어서 저장
# # map(함수,리스트)           


# # 람다 사용 - func 함수 정의 없이 바로 사용
# print(list(map(lambda a:a**2,aList)))

# map(lambda a:a**2,aList)




# # filter함수 : 리스트에 함수를 적용해서 조건에 맞는 것만 저장
# # filter(함수,리스트)

# aList = [1,2,3,4,5]
# aaList = []
# for i in aList:
#     if i%2 == 0:
#         aaList.append(i)
# print(aaList)        

# # filter함수 사용
# def func(x):
#     if x%2 == 0:
#         return x
    
# bList = list(filter(func,aList))
# print(bList)

# cList = list(filter(lambda a:a%2==0,aList))
# print(cList)