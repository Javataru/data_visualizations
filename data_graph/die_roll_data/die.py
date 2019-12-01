from random import randint

class Die():
    """class for a single die"""
    def __init__(self, num_sides=12):
        """assume a 12 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """return random value from 1 to number of sides"""
        return randint(1, self.num_sides)