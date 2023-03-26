class CodProfile:
    def __init__(self, gamer_tag, kills, deaths, rank, platform, weapon, id=None):
        self.gamer_tag=gamer_tag
        self.kills=kills
        self.deaths=deaths
        self.rank=rank
        self.platform=platform
        self.weapon=weapon
        self.id=id

    def calculate_kd_ratio(self) -> float:
            kd_ratio = self.kills / self.deaths
            return round(kd_ratio, 2)  # round to two decimal places  