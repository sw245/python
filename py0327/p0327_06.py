#

# num = 8
# print(0 < num < 7)


# 숫자를 입력받아 월 별 계절 구분 

month = float(input("계절을 알고 싶은 달을 입력하세요 >"))
if month==3 or month==4 or month==5:
    print("봄입니다.")
elif month==6 or month==7 or month==8:
    print("여름입니다.")
elif month==9 or month==10 or month==11:
    print("가을입니다.")
elif month==12 or month==1 or month==2:
    print("겨울입니다.")
else: print("잘못된 입력입니다.")

