
class Student:
    count = 1
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3
        self.rank = 0
        Student.count += 1
        
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"


# s = Student("홍길동",100,100,100)


class Students:
    def __init__(self):
        self.stuS = []
        
    def add(self,stu):
        self.stuS.append(stu)
    
    # def __str__(self):
    #     for s in self.stuS:
    #         return s
        
