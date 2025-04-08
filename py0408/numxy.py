
# 숫자맞추기 프로그램

num = [[0]*5 for _ in range(5)]

for i in range(5):
        for j in range(5):
            num[i][j] = i*5 + ( j + 1 )

while True:
    print()
    print("[ 숫자맞추기 프로그램 ]")
    print("*","ㅣ","\t",end="")
    for n in range(5):
        print(n,"\t",end="")
    print()
    print("ㅡ"*25)
    for i in range(5):
        print(i,"ㅣ","\t",end="")
        for j in range(5):
            print(num[i][j],end="\t")
        print()
    print()
    
    # # 숫자 직접 입력
    # try:
    #     my_num = int(input("원하는 숫자를 입력하세요. (종료:00) >"))
    #     if my_num == 00:
    #         break
    # except Exception as e:
    #     print(e)
    #     continue
        
    # for i in range(5):
    #     for j in range(5):
    #         if my_num == num[i][j]:
    #             num[i][j] = "X"
        
    # 좌표 입력
    try:
        num_x = int(input("원하는 숫자의 x좌표를 입력하세요. (종료:00) >"))
        if num_x == 00:
            break
        num_y = int(input("원하는 숫자의 y좌표를 입력하세요. (종료:00) >"))
        if num_y == 00:
            break
        num[num_y][num_x] = "X"
    except Exception as e:
        print(e)
        continue