# 날짜, 시간
# 날짜 클래스

# import datetime

# now = datetime.datetime.now()
# print("현재시간 :",now)

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print()
# print(now.year,"년",now.month,"월",now.day,"일",now.hour,"시",now.minute,"분",now.second,"초")
# print()
# print(now.year,end="")
# print("년",now.month,end="")
# print("월",now.day,end="")
# print("일",now.hour,end="")
# print("시",now.minute,end="")
# print("분",now.second,end="")
# print("초")
# print()
# print(now)

# 시간이 12시 이상이면 오후, 12시 미만이면 오전이라고 출력하시오.
# 13시 > 오후 1시
# 9시 > 오전 9시
# if 조건문 사용

import datetime
now = datetime.datetime.now()
hour = now.hour
minute = now.minute

if hour>13: 
    print(f"오후 {hour-12}:{minute:02d}")
elif hour==12:
    print(f"오후 {hour}:{minute:02d}")
else:
    print(f"오전 {hour}:{minute:02d}")
    
print(f"{now.year}-{(now.month):02d}-{now.day}")
    
