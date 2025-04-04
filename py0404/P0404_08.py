# P0404_07
# stu.txt 파일의 문자를 읽어와서 리스트타입으로 변경

# 파일 저장하기

students = [
    {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}, 
    {'no': 2, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': 1}, 
    {'no': 3, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 55, 'total': 255, 'avg': 85.0, 'rank': 4}, 
    {'no': 4, 'name': '강감찬', 'kor': 80, 'eng': 60, 'math': 71, 'total': 211, 'avg': 70.33333333333333, 'rank': 5}, 
    {'no': 5, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': 2}
]

# 리스트타입을 stu.txt에 저장
# 딕셔너리 형태를 >> 1,홍길동,60,100,100,260,86.66666666666667,2

s = {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}
data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
print(s)
print("-"*50)
print(data)

# stu.txt에 파일 저장
f = open("py0404/stu.txt","w",encoding="utf-8")
for s in students:
    data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
    f.write(data)
f.close()    
