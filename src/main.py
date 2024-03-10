from classes.board import Board
from classes.solver import Solver
from time import sleep

def main():
    
    board = Board()
    start_game = '\033[1;34mSTART GAME\033[m'
    solve_game = '\033[1;92mSOLVE GAME\033[m'
    user_row = 0
    user_col = 0
    user_choice = 0
    valid = False
    no_list = ['No', 'N', 'n', 'no']

    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f"|{f'Press 1 to {start_game} | 2 to {solve_game}':^118}|")
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()

    game_mode = int(input('>>> '))
    print()
    sleep(1)

    if game_mode == 2:
        board.display()
        solved_board = Solver(board)
        solved_board.solve(0, 0)
        print()
        solved_board.display()

    while game_mode == 1: 
        board.display()
        print()
        print('Enter the row and column number')
        user_row = int(input('row >>> '))
        user_col = int(input('col >>> '))
        print()
        print(f"Enter your number choice for row ${user_row} col ${user_col}")
        user_choice = int(input('choice >>> '))
        print()
        board.update(user_row, user_col, user_choice)
        valid = board.validate(user_row, user_col, user_choice)
        sleep(1)
        if valid:
            print("You're choice was valid! Continue?")
        else:
            print("You're choice wasn't right. Continue?")
        
        if input('Y/N >>> ') in no_list:
            game_mode = 3


if __name__ == "__main__":
    main()
