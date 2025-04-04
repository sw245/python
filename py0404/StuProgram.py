
# import stu_func

# import stu_func as stu                                      # 호출에 별칭 사용
# from stu_func import stu_input,stu_output,stu_print         # 각각의 함수명을 미리 불러옴
from StuFunc import *                                      # 모든 함수 불러오기

    
stuS = []
count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


### 파일 불러오기
# stu.txt 파일에서 데이터를 읽어와 stuS = []에 데이터 입력
with open("py0404/stu_list.txt","r",encoding="utf-8") as f:
    while True:                         # 여러 줄일 때 반복문으로 읽기
        line = f.readline()             # 1줄 읽어오기
        if not line: break              # 읽어오는 데이터가 없을 때 종료
        s = line.strip().split(",")     # 1줄 문자열을 "," 기준으로 분리
        stuS.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })


while True:
    choice = stu_print()                               # 초기화면 출력
    
    if choice == 1:
        count = stu_input(count,stuS)                  # 성적입력
        
    elif choice == 2:
        stu_output(stuS,title)                         # 성적출력
        
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        name_r = input("수정하려는 학생의 이름을 입력하세요 >")
        temp = 0
        print()
        for s in stuS:
            if name_r == s['name']:
                temp = 1
                print(f"{name_r} 학생의 성적을 수정합니다.")
                print("[ 수정과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                ch_r = int(input("원하는 번호를 입력하세요 >"))
                sub_list = ['','kor','eng','math']
                if ch_r == 1:
                    stu_renew(s,sub_list,ch_r,title)
                elif ch_r == 2:
                    stu_renew(s,sub_list,ch_r,title)
                elif ch_r == 3:
                    stu_renew(s,sub_list,ch_r,title)
        if temp == 0:
            print(f"{name_r} 학생을 찾지 못했습니다.")
            
    elif choice == 4:
        stu_rank(stuS)                                  # 등수처리
        
    elif choice == 5:
        stuS2 = [*stuS]                                 # 깊은 복사
        print("[ 학생성적 정렬 ]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면 이동")
        print("-"*30)
        choice = int(input("원하는 번호를 입력하세요 >"))
        if choice == 1:
            stuS2.sort(key=lambda x:x['name'])
        elif choice == 2:
            stuS2.sort(key=lambda x:x['name'],reverse=True)
        elif choice == 3:
            stuS2.sort(key=lambda x:x['total'])
        elif choice == 4:
            stuS2.sort(key=lambda x:x['total'],reverse=True)
        elif choice == 5:
            stuS2.sort(key=lambda x:x['no'])
        elif choice == 6:
            stuS2.sort(key=lambda x:x['no'],reverse=True)
        elif choice == 0:
            continue            
        stu_output(stuS2,title)
        
    elif choice == 6:                                   # 학생성적 삭제
        print("[ 학생성적 삭제 ]")
        name = input("삭제하고자 하는 학생이름을 입력하세요 >")
        temp = 0
        for i,s in enumerate(stuS):
            if name == s['name']:
                temp = 1
                print(f"{s['no']}번 {name} 학생을 찾았습니다.")
                answer = input("학생성적을 삭제합니까? (*삭제 후 복구 불가) y/n >")
                if answer == "y":
                    del stuS[i]
                else:
                    print("삭제를 취소했습니다.")
                    break
                print(f"{name}을 삭제했습니다.")
                break
        if temp == 0:
            print("삭제하려는 학생을 찾지 못했습니다.")
            
    elif choice == 7:                                   # 학생성적 저장
        print("[ 학생성적 저장 ]")
        with open("py0404/stu_list.txt","w",encoding="utf-8") as f:
            for s in stuS:
                line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(line)
        print("학생성적이 파일에 저장되었습니다.")
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break