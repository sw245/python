
# while문

# i = 0
# while i < 10:
#     print(i)
#     i += 1
    
# print("-"*30)

# for j in range(10):
#     print(j)

# listIn = [1,5,10,9,8,20]

# a = 5
# if a in listIn:
#     print(f"{a}은(는) 존재합니다.")
# else:
#     print(f"{a}이(가) 존재하지 않습니다.")

# 입력한 숫자를 5번 반복해서 리스트에 추가하는 프로그램 만들기

numList = []

# for i in range(10):
#     numIn = int(input("숫자를 입력하세요 >"))
#     if not(numIn in numList):
#         numList.append(numIn)
    

while len(numList) < 10:
    numIn = int(input(f"{len(numList)+1}번째 숫자를 입력하세요 >"))
    if not(numIn in numList):
        numList.append(numIn)
    
print(numList)