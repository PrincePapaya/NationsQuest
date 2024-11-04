import random

class Die:
    def __init__(self, sides: int):
        self.sides = sides
    
    def roll(self) -> int:
        return random.randint(1, self.sides)