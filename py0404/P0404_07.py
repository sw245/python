# 파일 읽어오기

# 1. open           ㄴ// mode "r":읽기, "w":쓰기, "a":이어쓰기
# 2. f.read()
# 3. f.close()


f = open("py0404/stu_list.txt","r",encoding="utf-8")
students = []

# 여러줄이면 1줄의 반복문을 실행
while True:
    data = f.readline()
    if not data: break
    s = data.strip().split(",")
    students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})
    
print(students)
    
f.close()