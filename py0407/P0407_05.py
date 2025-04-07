# 클래스
# 변수와 함수 집합체 - 변수에 대한 그룹핑? kor,eng,math
# 함수까지 sum,avg,rank 묶고 싶음 // list,dict타입으로는 불가
    # 여태까지 sum,avg,rank 처리 - 입력받을 때, 수정할 때 직접 처리
# 특정 데이터 값이 들어왔을 때, 잘못된 데이터는 입력이 안 되게 하기



# json >> 외부데이터 // 클래스 >> 내부 데이터 활용??

class Car:
    def __init__(self,color,tire,door):     # >> 생성자 함수 __init__()
        self.color = color      # self.color: Car 변수, color: 요청변수
        self.tire = tire
        self.door = door
        self.speed = 0
        
    color = "white"
    speed = 0
    tire = 4
    door = 5
    
    # 속도 올리기
    def speedUp(self,s):
        self.speed += s
    def speedDown(self,s):
        self.speed -= s
        
    
        
# # 리스트 선언 및 값 입력
# a_list = [1,2,3,4,5]
# a_list[0] = 50

# print(a_list)

# b_list = a_list     # 얕은 복사
# b_list = [*a_list]  # 깊은 복사


# # 클래스 객체 선언 및 값 입력
# a = Car()
# a.speed = 50        # " 참조변수.변수명 " 으로 호출 가능

# print(a.speed)

# # 클래스 함수 사용 방법 >> " 참조변수.함수명() "
# a.speedUp(20)
# print(a.speed)

# # 클래스 참조변수 추가: 다른 변수로 취급 - 선언하기 (클래스 내용 복사)
# a2 = Car()
# a3 = Car()      # 각각의 변수, 함수가 됨.


# # 클래스 내용 변경 >> 1. 직접 입력 / 2. 생성자
# # color = red, tire = 5, door = 4
# a2 = Car()
# a2.color = "red"
# a2.tire = 5
# a2.door = 4

# # color = blue, tire = 5, door = 5
# a3 = Car()
# a3.color = "blue"
# a3.tire = 5


# 생성자를 활용한 객체선언
c = Car("red",5,4)
c2 = Car("blue",5,5)