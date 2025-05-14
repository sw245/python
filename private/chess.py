
# visualizing chess

print("chessboard")

# idea
# 1. 행렬?
# 2. 이중 리스트 출력 >> 이게 간단할 듯?
# 3. blessed

import blessed
term = blessed.Terminal()

# print(term.height)
# print(term.width)

# print(term.clear)

row = ['1','2','3','4','5','6','7','8',]
column = ['a','','b','','c','','d','','e','','f','','g','','h']

for c in column:
    print(term.white(c))
print(term.gray('\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*row)))







