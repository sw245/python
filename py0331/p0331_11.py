## 1~25 2차원 리스트로 출력

import random

# 1. 랜덤 리스트 만들기
ranList = [i+1 for i in range(25)]
random.shuffle(ranList)

# 2. 2차원 리스트 만들기, 초기화 
d_list = [[0]*5 for i in range(5)]

# 3. 넣기

for i in range(5):
    for j in range(5):
        d_list[i][j] = ranList[i*5 + j]

while True:
    # 4. 출력
    print(" "*15,end="")
    print("[ 좌표 맞추기 프로그램 ]")
    print("-"*50)
    print(f"*ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*50)
    for i in range(5):
        print(f"{i}ㅣ",end="\t")
        for j in range(5):
            print(d_list[i][j],end="\t")
        print()


    # 5. 좌표 맞추기 입력

    num = int(input("숫자를 입력하세요 >"))
    for i in range(5):
        for j in range(5):
            if d_list[i][j] == num:
                d_list[i][j] = "X"
