import nations_quest
import random

# Agent types: missionaries, spies, recruiters, counter ops, thieves


class Agent:
    def __init__(self, affiliation: nations_quest.NationsCountry):
        self.name = random.choice(names)
        self.affiliation: nations_quest.NationsCountry = affiliation
        self.spent: bool = False
        self.set_action = None
        self.agent_type = 'unknown type'
        self.target: nations_quest.NationsCountry = None
    
    def __str__(self):
        return self.name
    
    def assign_missionary(self, target: nations_quest.NationsCountry):
        if self.spent == True:
            print('(nations_agent) invalid action')
            return None
        self.spent = True
        self.agent_type = 'missionary'
        if self.affiliation.religion_name == target.religion_name:
            self.set_action = self.missionary_bolster(target, self.affiliation.missionary_efficiency)
        else: self.set_action = self.missionary_atk(target, self.affiliation.missionary_efficiency)

    def assign_counter_ops(self, target: nations_quest.NationsCountry):
        if self.spent == True:
            print('(nations_agent) invalid action')
            return
        self.spent = True
        self.target = target
        self.target.defending_agents += 1
        self.agent_type = 'counter ops'

    def revoke_assignment(self):
        if self.spent == False: 
            print('(nations_agent) no assignment')
            return
        if self.set_action == None: 
            self.target.defending_agents -= 1
        self.target = None
        self.set_action = None
        self.spent = False
        self.agent_type = 'unknown type'

    def use_agent(self):
        if self.spent == False: return None
        self.spent = False
        if self.set_action != None: 
            self.set_action
        self.set_action = None
        self.agent_type = 'unknown type'
        self.target = None

    def missionary_atk(self, target: nations_quest.NationsCountry, efficiency):
        if self.attack_defenses(target):
            target.log_lose('religion', efficiency, f'enemy missionary from {self.affiliation.name}')

    def missionary_bolster(self, target: nations_quest.NationsCountry, efficiency):
        target.log_gain('religion', efficiency, f'friendly missionary from {self.affiliation.name}')

    def attack_defenses(self, target: nations_quest.NationsCountry) -> bool:
        if target.defending_agents > 0:
            target.defending_agents -= 1
            target.log_capture(self, self.affiliation)
            return False
        return True

    def get_captured(self, capturer: nations_quest.NationsCountry):
        if self.affiliation == capturer: return None
        self.affiliation.agents.remove(self)
        capturer.agent_jail.append(self)

    


names = [
    'Ableard',
    'Benjamin',
    'Bill',
    'Charles',
    'Colin',
    'Dave',
    'Donald',
    'Gary',
    'Hugh',
    'James',
    'Jerry',
    'Jichael',
    'Joe',
    'John',
    'Keagan',
    'Kevin',
    'Michael',
    'Reginald',
    'Steve',
    'Stewart',
    
]