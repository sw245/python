
a = "ㅎㅇㅎㅇ안녕안녕안녕하세요.안녕"

# a.find()
# 왼쪽부터 찾아서 처음 등장하는 위치를 저장

# if "안녕" in a:
#     print("안녕이라는 글자가 있습니다.")
    
    
# print(a.find("안녕"))


##  안녕이 몇 번 나오는지의 개수를 출력

# num = a.count("안녕")
# print(num)


# del a[1]
# print(a)


count = 0

while a.find("안녕") >= 0:
    index_a = a.find("안녕")
    a = a[index_a+1:]
    count += 1
        
print(count)
    
    
# 선생님 방법 : i번째 문자열부터 find함수 적용, 카운트 +1 >> 반복