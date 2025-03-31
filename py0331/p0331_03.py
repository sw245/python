
# 5 X 5 리스트 - 0으로 초기화

sampleList = list()  # 초기화: 데이터를 빈공간으로 만들기
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(0)
    sampleList.append(temp)
    
print(sampleList)






# # 번호 섞어서 2차원 리스트 생성하기
# import random
# # 1. 순차 리스트 생성
# sample_list = [i+1 for i in range(25)]
# # 2. 랜덤 셔플
# random.shuffle(sample_list)
# # 3. 2차원 초기화 리스트 생성
# a_list = [[0]*5 for j in range(5)]      # 5 X 5 리스트 0으로 초기화2

# # 4. 2차원 리스트에 랜덤 리스트의 값 입력
# for k in range(5):
#     for l in range(5):
#         a_list[k][l] = sample_list[(5*k)+l]

# print(a_list)



# # 5 X 5 리스트 출력
# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j],end="\t")
#     print()


# 5X5 리스트 초기화
# A_list = [[0]*5 for i in range(5)]  # 깊은 복사

# for i in range(5):
#    for j in range(5):
#        A_list[i][j] = 5*i + (j+1)

# print(A_list)


# import random

# a_list = [i+1 for i in range(25)]
# random.shuffle(a_list)  # 랜덤으로 섞인 리스트 출력




# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# (생략)
# 21 22 23 24 25


# list_d = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]


## for a in range(25):

    


# for i in range(5):
#     for j in range(5):
#         print(list_d[i][j],end=" ")
#     print()



# # 1차원 리스트
# aa = [10,20,30]
# print(aa[0])  # 10

# # 2차원 리스트
# bb = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(bb[0])    # [1,2,3,4]
# print(bb[0][0]) # 1


# a_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(a_list)

# for i in range(3):
#     for j in range(3):
#         print(a_list[i][j],end="\t")
#     print()



# # 역순 출력
# a_list = [1,2,3,4,5]
# print(a_list[::-1])


# # 리스트 값 지정
# a_list[2] = 7
# print(a_list)

# # 값을 변경할 때는 [1:2]에서 2의 위치값이 포함
# a_list[1:2] = [100,200]
# print(a_list)


# # 모양 출력
# for n in range(10):
#     print("*"*n)


# for i in range(10):
#     for j in range(i):
#         print("*",end="")
#     print()




# continue 키워드

# for i in range(10):
#     if i % 2 == 0: continue
#     print(i)



# 입력한 숫자의 합이 50이 넘으면 프로그램을 종료하고 총합을 구하시오.
# 입력한 숫자 중 5의 배수는 제외시킬 것.

# sum = 0

# while sum < 50:
#     inNum = int(input("숫자를 입력하세요 >"))
#     if inNum % 5 != 0: 
#         sum += inNum
#     else: print(f"입력한 숫자: {inNum} / 5의 배수는 제외합니다.")
        
# print(f"5의 배수를 제외한 숫자의 총합 : {sum}")








# # 1-100까지의 숫자의 합을 구할 때 합계가 200을 넘을 때의 숫자를 출력하시오

# sum = 0
# # n = 0 >> for문의 변수는 따로 지정할 필요 없음?? 파이썬에서는!!! 가능

# for n in range(1,100+1):
#     sum += n
#     if sum >= 200: break
    
# print(f"200을 넘을 때의 숫자 : {n}")
# print(f"200을 넘을 때의 합계 : {sum}")


# # 200 이전의 값
# print(f"200 이전의 숫자 : {n-1}")
# print(f"200 이전의 합계 : {sum-n}")




# a_list = [i+1 for i in range(100)]
# # print(a_list)

# # a_list에서 홀수의 합계를 구하시오

# sum = 0
# for i in a_list:
#     if i % 2 == 1:
#         sum += i
# print(f"홀수 합계 :",sum)        





# import random

# # random.random() 함수 : 0<=x<1 사이의 랜덤실수를 가져옴
# print(random.random())  #0.00000000000000~(18자리) <= x < 1.0000000000000000~
# print(int(random.random()*10)+1)  # print(random.randint(1,10))
# print(int(random.random()*10)+0) # 0~9



# a_list = [i+1 for i in range(45)]
# print(a_list)

# random.shuffle(a_list)
# print(a_list[:6])
# 이런 식으로도 랜덤샘플 구할 수 있음 >> 샘플 로직이 이런 식?


# 로또 프로그램
# 6개 랜덤숫자, 입력숫자 출력

# import random

# lotto = random.sample(range(1,45+1),6)

# # lotto = []
# # i = 0
# # while i < 6:
# #     ranNum = random.randint(1,45)
# #     if ranNum not in lotto:
# #         lotto.append(ranNum)
# #         i = i + 1

# my_input = []

# while len(my_input) < 6:
#     inNum = int(input(f"1부터 45까지의 숫자 중 6개를 입력하세요 {len(my_input)}/6 >"))
#     if inNum not in my_input:
#         my_input.append(inNum)
        
# print(f"로또번호 : {lotto}")
# print(f"입력숫자 : {my_input}")



# hitLotto = []

# for n in range(6):
#     if my_input[n] in lotto:
        






# 10번의 숫자를 입력받아, 합계를 구하시오.
# for문으로, while문으로



# sum = 0

# for i in range(10):
#     inNum = int(input(f"합계를 구할 숫자를 입력하세요 {i+1}/10 >"))
#     sum = sum + inNum  # sum += inNum 와 같음
# print(sum)
    

# sum2 = 0 
# i = 0
# while i < 10:
#     inNum2 = int(input(f"합계를 구할 숫자를 입력하세요 {i+1}/10 >"))
#     sum2 = sum2 + inNum2
#     i = i + 1
# print(sum2)







# while문


# for문과 비슷하게 사용
# i = 0 
# while i < 10:
#     print(i)
#     i = i+1


# for문

# for i in range(10):
#     print(i)


