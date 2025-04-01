
a_list = [[1,2,3,4,5],[6,7,8,9,10]]

# 현재 리스트의 X개수 확인
no = 0
for i in range(5):
    if a_list[0][i] == "X":
        no += 1
        
if no == 5:
    print("빙고 완성!")
print(f"현재 [0]번방의 X 개수는 {no}개입니다.")