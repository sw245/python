
# 파일 입, 출력

# 입력
# read()
# readline()
# readlines()

# 출력
# write()
# writelines()


## 진행 과정

# 파일 열기 > 읽기 및 쓰기 > 파일 닫기

# 1. 파일 열기 - 3가지 모드 : r:읽기모드, w:쓰기모드, a:추가모드 
#                           // b:이진모드-파일 복사할 때 씀
# f = open("a.txt","r")       # >> 읽기모드로 열기
# f = open("a.txt","w")       # >> 쓰기모드로 열기
# f = open("a.txt","a")       # >> 추가모드로 열기


# # 파일읽기 - readlines(): 모두 읽어오기
# f = open("a.txt","r",encoding="utf-8")
# lines = f.readlines()       # 모두 읽어오기
# for line in lines:
#     print(line.strip())
# f.close

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line.strip())


# # 파일 읽기 - 1줄 읽기
# f = open("a.txt","r",encoding="utf-8")      # 파일이 없으면 에러, python(루트 폴더)에 있으면 경로 지정 없이도 읽음
# print(type(f))
# for line in f:              # 모든 줄을 출력하려고 for문 사용
#     print(line.strip())
# # f.close()


# # # 파일 읽어오기 - 절대경로
# # f = open("C:\\workspace/python\\a.txt","r",encoding="utf-8")       # 역슬래시 두 번 또는 슬래시
# f = open("py0404/b.txt","r",encoding="utf-8")       # 폴더 안에 있는 파일 읽기
# for line in f:
#     print(line.strip())
# f.close()


f = open("py0404/news.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()



print("완료되었습니다.")