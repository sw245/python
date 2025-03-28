
# 000~999 출력

# for i in range(1,1000):
#     print(f"{i:03d}")

# 구구단 출력
# 2 X 1 = 2

# 가로
for i in range(2,9+1):
    for j in range(1,9+1):
        print(f"{i} X {j} = {i*j}",end="\t")    
    print()

print()
    
#세로    
for n in range(1,9+1):
    for k in range(2,9+1):
        print(f"{k} X {n} = {k*n}",end="\t")
    print()