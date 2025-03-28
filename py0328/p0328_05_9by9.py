
# 두 수를 입력받아, 두 수를 포함한 두 수 사이의 모든 수의 합계를 구하기

# num1 = int(input("첫 번째 숫자 >"))
# num2 = int(input("두 번째 숫자 >"))
# if num1 > num2:
#     p = num1; num1 = num2; num2 = p

# sum = 0
# for i in range(num1,num2+1):
#     sum = sum + i
#     print("i:{}, sum:{}".format(i,sum))
    
# print(f"{num1}와 {num2}사이의 모든 수의 합 : {sum}")


# 구구단
num1 = int(input("출력할 구구단의 시작 단 수를 입력하세요 >"))
num2 = int(input("출력할 구구단의 끝 단 수를 입력하세요 >"))
if num1 > num2:
    t = num1
    num1 = num2
    num2 = t

num_100 = []
i_100 = []
j_100 = []

for i in range(num1,num2+1):
    print(f"< {i}단 >")
    for j in range(1,9+1):
        print(f"{i} X {j} = {i*j}",end="\t")
    print()
    print()
    if i*j >= 100:
        num_100.append(i*j)
        i_100.append(i)
        j_100.append(j)

if len(num_100) > 0:
    print("100이 넘는 두 수의 곱들은 다음과 같습니다.")

    for n,num100a in enumerate(num_100):
        print(f"{i_100[n]} X {j_100[n]} = {num_100[n]}")
        
        

