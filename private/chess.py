
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






# pawns_w = {'a':'p','b':'p','c':'p','d':'p','e':'p','f':'p','g':'p','h':'p'}
# pawns_w = ['p' for _ in range(8)]
pieces_w = ['R','N','B','Q','K','B','N','R']

# pawns_r = {'a':term.red('p'),'b':term.red('p'),'c':term.red('p'),'d':term.red('p'),'e':term.red('p'),'f':term.red('p'),'g':term.red('p'),'h':term.red('p')}
# pawns_r = [term.red('p') for _ in range(8)]
pieces_r = [term.red('R'),term.red('N'),term.red('B'),term.red('K'),term.red('Q'),term.red('B'),term.red('N'),term.red('R')]

moves = []

location = {}   # 기물 데이터 (기물:위치)
on_board = {}   # location 보조 (위치:기물)

pawns_r_key = ['bap','bbp','bcp','bdp','bep','bfp','bgp','bhp']
pieces_r_key = ['bR1','bN1','bB1','bK','bQ','bB2','bN2','bR2']

pawns_w_key = ['wap','wbp','wcp','wdp','wep','wfp','wgp','whp']
pieces_w_key = ['wR1','wN1','wB1','wQ','wK','wB2','wN2','wR2']

promo = ''
promo_count = 0
gameset = 0



### 초기 세팅 ###


## 칸 만들기

for i in range(8):
    for x in alphabet:
        rows[f'{x}{i+1}'] = ' '


## 칸에 기물 할당 

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
        else:
            on_board[f'{x}{i+1}'] = ''





## 기물:위치 값 저장


## 위치 저장 필요한가?? ㅇㅇ 근데 단순 위치 말고 기물까지 포함하는 위치


#### DEBUGGING ####

# move = 'e4'
# print(pawns_w[move[0]])
# print(rows[move])

# print(on_board)
# print(location)

# print(rows)

