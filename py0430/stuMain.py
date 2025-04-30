
## 학생성적 프로그램

import json

with open("py0430/stuData.txt","r",encoding="utf-8") as f:
    stu_list = f.read()
    stuS = json.loads(stu_list)
    
# print(stuS)
# print(type(stuS))
# input()

# stuS = [
#     {"no":1,"name":"홍","kor":100,"eng":70,"math":82,"total":252,"avg":84,"rank":0},
#     {"no":2,"name":"유","kor":80,"eng":94,"math":96,"total":270,"avg":90,"rank":0},
#     {"no":3,"name":"김","kor":56,"eng":87,"math":76,"total":219,"avg":73,"rank":0}
# ]
stu = {}
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
title_eng = ["no","name","kor","eng","math","total","avg","rank"]
# stu_sample = {"no":0,"name":"이름","kor":00,"eng":00,"math":00,"total":000,"avg":00.00,"rank":0}

def stu_renew(n):
    ch_subname = int(input(f"{title[n+1]}점수를 변경합니다. 새 점수를 입력해주세요 >"))
    stu[f"{title_eng[n+1]}"] = ch_subname
    stu[f"{title_eng[-3]}"] = stu[f"{title_eng[2]}"] + stu[f"{title_eng[3]}"] + stu[f"{title_eng[4]}"]
    stu[f"{title_eng[-2]}"] = stu[f"{title_eng[-3]}"] / 3
    print("성적 변경이 완료되었습니다.")


# stu["no"]=1
# print(stu["no"])

while True:
    # 초기화면
    print("-"*30)
    # print(" "*15,end="")
    print(" [ 학생성적 프로그램 ] ")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 등수처리")
    print("5. 학생성적 저장")
    print("6. 학생성적 삭제")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 선택하세요."))
    
    if choice == 1:
        print("[ 학생성적 입력 ]")
        no = 4      # 디버깅 ㄱㄱ
        name = input("성적을 입력할 학생의 이름을 입력하세요 >")
        kor = int(input("국어성적을 입력하세요 >"))
        eng = int(input("영어성적을 입력하세요 >"))
        math = int(input("수학성적을 입력하세요 >"))
        total = kor + eng + math
        avg = total / 3
        stuS.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":0})
        print("성적 입력이 완료되었습니다.")
        no += 1
        input()
        
    elif choice == 2:
        print(" "*25,end="")
        print("[ 학생성적 출력 ]")
        print("-"*65)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for stu in stuS:
            print(f"{stu["no"]}\t{stu["name"]}\t{stu["kor"]}\t{stu["eng"]}\t{stu["math"]}\t{stu["total"]}\t{stu["avg"]:.2f}\t{stu["rank"]}")
        print("-"*65)
        print()
        input("(아무 키나 입력해 메인 화면으로)")
    
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        ch_r = input("성적을 수정할 학생의 이름을 입력하세요 >")
        temp = 0
        for stu in stuS:
            if ch_r == stu["name"]:
                print(f"{stu["no"]}번 {ch_r} 학생을 찾았습니다.")
                temp = 1
                print("[ 수정과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                ch_sub = int(input("수정할 과목의 번호를 입력해 주세요 >"))
                if ch_sub == 1:
                    stu_renew(1)
                
                elif ch_sub == 2:
                    stu_renew(2)
                    
                elif ch_sub == 3:
                    stu_renew(3)
        input()
                    
        if temp == 0:
            print(f"{ch_r} 학생을 찾지 못했습니다.")
            
    elif choice == 4:
        print("[ 등수 처리 ]")
        for s in stuS:
            rank = 1
            for ss in stuS:
                if s["total"] < ss["total"]:
                    rank += 1
                s["rank"] = rank
                
        print("등수처리가 완료되었습니다.")
        input()
    
    elif choice == 5:
        print("[ 학생성적 저장 ]")
        with open("py0430/stuData.txt","w",encoding="utf-8") as f:
            json_stuS = json.dumps(stuS,ensure_ascii=False)
            f.write(json_stuS)
            print("학생성적 저장이 완료되었습니다.")
            input()
            
    elif choice == 6:
        print('[ 학생성적 삭제 ]')
        del_name = input("성적을 삭제할 학생의 이름을 입력하세요 >")
        temp = 0
        for s in stuS:
            if s['name'] == del_name:
                temp = 1
                del_warn = input("정말로 삭제하시겠습니까? (삭제 y / 취소 n) >")
                if del_warn == 'y':
                    del s   # 디버깅 ㄱㄱ (아마 stuData.txt 때문인 듯)
                    print("삭제가 완료되었습니다.")
                elif del_warn == 'n':
                    break
        if temp == 0:
            print(f"{del_name} 학생을 찾지 못했습니다.")
                    
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break