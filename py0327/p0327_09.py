## 랜덤

import random

# 0보다 같거나 크고, 1미만인 임의의 실수 값을 뽑아서 전달함
# print(random.random())

# print(random.randint(1,10))

#랜덤한 숫자 맞히기

# ran_num = random.randint(1,5)
# in_num = int(input("랜덤숫자 맞히기: 1부터 5사이의 수를 하나 입력하세요 > "))
# if in_num==ran_num:
#     print(f"{ran_num}입니다. 맞혔습니다.")
# else:
#     print(f"{ran_num}입니다. 틀렸습니다.")
    

# 1-100까지의 숫자 10개를 입력 받고

num = []
# for 반복문
# for n in range(10): #0,1,2,3,4,5,6,7,8,9
#     print(n)
    
ran_num = random.randint(1,100)
n = 0       # 시도 횟수 출력하려고
 

for n in range(1,11):
    in_num = int(input("랜덤숫자 맞히기: 숫자를 입력하세요."))
    num.append(in_num)
    if ran_num == in_num:
        print("정답입니다.")
        break
    elif ran_num>in_num:
        print(f"{in_num}보다 큽니다.")
    else:
        print(f"{in_num}보다 작습니다.")
print(f"도전 횟수 : {n}")
print(f"입력된 숫자 : {num[0]},{num[1]},{num[2]},{num[3]},{num[4]},{num[5]},{num[6]},{num[7]},{num[8]},{num[9]}")
print(f"랜덤 숫자 : {ran_num}")