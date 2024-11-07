#chaos event characters

class Character:
    def __init__(self, character_name: str, main_stat: str, char_class: str = "<insert class here>", race: str = "<insert race here>"):
        self.name = character_name
        self.level = 1
        self.main_stat = main_stat
        self.char_class = char_class
        self.race = race

        self.strength = 1
        self.dexterity = 1
        self.constitution = 1
        self.intelligence = 1
        self.wisdom = 1
        self.charisma = 1

        self.stats_to_allocate = 4

        self.max_hp = 15 + self.constitution * 5
        self.hitpoints = self.max_hp

    def __str__(self):
        return_string = ''
        #overview
        return_string = return_string + f'{self.name}, {self.race} {self.char_class}\nLevel {self.level}\n\n'
    
        #stats
        return_string = return_string + f'Strength: {self.strength}\nDexterity: {self.dexterity}\n'
        return_string = return_string + f'Constitution: {self.constitution}\nIntelligence: {self.intelligence}\n'
        return_string = return_string + f'Wisdom: {self.wisdom}\nCharisma: {self.charisma}\n\n'

        return_string = return_string + f'AC: {self.get_AC()}\nHP: {self.hitpoints}/{self.max_hp}'

        return_string = return_string + f'Attacks:'

        return return_string
        
    
    def get_AC(self) -> int:
        "returns 10 + wisdom/2 + (str or dex)/2. All division rounds down."
        base_AC = 10
        mental_component = self.wisdom // 2
        if self.strength > self.dexterity:
            physical_component = self.strength // 2
        else:
            physical_component = self.dexterity // 2
        return base_AC + mental_component + physical_component
    
    def assign_stat(self, stat: str, amount: int):
        if self.stats_to_allocate < amount:
            raise ValueError("Not enough available statpoints.")
        ability_to_change = getattr(self, stat.lower())
        if ability_to_change == None:
            raise ValueError("Invalid ability.")
        else: 
            ability_to_change += amount
            self.stats_to_allocate -= amount


    def level_up(self):
        self.level += 1
        self.stats_to_allocate += 2

class Attack:
    def __init__(self, attack_name: str, skill_modifier: int):
        self.attack_name = attack_name
        self.damage = "not implemented yet"
    
    def __str__(self):
        return f'{self.attack_name}: {self.damage} damage'