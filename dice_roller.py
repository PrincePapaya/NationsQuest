import random

class Die:
    def __init__(self, sides: int):
        self.sides = sides
        self.value = 0
    
    def roll(self) -> int:
        self.value = random.randint(1, self.sides)
        return self.value
    
class Modifier:
    def __init__(self, modifier: int):
        self.bonus = modifier