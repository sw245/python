# a1.jpg / a2.jpg
## 게시판 글쓰기



# 1. db연결
from stuConn import *

conn = connections()
cursor = conn.cursor()

## 2. 게시글 작성

title = input("게시글 제목을 입력하세요 >")
content = input("게시글 내용을 입력하세요 >>")
id = input("id를 입력해 주세요 > ")

# 2. bno
query3 = "select board_seq.nextval from dual"
cursor.execute(query3)
bno = cursor.fetchone()[0]

# 3. bfile 컬럼에 a1, a2 저장
bfile = []
i = 1
while True:
    q_more = input("파일을 첨부하시겠습니까? 예: y / 아니오: n >>")
    if q_more == 'n':
        break
    
    bfile_in = input(f"{i}번째 파일 이름을 입력하세요 >")
    i += 1
    bfile.append([bno,bfile_in])

# print(bno)

##
# 4. db에 저장

query2 = "insert into board values (:bno,:btitle,:bcontent,:id,:bgroup,0,0,0,sysdate)"
cursor.execute(query2,bno=bno,btitle=title,bcontent=content,id=id,bgroup=bno)

query = "insert into bfile values (:1,:2)"
cursor.executemany(query,bfile)
print("db 저장 완료")

conn.commit()
conn.close()



