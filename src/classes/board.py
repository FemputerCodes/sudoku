from classes.cell import Cell

class Board:
    def __init__(self):
        self.rows = 9
        self.cols = 9
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.puzzle = [
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
        self.cells = [
                [Cell(row, col) for col in range(self.cols)]
                for row in range(self.rows)
            ]

        for row in range(self.rows):
            for col in range(self.cols):
                number = self.puzzle[row][col]
                self.cells[row][col].set_number(number)


    def update(self, row, col, choice):
        if choice in self.choices:
            self.cells[row][col].insert_choice(choice)


    def validate(self, row, col, choice):
        validation_results = [False, False, False]
        validation_results[0] = self.__check_row(row, choice)
        validation_results[1] = self.__check_col(col,choice)
        validation_results[2] = self.__check_subgrid(row, col, choice)
        for result in validation_results:
            if not result:
                return False
        return True


    def __check_row(self, row, choice):
        for col in range(self.cols):
            if self.puzzle[row][col] == choice:
                return False
        return True


    def __check_col(self, col, choice):
        for row in range(self.rows):
            if self.puzzle[row][col] == choice:
                return False
        return True
        

    def __check_subgrid(self, row, col, choice):
        """
        Using  interger division to find the subgrid.
        Integer division returns the quotient as an integer.
        This function returns the start row and start column of the
        subgrid.
        """
        #determine the subgrid of the cell
        subgrid_row = row // 3
        subgrid_col = col // 3
        start_row = subgrid_row * 3
        start_col = subgrid_col * 3
        # check subgrid
        for sub_row in range(start_row, start_row + 3):
            for sub_col in range(start_col, start_col + 3):
                if self.puzzle[sub_row][sub_col] == choice:
                    return False
        return True
    
    
    def solve(self, row, col):
        # base case 1: end of grid (success!)
        if row == len(self.puzzle):
            return True
        # base case 2: out of bounds, go to next row
        if col == len(self.puzzle):
            return self.solve(row+1, 0)
        # base case 3: not empty, go to next cell
        if self.puzzle[row][col] != 0:
            return self.solve(row, col+1)
        # try possible choices
        for choice in self.choices:
            if self.validate(row, col, choice):
                self.cells[row][col].insert_choice(choice)
                if self.solve(row, col+1):
                    return True
        # exhausted all possibilities (backtrack)
        self.cells[row][col].remove_choice()
        return False

    
    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.cells[row][col].get_number(), end=" ")
            print()