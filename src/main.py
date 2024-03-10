from classes.board import Board

def main():
    row = 0
    col = 0
    choice = 0
    board = Board()
    board.display()

    row = int(input("enter a valid row number: "))
    col = int(input("enter a valid col number: "))
    choice = int(input("enter a valid choice: "))

    board.update(row, col, choice)
    is_valid = board.validate(row, col, choice)
    print("valid: ", is_valid)
    board.display()


if __name__ == "__main__":
    main()
