# import math
# import random

# # 0.0000000000000 <= x < 1.000000000000000
# print(random.random())

# # 1부터 45까지 숫자 중 1개를 랜덤으로 추출 randint(a,b) >> b 포함!!!!!
# print(random.randint(1,45))

# # 리스트에서 무작위로 1개 추출
# a_list = [1,2,3,4,5]
# print(random.choice(a_list))


# # 리스트에서 개수만큼 랜덤 추출 - 중복 없이
# print(random.sample(a_list,3))  

# # 리스트 순서를 랜덤으로 섞기
# random.shuffle(a_list)
# print(a_list)


# 카드 모양 SPADE:4, DIAMOND:3, HEART:2, CLOVER:1
# 번호 1-A,2~10,11-J,12-Q,13-K

# 카드 1장에는 카드 모양과 번호가 있음
# 모양 - 4개, 번호 - 13개 >> 총 52장의 카드

# 리스트 - 딕셔너리 형태에 입력
# cardList = [
#     {"shape":"SPADE","no":1},{"shape":"SPADE","no":2},{"shape":"SPADE","no":3},
# ]

import random
cardList = []
cardShape = ["CLOVER","HEART","DIAMOND","SPADE"]
cardNum = ["",'A','2','3','4','5','6','7','8','9','10','J','Q','K']
# 11-J, 12-Q, 13-K, 1-A


# 카드 생성
for i in range(52):
    cardList.append({'shape':i//13,'no':(i%13)+1})

# 카드 랜덤으로 섞기
random.shuffle(cardList)        

# 카드 5장씩 배분
myCard = []
urCard = []

for i in range(5):
    myCard.append(cardList[i])
for i in range(5,9+1):
    urCard.append(cardList[i])


def card_print(List):
    for i in List:
        print(f"[ {cardShape[i['shape']]}, {cardNum[i['no']]} ]")


# 카드 출력
card_print(myCard)
print("vs")
card_print(urCard)

print(myCard)
print(urCard)

# 비교 출력

myWin = []
urWin = []
noWin = []
score = {"myWin":0,"urWin":0,"noWin":0}

# score = [0]*5


for i in range(5):
    if myCard[i]['no'] > urCard[i]['no']:
        score['myWin'] += 1
        myWin.append(myCard[i])
    elif myCard[i]['no'] < urCard[i]['no']:
        score['urWin'] += 1
        urWin.append(myCard[i])
    else:
        score['noWin'] += 1
        noWin.append(myCard[i])
    

# for i in range(5):
#     if myCard[i]['no'] > urCard[i]['no']:
#         score[i] = 2
#     elif myCard[i]['no'] < urCard[i]['no']:
#         score[i] = 1
#     else:
#         score[i] = 0
      
    
        
print(f"나의 승리: {score['myWin']}, 나의 패배 : {score['urWin']}, 무승부 : {score['noWin']}")        

# print(f"승리: {score.count(2)}, 패배: {score.count(1)}, 무승부: {score.count(0)})


        
# 승리 카드, 패배 카드, 무승부 카드 출력

print("승리한 카드")
card_print(myWin)
print()
print("패배한 카드")    
card_print(urWin)
print()    
print("무승부 카드")    
for i in noWin:
    if noWin == []:
        print("없음")
    else:
        print(f"[ {cardShape[i['shape']]}, {cardNum[i['no']]} ]")


# print("[ 승리한 카드 ]")
# for i,c in enumerate(myCard):
#     if score[i] == 2:
#         print(f"[ {cardShape[c['shape']]}, {cardNum[c['no']]} ]",end=", ")
    




# # 카드 전체 출력    
# for c in cardList:
#     print(c['shape'],c['no'])

    

    
        
        




# a = 3.141592
# b = 3.515826



# # a의 소수점 셋째 자리에서 올림해서 둘째 자리까지 출력
# a * 100                     # 314.1592
# math.ceil(a*100) / 100

# # b의 소수점 다섯째 자리에서 올림하여 넷째 자리까지 출력
# print(math.ceil(b*10000) / 10000)

# # math모듈 안에 있는 함수를 모두 출력
# print(dir(math))



# # 올림
# print(math.ceil(a))         # 4
# # 반올림
# print(round(a))             # 3
# print(round(b,3))           # 반올림해서 소수점 셋째 자리까지 표기: 3.516
# print(round(a,4))           # 반올림해서 소수점 넷째 자리까지 표기: 3.1416
# # 버림
# print(math.floor(a))        # 3
# print(math.floor(b))        # 3

