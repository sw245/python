
# 파일 이어쓰기 - a (있는 글에 이어 쓰기)
f = open("py0404/memo2.txt","a",encoding="utf-8")
f.write("1,홍길동,100,100,99\n")
f.close()

f = open("py0404/memo2.txt","a",encoding="utf-8")
f.write("2,유관순,50,50,50\n")
f.close()







# # 파일쓰기 - w (모두 삭제 후 다시 쓰기)

print("[메모장]")
print("-------------")
f = open("py0404/memo.txt","w",encoding="utf-8")
while True:
    line = input("저장하려는 글자를 입력하세요. (x를 눌러 종료) >>")
    if line.lower() == "x": break
    f.write(line + "\n")
f.close()



# f = open("py0404/aaa.txt","w",encoding="utf-8")
# # "안녕하세요" 10번 반복해서 저장 
# for i in range(10):
#     f.write(f"{i+1}. 안녕하세요.\n")
# f.close()




# f = open("aa.txt","w",encoding="utf-8")          # 파일 쓰기는 없는 파일을 생성해줌

# f.write("안녕하세요.\n")        #\r : 문장의 끝으로 이동, \n : 줄바꿈
# f.write("반가워요.\n")
# f.close()


print("글쓰기 종료")