

import random

# listA =  random.sample(range(1,45+1),6)
# print(listA)



# 랜덤 1~45 숫자 6개 ranList 저장
# 입력받은 숫자 6개를 myList에 저장하기
# 랜덤번호, 입력번호, 당첨개수, 당첨번호 출력
    
    


ranList = random.sample(range(1,45+1),6)
myList = []
lottoList = []

print(f"랜덤번호 : {ranList}")

while len(myList) < 6:
    myNum = int(input(f"1부터 45까지의 숫자를 6개 입력하세요 {len(myList)}/6 >")) 
    if myNum not in myList:
        myList.append(myNum)

for n in range(6):
    if myList[n] in ranList:
        lottoList.append(myList[n])

# for j in range(6):
#     for k in range(6):
#         if ranList[j] == myList[k]:
#             lottoList.append(myList[k])

lottoCount = len(lottoList)

print(f"랜덤번호 : {ranList}")
print(f"입력번호 : {myList}")
print(f"당첨개수 : {lottoCount}")
print(f"당첨번호 : {lottoList}")



#







# ranList = []

# while len(ranList) < 6:
#     ranIn = random.randint(1,45)
#     if not(ranIn in ranList):
#         ranList.append(ranIn)
        
# print(ranList)

