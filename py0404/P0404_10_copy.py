# 문서 읽어오기 - r
# 문서 이외의 파일 읽어오기 - rb (바이너리)

# 파일 읽기
f = open('py0404/a.jpg','rb')

# 이진파일은 용량이 클 수 있으므로, 1바이트씩 읽어오기 >> f.read(1)
while True:
    fData = f.read(1)
    if not fData: break
f.close()

print("파일 읽어오기 완료")


# 문서저장 - w,a
# 파일저장 - wb

# 폴더 존재 확인 : os.path.exists()
# 폴더 생성 : os.makedir() : 폴더 1개 생성 >> 없는 폴더가 여러 개면 에러 발생
# 폴더 생성 : os.makedirs(): 모든 폴더 생성   

import os

if not os.path.exists("C:/down1"):      # 폴더가 없으면 생성 후 진행
    os.makedirs("C:/down1")

# 파일 쓰기    
ff = open("C:/down1/b.jpg","wb")         # 없는 폴더는 에러 발생

len = ff.write(fData)
print(f"파일크기 : {len} 바이트")


print("파일 저장 완료")