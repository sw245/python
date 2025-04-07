
# 파이썬 - 파일 구성 : 다른 타입형태를 넣을 수 있다는 장점이 있음

# 변수 >> 배열(같은 타입) >> 구조체(다른 타입) >> 객체(클래스)-변수, 함수를 같이 담을 수 있는 형태
# *객체 지향 언어 - 고급 언어

# 클래스
#  - 변수, 함수를 모두 포함할 수 있음
#  - 변수에 대한 값을 확인하고 비교할 수 있음 >> 유지보수 편리
###  - 캡슐화 : 변수에 직접 접근하는 것을 막을 수 있음 

# stu = [1,"홍길동",100,100,100,300,100.0,1]
# while True:
    
#     print("1. 학생 출력")
#     choice = int(input("원하는 번호를 입력하세요 >"))
#     if choice == 1: 
#         print(stu)


# 관용적으로 클래스는 첫글자를 대문자로 사용 (권장 사항)
# 설계도 ?
class Stu:
    # 생성자 - 클래스가 선언될 때 데이터를 받아서 변수에 저장해주는 함수
    def __init__(self,no,name,kor,eng,math,total,avg,rank):
        self.no = no            # 클래스 안에 변수 선언
        self.name = name
        if 0 <= kor <= 100:
            self.kor = kor
        self.__eng = eng        # >> eng에 대한 직접 접근을 막음
        self.math = math
        self.total = total
        self.avg = avg
        self.rank = rank
        
        
s = Stu(1,"홍길동",100,100,100,300,100.0,1)

print(s.no)

s.eng = 200
print(s.eng)




# 클래스 선언 후, 변수 선언을 해서 사용 가능
class Stu:
    pass

s = Stu()               # 클래스 선언
s.no = 1                # 변수 선언
s.name = "홍길동"       
s.kor = 100
s1 = Stu()

print(s.no)