#------------------#

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
            rows['g1'] = 'K'
            rows['e1'] = ' '
            location['wK'] = 'g1'
            on_board['g1'] = 'wK'

            # 룩 이동
            rows['f1'] = 'R'
            rows['h1'] = ' '
            location['wR2'] = 'f1'
            on_board['f1'] = 'wR2'
            
            turn += 1
            continue

        elif move == 'O-O-O':
            #킹 이동
            rows['c1'] = 'K'
            rows['e1'] = ' '
            location['wK'] = 'c1'
            on_board['c1'] = 'wK'

            #룩 이동
            rows['d1'] = 'R'
            rows['a1'] = ' '
            location['wR1'] = 'd1'
            on_board['d1'] = ['wR1']

            turn += 1
            continue

        
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
        
        
        ### TAKES ###
        if 'x' in move:     # 다른 기물은 takes만 구현
            if move[0] in ['R','N','B','Q','K']:
                location[on_board[move[-2:]]] = ''
            else:   # 폰 - 움직임까지 포함                      ## 백 ##
                if on_board[move[-2:]] == '':   # 앙파상                                 # (앙파상)
                    location[on_board[f'{move[-2]}{int(move[-1])-1}']] = ''             # 잡힌 폰 location 업데이트
                    rows[f'{move[-2]}{int(move[-1])-1}'] = ' '                          # 잡힌 폰 rows 업데이트

                else:                                                                   # (그냥 takes)
                    location[on_board[move[-2:]]] = ''                                  # 잡힌 기물 location 업데이트

                if promo in ['R','B','N','Q']:                  ## 프로모션
                    rows[move[-2:]] = promo                                             # promotion
                    rows[f'{move[0]}{int(move[-1])-1}'] = ' '                           # 원래 자리
                    # location, on_board 업데이트
                    location[on_board[f'{move[0]}{int(move[-1])-1}']] = ''              # 원래 자리에 있던 폰은 아웃

                    if promo == 'Q' and isinstance(location['wQ'],list):                # 프로모션 있었는지 판별(Q)
                        location['wQ'].append(move[-2:])                                 # 후 location 업데이트
                    elif promo == 'Q' and not isinstance(location['wQ'],list):
                        location['wQ'] = [location['wQ'], move[-2:]]
                    elif promo in ['R','B','N'] and not f'w{promo}' in location:        # 프로모션 있었는지 판별(나머지)
                        location[f'w{promo}'] = [move[-2:]]                              # 후 location 업데이트
                    elif promo in ['R','B','N'] and f'w{promo}' in location:
                        location[f'w{promo}'].append(move[-2:])           

                    on_board[move[-2:]] = f'w{promo}'                                    # 이동한 자리 on_board 업데이트
                    on_board[f'{move[0]}{int(move[-1])-1}'] = ''                        # 이동 전 자리 on_board 업데이트

                    promo = ''
                    turn += 1
                    continue 

                # 폰 움직임
                rows[move[-2:]] = 'p'                                                   # 이동한 폰 rows 업데이트
                rows[f'{move[0]}{int(move[-1])-1}'] = ' '                               # 이동 전 자리 rows 업데이트
                # location, on_board 업데이트
                location[on_board[f'{move[0]}{int(move[-1])-1}']] = move[-2:]           # 이동한 폰 location 업데이트
                on_board[move[-2:]] = on_board[f'{move[0]}{int(move[-1])-1}']           # 이동한 자리 on_board 업데이트
                on_board[f'{move[0]}{int(move[-1])-1}'] = ''                            # 이동 전 자리 on_board 업데이트
                turn += 1
                continue
                

        ### 단순 이동 ###

        # 폰 움직임
        if len(move) == 2:   

            if promo in ['R','B','N','Q']:                          ## 프로모션
                rows[move] = promo
                rows[f'{move[0]}{int(move[-1])-1}'] = ' '
                # location, on_board 업데이트
                location[on_board[f'{move[0]}{int(move[-1])-1}']] = ''              # 원래 자리에 있던 폰은 아웃

                if promo == 'Q' and isinstance(location['wQ'],list):                # 프로모션 있었는지 판별(Q)
                    location['wQ'].append(move)                                     # 후 location 업데이트
                elif promo == 'Q' and not isinstance(location['wQ'],list):
                    location['wQ'] = [location['wQ'], move]
                elif promo in ['R','B','N'] and not f'w{promo}' in location:        # 프로모션 있었는지 판별(나머지)
                    location[f'w{promo}'] = [move]                                     # 후 location 업데이트
                elif promo in ['R','B','N'] and f'w{promo}' in location:
                    location[f'w{promo}'].append(move)           

                on_board[move] = f'w{promo}'                                        # 이동한 자리 on_board 업데이트
                on_board[f'{move[0]}{int(move[-1])-1}'] = ''                        # 이동 전 자리 on_board 업데이트 
                
                promo = ''
                turn += 1
                continue


            # 기물 이동(쓰고, 지우기)
            rows[move] = 'p'
            rows[location[f'w{move[0]}p']] = ' '                    #@@@@@@ takes로 열 변경된 폰은 제거 안 됨.....
            # location, on_board 업데이트
            on_board[move] = f'w{move[0]}p'
            on_board[location[f'w{move[0]}p']] = ''
            location[f'w{move[0]}p'] = move
        
             


        # 다른 기물 움직임
        else:                    
            # 기물 이동(쓰기)
            rows[move[-2:]] = move[0]   
            # R, N, B

            if f'w{move[0]}' in location and isinstance(location[f'w{move[0]}'],list):
                before_m = input("from where >>")

                rows[move[-2:]] = move[0]
                rows[before_m] = ' '
                # location, on_board
                location[f'w{move[0]}'].remove(before_m)
                location[f'w{move[0]}'].append(move[-2:])
                on_board[before_m] = ''
                on_board[move[-2:]] = f'w{move[0]}'

                turn += 1
                continue

            if move[0] in ['R','N','B']:
                # 기물 이동(지우기)
                qork = input(f"from {location[f'w{move[0]}1']} or {location[f'w{move[0]}2']}? >>")
                rows[qork] = ' '
                # location, on_board 업데이트
                on_board[move[-2:]] = on_board[qork]
                on_board[qork] = ''
                location[on_board[move[-2:]]] = move[-2:]
                
            else:
                # 기물 이동(지우기)
                rows[location[f'w{move[0]}']] = ' '
                # location, on_board 업데이트
                on_board[move[-2:]] = f'w{move[0]}'
                on_board[location[f'w{move[0]}']] = ''
                location[f'w{move[0]}'] = move[-2:]
            
        turn += 1
        

    # 흑 턴
    elif turn % 2 == 0:
        move = input("흑 차례>>")
        moves.append(move)
        

        ### CASTLING ### 
        if move == 'O-O':
            # 킹 이동
            rows['b8'] = term.red('K')
            rows['d8'] = ' '
            location['bK'] = 'b8'
            on_board['b8'] = 'bK'

            # 룩 이동
            rows['c8'] = term.red('R')
            rows['a8'] = ' '
            location['bR1'] = 'c8'
            on_board['c8'] = 'bR1'

            turn += 1
            continue

        elif move == 'O-O-O':
            #킹 이동
            rows['f8'] = term.red('K')
            rows['d8'] = ' '
            location['bK'] = 'f8'
            on_board['f8'] = 'bK'

            #룩 이동
            rows['e8'] = term.red('R')
            rows['h8'] = ' '
            location['bR2'] = 'e8'
            on_board['e8'] = ['bR2']

            turn += 1
            continue


        ### check, mate ###
        if '+' in move:
            move = move[:-1]
        elif '#' in move:
            move = move[:-1]
            gameset = 1
        
        ### TAKES ###
        if 'x' in move:     # 다른 기물은 takes만 구현
            if move[0] in ['R','N','B','Q','K']:
                location[on_board[move[-2:]]] = ''
            else:   # 폰은 움직임까지 포함                  ## 흑 ##
                if on_board[move[-2:]] == '':   # 앙파상
                    location[on_board[f'{move[-2]}{int(move[-1])+1}']] = ''
                    rows[f'{move[-2]}{int(move[-1])+1}'] = ' '
                else: 
                    location[on_board[move[-2:]]] = ''
                # 폰 움직임
                rows[move[-2:]] = term.red('p')
                rows[f'{move[0]}{int(move[-1])+1}'] = ' '
                # location, on_board 업데이트                                       
                location[on_board[f'{move[0]}{int(move[-1])+1}']] = move[-2:]
                on_board[move[-2:]] = on_board[f'{move[0]}{int(move[-1])+1}']             
                on_board[f'{move[0]}{int(move[-1])+1}'] = ''
                turn += 1
                continue
        

        ### 단순 이동 ###

        # 폰 움직임
        elif len(move) == 2:        
            # 기물 이동(쓰고, 지우기)
            rows[move] = term.red('p')
            rows[location[f'b{move[0]}p']] = ' '
            # location, on_board 업데이트
            on_board[move] = f'b{move[0]}p'
            on_board[location[f'b{move[0]}p']] = ''
            location[f'b{move[0]}p'] = move
        
        # 다른 기물 움직임
        else:
            # 기물 이동(쓰기)
            rows[move[-2:]] = term.red(move[0])
            # R, N, B
            if move[0] in ['R','N','B']:
                # 기물 이동(지우기)
                qork = input(f"from {location[f'b{move[0]}1']} or {location[f'b{move[0]}2']}? >>")
                rows[qork] = ' '
                # location, on_board 업데이트
                on_board[move[-2:]] = on_board[qork]
                on_board[qork] = ''
                location[on_board[move[-2:]]] = move[-2:]
                
            else:
                # 기물 이동(지우기)
                rows[location[f'b{move[0]}']] = ' '
                # location, on_board 업데이트
                on_board[move[-2:]] = f'b{move[0]}'
                on_board[location[f'b{move[0]}']] = ''
                location[f'b{move[0]}'] = move[-2:]
            
        turn += 1
        

    
        