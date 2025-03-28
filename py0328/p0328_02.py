# 반복문 명령어 for

for i in range(1,11,2):
    print(i,end=",") # end="" 줄바꿈 없이 출력
    

# range() 대신에 list타입 변수를 쓰기도 함 
a_list = [1,2,3,4,5]
for j in a_list:
    print(j)