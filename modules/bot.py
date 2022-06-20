import json

from enum import Enum, auto

from .bdo import Ability
from .utils import grab_screen


class BotState(Enum):
    INIT = auto()
    SEARCHING = auto()
    NAVIGATING = auto()
    KILLING = auto()


class BlackDesertBot:
    state = None
    buff_queue = []
    food_queue = []
    skill_queue = []
    # threading properties
    stopped = True
    lock = None

    def __init__(self):
        self.state = BotState.INIT
        self.buffs = self.load_abilities(ability_type='buff')
        self.foods = self.load_abilities(ability_type='food')
        self.skills = self.load_abilities(ability_type='skill')

    def load_abilities(self, ability_type='skill') -> list[Ability]:
        path = f'data/{ability_type}s.json'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data = [Ability(*tuple(i.values())) for i in data]
            return data

    def find_target(self):
        pass

    def follow_target(self):
        pass

    def move_to_target(self):
        pass

    def kill_target(self):
        pass

    def use_buff(self):
        pass

    def use_food(self):
        pass

    def use_skill(self):
        pass

    def run(self):
        pass
