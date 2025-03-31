

a_list = [1,2,3,4,5]
a = 10

print("a :",a)
print("a_list :",a_list)

# a 변수와 b 변수는 다른 변수임
b = a
b = 1000
a_list[0] = 100

print("a : ",a)
print("b : ",b)

### 새롭게 복사 : 깊은 복사 (매우 중요)

a_list = [1,2,3,4,5]
b_list = [*a_list]
b_list[1] = 200

print(a_list)
print(b_list)

### 주소값 복사 : 얕은 복사
# a_list, b_list는 다른 리스트인가?
a_list = [1,2,3,4,5]
b_list = a_list

b_list[1] = 200

print(a_list)



# a_list = [1,2,3,4,5]
# sum = 0

# for i in a_list:
#     sum = sum + i
# print(sum)





# 구구단
# "2 X 1 = 2"

# for i in range(2,9+1):
#     print(f"< {i}단 >")
#     for j in range(1,9+1):
#         print(f"{i} X {j} = {i*j}")
#     print()
    
    