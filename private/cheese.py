
# not cheese but chess though. (ver 2)


# visualizing chess

print("chessboard")
print()

import blessed
term = blessed.Terminal()


### 객체 지정 ###

board_number = [' ','8',' ','7',' ','6',' ','5',' ','4',' ','3',' ','2',' ','1']
alphabet = ['a','b','c','d','e','f','g','h']

rows = {}

for i in range(8):
    for x in alphabet:
        rows[f'{x}{i+1}'] = ' '


pieces_w = ['R','N','B','Q','K','B','N','R']
pieces_r = [term.red('R'),term.red('N'),term.red('B'),term.red('K'),term.red('Q'),term.red('B'),term.red('N'),term.red('R')]

moves = []

location = {}   # 기물 데이터 (기물:위치)
on_board = {}   # location 보조 (위치:기물)

pawns_r_key = ['bap','bbp','bcp','bdp','bep','bfp','bgp','bhp']
pieces_r_key = ['bR1','bN1','bB1','bK','bQ','bB2','bN2','bR2']

pawns_w_key = ['wap','wbp','wcp','wdp','wep','wfp','wgp','whp']
pieces_w_key = ['wR1','wN1','wB1','wQ','wK','wB2','wN2','wR2']



# ### 칸에 기물 할당 ###

## 초기 세팅 


for i in range(8):
    for n,x in enumerate(alphabet):
        if i+1 == 1:
            rows[f'{x}{i+1}'] = pieces_w[n]
            on_board[f'{x}{i+1}'] = pieces_w_key[n]
            location[pieces_w_key[n]] = f'{x}{i+1}'
        elif i+1 == 2:
            rows[f'{x}{i+1}'] = 'p'
            on_board[f'{x}{i+1}'] = pawns_w_key[n]
            location[pawns_w_key[n]] = f'{x}{i+1}'
        elif i+1 == 7:
            rows[f'{x}{i+1}'] = term.red('p')
            on_board[f'{x}{i+1}'] = pawns_r_key[n]
            location[pawns_r_key[n]] = f'{x}{i+1}'
        elif i+1 == 8:
            rows[f'{x}{i+1}'] = pieces_r[n]
            on_board[f'{x}{i+1}'] = pieces_r_key[n]
            location[pieces_r_key[n]] = f'{x}{i+1}'
            
turn = 1
            
while True:
    
    ### 터미널 출력 부분 (그래픽) ###
    for r in board_number:
        if r == ' ':
            print(r,'  |',end='')
            print('￣￣￣|'*8)
        else:
            print(r,'  |',end='')
            print(f'\t{rows[f'a{r}']}  |   {rows[f'b{r}']}  |   {rows[f'c{r}']}  |   {rows[f'd{r}']}  |\
   {rows[f'e{r}']}  |   {rows[f'f{r}']}  |   {rows[f'g{r}']}  |   {rows[f'h{r}']}  ',end='')
            print('|')
            
        
    print(' '*4,'￣'*28)

    print()
    print('\t{}      {}      {}      {}      {}      {}      {}      {}  '.format(*alphabet))

    print()
    
    
    if gameset == 1: 
        print(moves[-1])
        break


    
    # 백 턴
    if turn % 2 == 1:   
        move = input("백 차례>>")
        moves.append(move)

        ### CASTLING ###     
        if move == 'O-O':
            # 킹 이동
            rows['e1'] = ' '
            rows['g1'] = 'K'
            # 룩 이동
            rows['h1'] = ' '
            rows['f1'] = 'R'
            
            turn += 1
            continue

        elif move == 'O-O-O':
            #킹 이동
            rows['e1'] = ' '
            rows['c1'] = 'K'
            #룩 이동
            rows['a1'] = ' '
            rows['d1'] = 'R'

            turn += 1
            continue


        movefrom = input("from where? >>")

        
        ### promotion ###
        if move[-1] in ['R','N','B','Q']:
            promo = move[-1]
            if '=' in move:
                move = move[:-2]
            else:
                move = move[:-1]


        ### check / mate ###
        if '+' in move:
            move = move[:-1]
        elif '#' in move:
            move = move[:-1]
            gameset = 1
                

        ### 이동 ###

        # 폰 움직임
        if len(move) == 2:   

            if promo in ['R','B','N','Q']:                          ## 프로모션
                rows[move] = promo
                rows[movefrom] = ' '
                promo = ''
                turn += 1
                continue

            rows[move] = 'p'

        elif 'x' in move:           # takes시 폰 이동 따로
            if move[0] in alphabet:
                rows[move[-2:]] = 'p'
            else:
                rows[move[-2:]] = move[0]
                        
        # 다른 기물 움직임
        else:                    
            rows[move[-2:]] = move[0]   
                
                
        rows[movefrom] = ' '
        turn += 1
        

    # 흑 턴
    elif turn % 2 == 0:
        move = input("흑 차례>>")
        moves.append(move)

        ### CASTLING ###     
        if move == 'O-O':
            # 킹 이동
            rows['d8'] = ' '
            rows['b8'] = term.red('K')
            # 룩 이동
            rows['a8'] = ' '
            rows['c8'] = term.red('R')
            
            turn += 1
            continue

        elif move == 'O-O-O':
            #킹 이동
            rows['d8'] = ' '
            rows['f8'] = term.red('K')
            #룩 이동
            rows['h8'] = ' '
            rows['e8'] = term.red('R')

            turn += 1
            continue


        movefrom = input("from where? >>")
        
        
        ### promotion ###
        if move[-1] in ['R','N','B','Q']:
            promo = move[-1]
            if '=' in move:
                move = move[:-2]
            else:
                move = move[:-1]


        ### check / mate ###
        if '+' in move:
            move = move[:-1]
        elif '#' in move:
            move = move[:-1]
            gameset = 1
                

        ### 이동 ###

        # 폰 움직임
        if len(move) == 2:   

            if promo in ['R','B','N','Q']:                          ## 프로모션
                rows[move] = term.red(promo)
                rows[movefrom] = ' '
                promo = ''
                turn += 1
                continue

            rows[move] = term.red('p')

        elif 'x' in move:           # takes시 폰 이동 따로
            if move[0] in alphabet:
                rows[move[-2:]] = term.red('p')
            else:
                rows[move[-2:]] = move[0]
                        
        # 다른 기물 움직임
        else:                    
            rows[move[-2:]] = term.red(move[0])
                
                
        rows[movefrom] = ' '
        turn += 1