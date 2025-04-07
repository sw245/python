
class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no = no
        self.__name = name
        self.__kor = kor        # __ 언더바 2개 >> 접근 제한 : 캡슐화
        self.__eng = eng
        
    def __str__(self):      # >> 무슨 함수??
        return f"{self.__no},{self.__name},{self.__kor},{self.__eng}"
        
    # setter :              캡슐화된 변수에 값을 변경할 수 있게 함
    def setKor(self,kor):
        if kor >= 0 and kor <= 100:
            self.__kor = kor
        else:
            raise NotImplementedError("유효한 값이 아닙니다.")
    
    # @어노테이션: @property, @변수.setter - getter, setter로 만들 수 있음.
    @kor.setter     # s.kor = 90  같은 식으로 변경 가능
    def kor(self,kor):
        if kor >= 0 and kor <= 100:
            self.__kor = kor
        else:
            raise NotImplementedError("유효한 값이 아닙니다.")
        
    def setEng(self,eng):
        if eng >= 0 and eng <= 100:
            self.__eng = eng
        else:
            raise NotImplementedError("유효한 값이 아닙니다.")
        
    def getNo(self):
        return self.__no
    
    def getKor(self):
        return self.__kor
    
    @property       # print(Stu.kor)
    def kor(self):
        return self.__kor
    
    def getName(self):
        return self.__name
    
    def getEng(self):
        return self.__eng
        
s = Stu(1,"홍길동",100,99)
# s.__kor = 200

print(s.getName())
# print(s.no,s.__name,s.__kor)          # 바로 위에 있는 s.__kor변수에 대해 출력
# s.eng = 2000
# s.SetKor(500)               # 
# print(s)
