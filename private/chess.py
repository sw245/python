
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

number = ['8',' ','7',' ','6',' ','5',' ','4',' ','3',' ','2',' ','1']
alphabet = ['a','b','c','d','e','f','g','h']

rows = [
    [' ',' ',' ',' ',' ',' ',' ',' '] for _ in range(8)
]

pawns_w = ['p','p','p','p','p','p','p','p']
pieces_w = ['R','N','B','Q','K','B','N','R']

pawns_r = ['p','p','p','p','p','p','p','p']
pieces_r = ['R','N','B','K','Q','B','N','R']

# print(rows)



### 터미널 출력 부분 (그래픽) ###

print(' '*4,end='')
print('|',end='')
print('￣'*31,end='')
print('|')

for r in number:
    if r == '8':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[8-1]),end='')
        print('  |')
        
    elif r == '7':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[7-1]),end='')
        print('  |')
        
    elif r == '6':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[6-1]),end='')
        print('  |')
        
    elif r == '5':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[5-1]),end='')
        print('  |')
        
    elif r == '4':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[4-1]),end='')
        print('  |')
        
    elif r == '3':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[3-1]),end='')
        print('  |')
        
    elif r == '2':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[2-1]),end='')
        print('  |')
        
    elif r == '1':
        print(r,'  |',end='')
        print('\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}   |\t{}'.format(*rows[1-1]),end='')
        print('  |')
        
    elif r == ' ':
        print(r,'  |',end='')
        print('￣'*31,end='')
        print('|')
        
    else:
        print(r,'  |\t\t\t\t\t\t\t\t   |')
        
print(' '*4,'￣'*31)
    
print()
print('\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*alphabet))


    
### 칸에 기물 할당 ###

for row in rows:
    pass





