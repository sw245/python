
stuS = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
    {"no":3,"name":"이순신","kor":90,"eng":99,"math":98,"total":287,"avg":95.67,"rank":0}
]

students = []

# 1. stu_list.txt 읽어오기
# 2. 딕셔너리 타입으로 형태 변환
# 3. students = []에 넣기

f = open("py0404/stu_list.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    s = line.strip().split(",")
    # students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})
print(s)

f.close()

# for s in students:
#     print(s)

# 1,2,3
# stu.txt

# 1. stuS 리스트를 문자열로 변환
# 2. 파일쓰기 후 문자열 저장


# 1.

# for s in stuS:
#     print(str(s))


# # 2.

# # 내 코드
# f = open("py0404/stu_list.txt","a",encoding="utf-8")
# for s in stuS:
#     f.write(str(s))
#     f.write("\n")


# f.close

# # 쌤 코드
# f = open("py0404/stu_list.txt","a",encoding="utf-8")
# for s in stuS:
#     line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
#     f.write(line)

# print("저장완료")

# f.close




# 1. stu_list.txt 읽어오기
# 2. 딕셔너리 타입으로 형태 변환
# 3. students = []에 넣기

# 1.
f = open("py0404/stu_list.txt","r",encoding="utf-8")
# line = f.readlines()
# line = f.readline()
line = f.read()
# print(list(line))

f.close()