# 당첨번호 확인
# 출력

import random
lotto = [i+1 for i in range(45)]
random.shuffle(lotto)
Num45 = [[0]*7 for _ in range(7)]
myNum = []
hitNum = []

while True:
    print()
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가 입력한 번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 >"))
    
    if choice == 1:
        random.shuffle(lotto)
        myNum = []
        hitNum = []
        print("로또번호가 재생성되었습니다.")
        
    elif choice == 2:
        # 번호 사각형 출력
        print()
        print("[ 로또번호 입력 ]")
        for i in range(7):
                for j in range(7):
                    Num45[i][j] = i*7 + j+1
                    print(Num45[i][j],end="\t")
                    if i == 6 and j>=2:
                        break
                print()
        while len(myNum) < 6:
            inNum = int(input(f"1부터 45까지 원하는 번호를 입력하세요 {len(myNum)+1}/6 >"))
            if  inNum < 1 or inNum >45:
                print("잘못된 입력입니다.") 
            elif inNum in myNum:
                print("이미 입력된 번호입니다.")
            print()
            for i in range(7):
                for j in range(7):
                    if inNum == Num45[i][j]:
                        Num45[i][j] = "X"
                        myNum.append(inNum)
                    print(Num45[i][j],end="\t")
                    if i == 6 and j>=2:
                        break
                print()
        print("번호가 모두 입력되었습니다.")
        
    elif choice == 3:
        print()
        print("[ 로또번호 당첨 확인 ]")
        print(f"로또번호 : {lotto[:6]}")
        print(f"나의 번호 : {myNum}")
        for i in range(6):
            for j in range(6):
                if myNum[i] == lotto[j]:
                    hitNum.append(myNum[i])
        print(f"당첨 개수 : {len(hitNum)}")
        print(f"당첨 번호 : {hitNum}")
        
    elif choice == 4:
        print()
        print("[ 로또리스트 모두 확인 ]")
        print(lotto)
        
    elif choice == 5:
        print()
        print("[ 내가 입력한 번호 확인 ]")
        print(f"나의 번호 : {myNum}")
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break