
# 1-25 랜덤 리스트 생성

import random

sampleList = [i+1 for i in range(25)]
random.shuffle(sampleList)

# 5*5 '0' 2차원 리스트 생성
aList = [[0]*5 for j in range(5)]


# 초기화 리스트에 랜덤 숫자 리스트 입력
for n in range(5):
    for l in range(5):
        aList[n][l] = sampleList[n*5 + l]

# for n in range(5):
#     for l in range(5):
#         aList[n][l] = random.sample(range(1,25+1),25)[n*5 + l]  # >>> 약간 다름

        
# 5 X 5 배열 출력
while True:
    print("        [좌표 맞추기 프로그램]    ")
    print("0ㅣ",end="")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*40)
    for k in range(5):
        print(f"{k}ㅣ",end="")
        for m in range(5):
            print(aList[k][m],end="\t")
        print()
        
        
    print()
    num1 = int(input("x좌표를 입력하세요 >"))
    num2 = int(input("y좌표를 입력하세요 >"))
    aList[num2][num1] = "X"