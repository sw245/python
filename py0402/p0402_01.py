
list = [1,2,3,4,5]
dic = {'no':1,"name":"rr"}

# 리스트, 딕셔너리 추가
list.append(6)
dic['kor'] = 99

# 리스트, 딕셔너리 삭제
del list[0]
del dic['no']

# 리스트, 딕셔너리 수정
list[1] = 10
dic['kor'] = 100

# # 개별 출력
# print(list[0])
# print(dic['kor'])
# print(dic.get('eng'))   # get 함수 사용 시 없는 키에 대해 None 출력

# # 딕셔너리 키, 밸류 출력
# print(dic.keys())       # key만 출력
# print(dic.values())     # value만 출력
# print(dic.items())      # key, value 동시 출력 - tuple형태

# 전체 출력
for k in dic:
    print(dic[k])           # value 출력
    print(k,dic[k])
        
for k,v in dic.items():
    print(k,v)

for i in list:
    print(i)

###
if 'no' in dic:     # 딕셔너리를 비교할 때 key를 가지고 비교?
    print("있습니다.")
    
    
# dic = {'no':1,"name":"rr",'kor':100,'eng':100,'math':100,'total':300}    

# # 딕셔너리 정렬
# import operator
# dic_sort = sorted(dic.items(),key=operator.itemgetter(0))   # 0 >> key를 가지고 정렬?
# print(dic_sort)
    

# list = [1,2,3,4,5,4,6,7,3,5,9,2,4,5]    

# # 리스트 정렬
# list.sort()             # 리스트 순차정렬
# print(list)

# list.sort(reverse=True) # 리스트 역순 정렬
# print(list)


# # 리스트 내포       # # append로 일일이 추가하는 것보다 효율적..
# # 1-10까지 리스트 생성
# alist = [i for i in range(1,10+1)]
# blist = [0]*10      

# clist = [i for i in range(1,50+1) if i%2==1]        # 홀수 출력


# txt_list = ['안녕','반가워','다음','내일','봐','잘','지내','봐요']
# # # zip
# # for i,t in zip(list,txt_list):
# #     print(i,t)
    
# # zip 사용해서 list 생성 
# new_list = list(zip(alist,txt_list))
# print(new_list)

# # zip 사용해서 dict생성
# new_dic = dict(zip(blist,txt_list))
# print(new_dic)


# # 얕은 복사, 깊은 복사
# alist = clist       # 얕은 복사 >> 두 리스트가 실시간으로 같아지게 됨ㄴ
# alist = [*clist]    # 깊은 복사 >> clist와 같아졌지만 별개의 리스트