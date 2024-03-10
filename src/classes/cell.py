class Cell:
    def __init__(self, row, col):
        self.row = row
        self.column = col
        self.number = 0
        self.fixed = False
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    
    def set_number(self, a_number):
        self.number = a_number
        if a_number != 0:
            self.fixed = True

    
    def insert_choice(self, a_choice):
        if self.fixed is False:
            self.number = a_choice


    def remove_choice(self):
        if self.fixed is False:
            self.number = 0
