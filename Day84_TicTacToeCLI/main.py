import curses
from curses.textpad import Textbox, rectangle
from time import sleep
from math import ceil

## GAME CONFIG GLOBALS
BOARD_TOP = 0
BOARD_BOTTOM = 4
BOARD_LEFT = 1
BOARD_RIGHT = 9
X_SPACE = 2
Y_SPACE = 4
WINNING_COMBINATIONS = [['0-0', '0-1', '0-2'], ['1-0', '1-1', '1-2'], ['2-0', '2-1', '2-2'],
                        ['0-0', '1-0', '2-0'], ['0-1', '1-1', '2-1'], ['0-2', '1-2', '2-2'],
                        ['0-0', '1-1', '2-2'], ['2-0', '1-1', '0-2']]

def draw_board(win, board):
        for i, row in enumerate(board):
            win.addstr(i * 2, 0, "|".join(row))
            if i<2:
                win.addstr(i * 2 + 1, 0, "-" * 11)


def check_win(win, board):
    for list in WINNING_COMBINATIONS:
        print(list)
        check = [ board[int(iter[0])][int(iter[2])] for iter in list ]
        print('check:\n' + ':'.join(check).replace(' ', '') + '\n+++++++++++++++++')
        if ''.join(check).replace(' ', '') == 'XXX' or ''.join(check).replace(' ', '') == 'OOO':
            win.clear()
            draw_board(win, board)
            win.addstr(BOARD_BOTTOM + 2, BOARD_LEFT, f'{check[0]} WINS!')
            return True

def display_turn(win, sym):    
    win.addstr(BOARD_BOTTOM + 2, BOARD_LEFT, f"It's {sym} turn")


def main(stdscr, game=0):
    board =  [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
    curses.curs_set(True)
    y, x = 5, 2
    current_symbol = 'O' if game % 2 == 1 else 'X'
    display_turn(stdscr, current_symbol)
    
    while True:
        
        draw_board(stdscr, board)        
        stdscr.move(x,y)
        key = stdscr.getch()

        if key == curses.KEY_UP and x > BOARD_TOP:
            x -= X_SPACE            
        elif key == curses.KEY_DOWN and x < BOARD_BOTTOM:
            x += X_SPACE

        elif key == curses.KEY_LEFT and y > BOARD_LEFT:
            y -= Y_SPACE

        elif key == curses.KEY_RIGHT and y < BOARD_RIGHT:
            y += Y_SPACE

        elif key == 10:
            if board[x // X_SPACE][y // Y_SPACE] == "   ":
                board[x // X_SPACE][y // Y_SPACE] = f" {current_symbol} "
                print(*board, sep='\n')
                print('~~~~~~~~~~~~~~~~~')
                if check_win(stdscr, board):
                    draw_board(stdscr, board)
                    
                    break
                current_symbol = "O" if current_symbol == "X" else "X"
                display_turn(stdscr, current_symbol)

        elif key == curses.ascii.ESC:
            exit()
        
        check_win(stdscr, board)

        stdscr.refresh()
    game += 1
    stdscr.addstr(BOARD_BOTTOM + 4, BOARD_LEFT, f"Hit ENTER to play again, hit anything else to quit")
    key = stdscr.getch()
    if key == 10:
        stdscr.addstr(BOARD_BOTTOM + 6, BOARD_LEFT, f"Great, you'll start as {'O' if game % 2 == 1 else 'X'} this time!")
        stdscr.refresh()
        for x in (1,2,3):
            stdscr.addstr('.')
            stdscr.refresh()
            sleep(1)
        stdscr.clear()
        main(stdscr, game)
    

curses.wrapper(main)
