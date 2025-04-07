

class Student:
    # 인스턴스 변수 - 객체선언 시 각각의 객체에 할당되는 변수.
    # no = 1
    # name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0.0
    # rank = 0
    count = 1
    
    # 생성자 함수
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3
        self.rank = 0
        Student.count += 1      # 모든 객체가 공용으로 사용함

    def __str__(self):          # 특별함수 (오버라이딩??)
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"

class Students:
    def __init__(self):
        self.students = []
        
    def add(self,s):
        self.students.append(s)
        
    def __str__(self):      # 리턴이 무조건 문자열
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""
    
    
# ss = Students()
s1 = Student("홍길동",100,100,99)
s2 = Student("유관순",90,90,91)
s3 = Student("이순신",80,80,89)
# ss.add(s1)
# ss.add(s2)
# ss.add(s3)



# # s = Student()
# # s.name = "홍길동"       # 참조변수. ?? ## 기본 생성자 활용
# # print(s.no,s.name)      
    
# # s2 = Student()
# # s2.no = 2
# # s2.name = "이순신"

# s3 = Student("홍길동",100,100,95)       # 매개변수가 있는 생성자 객체선언
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math,Student.count)
# # print(s)
# print(Student.__str__(s3))


# s4 = Student("유관순",100,94,90)
# print(s4.no,s4.name,s4.kor,s4.eng,s4.math,Student.count)