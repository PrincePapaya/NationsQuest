import nations_quest
from nations_quest import NationsCountry
import random
import action_logs
from action_logs import LogEntry
from typing import List, Tuple, Set
from abc import ABC, abstractmethod

# Agent types: missionaries, spies, recruiters, counter ops, thieves

# revised agent types: missionaries, spies, mages, counter ops, recruiters,
# thieves, explorers, champions, smiths, inscribers, alchemists, travel agents, medics

# importance 0: counter ops
# importance 1: harmful
# importance 2: meddling
# importance 3: internal



class Agency:
    def __init__(self, affiliation: NationsCountry):
        self.affiliation = affiliation
        self.agents: List[Agent] = list()
        self.agent_types: Set[str] = set()
        self.action_list = list()
        self.spent = 0
        self.defending_agents = 0

        # usually internal variables
        self.counter_ops_efficiency = 1

    def gain_agent(self):
        self.agents.append(Agent(self.affiliation))
    
    def remove_action(self, action: LogEntry):
        pass
        # raise error if action isn't in internal reference log
        # removes an action from the internal reference log
        # decrease spent agent count by 1

    
    def assign_agent(self, mission: str, target: NationsCountry):
        if target == None:
            target = self.affiliation
        mission = mission.lower()
        if self.spent >= len(self.agents):
            raise ValueError('not enough agents')
        if mission not in self.agent_types:
            raise TypeError('agent type unavailable')
        
        if mission == 'counter ops':
            importance = 0
            self.action_list.append(tuple(importance, self.counter_ops(target)))

        if mission == 'missionary':
            pass

        if mission == "mage":
            pass

        if mission == "recruiter":
            pass

        if mission == "spy":
            pass
        # create a new internal reference log of what the agent is doing
        # increase spent agent count by 1
        # returns the reference log

        self.spent += 1


    
    def defend(self) -> int:
        'to be executed before calling execute_orders. ensures counter ops are counter opping correctly.'
        defending = 0
        for log in self.action_list:
            if log.importance == 0:
                defending += 1
        return defending

        # find all instances of counter ops in internal log
        # tally and remove them
        # return tally to parent country

    def execute_orders(self):
        'only execute after calling defend, to ensure counter ops are already in place.'

        # collects all actions done by agents, passes them to parent country to carry out
        # agent actions should be orderd by maliciousness, for defending country's counter ops
        # resets all agents to being free
        # clears internal action log
    
    # specific agent actions
    def missionary(self, target: NationsCountry, devotion_change_val: int):
        if target.religion_name.lower() == self.affiliation.religion_name.lower():
            target.religion += devotion_change_val
        else:
            target.religion -= devotion_change_val
        
    
    def counter_ops(self, target: NationsCountry):
        target.agents.defending_agents += 1


class Action(ABC):
    def __init__(self, importance: int):
        self.importance = importance

    @abstractmethod
    def execute(self):
        pass

class Missionary(Action):
    def __init__(self, target: NationsCountry, devotion_change_val: int):
        super().__init__(2)
        self.target = target
        self.devotion_change_val = devotion_change_val
    
    def execute(self):
        pass


class RevisedAgent:
    def __init__(self):
        self.name = random.choice(names)
        
        # usually internal variables
        self.counter_ops_efficiency = 1
        self.thief_catch_chance = 10

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