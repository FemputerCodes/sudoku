class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.__number = 0
        self.__fixed = False
        self.__valid = False
    
    def set_number(self, a_number):
        self.__number = a_number

    def set_fixed(self, is_fixed):
        self.__fixed = is_fixed

    def get_number(self):
        return self.__number

    def get_fixed(self):
        return self.__fixed
    
    def insert_choice(self, a_choice):
        if not self.__fixed:
            self.__number = a_choice

    def remove_choice(self):
        if not self.__fixed:
            self.__number = 0
