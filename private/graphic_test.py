
# ## 1. ANSI 이스케이프 코드
# # 특징: 텍스트 색상, 배경 색상, 위치 이동 등을 제어할 수 있습니다.

# print("\033[1;32;40m Green Text on Black Background \033[0m")
# print("\033[2J")  # 화면 지우기
# print("\033[H")   # 커서를 화면 맨 위로 이동




# ## 2. curses 라이브러리
# # 특징: 터미널 기반의 UI를 생성할 때 사용되며, 창, 색상, 텍스트 배치 등을 지원합니다.
# # 장점: 윈도우 및 색상을 쉽게 다룰 수 있음.
# # 단점: 윈도우 환경에서 설정이 약간 복잡.

# import curses

# def main(stdscr):
#     curses.start_color()
#     curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
#     stdscr.addstr(0, 0, "Hello, World!", curses.color_pair(1))
#     stdscr.refresh()
#     stdscr.getch()

# curses.wrapper(main)




# ## 3. rich 라이브러리
# # 특징: 터미널에서 컬러풀한 출력과 간단한 그래픽을 지원합니다.

# from rich.console import Console

# console = Console()
# console.print("[bold magenta]Hello, [red]World![/red][/bold magenta]")




## 4. blessed 라이브러리
# 특징: ANSI 코드의 상위 래퍼로, 더 직관적인 터미널 제어를 제공합니다.

# from blessed import Terminal

# term = Terminal()
# print(term.clear)
# print(term.red('This is red text!'))
# print(term.move_xy(10, 5) + 'Moved text')


# print(term.bold('Q'))
# print('Q')


# ## 5. tqdm (애니메이션 효과)
# # 특징: 진행 바와 간단한 애니메이션을 지원.

# from tqdm import tqdm
# import time

# for i in tqdm(range(100)):
#     time.sleep(0.05)





# ## 6. pygame (그래픽 게임 라이브러리)
# # 특징: 텍스트 기반이 아닌, 실제 그래픽 창을 띄우고 싶다면 적합.

# import pygame

# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Terminal Graphic Example')
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (255, 0, 0), (200, 150), 50)
#     pygame.display.flip()

# pygame.quit()





# ## 7. asciimatics (애니메이션과 UI)
# # 특징: 터미널에서 애니메이션과 텍스트 UI를 만들기 위한 강력한 라이브러리.

# from asciimatics.screen import Screen

# def demo(screen):
#     screen.print_at('Hello, World!', 10, 5, colour=Screen.COLOUR_RED)
#     screen.refresh()
#     screen.wait_for_input(10)

# Screen.wrapper(demo)








# ## 8. turtle (GUI 터미널용 그래픽)
# import turtle

# t = turtle.Turtle()
# t.forward(100)
# t.right(90)
# t.forward(100)
# turtle.done()





# print()

# def draw_grid(rows, cols):
#     for i in range(rows):
#         print("+---" * cols + "+")
#         print("|   " * cols + "|")
#     print("+---" * cols + "+")

# draw_grid(5, 5)


move = 'exf4'
# print(len(move))

if 'x' in move:
    print('가능')