
# []가 세 번 중첩되어 있는 리스트
a = [[1,2,3],[4,[5,6],7,[8,9]]]

# for i in a:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     print(k,end="")
#             else: 
#                 print(j,end="")
#     else: 
#         print(i,end="")
        
        
def flatten(data):
    output = []
    for i in data:
        if type(i) == list:
            output.extend(flatten(i))        # 재귀함수 호출
        else:
            output.append(i)
    return output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    
            
output_a = flatten(a)
print(output_a)
