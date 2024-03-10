from classes.board import Board

def main():
    row = 0
    col = 0
    choice = 0
    board = Board()
    board.set_cells()
    board.display()

    # row = input("enter a valid row number: ")
    # col = input("enter a valid col number: ")
    # choice = input("enter a valid choice: ")

    # board.get_cell(row, col, choice)
    # board.display()


if __name__ == "__main__":
    main()
