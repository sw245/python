
# db연결
import oracledb

def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn

## 등수처리 (1,2,3...)
def rankUpdate():
    print("[ 등수처리 ]")
    conn = connections()
    cursor = conn.cursor()
    query2 = """update stuscore a set rank = ( select rank_total from
    ( select sno,rank() over(order by total desc) rank_total from stuscore ) b where a.sno=b.sno)"""
    cursor.execute(query2)
    conn.commit()
    print("등수처리가 완료되었습니다.")
    conn.close()

## 등급처리 (A,B,C...)
def gradeUpdate():
    print("[ 등급처리 ]")
    conn = connections()
    cursor = conn.cursor()
    query3 = """update stuscore s set sgrade = 
        ( select grade from
            ( select sno,grade from stuscore,scoregrade where floor(avg) between minscore and maxscore) g
                where g.sno = s.sno)"""
    cursor.execute(query3)
    conn.commit()
    print("등급처리가 완료되었습니다.")
    conn.close()

## 학생 전체 출력
def stuAllSelect(query='select * from stuscore'):
    conn = connections()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.close()
    
## 학생성적 입력
def stuInsert():
    print("[ 학생성적 입력 ]")
    ## 등급, 등수까지 처리?
    stu_name = input("학생의 이름을 입력하세요 >")
    stu_kor = int(input("국어점수를 입력하세요 >"))
    stu_eng = int(input("영어점수를 입력하세요 >"))
    stu_math = int(input("수학점수를 입력하세요 >"))
    total = stu_math + stu_kor + stu_eng
    avg = total / 3 
    conn = connections()
    cursor = conn.cursor()
    query4 = "insert into stuscore values(stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0,'Z')"
    cursor.execute(query4,name=stu_name, kor=stu_kor, eng=stu_eng, math=stu_math,total=total,avg=avg)
    conn.commit()
    rankUpdate()
    gradeUpdate()
    print("성적 입력 완료")
    conn.close()
    
## 학생성적 검색 - 미완
def stuSearch():
    search = input("검색할 학생의 이름을 입력하세요 >")
    conn = connections()
    cursor = conn.cursor()
    sql = "select * from stuscore where name like '%'||:search||'%'"
    cursor.execute(sql,search = search)
    rows = cursor.fetchall()
    if len(rows) ==0:
        print(f"{search} 학생을 찾지 못했습니다.")
    else:
        for r in rows:
            print(r) 
    
    
    
## 학생성적 정렬
def stuSort():
    print("[ 학생성적 정렬 ]")
    print("1. 이름 순으로 정렬")
    print("2. 점수 합계 순으로 정렬")
    print("3. 국어점수 순으로 정렬")
    print("4. 영어점수 순으로 정렬")
    print("5. 수학점수 순으로 정렬")
    print("9. 번호 순으로 정렬")
    ch_sort = input("원하는 번호를 입력하세요 >")
    if ch_sort == '1':
        ch_desc = input('내림차순 정렬은 1을 입력해 주세요(기본 오름차순) >')
        query_sort = 'select * from stuscore order by name desc' if ch_desc=='1' else 'select * from stuscore order by name asc'
    elif ch_sort == '2':
        ch_asc = input('오름차순 정렬은 1을 입력해 주세요(기본 내림차순) >')
        query_sort = 'select * from stuscore order by total asc' if ch_asc=='1' else 'select * from stuscore order by total desc'
    elif ch_sort == '3':
        ch_asc = input('오름차순 정렬은 1을 입력해 주세요(기본 내림차순) >')
        query_sort = 'select * from stuscore order by kor asc' if ch_asc=='1' else 'select * from stuscore order by kor desc'
    elif ch_sort == '4':
        ch_asc = input('오름차순 정렬은 1을 입력해 주세요(기본 내림차순) >')
        query_sort = 'select * from stuscore order by eng asc' if ch_asc=='1' else 'select * from stuscore order by eng desc'
    elif ch_sort == '5':
        ch_asc = input('오름차순 정렬은 1을 입력해 주세요(기본 내림차순) >')
        query_sort = 'select * from stuscore order by math asc' if ch_asc=='1' else 'select * from stuscore order by math desc'
    elif ch_sort == '9':
        ch_desc = input('내림차순 정렬은 1을 입력해 주세요(기본 오름차순) >')
        query_sort = 'select * from stuscore order by sno desc' if ch_desc=='1' else 'select * from stuscore order by sno asc'
    stuAllSelect(query_sort)
    
    
def stuInfo():
    print("[ 학생정보 출력 ]")
    conn = connections()
    cursor = conn.cursor()
    query5 = "select s.*,id,phone from stuscore s,member m where s.name=m.name"
    cursor.execute(query5)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.close()
    