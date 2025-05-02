
from stuConn import *

conn = connections()
cursor = conn.cursor()


# query = "select board_seq.nextval from dual"
# cursor.execute(query)
# rows = cursor.fetchone()[0]

# print(rows)

# print("end")



## 시퀀스 번호 생성

cursor = conn.cursor()
query = "select board_seq.nextval from dual"
cursor.execute(query)
bno = cursor.fetchone()[0]

# 여러 파일을 리스트 형태로 저장

bfile = []
bfile.append([bno,'11.jpg'])
bfile.append([bno,'12.jpg'])
bfile.append([bno,'13.jpg'])


# db에 저장

query = "insert into bfile values (:1,:2)"  # (bno,bfile)
cursor.executemany(query,bfile)             # executemany 여러 번 실행
conn.commit()

# 프로그램 종료

print(bfile)
print("프로그램 종료")