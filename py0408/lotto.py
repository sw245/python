#  lotto 프로그램

## int >> try 구문 사용         완



import random

num = [i for i in range(1,45+1)]
show_num = [[0]*7 for _ in range(7)]
my_num = []
lotto_num = []
lotto_hit = []

while True:
    print()
    print("[ 로또 프로그램 ]")
    print("1. 로또번호 생성 및 입력번호 초기화 ")
    print("2. 번호 입력")
    print("3. 결과 출력")
    print("4. 모든 번호 출력")
    print("0. 프로그램 종료")
    try:
        choice = int(input("원하는 번호를 선택하세요 >"))
    except Exception as e:
        print(e)
        continue
    
    if choice == 1:
        random.shuffle(num)
        print("로또번호 생성 및 초기화가 완료되었습니다.")
        my_num.clear()
        lotto_hit.clear()
        for i in range(7):
            for j in range(7):
                show_num[i][j] = 7*i + ( j + 1 )
                if i == 6 and j == 2: break
        lotto_num = num[:6]
        
        
    elif choice == 2:
        while len(my_num) < 6:
            for i in range(7):
                for j in range(7):
                    print(show_num[i][j],end="\t")
                    if i == 6 and j == 2: break
                print()
            try:
                sel_num = int(input(f"1부터 45까지의 숫자를 입력하세요 ({len(my_num)+1}/6) >"))
            except Exception as e:
                print(e)
                continue
            
            my_num.append(sel_num)
            for n in lotto_num:
                if sel_num == n:
                    lotto_hit.append(n)
            for i in range(7):
                for j in range(7):
                    if sel_num == show_num[i][j]:
                        show_num[i][j] = "X"
            print()
        
        print("입력이 완료되었습니다.")
        print("내가 입력한 번호 : {}, {}, {}, {}, {}, {}".format(*my_num))
            
    elif choice == 3:
        print("[ 결과 출력 ]")
        print("-"*30)
        print(" "*10,end="")
        print(f"당첨 개수 : {len(lotto_hit)}")
        print("-"*30)
        print("입력 번호 :, {}, {}, {}, {}, {}, {}".format(*my_num))
        print("로또 번호 : {}, {}, {}, {}, {}, {}".format(*lotto_num))
        print("당첨된 번호 :",*lotto_hit)
        # for n in lotto_hit:
        #     print(n,end=", ")
        
    elif choice == 4:
        print("[ 모든 번호 출력 ]")
        print(num)   
        
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
        
    