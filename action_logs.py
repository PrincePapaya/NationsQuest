import time
import nations_agent
import nations_quest

from typing import List

class ActionLog:
    def __init__(self):
        self.history: List[LogEntry] = []
    
    def get_log(self, index: int):
        return self.history[len(self.history) - index]
    
    def get_logs(self):
        return self.history
    
    def log_gain(self, resource_type: str, amount: int, final_value: int, reason: str):
        new_log = ResourceGain(resource_type, amount, final_value, reason)
        self.history.append(new_log)
    
    def log_lose(self, resource_type: str, amount: int, final_value: int, reason: str):
        new_log = ResourceLose(resource_type, amount, final_value, reason)
        self.history.append(new_log)

    def log_set(self, resource_type: str, prior_value: int, new_value: int, reason: str):
        new_log = ResourceSet(resource_type, prior_value, new_value, reason)
        self.history.append(new_log)

    def log_capture(self, agent: nations_agent.Agent, other_nation: nations_quest.NationsCountry, capturing: bool):
        new_log = AgentCapture(agent, other_nation, capturing)
        self.history.append(new_log)



class LogEntry:
    def __init__(self):
        self.time = time.time()
        self.action_type: str

    # types of actions:
    # gain, lose, set, agent, army, upgrade, train
    
    def get_type(self):
        return self.action_type
    def __str__(self):
        return '(action_logs) undefined log type'
    
class NewRound(LogEntry):
    def __init__(self, round: int):
        super().__init__()
        self.round = round
    
    def __str__(self):
        return f'**New Round: {round}**'

class AgentAction(LogEntry):
    def __init__(self, agent: nations_agent.Agent):
        super().__init__()
        self.agent = agent

class AgentDefend(AgentAction):
    def __init__(self, agent: nations_agent.Agent):
        super().__init__(agent)
        

class AgentCapture(LogEntry):
    def __init__(self, agent: nations_agent.Agent, other_nation: nations_quest.NationsCountry, capturing: bool):
        super.__init__()
        self.agent = agent
        self.capturing = capturing
        self.other_nation = other_nation
    
    def __str__(self):
        if (self.capturing):
            return f'Captured {self.agent.agent_type} {self.agent.name} from {self.other_nation}. {time.ctime(self.time)}'
        else:
            return f'{self.agent.agent_type} {self.agent.name} went missing in {self.other_nation}. {time.ctime(self.time)}'

class AssignAgent(LogEntry):
    def __init__(self, agent: nations_agent.Agent, destination: nations_quest.NationsCountry):
        super().__init__()
        self.agent = agent
        self.destination = destination

    def __str__(self):
        return f'assigned {self.agent} as a {self.agent.agent_type} to {self.destination}. {time.ctime(self.time)}'



class ResourceChange(LogEntry):
    def __init__(self, resource: str, amount: int, final: int, reason: str):
        super().__init__()
        self.resource_type = resource
        self.amount = amount
        self.final_value = final
        self.reason = reason
        self.verb: str

    def __str__(self):
        return f'{self.verb} {self.amount} {self.resource_type} due to {self.reason}, new total of {self.final_value} {self.resource_type}. {time.ctime(self.time)}'

class ResourceGain(ResourceChange):
    def __init__(self, resource: str, amount: int, final: int, reason: str):
        super().__init__(self, resource, amount, final, reason)
        self.action_type = 'Gain'
        self.verb = 'Gained'

class ResourceLose(ResourceChange):
    def __init__(self, resource: str, amount: int, final: int, reason: str):
        super().__init__(self, resource, amount, final, reason)
        self.action_type = 'Lose'
        self.verb = 'Lost'

class ResourceSet(ResourceChange):
    def __init__(self, resource: str, amount: int, final: int, reason: str):
        super().__init__(self, resource, amount, final, reason)
        self.action_type = 'Set'
        self.verb = 'Overwrote'
    