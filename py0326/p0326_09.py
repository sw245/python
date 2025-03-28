# 이름, 국어성적, 영어성적, 수학성적 입력받아 합계, 평균 출력
# 이름 : 
# 합계 :
# 평균 :   소수점 1자리까지 출력

# name1 = input("이름을 입력하세요. >")


# kor = input("국어성적을 입력하세요. >")
# eng = input("영어성적을 입력하세요. >")
# math = input("수학성적을 입력하세요. >")
# sci = int(input("과학성적을 입력하세요. >"))

# kor = int(kor)
# eng = int(eng)
# math = int(math)

# sum = kor+eng+math+sci


# print("이름 :",name1)
# print("합계 :",sum)
# print("%s : %.1f" % ("평균",sum/4))

# print("안녕하세요. \n반갑습니다. \t 저는 홍길동이라고 ㄴㅇㅁㄴ")

a = 10
b = 5
print("%d / %d = %.2f" % (a,b,a/b))
str_print = "{} / {} = {:.2f}".format(a,b,a/b)
print(str_print)

str_print2 = f"{a} / {b} = {(a/b):.2f}"
print(str_print2)