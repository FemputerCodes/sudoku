class Cell:
    """Represents a cell in a Sudoku board."""

    def __init__(self, row: int, col: int):
        """Initialize a cell with its row and column position.
        
        Args:
            row (int): The row index of the cell.
            col (int): The col index of the cell.
        """
        self.row = row
        self.col = col
        self.__number = 0
        self.__fixed = False
        self.__valid = False
    
    def set_number(self, a_number: int) -> None:
        """Set the number of the cell.

        Args:
            a_number (int): The number to set for the cell.
        """
        self.__number = a_number

    def set_fixed(self, is_fixed: bool) -> None:
        """Set the fixed status of the cell.

        Args:
            is_fixed (bool): True if the cell is fixed, False otherwise.
        """
        self.__fixed = is_fixed
        if is_fixed:
            self.__valid = True

    def set_valid(self, is_valid: bool) -> None:
        """Set the validity status of the cell.

        Args:
            is_valid (bool): True if the cell is valid, False otherwise.
        """
        self.__valid = is_valid

    def get_number(self) -> int:
        """Get the number of the cell.

        Returns:
            int: The number of the cell.
        """
        return self.__number

    def get_fixed(self) -> bool:
        """Check if the cell is fixed.

        Returns:
            bool: True if the cell is fixed, False otherwise.
        """
        return self.__fixed
    
    def get_valid(self) -> bool:
        """Check if the cell is valid.

        Returns:
            bool: True if the cell is valid, False otherwise.
        """
        return self.__valid
    
    def insert_choice(self, a_choice: int) -> None:
        """Insert a choice into the cell, if it's not fixed.

        Args:
            a_choice (int): The choice to insert into the cell.
        """
        if not self.__fixed:
            self.__number = a_choice

    def remove_choice(self) -> None:
        """Remove the choice from the cell, if it's not fixed."""
        if not self.__fixed:
            self.__number = 0
