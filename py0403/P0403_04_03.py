# 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력
my_lotto = [0]*6
win_lotto = []
lotto = [i+1 for i in range(45)]  # 로또 랜덤번호
lotto2 = [i+1 for i in range(45)] # 로또 순차적번호 출력
def lotto_mix():
    global lotto
    random.shuffle(lotto)
lotto_mix()
while True:
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print('1. 로또프로그램 재실행')
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        lotto_mix()
    elif choice == 2:
        count = 0 # 로또번호 입력개수
        while True:
            print("[ 로또번호입력 ]")
            print("-"*50)
            # 로또번호 순번출력부분------------
            for i in range(45):
                if i%7 != 0: print(lotto2[i],end="\t")
                else:
                    print()
                    print(lotto2[i],end="\t")
            print()
            # ------------------------------
            choice = int(input("로또번호를 입력하세요.(0.이전화면이동)>> "))
            if choice == 0: break
            # 해당로또번호 X표시부분 ----------------
            if choice<0 or choice>45:
                print(f"{choice}번 번호는 없는 번호입니다. 다시 확인해주세요.")
                continue # 재실행
            temp = 0
            for i in lotto2:
                if i==choice:
                    lotto2[i-1] = "X"
                    my_lotto[count] = choice  # append보다 속도가 빠름.
                    count += 1     # 입력로또번호개수 1증가
                    temp = 1       # 로또번호 존재확인변수
            if temp == 0:
                print(f"{choice}번 번호는 입력하신 번호입니다. 다시 입력하세요.")
            if count >= 6:
                print("로또번호 6개를 모두 입력하셨습니다.! ")
                break
    elif choice == 3:
        # 로또당첨확인
        for i in lotto[:6]:
            for j in my_lotto:
                if i == j: win_lotto.append(i)
        print("[ 로또당첨번호 확인 ]")
        print("-"*50)
        print("로또당첨번호 :",lotto[:6])
        print(f"내가입력한 로또번호 : {my_lotto}")
        print(f"당첨된 로또번호 : {win_lotto}")
        print("당첨개수 : ",len(win_lotto))
    elif choice == 4:
        print("[ 로또리스트 모두 확인 ]")
        print(lotto)
    elif choice == 5:
        print("[ 내가입력한 로또번호 확인 ]")
        print(my_lotto.sort())     # reverse=True
    else:
        print("[ 프로그램 종료 ]")
        break