## 1. 오라클 연결

from stuConn import *

conn = connections()
cursor = conn.cursor()

## 2. 게시판 게시글 등록 board table

# 2-0. 번호 부여
query2 = "select board_seq.nextval from dual"
cursor.execute(query2)
bno = cursor.fetchone()[0]

# 2-1. 게시글 입력
title = input("게시글 제목 입력 >")
content = input("게시글 내용 입력 >>")
id = input("id를 입력하세요 >")

# 2-2. 게시글 db 저장
# bno,btitle,bcontent,id,bgroup,bstep,bindent,bhit,bdate
query1 = "insert into board values(:bno,:btitle,:bcontent,:id,:bgroup,0,0,0,sysdate)"
cursor.execute(query1,bno=bno,btitle=title,bcontent=content,id=id,bgroup=bno)
print("게시글이 등록되었습니다.")

## 3. 파일첨부 bfile table

# 3-1. 리스트로 받기
bfile = []
i = 1
while True:
    ask = input("파일을 첨부하시겠습니까? 예: y / 아니오: (아무 키나 입력)")
    if ask == 'y':
        bfile_in = input(f"{i}번째 첨부할 파일을 입력해 주세요 >")
        i += 1
        bfile.append([bno,bfile_in])
    else: break
    
# 3-2. 파일 첨부 리스트 db에 저장
query3 = "insert into bfile values(:1,:2)"
cursor.executemany(query3,bfile)
print("파일 첨부가 완료되었습니다.")

# 4. 커밋, 종료

conn.commit()
conn.close()