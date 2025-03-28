# 반복문을 사용해서 1부터 10까지 출력

# for i in range(1,11):
# #     print(i)
    
# a = "안녕하세요"
# print(a[3])
# print(a[:3])
# print(a[:4])
# print(a[::-1])
# print(a[:-1])
# print(a[::2])

# print(len(a))
# print(len(a[:3]))

sum = 0
# for i in range(1,100+1):
#     sum = sum + i 
#     print(f"i:{i}, sum:{sum}")
    
# print("1부터 100까지의 합계 : {}".format(sum))

# 합계가 100을 넘는 순간의 수는 어디인지 출력

i = 0

for i in range(1,100+1):
    sum = sum + i
    if sum >= 100:
        print(f"100을 넘는 i의 값 : {i}, 합계 : {sum}")
        break
        
        