
# 5 * 5 2차원 리스트 >> 랜덤으로 1~25까지의 숫자를 넣기

# 1. 1차원 리스트 생성
# 2. 랜덤으로 섞기
# 3. 2차원 리스트 생성
# 4. 2차원 리스트에 1차원 랜덤번호 넣기


import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)  # 변수 지정 필요 없음

a_list = [[0]*5 for i in range(5)]

for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[i*5 + j]

# print(a_list)

# 5. 정사각형 형태 출력
X_list = [["X"]*5 for i in range(5)]
while True:
    print("             [좌표 맞추기 프로그램]    ")
    print("-"*45)
    print("* ㅣ\t",end="")
    for i in range(5):
        print(i,end="\t")
    print()    
    print("-"*45)            
    for i in range(5):
        print(f"{i} ㅣ\t",end="")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()
    print("-"*45)
    if a_list == X_list: break
    
    # a_list[num2][num1] = "X"
    
    # num1 = int(input("x좌표를 입력하세요 >"))
    # if num1 < 1 or num1 > 5:
    #     print("숫자를 잘못 입력하셨습니다. 다시 입력하세요")
    #     continue
    # num2 = int(input("y좌표를 입력하세요 >"))
    # if num1 < 1 or num1 > 5:
    #     print("숫자를 잘못 입력하셨습니다. 다시 입력하세요")
    #     continue
    # a_list[num2][num1] = "X"
    
    
    