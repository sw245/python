# dic_a = {"no":1,"name":"ㄱㄱㄱ"}
# a = "ㄱㄱㄱ"

# if a in dic_a:
#     print("딕셔너리도 in 쓸수 있음!")
# else:
#     print("응 못 써~")
    

stuS = [
    {"no":1,"name":"홍","kor":100,"eng":70,"math":82,"total":252,"avg":84,"rank":0},
    {"no":2,"name":"유","kor":80,"eng":94,"math":96,"total":270,"avg":90,"rank":0},
    {"no":3,"name":"김","kor":56,"eng":87,"math":76,"total":219,"avg":73,"rank":0}
]

    
w_stuS = f"{stuS}"
print(type(w_stuS))    
print(w_stuS)