
from stuConn import *

conn = connections()

# 게시판 글쓰기
title = input("제목을 입력하세요 >")
content = input("내용을 입력하세요 >")
# 파일첨부
bfile = []
bfile1 = input("첨부할 파일을 입력하세요 >")
bfile2 = input("첨부할 파일을 입력하세요 >")
bfile3 = input("첨부할 파일을 입력하세요 >")
cursor = conn.cursor()
query = "select board_seq.currval from dual"
cursor.execute(query)
bno = cursor.fetchone()
bfile.append([bno,bfile1])
bfile.append([bno,bfile2])
bfile.append([bno,bfile3])

# 여러 개 저장을 하려고 리스트형태로 구성..? 


# query = "insert into board values (board_seq.nextval,:btitle,:bcontent,'aaa',board_seq.currval,0,0,0,sysdate)"
# cursor.execute(query,btitle=title,bcontent=content)


conn.commit()

conn.close()
print("프로그램 종료.")

