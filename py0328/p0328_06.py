# 숫자 맞추기 프로그램

import random

# random.randint(1,45) 1~44까지의 숫자 중 1개를 무작위로 가져옴

lotto = random.randint(1,45)
listIn = []

for i in range(1,10+1):
    numIn = int(input(f"{i}번째 시도: 1부터 44까지의 숫자 중 하나를 입력하세요 >"))
    listIn.append(numIn)
    if lotto == numIn:
        print("당첨입니다.")
        break
    elif lotto > numIn:
        print(f"틀렸습니다. {numIn}보다 큰 수를 입력하세요.")
    else:
        print(f"틀렸습니다. {numIn}보다 작은 수를 입력하세요.")
        
print(f"랜덤번호 : {lotto}")
print(f"입력한 번호 : {listIn}")