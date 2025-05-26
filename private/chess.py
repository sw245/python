
# visualizing chess

print("chessboard")
print()

# idea
# 1. 행렬?
# 2. 이중 리스트 출력 >> 이게 간단할 듯?
# 3. blessed

import blessed
term = blessed.Terminal()

# print(term.height)
# print(term.width)

# print(term.clear)



### 객체 지정 ###

board_number = [' ','8',' ','7',' ','6',' ','5',' ','4',' ','3',' ','2',' ','1']
alphabet = ['a','b','c','d','e','f','g','h']

# rows = [
#     [' ',' ',' ',' ',' ',' ',' ',' '] for _ in range(8)
# ]

# rows = [
#     [] for _ in range(8)
# ]

rows = {}

for i in range(8):
    for x in alphabet:
        rows[f'{x}{i+1}'] = ' '
        
        # if i == 1-1: rows[1-1].append({f'{x}{i+1}':' '})
        # elif i == 2-1: rows[2-1].append({f'{x}{i+1}':' '})
        # elif i == 3-1: rows[3-1].append({f'{x}{i+1}':' '})
        # elif i == 4-1: rows[4-1].append({f'{x}{i+1}':' '})
        # elif i == 5-1: rows[5-1].append({f'{x}{i+1}':' '})
        # elif i == 6-1: rows[6-1].append({f'{x}{i+1}':' '})
        # elif i == 7-1: rows[7-1].append({f'{x}{i+1}':' '})
        # elif i == 8-1: rows[8-1].append({f'{x}{i+1}':' '})






pawns_w = {'a':'p','b':'p','c':'p','d':'p','e':'p','f':'p','g':'p','h':'p'}
pieces_w = ['R','N','B','Q','K','B','N','R']

pawns_r = {'a':term.red('p'),'b':term.red('p'),'c':term.red('p'),'d':term.red('p'),'e':term.red('p'),'f':term.red('p'),'g':term.red('p'),'h':term.red('p')}
pieces_r = [term.red('R'),term.red('N'),term.red('B'),term.red('K'),term.red('Q'),term.red('B'),term.red('N'),term.red('R')]

moves = []

on_board = {}




# ### 칸에 기물 할당 ###

## 초기 세팅 


for i in range(8):
    for n,x in enumerate(alphabet):
        if i+1 == 1:
            rows[f'{x}{i+1}'] = pieces_w[n]
        elif i+1 == 2:
            rows[f'{x}{i+1}'] = pawns_w[x]
        elif i+1 == 7:
            rows[f'{x}{i+1}'] = pawns_r[x]
        elif i+1 == 8:
            rows[f'{x}{i+1}'] = pieces_r[n]



## 기물:위치 값 저장


## 위치 저장 필요한가?? ㅇㅇ 근데 단순 위치 말고 기물까지 포함하는 위치


print(on_board)

# print(rows)


# ### 터미널 출력 부분 (그래픽) ###

# for r in board_number:
#     if r == ' ':
#         print(r,'  |',end='')
#         print('￣￣￣|'*8)
#     else:
#         print(r,'  |',end='')
#         print(f'\t{rows[f'a{r}']}  |   {rows[f'b{r}']}  |   {rows[f'c{r}']}  |   {rows[f'd{r}']}  |\
#    {rows[f'e{r}']}  |   {rows[f'f{r}']}  |   {rows[f'g{r}']}  |   {rows[f'h{r}']}  ',end='')
#         print('|')
        
    

# print(' '*4,'￣'*28)

# print()
# print('\t{}      {}      {}      {}      {}      {}      {}      {}  '.format(*alphabet))

# print()
# turn = 1
# move = input("백 차례>>")
        

# ### 단순 이동 ###
# if turn % 2 == 1:   # 백 턴
#     moves.append(move)
#     if len(move) == 2:
#         rows[move] = pawns_w[move[0]]
#         rows[f'{move[0]}'] = ''
#     rows[move[-2:]] = move[0]
    


