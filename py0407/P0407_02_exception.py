# 예외처리

# 외부 데이터를 받거나, 클라이언트가 에러를 낼 수 있을 때 주로 사용

# 에러
# 1. 구문에러 
# 2. 런타임 에러

# print("데이터 출력")
# # priint("데이터 출력") >> # 구문에러 - 오타 등 잘못 씀

# a_list = [1,2,3,4,5]
# for a in a_list:
#     print(a)

# for i in range(6):        # 런타임 에러 - 구문에 에러는 없지만 실행 시 에러
#     print(a_list[i])      # >> IndexError
    
# 에러가 나면 프로그램이 멈춤
# >> 을 방지하기 위한 '예외처리'

# # 1. if문 사용

# print("1. 학생성적 출력")
# choice = input("원하는 번호를 입력하세요 >")
# # 숫자로 변환 가능한지 확인
# if choice.isdigit():
#     choice = int(choice)
# else:
#     print("숫자만 입력이 가능합니다.")
# print("입력한 번호 :",choice)


# 2. 예외처리

print("1. 학생성적 출력")
choice = input("원하는 번호를 입력하세요 >")
# 숫자로 변환 가능한지 확인
try:                        # 예외처리: 프로그램이 에러로 종료되는 문제 해결, 에러에 대한 문제점 확인 가능
    choice = int(choice)
except Exception as e:
    print("숫자만 입력이 가능합니다.")
    print(e)                # 에러의 구문 출력 가능
print("입력한 번호 :",choice)
