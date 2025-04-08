
a = [10,5,24,2,4,7]

print(min(a))       # 최솟값
print(max(a))       # 최댓값
print(sum(a))       # 합계
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a_dict = [
    {'no':1,'name':"홍길동"},
    {'no':5,'name':"유관순"},
    {'no':3,'name':"이순신"},
    {'no':4,'name':"강감찬"},
    {'no':2,'name':"김구"},
]

print(max(a_dict,key=lambda x:x['no']))
a_dict.sort(key=lambda x:x['no'])
print(a_dict)
a_dict.sort(key=lambda x:x['no'],reverse=True)
print(a_dict)
