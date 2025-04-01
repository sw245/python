
# 1차원 리스트

s_list = [i for i in range(1,25+1)]
# print(s_list)

import random
random.shuffle(s_list)
# random.random(), random.randint(), random.sample(), random.shuffle()
# print(s_list)

# 2차원 리스트
my_list = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        my_list[i][j] = s_list[i*5 + j]


while True:
# 5 X 5 출력
    print(" "*10,end="")
    print("[ 좌표 맞추기 프로그램 ]")
    print("-"*45)
    print("* ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i} ㅣ",end="\t")
        for j in range(5):
            print(my_list[i][j],end="\t")
        print()
    
    # 정지 조건
    list_B = [["X"]*5 for _ in range(5)]
    if my_list == list_B: break        
        
    # 맞추기 프로그램 (숫자)
    inNum = int(input("숫자를 입력하세요 >"))
    stop = 0
    for i in range(5):
        for j in range(5):            
            if  inNum == my_list[i][j]:
                my_list[i][j] = "X"
                stop = 1
                break
        if stop == 1: break

    # 맞추기 프로그램 (좌표)
    # numX = int(input("x좌표를 입력하세요 >"))
    # numY = int(input("y좌표를 입력하세요 >"))
    # stop = 0
    # for i in range(5):
    #     for j in range(5):
    #         if numY == i and numX == j:
    #             my_list[i][j] = "X"
    #             stop = 1
    #             break
    #     if stop == 1: break
    # 이렇게도 됨
    # my_list[numY][numX] = "X"     >> 올바른 좌표값이 아니면 에러
    
# 화면 꾸미기
    # print(" "*10,end="")
    # print("[ 좌표 맞추기 프로그램 ]")
    # print("-"*45)
    # print("* ㅣ",end="\t")
    # for i in range(5):
    #     print(i,end="\t")
    # print()
    # print("-"*45)
    #         print(f"{j} ㅣ",end="\t")
    
# 정지 조건
    # list_B = [["X"]*5 for _ in range(5)]
    # if my_list == list_B: break