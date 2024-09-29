#greetings.

import nations_quest

class ResearchTask:
    def __init__(self, round = int, requirement = None) -> None:
        self.round_unlocked = round
        self.required_task = requirement