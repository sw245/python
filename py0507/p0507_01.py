
from stuFunc import *



# ## select
# sql = "select * from stuscore2"
# cursor.execute(sql)

# rows = cursor.fetchall()
# for r in rows:
#     print(r)
    
# conn.close()
# print("종료")


# ## update
# sql = "update stuscore2 set rank=0"
# cursor.execute(sql)
# conn.commit()
# conn.close()


while True:
    print("[ 학생성적 프로그램 ]")
    print("-"*20)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 검색")
    print("4. 학생성적 정렬")
    print("5. 학생정보 출력")   # member, stuscore join해서 id,전화번호 출력
    print("8. 등수처리")
    print("9. 등급처리")
    print("0. 프로그램 종료")
    choice = input("원하는 번호를 입력하세요 >")
    
    if choice == "1":
        stuInsert()
        
    elif choice == "2":
        print("[ 학생성적 출력 ]")
        stuAllSelect()      # 성적 출력
        
    elif choice == "3":
        stuSearch()
        
    elif choice == "4":     # 성적 정렬
        stuSort()
        
    elif choice == "5":
        stuInfo()
        
    elif choice == "8":
        rankUpdate()        # 등수 처리
    
    elif choice == "9":
        gradeUpdate()
        
        
    elif choice == "0":
        print("프로그램 종료")
        break