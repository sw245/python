
from stuModule import *

s1 = Student("홍길동",100,60,99)
s2 = Student("유관순",99,70,100)


if s1 == s2:                          # __eq__ 메서드 호출
    print("합계 점수가 같습니다.")
else:
    print("합계 점수가 다릅니다.")

if s1 >= s2:                          # __ge__ 메서드 호출
    print("s1이 더 크거나 같습니다.")
else:
    print("s1이 더 작습니다.")
    
if s1 <= s2:                          # __le__ 메서드 호출
    print("s1이 더 작거나 같습니다.")
else:
    print("s1이 더 큽니다.")


print(s1)       #   __str__ 메서드 호출

# 변수의 if문 비교
# a = 10
# b = 20

# if a > b:
#     print("a가 큽니다.")
# else:
#     print("a가 작습니다.")