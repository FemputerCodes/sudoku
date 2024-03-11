class Solver():
    def __init__(self, grid):
        self.board = grid.board

    def solve(self, row, col):
        # base case 1: end of grid (success!)
        if row == len(self.board.puzzle):
            return True
        # base case 2: out of bounds, go to next row
        if col == len(self.board.puzzle):
            return self.solve(row + 1, 0)
        # base case 3: not empty, go to next cell
        if self.board.puzzle[row][col] != 0:
            return self.solve(row, col + 1)
        # try possible choices
        for choice in self.choices:
            if self.board.validate(row, col, choice):
                self.board.update(row, col, choice)
                if self.solve(row, col + 1):
                    return True
        # exhausted all possibilities (backtrack)
        self.board.update(row, col, 0)
        return False