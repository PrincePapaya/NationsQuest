#hello there.

import random
import nations_quest

class NationalArmy:
    def __init__(self):
        self.max_level = 0
        self.weapons = 0
        self.armor = 0
        self.divisions: list[ArmyDivision] = [
            ArmyDivision(0, 0)
        ]
        self.increase_max_level()
    
    def increase_max_level(self):
        self.max_level += 1
        self.divisions.append(ArmyDivision(0, self.max_level))
    
    def train_troops(self, new_level, troops_trained):
        if new_level > self.max_level or new_level < 1:
            print('(nations_armies) invalid level')
            return False
        old_level = new_level - 1
        if self.divisions[old_level].get_troops > troops_trained or troops_trained < 0:
            print('(nations_armies) invalid amount')
            return False
        self.divisions[old_level].lose_troops(troops_trained)
        self.divisions[new_level].gain_troops(troops_trained)

    def get_total_power(self):
        power = 0
        for division in self.divisions:
            power += division.calculate_power(self.weapons)   
        return power     
    
    def recruit_troops(self, num_troops: int, base_level:int = 0):
        self.divisions[base_level].gain_troops(num_troops)




class ArmyDivision:
    def __init__(self, num_troops: int, division_level: int):
        self.num_troops = num_troops
        self.level = division_level
    
    def get_troops(self):
        return self.num_troops

    def gain_troops(self, number: int):
        self.num_troops += number

    def lose_troops(self, number: int):
        if self.num_troops < number:
            print('(nations_armies) invalid number')
            return False
        self.num_troops -= number
    
    def calculate_power(self, weapons: int):
        skill = weapons + self.level
        return skill * self.num_troops


class Battlefield:
    def __init__(self, attacker: nations_quest.NationsCountry, defender: nations_quest.NationsCountry) -> None:
        pass
