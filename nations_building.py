import nations_quest

class BuildingList:
    def __init__(self, allegiance: nations_quest.NationsCountry, food_type, farm_enrichment, ore_enrichment):
        self.allegiance = allegiance
        self.farms: FarmList = FarmList(food_type, farm_enrichment)
        self.mines: MineList = MineList(ore_enrichment)
        self.centers: RecruitmentCenterList = RecruitmentCenterList()

    def gather_all(self, reason: str):
        self.allegiance.log_gain('food', self.farms.gather(), reason)
        self.allegiance.log_gain('ore', self.mines.gather(), reason)
    
    def recruit(self, num_soldiers: int, starting_level: int = 0):
        if self.centers.recruit(num_soldiers):
            self.allegiance.army.recruit_troops(num_soldiers, starting_level)
    
    def new_round(self):
        self.gather_all('new round beginning')
        self.centers.recruited = 0
    
    def build_farms(self, num_farms: int):
        if not self.farms.can_build(self.allegiance, num_farms): return None
    




class Buildings:
    def __init__(self, gold_cost: int, ore_cost: int, food_cost: int):
        pass
    
        self.gold_cost = gold_cost
        self.ore_cost = ore_cost
        self.food_cost = food_cost
    
    def can_build(self, nation: nations_quest.NationsCountry, num: int):
        if nation.gold < self.gold_cost * num:
            raise ValueError('(can_build) Not enough gold.')
            return False
        if nation.ore < self.ore_cost * num:
            raise ValueError('(can_build) Not enough ore.')
            return False
        if nation.food < self.food_cost * num:
            raise ValueError('(can_build) Not enough food.')
            return False
        return True
    
    

class FarmList(Buildings):
    def __init__(self, food_type: str, enrichment_val: int, starting_farms: int = 0):
        super().__init__(2,000,000, 500, 10,000)
        self.base_output = 200,000
        self.food_type = food_type
        self.enrichment_val = enrichment_val
        self.num_farms = starting_farms
    
    def gather(self):
        return self.base_output * self.enrichment_val * self.num_farms

class MineList(Buildings):
    def __init__(self, enrichment_val: int, starting_mines: int = 0):
        super().__init__(3,500,000, 500, 0)
        self.base_output = 5000
        self.enrichment_val = enrichment_val
        self.num_mines = starting_mines
    
    def gather(self):
        return self.base_output * self.enrichment_val * self.num_mines
    
class RecruitmentCenterList(Buildings):
    def __init__(self, num_centers: int = 0):
        super().__init__(4,000,000, 1,000, 0)
        self.num_centers = num_centers
        self.recruits_per_center = 5000
        self.recruited: int = 0
    
    def recruit(self, soldiers: int):
        max_recruits = self.num_centers * self.recruits_per_center
        if self.recruited + soldiers > max_recruits:
            raise ValueError('(recruitment_center) too many soldiers recruited.')
            return False
        self.recruited += soldiers
        return True