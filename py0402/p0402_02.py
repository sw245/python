
# txt = "안녕하세요"
# a_list = [1,2,3,4,5]

# # 텍스트(문자열)가 입력된 변수는 리스트와 비슷한 성질을 가짐: 
# # index번호를 가짐

# print(txt[1])
# print(a_list[1])

# # 슬라이싱 가능
# print(txt[1:3])     # 녕하
# print(txt[2:])
# print(txt[:3])
# print(a_list[1:3])  # [2,3]

# ##
# print(txt*3)
# print(len(txt))     # 글자길이
# print(txt[::-1])    # 글자 역순 출력


# #문자열

# txt = "abBBcDd"
# print(txt)
# print(txt.upper())      # 모두 대문자로 출력
# print(txt.lower())      # 모두 소문자로 출력
# print(txt.swapcase())   # 대소문자 전환
# print(txt.title())      # 단어 첫글자를 대문자로, 나머지는 소문자로


# txt = "파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt.count("파이썬"))          # 문자열에서 특정 구문의 반복 횟수 출력
# print(txt.count("요"))
# print(txt.find("공부"))             # 특정 문자의 위치(index번호) 출력
# print(txt.find("자바"))             # 없으면 -1

# t = "aaa.py"
# print(t.endswith("py"))             # 특정 구문이 있으면 True, 없으면 False
# print(t.endswith("b"))

# txt = "    안녕 하 세 요 "
# print(txt)
# print(txt.strip())                  # 앞, 뒤 문자를 제거 / 기본은 공백 제거 (중간 문자는 남음)
# print(txt.rstrip())                 # 오른쪽 공백 제거
# print(txt.lstrip())                 # 왼쪽 공백 제거
# print(txt.replace(" ",""))          # 특정 문자를 다른 문자로 치환
# print(txt.replace("안녕","뭐"))

# txt2 = "----파이썬----"
# print(txt2.strip("-"))


# txt.zfill()


# txt3 = "a,b,c,d,안녕,반가워"
# txt3_list = txt3.split(",")      # 괄호 안의 문자로 값을 나눠서 리스트로 저장
# print(txt3_list)


### 데이터베이스(DB)는 리스트를 저장할 수 없음 !! ###
# 그래서 다른 형태로 만들어서 값 변경 ?

# txt4 = "1,홍길동,100,100,100,300,100.0,1"
# txt4_list = txt4.split(",")
# txt4_list[1] = '유관순'
# print(txt4_list)


# txt5 = "1"
# txt6 = txt5.join("안녕하세요")      # 문자열을 괄호 안의 문자열 각 값 사이에 넣어 줌
# print(txt6)


# 문자열

# a = "1234"
# if a.isdigit():     # 정수인지 알려줌: boolean?
#     print("숫자로 가능합니다.")

# my_input = input("숫자를 입력하세요 >")
# if my_input.isdigit():
#     my_input = int(my_input)
# else:
#     print("숫자가 아닙니다. 숫자를 입력하세요.")


print('1234.23'.isdigit())      # 정수인지 확인
print('abc'.isalpha())          # 알파벳인지 확인
print('abc123'.isalnum())       # 글자 또는 숫자인지 확인
print('ABC'.islower())          # 모두 소문자인지 확인
print('abc'.isupper())          # 모두 대문자인지 확인


# # map
# score = ['100','99','90']
# sum = ""
# for s in score:
#     sum = sum + s       # 타입 변환 필요 (덧셈하려면)
# print(sum)    

# s_list = list(map(int,score))       # 모든 요소를 변환
# print(s_list)

# # 함수

# #??? 에러
# def cal(x):
#     return int(x)*100

# s_list = list(cal(score))