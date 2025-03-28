# 1에서 100까지의 홀수 합계 구하기

# sum = 0

# for i in range(1,100,2):
#     sum = sum + i
    
# print(f"100까지의 홀수 합계 : {sum}")

# 1부터 100까지의 수 중 3의 배수의 합계 구하기

# sum = 0

# for i in range(1,100+1):
#     if i % 3 == 0 and i % 5 == 0:
#         sum = sum + i
#         print("i : {}, sum : {}".format(i,sum))
        
# print(f"3의 배수의 합계 : {sum}")

sum = 0

for i in range(1,100+1):
    if i % 3 == 0 or i % 7 == 0:
        sum = sum + i
        print("i : {}, sum : {}".format(i,sum))
        
print(f"3 또는 7의 배수의 합계 : {sum}")

