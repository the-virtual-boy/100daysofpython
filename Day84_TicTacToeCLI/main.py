import curses
from curses.textpad import Textbox, rectangle
from time import sleep
from math import ceil


WINNING_COMBINATIONS = [['0-0', '0-1', '0-2'], ['1-0', '1-1', '1-2'], ['2-0', '2-1', '2-2'],
                        ['0-0', '1-0', '2-0'], ['0-1', '1-1', '2-1'], ['0-2', '1-2', '2-2'],
                        ['0-0', '1-1', '2-2'], ['2-0', '1-1', '0-2']]
class GameBoard:
    def __init__(self, window):
        self.win = window
        self.new_game()        

    def new_game(self, sym='X'):
        self.board =  [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
        self.player = sym
        self.BOARD_TOP = 0
        self.BOARD_BOTTOM = 4
        self.BOARD_LEFT = 0
        self.BOARD_RIGHT = 10
        self.X_SPACE = self.BOARD_BOTTOM // 2
        self.Y_SPACE = (self.BOARD_RIGHT - 2) // 2
        self.set_center()
        self.display_turn()


    def draw_board(self):
        for i, row in enumerate(self.board):
            self.win.addstr(i * 2, 0, "|".join(row))
            if i<2:
                self.win.addstr(i * 2 + 1, 0, "-" * (self.BOARD_RIGHT + 1))

    def move_player(self, dir):
        if dir == 0 and self.X_LOC > self.BOARD_TOP:
            self.X_LOC -= self.X_SPACE
        elif dir == 1 and self.Y_LOC < self.BOARD_RIGHT - 1:
            self.Y_LOC += self.Y_SPACE
        elif dir == 2 and self.X_LOC < self.BOARD_BOTTOM:
            self.X_LOC += self.X_SPACE
        elif dir == 3 and self.Y_LOC > self.BOARD_LEFT + 1:
            self.Y_LOC -= self.Y_SPACE

    def make_move(self):
        if self.board[self.X_LOC // self.X_SPACE][self.Y_LOC // self.Y_SPACE] == "   ":
            self.board[self.X_LOC // self.X_SPACE][self.Y_LOC // self.Y_SPACE] = f" {self.player} "


    def change_player(self):
        self.player = 'X' if self.player == 'O' else 'O'

    def check_win(self):
        for list in WINNING_COMBINATIONS:
            check = [self.board[int(iter[0])][int(iter[2])] for iter in list ]
            if ''.join(check).replace(' ', '') == 'XXX' or ''.join(check).replace(' ', '') == 'OOO':
                self.win.clear()
                self.draw_board()
                self.win.addstr(self.BOARD_BOTTOM + 2, self.BOARD_LEFT, f'{check[0]} WINS!')
                return True
        return False
    
    def set_cursor(self):
        self.win.move(self.X_LOC, self.Y_LOC)

    def set_center(self):
        self.X_LOC = self.BOARD_BOTTOM // 2
        self.Y_LOC = self.BOARD_RIGHT // 2

    def display_turn(self):    
        self.win.addstr(self.BOARD_BOTTOM + 2, self.BOARD_LEFT, f"It's {self.player} turn")

    def print_win(self):
        self.win.addstr(self.BOARD_BOTTOM + 4, self.BOARD_LEFT, f"{self.player}WINS! ")

    def prompt_newgame(self):
        self.win.addstr(self.BOARD_BOTTOM + 4, self.BOARD_LEFT, f"Hit ENTER to play again, hit anything else to quit")
        key = self.win.getch()
        if key == 10:            
            ## needed for when computer is added?
            # self.win.addstr(self.BOARD_BOTTOM + 6, self.BOARD_LEFT, f"Great, you'll start as {'X' if self.player == 'O' else 'O'} this time!")
            self.win.addstr(self.BOARD_BOTTOM + 6, self.BOARD_LEFT, f"Great! Make sure to swap players!")
            self.win.refresh()
            for x in (1,2,3):
                self.win.addstr('.')
                self.win.refresh()
                sleep(1)
            self.win.clear()
            return True
        return False

    def new_player(self):
        return ('X' if self.player == 'O' else 'O')            

def main(stdscr):
    board = GameBoard(stdscr)

    while True:

        board.draw_board()
        board.set_cursor()
        key = stdscr.getch()
        if key == curses.KEY_UP:
            board.move_player(0)
        elif key == curses.KEY_RIGHT:
            board.move_player(1)       
        elif key == curses.KEY_DOWN:
            board.move_player(2)
        elif key == curses.KEY_LEFT:
            board.move_player(3)
        elif key == 10:
            board.make_move()
            if board.check_win():
                board.print_win()
                stdscr.refresh()
                if board.prompt_newgame():
                    board.new_game()
                else:
                    break
            else:
                board.change_player()
                board.display_turn()
        elif key == curses.ascii.ESC:
            exit()

                
        
        stdscr.refresh()
        


curses.wrapper(main)
