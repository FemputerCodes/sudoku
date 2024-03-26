# Sudoku

Welcome to the Sudoku progam! This application allows you to play and solve a Sudoku puzzle.
If you need to review the rules of Sudoku, consider visiting the [Sudoku Wikipedia Page](https://simple.wikipedia.org/wiki/Sudoku).

# Prerequistes
Have [Python](https://www.python.org/downloads/) and pip installed on your computer.

# Getting Started
To get started, download the code and open the directory in VS Code. Then follow these steps in terminal:

1. Run `make install` to set up the necessary dependencies.
2. Activate the virtual environment in your shell (you'll need to do this whenever you open a new shell).
   `source ./.venv/bin/activate`
3. Ensure that the Python interpreter is set to "Python 3.11.6 ('.venv':venv) ./venv/bin/python".
4. Run `make run` to run the program


## Learn About the Backtracking Algorithm

The core functionality of the Sudoku Solver is based on the backtracking algorithm. The basic idea is to explore all possible solutions to the problem and backtrack when the current solution reaches a point where it cannot be extended to a valid one. In the context of Sudoku, the solver examines each row, making choices and validating them until a solution is found.

### 3 Key Elements of Backtracking

1. Choices: Fill the empty cells by making a choice. Available choices range from 1 to 9.
2. Constaints: A cell cannot contain a number that already exists in its current row, column, or subgrid.
3. Goal: Successfully solve the Sudoku puzzle.

Enjoy the Sudoku-solving experience, and feel free to reach out if you have any questions or suggestions!

Meghan Leicht
