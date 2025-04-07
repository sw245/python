
# a_list = [1,2,3,4,5]
# print(a_list)
# try:
#     print(a_list[5])
# except ValueError:          # ValueError만 처리함
#     print("출력되어야 함")
# except IndexError:
#     print("인덱스 에러")
# except Exception as e:           # 모든 에러에 다 대응됨
#     print(e)
#     print("모든 예외처리가 다 가능")

# #  >> ValueError, IndexError 거의 안 씀

# print(7)
# print(8)




# # finally 에외 시, 예외 없을 시 모두 실행

# try:
#     f = open("info.txt","w")
#     raise NotImplementedError
# except Exception as e:
#     print(e)
# finally:
#     f.close()



print(1)
print(2)
raise NotImplementedError("프로그램 미구현")        # 오류 메시지 입력 가능
print(3)