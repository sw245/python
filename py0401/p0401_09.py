
n_list = []


# dic = {1,3,4,5,6,1}
# students = {"no":1,"name":"홍길동","kor":100}
# for key,value in students.items():      # 키, 밸류 출력
#     print(f"{key} : {value}")
    

# for index,key in enumerate(students):   # 인덱스, 키 출력
#     print(f"{index} : {key}")


# 2개의 리스트를 한 번에 출력할 수 있음.
n_list = ['홍길동','유관순','이순신','강감찬','김구']
t_list = [100,99,89,79,100]

print(list(zip(n_list,t_list)))     # 튜플()로 출력 // 리스트[], 딕셔너리{}
[
    ['홍길동',100],
    ['유관순',99]
]

print(dict(zip(n_list,t_list)))     # 튜플 없이 딕셔너리 타입으로 출력



for n,t in zip(n_list,t_list):
    print(f"{n} : {t}")



# # 리스트 내포 - if 조건문을 넣을 수 있음(한 줄짜리만)
# n_list = [i for i in range(1,50+1) if i%2==1]
# print(n_list)



# # 
# list = [1,2,3,4,5]
# # list2 = ['10,100','10,200','10,300','10,400','10,500']
# # list의 값에 +100 후 *100, 천 단위 표시

# # format함수(f함수) 천 단위 표시
# list2 = [f"{(i+100)*100:,d}" for i in list]         # 암기하면 좋다
# print(list2)


# # list2 = [i+100 for i in list]
# # print(list2)



#---------------------------------
# set >> 중복을 제거해서 키를 확인

# myset1 = {1,2,2,2,3,3,5,5,6,7}
# print(myset1)


# menu_list = ['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','바나나']
# print(set(menu_list))       # list타입을 set타입으로 변경해서 확인