from classes.cell import Cell

# will implement for more boards later, let's stick with one board for now
board = [
        [0, 2, 0, 0, 0, 3, 1, 5, 0],
        [8, 7, 0, 4, 1, 5, 0, 2, 6],
        [1, 0, 0, 0, 0, 8, 0, 0, 7],
        [4, 8, 0, 6, 0, 0, 5, 0, 3],
        [0, 5, 0, 0, 0, 1, 0, 0, 4],
        [0, 0, 6, 5, 0, 0, 8, 0, 2],
        [0, 0, 8, 1, 5, 7, 4, 0, 0],
        [6, 9, 0, 0, 8, 0, 7, 0, 0],
        [0, 4, 7, 0, 0, 0, 2, 0, 0],
    ]

class Board:
    def __init__(self):
        self.rows = 9
        self.cols = 9
        self.cells = [
                [Cell(row, col) for col in range(self.cols)]
                for row in range(self.rows)
            ]


    def set_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                number = board[row][col]
                self.cells[row][col].set_number(number)


    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.cells[row][col].number, end=" ")
            print()