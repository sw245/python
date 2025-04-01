


# a_list = [1,2,1,2,1,2,1]
# count = 0
# for i in a_list:
#     if i == 1: count += 1
# print(f"개수 : {count}")




x_list = ["x","x",3,"x",5]

while True:
    # 화면 출력
    print(x_list)
    
    # 숫자 입력
    num = int(input("숫자를 입력하세요 >"))
    for i in range(len(x_list)):
        if x_list[i] == num:
            x_list[i] = "x"

    for i in range(len(x_list)):
        if x_list[i] == "x":
            print("빙고 완성!!")
            print(f"완성 개수 : {count_x}")
            break