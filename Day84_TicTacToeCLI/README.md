# Terminal TicTacToe Game

This program is a terminal based tic tac toe game that utilizes the [Python curses library](https://docs.python.org/3/library/curses.html) to make it fully interactive, and allow the player to move around the board and select where they want to place their token. The game has support for 2 players playing against each other as well as a single player playing against an AI opponent (albeit, a very simple one currently)

## Install instructions

Clone this repo, and install the curses module, if on Windows, the `windows-curses` module is available. once that's installed, you can simply run `python main.py`.

## Game Instructions

Upon launching the game and seeing the welcome text, you will need to choose to play a 1 player or 2 player game. A selection is made with the Enter key. If `1 player` is chosen, then the player will play against the computer. The player always starts as `X` and will go first. The game is played as standard TicTacToe, whoever gets three tokens in a row, either horizontally, vertically or diagonally, wins. After the round is over, the player will be asked to hit ENTER to play another game, or press any other key to quit. After every sequential game, the player and the computer will change tokens, taking turns who goes first. In 2 player, a reminder will pop up between each new game to remind players to switch tokens.

## Project Writeup

Day 84 tested my patience. I really enjoyed it compared to the web development project, but in the end, the additional steps I wanted to take ended up taking a lot longer, and requiring a lot more effort than I expected. 

I originally wrote the program without the use of classes, and it only required a few functions. I noticed parameters were being thrown between functions however, and so I saw it as a good opportunity to add a class to the project. I ended up having to almost rewrite the program to acoomodate the class, and the number of functions grew as well, it felt a bit cumbersome. 

The last addition was creating the computer player, instead of just 2 player play. I did leave the computer very basic, as I wasn't wanting to focus on that for this project, so it simply makes its move in the first random empty square it finds, but can easily be modified for more intelligent moves in the future. This change however almost required another rewrite, as much of the logic, and many of the functions had to be rewritten in a way so it accounted for either 2 player, or 1 player play. 

After a certain point, each time I sat down to write more code, I lasted even shorter than the previous time, and just found myself feeling frustrated more often, and more easily. I feel that this approach to slowly building the application did teach me a lot, but I think proper planning, and things like starting from classes from the offset might be better for my sanity.

On a more positive note, it was a really interesting experience to have to start delving into multiple libraries and pick which one would be best to achieve the goals I was aiming to accomplish, finally landing on curses and having to learn the functions and requirements for it. There was even some interesting tricks I learned in general, like multiplying a single character by an int to print out that character multiple times in one line, which really helped build the lines on the board. 