# 로또 프로그램
 
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력 번호 생성
# 당첨번호 확인
# 출력

lotto = [i+1 for i in range(45)]        # 로또 당첨 숫자               
Num45 = [i+1 for i in range(45)]       # 입력을 위해 보여지는 숫자
myNum = []
random.shuffle(lotto)

while True:
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또번호 뽑기")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨 확인")
    print("4. 로또 리스트 모두 확인")
    print("5. 내가 입력한 로또 번호 확인")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 >"))
    

    if choice == 1:
        random.shuffle(lotto)
        print("로또번호가 재설정 되었습니다.")
    elif choice == 2:
        while len(myNum) < 6:
            print("[ 로또번호 입력 ]")
            for i in Num45:
                if i % 7 == 1:
                    print()
                    print(i,end="\t")
                else: 
                    print(i,end="\t")
            print()
            inNum = int(input("원하는 번호를 입력하세요 >"))
            for i in Num45:
                if inNum == i:
                    myNum.append(inNum)
                    Num45[i-1] = "X"
        
    elif choice == 3:
        pass
    elif choice == 4:
        print(lotto)
    else: 
        print("[ 프로그램 종료 ]")
        break
    
    
    
    
    # for i in Num45:
            #     if int(i) % 7 == 1:
            #         print()
            #         print(i,end="\t")
            #     else:
            #         print(i,end="\t")
            # print()
            # inNum = int(input("원하는 번호를 입력하세요 >"))
            # if inNum in Num45:
            #     Num45[inNum - 1] = "X"
            #     myNum.append(inNum)
            # else: 
            #     print("잘못된 번호입니다. 다시 입력해주세요.")s