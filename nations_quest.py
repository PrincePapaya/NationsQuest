# hello there.

import nations_armies
import action_logs
import nations_agent

from typing import List

class NationsCountry:
    def __init__(self, name: str):
        self.name = name
        # standard resources
        self.food = 0
        self.population = 0
        self.stone = 0
        self.iron = 0
        self.gold = 0
        self.dedication = 0
        self.religion_name = ''
        self.knowledge_points = 0
        self.happiness = 50
        self.chaos_points = 0
        self.action_log = action_logs.ActionLog()

        # nonstandard resources
        # agents
        self.agents = nations_agent.Agency(self)
        self.counter_ops = 0
        self.missionary_efficiency = 2
        self.agent_jail: List[nations_agent.Agent] = []
        # buildings
        # army stuff
        self.army = nations_armies.NationalArmy()
        # research (researched and not)
        # enrichment values

    def __str__(self) -> str:
        return self.name

    def new_round(self):
        self.use_all_agents()

    def use_all_agents(self):
        for agent in self.agents:
            agent.use_agent()
    
    def set_religion(self, religion: str):
        self.religion_name = religion

    def see_log(self) -> str:
        output: List[str] = list()
        for item in self.action_log.get_log():
            output.append(str(item))
        return output
    
    def log_gain(self, resource: str, amount: int, reason: str):
        initial = getattr(self, resource, False)
        if initial == False:
            print('(log_gain) invalid resource')
            return None
        getattr(self, resource) += amount
        if (resource == 'religion') or (resource == 'happiness') and (initial + amount > 100):
            getattr(self, resource) = 100
            print('(log_gain) too much was gained')
        self.action_log.log_gain(resource, amount, getattr(self, resource), reason)
        print(self.action_log.get_log(0))

    def log_lose(self, resource: str, amount: int, reason: str):
        initial = getattr(self, resource, False)
        if initial == False: 
            print('invalid resource')
            return None
        if initial < amount: 
            print('invalid amount')
            return None
        getattr(self, resource) -= amount
        self.action_log.log_lose(resource, amount, getattr(self, resource), reason)
        print(self.action_log.get_log(0))




    def log_set(self, resource: str, amount: int, reason: str):
        initial = getattr(self, resource, False)
        if initial == False: 
            print('invalid resource')
            return None
        getattr(self, resource) = amount
        self.action_log.log_set(resource, initial, amount, reason)
        print(self.action_log.get_log(0))
    
    def log_capture(self, agent: nations_agent.Agent, other_nation):
        self.action_log.log_capture(agent, other_nation, True)
        agent.get_captured(self)

'''

    def see_log(self) -> str:
        output: list[str] = []
        for log in self.action_log:
            output.append(self.translate(log))
        return output

    def see_resource(self, resource: str) -> int:
        value = getattr(self, resource, False)
        if value == False: return -1
        return value

    def log_gain(self, resource: str, amount: int, reason: str) -> bool:
        initial = getattr(self, resource, False)
        if initial == False: return False
        getattr(self, resource, False) += amount
        if (resource == 'religion') or (resource == 'happiness') and (initial + amount > 100):
            getattr(self, resource, False) = 100
        self.add_log('gain', amount, resource, initial + amount, reason)
        return True
    
    def log_lose(self, resource: str, amount: int, reason: str) -> bool:
        initial = getattr(self, resource, False)
        if initial == False: return False
        if initial < amount: return False
        getattr(self, resource, False) -= amount
        self.add_log('lose', amount, resource, initial - amount, reason)
        return True
    
    def log_set(self, resource: str, amount: int, reason: str):
        initial = getattr(self, resource, False)
        if initial == False: return False
        getattr(self, resource, False) = amount
        self.add_log('set', initial, resource, amount, reason)
        return True

    def add_log(self, verb: str, amount: int, resource: str, final: int, reason: str) -> log_entry:
        log: log_entry = time.time(), verb, amount, resource, final, reason
        self.action_log.append(log)
        return log

'''

class NationsGame:
    def __init__(self) -> None:
        self.nations_list: list[NationsCountry] = []
        self.round: int = 0

    def add_country(self, nation: NationsCountry):
        self.nations_list.append(nation)
    
    def add_new_country(self, name: str):
        country: NationsCountry = NationsCountry(name)
        self.add_country(country)
    
    def get_country(self, name: str) -> NationsCountry:
        for country in self.nations_list:
            if country.name == name:
                return country
        raise ValueError('(get_country) invalid country name')
    
    # keep track of:
    # research available
    # fights
    # trades
    # agent actions
    # wall levels
    # borders