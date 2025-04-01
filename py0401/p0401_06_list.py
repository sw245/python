
# 리스트에서 삭제
a_list = [1,2,3,4,5]

del a_list[0]   # index번호를 가지고 삭제
a_list.pop()    # 마지막 데이터 삭제
a_list.pop(2)   # index번호 삭제
a_list.remove(2) # 2라는 값을 삭제
a_list.clear()    # 모두 삭제

# print(a_list)

# 리스트에 추가
a_list.append(1)    # 리스트 마지막에 추가, 데이터 묶음도 추가 가능(리스트 안의 리스트)
a_list.append(2)
a_list.insert(0, "홍길동")  # 0번째 자리에 "홍길동" 추가
a_list.extend([10,11,12])   # 리스트 추가 (뒷부분에)

# print(a_list)

# 리스트 수정
a_list[0] = "유관순"

# print(a_list)

# 리스트 출력
# print(a_list)

for a in a_list: print(a)
# print(a_list)


# 리스트 길이
print(len(a_list))


# 리스트 안의 해당 값의 개수 파악

s_list = [1,2,3,1,2,2,2,1,3,4,5,7,7,7,8,10,9,8]
print("{}:{}".format(1,s_list.count(1)))
print(s_list.count(1))

num = 0
for s in s_list:
    if s == 1:
        num += 1
print(num)        


# 리스트 정렬
s_list.sort()   # 순차정렬, 낮은 순
# print(s_list)

s_list.sort(reverse=True)   # 역순정렬, 높은 순
s_list.reverse()            # 역순정렬, 높은 순
print(s_list)