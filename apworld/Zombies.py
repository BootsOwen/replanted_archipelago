from dataclasses import dataclass, field
import copy

@dataclass
class ZombieStateChange:
    name: str
    health: int = 270
    helmet_health: int = 0
    shield_health: int = 0
    speed: int = 0
    attack: int = 100

@dataclass
class Zombie:
    name: str
    zombie_id: int
    weight: int = 4000
    value: int = 1
    aquatic: bool = False
    health: int = 270
    helmet_health: int = 0
    shield_health: int = 0
    balloon_health: int = 0
    speed: int = 0
    attack: int = 0
    state_changes: list[ZombieStateChange] = field(default_factory=list)

    def __post_init__(self):
        self.unmodified = copy.deepcopy(self)

    def generate_multiplier(self, world):
        return world.random.randint(0, 1) + (world.random.random() ** 2)

    def reduce_importance(number, amount):
        return number + (1 - number) * amount

    def randomise_stats(self, world):
        self.speed_multiplier = self.generate_multiplier(world)
        self.health_multiplier = self.generate_multiplier(world)
        self.attack_multiplier = self.generate_multiplier(world)
        value_modifiers = [self.speed_multiplier, self.health_multiplier, reduce_importance(self.attack_multiplier, 0.7)]

        if self.helmet_health > 0:
            self.helmet_health_multiplier = self.generate_multiplier(world)
            value_modifiers.append(self.helmet_health_multiplier)
        if self.shield_health > 0:
            self.shield_health_multiplier = self.generate_multiplier(world)
            value_modifiers.append(self.shield_health_multiplier)
        if self.balloon_health > 0:
            self.balloon_health_multiplier = self.generate_multiplier(world)
            value_modifiers.append(reduce_importance(self.balloon_health_multiplier, 0.9))
        
        self.value_multiplier = sum(all_multipliers)/len(all_multipliers)

def create_zombies():
    return {
        "Normal": Zombie(name = "Normal", zombie_id = 0),
        "Flag": Zombie(name = "Flag", zombie_id = 1, weight = 0),
        "Conehead": Zombie(name = "Conehead", zombie_id = 2, value = 2, helmet_health = 370),
        "Polevaulter": Zombie(name = "Polevaulter", zombie_id = 3, weight = 2000, value = 2, health = 335),
        "Buckethead": Zombie(name = "Buckethead", zombie_id = 4, weight = 3000, value = 4, helmet_health = 1100),
        "Newspaper": Zombie(name = "Newspaper", zombie_id = 5, weight = 1000, value = 2, shield_health = 150),
        "ScreenDoor": Zombie(name = "ScreenDoor", zombie_id = 6, weight = 3500, value = 4, shield_health = 1100),
        "Football": Zombie(name = "Football", zombie_id = 7, weight = 2000, value = 7, helmet_health = 1500),
        "Dancer": Zombie(name = "Dancer", zombie_id = 8, weight = 1000, value = 5, health = 340),
        "BackupDancer": Zombie(name = "BackupDancer", zombie_id = 9, weight = 0),
        "DuckyTube": Zombie(name = "DuckyTube", zombie_id = 10, aquatic = True, weight = 0),
        "Snorkel": Zombie(name = "Snorkel", zombie_id = 11, aquatic = True, weight = 2000, value = 3),
        "Zomboni": Zombie(name = "Zomboni", zombie_id = 12, weight = 2000, value = 7, health = 1350),
        "Bobsled": Zombie(name = "Bobsled", zombie_id = 13, weight = 2000, value = 3),
        "DolphinRider": Zombie(name = "DolphinRider", zombie_id = 14, aquatic = True, weight = 1500, value = 3, health = 340),
        "JackInTheBox": Zombie(name = "JackInTheBox", zombie_id = 15, weight = 1000, value = 3, health = 340),
        "Balloon": Zombie(name = "Balloon", zombie_id = 16, weight = 2000, value = 2, health = 190, balloon_health = 20),
        "Digger": Zombie(name = "Digger", zombie_id = 17, weight = 1000, value = 4, helmet_health = 100),
        "Pogo": Zombie(name = "Pogo", zombie_id = 18, weight = 1000, value = 4, health = 340),
        "Yeti": Zombie(name = "Yeti", zombie_id = 19, weight = 1, value = 4, health = 1350),
        "Bungee": Zombie(name = "Bungee", zombie_id = 20, weight = 1000, value = 3, health = 450),
        "Ladder": Zombie(name = "Ladder", zombie_id = 21, weight = 1000, value = 4, health = 340, shield_health = 500),
        "Catapult": Zombie(name = "Catapult", zombie_id = 22, weight = 1500, value = 5, health = 651),
        "Gargantuar": Zombie(name = "Gargantuar", zombie_id = 23, weight = 1500, value = 10, health = 3000),
        "Imp": Zombie(name = "Imp", zombie_id = 24, weight = 3000, health = 190),
        "Boss": Zombie(name = "Boss", zombie_id = 25, weight = 0, health = 40000),
        "PeaHead": Zombie(name = "PeaHead", zombie_id = 26, weight = 4000, value = 1, health = 190),
        "WallnutHead": Zombie(name = "WallnutHead", zombie_id = 27, weight = 3000, value = 4, health = 1290),
        "JalapenoHead": Zombie(name = "JalapenoHead", zombie_id = 28, weight = 1000, value = 3, health = 340),
        "GatlingHead": Zombie(name = "GatlingHead", zombie_id = 29, weight = 2000, value = 3, health = 190),
        "SquashHead": Zombie(name = "SquashHead", zombie_id = 30, weight = 2000, value = 3, health = 190),
        "TallnutHead": Zombie(name = "TallnutHead", zombie_id = 31, weight = 2000, value = 4, health = 2390),
        "GigaGargantuar": Zombie(name = "GigaGargantuar", zombie_id = 32, weight = 6000, value = 10, health = 6000),
        "Zombatar": Zombie(name = "Zombatar", zombie_id = 33, weight = 0),
        "Target": Zombie(name = "Target", zombie_id = 34, weight = 0),
        "TrashCan": Zombie(name = "TrashCan", zombie_id = 35, weight = 4000, shield_health = 800)
    }