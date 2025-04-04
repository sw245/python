

# with 파일

with open("py0404/a1.txt","w",encoding="utf-8") as f:       # f.close 없어도 됨
    f.write("안녕")
    
print("저장 완료")    


# 학생성적 입력 > 파일 쓰기

# f = open("py0404/stu.txt","a",encoding="utf-8")
# count = 1

# while True:
#     no = count
#     name = input("이름을 입력하세요. (0.종료) >")
#     if name == "0": break
#     kor = int(input("국어점수를 입력하세요 >"))
#     eng = int(input("영어점수를 입력하세요 >"))
#     math = int(input("수학점수를 입력하세요 >"))
#     total = kor + eng + math
#     lines = f"{no},{name},{kor},{eng},{math},{total}\n"
#     f.write(lines)
#     count += 1
    
#     f.close                             # 파일 닫아야 저장됨?
#     print("학생성적이 저장되었습니다.")






