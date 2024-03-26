from .cell import Cell
from typing import Tuple

class Board:
    """Represents a Sudoku board."""

    def __init__(self):
        """Initializes a Sudoku board."""
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
                if number != 0:
                    self.cells[row][col].set_fixed(True)


    def get_cell(self, row: int, col: int) -> Cell:
        """Get the cell at the specified row and column.
        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            Cell: The cell at the specified row and column.
        """
        return self.cells[row][col]
    

    def update(self, row: int, col: int, choice: int) -> None:
        """Update the cell at the specified row and column with a choice.
        
        Args:
            row (int): The row index.
            col (int): The column index.
            choice (int): The choice to update the cell with.
        """
        if not self.cells[row][col].get_fixed():
            if choice in self.choices:
                self.cells[row][col].insert_choice(choice)
                self.puzzle[row][col] = choice
            if choice == 0:
                self.cells[row][col].remove_choice()
                self.puzzle[row][col] = choice


    def get_next(self, row: int, col: int) -> Tuple:
        """Get the next cell coordinates to solve.
        
        Args:
            row (int): The current row index.
            col (int): The current column index.

        Returns:
            Tuple: The coordinates (row, col) of the next cell to solve.
        """
        # base case: end of puzzle
        if (row > 8):
            return (0, 0)
        # base case: end of the row
        if (col > 8):
            return self.get_next(row + 1, 0)
        # base case: next is fixed
        if not self.cells[row][col].get_fixed():
            return (row, col)
            
        return self.get_next(row, col+1)


    def validate(self, row: int, col: int, choice: int) -> bool:
        """Validate a choice for the cell at the specified row and column.
        
        Args:
            row (int): The row index.
            col (int): The column index.
            choice (int): The choice to validate.

        Returns:
            bool: True if the choice is valid, False otherwise.
        """
        validation_results = [False, False, False]

        if choice == 0:
            return False
        
        validation_results[0] = self.__check_row(row, col, choice)
        validation_results[1] = self.__check_col(row, col, choice)
        validation_results[2] = self.__check_subgrid(row, col, choice)
        for result in validation_results:
            if not result:
                if not self.cells[row][col].get_fixed():
                    self.cells[row][col].set_valid(False)
                return False
        self.cells[row][col].set_valid(True)
        return True


    def __check_row(self, row: int, col: int, choice: int) -> bool:
        """Check if the choice is valid in the same row.

        Args:
            row (int): The row index.
            col (int): The column index.
            choice (int): The choice to validate.

        Returns:
            bool: True if the choice is valid, False otherwise. 
        """
        for j in range(self.cols):
            if j != col:
                if self.puzzle[row][j] == choice:
                    return False
        return True


    def __check_col(self, row: int, col: int, choice: int) -> bool:
        """Check if the choice is valid in the same column.

        Args:
            row (int): The row index.
            col (int): The column index.
            choice (int): The choice to validate.

        Returns:
            bool: True if the choice is valid, False otherwise.
        """
        for i in range(self.rows):
            if i != row:
                if self.puzzle[i][col] == choice:
                    return False
        return True
        

    def __check_subgrid(self, row: int, col: int, choice: int) -> bool:
        """Check if the choice is valid in the subgrid by using integer division.
         Integer division returns the quotient as an integer.

        Args:
            row (int): The row index.
            col (int): The column index.
            choice (int): The choice to validate.

        Returns:
            bool: True if the choice is valid, False otherwise.
        """
        subgrid_row = row // 3
        subgrid_col = col // 3
        start_row = subgrid_row * 3
        start_col = subgrid_col * 3
        for sub_row in range(start_row, start_row + 3):
            for sub_col in range(start_col, start_col + 3):
                if sub_row != row and sub_col != col:
                    if self.puzzle[sub_row][sub_col] == choice:
                        return False
        return True


    def solve(self, row: int, col: int) -> bool:
        """Solve the Sudoku puzzle recursively using the backtracking algorithm.

        Args:
            row (int): The current row index.
            col (int): The current column index.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        # base case 1: end of grid (success!)
        if row == len(self.puzzle):
            return True
        # base case 2: out of bounds, go to next row
        if col == len(self.puzzle):
            return self.solve(row + 1, 0)
        # base case 3: not empty, go to next cell
        if self.puzzle[row][col] != 0:
            return self.solve(row, col + 1)
        # try possible choices
        for choice in self.choices:
            if self.validate(row, col, choice):
                self.update(row, col, choice)
                if self.solve(row, col + 1):
                    return True
        # exhausted all possibilities (backtrack)
        self.update(row, col, 0)
        return False
    
    
    def display(self) -> None:
        """Prints the Sudoku board."""
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.cells[row][col].get_number(), end=" ")
            print()