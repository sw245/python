
class Student:
    p_number = ""       # 인스턴스 변수 - 객체 변수
    address = ""
    count = 1           # 클래스 변수로 사용
    
    def __init__(self,name,kor,eng,math):       # 생성자 함수
        self.no = Student.count
        Student.count += 1      # 클래스 변수 사용
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3
        self.rank = 0
    
    def s_print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank)
    
    
    # no = 0
    # name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0.0
    # rank = 0
    
    # def total(self):
    #     self.total = self.kor + self.eng + self.math
        
    # def avg(self):
    #     self.total / 3
    
    
# 객체선언  >>    변수 = 생성자 호출
# no 번호를 부여하지 않음 > 1
s = Student("홍길동",100,100,99)
# no 번호를 부여하지 않음 > 2
s2 = Student("유관순",90,90,91)
s3 = Student("이순신",80,80,88)     # 3번 부여


s3.s_print()
s.s_print()
print(s.total)
print("클래스 변수:",Student.count)

# print("학생:",s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
    