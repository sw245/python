# with 명령어 사용 시 f.close() 생략

# aStr = "1,홍길동,100,99,199"
# a_list = aStr.split(",")        # list 타입으로 변경해서 전달
# print(a_list)
# print(int(a_list[3])+1)

stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":0}
]


# stu.txt >> 
# 영어성적 +1, 합계 +1 해서 전체 리스트 출력

# 시도한 것
with open("py0404/stu.txt","r",encoding="utf-8") as f:
    for line in f:
        list(line)
        # print(line.strip())
    #     stu_list = line.split(",")
    # print(stu_list)
    
# 받아쓰기
f = open("py0404/stu.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line.strip())
    s = line.strip().split(",")
    
    print("변경 영어 :",{int(s[3])+1})
    print("변경 합계 :",{int(s[4])+1})

    #리스트 수정
    s[0] = int(s[0])
    s[2] = int(s[2])
    s[3] = int(s[3]+1)
    s[4] = int(s[4]+1)
    print("{},{},{},{},{}".format(*s))
    stuS.append({"no":int(s[0]),"name":int(s[1]),"kor":int(s[2]),"eng":int(s[3]),"total":int(s[4])})
f.close




# f = open("py0404/stu2.txt","r",encoding="utf-8")
# line = f.readline()
# a_list = line.strip().split(",")
# print(a_list)
# print(int(a_list[3])+1)
# f.close

# while True:
#     line = f.readline()
#     if not line:
#         break
#     a_list = line.split(",")
    




# with open("py0404/stu.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
        
        
# 모든 학생 영어점수 +2

