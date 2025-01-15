#hello there

from typing import Dict


class GloryPoints:
    def __init__(self):
        self.points: Dict[str: int] = {}

    
    def add_country(self, country_name: str):
        if country_name not in self.points:
            self.points[country_name] = 0
    
    def get_country(self, country_name: str):
        if country_name in self.points:
            return self.points[country_name]