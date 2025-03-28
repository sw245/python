

fruits = ['사과','배','딸기','바나나','멜론']

for i,fruit in enumerate(fruits):
    if i != len(fruits)-1:
        print("{}. {}".format(i+1,fruit),end=" / ")
    else:
        print("{}. {}".format(i+1,fruit))