import pytest

from unittest import TestCase

from ..bdo import Ability
from ..bot import BotState, BlackDesertBot


class TestBotState(TestCase):
    def setUp(self):
        self.state_1 = BotState.INIT
        self.state_2 = BotState.SEARCHING
        self.state_3 = BotState.KILLING

    def test_types(self):
        assert self.state_1.name == 'INIT'
        assert isinstance(self.state_1, BotState)
        assert self.state_2.name == 'SEARCHING'
        assert isinstance(self.state_2, BotState)
        assert self.state_3.name == 'KILLING'
        assert isinstance(self.state_3, BotState)


class TestBlackDesertBot(TestCase):
    def setUp(self):
        self.bot = BlackDesertBot()

    def test_state(self):
        assert self.bot.state == BotState.INIT

    def test_load_abilities(self):
        buffs = self.bot.load_abilities(ability_type='guard_buff')
        foods = self.bot.load_abilities(ability_type='guard_food')
        skills = self.bot.load_abilities(ability_type='guard_skill')
        assert isinstance(buffs, list)
        assert isinstance(foods, list)
        assert isinstance(skills, list)
        assert isinstance(self.bot.buffs[0], Ability)
        assert isinstance(self.bot.foods[0], Ability)
        assert isinstance(self.bot.skills[0], Ability)

    @pytest.mark.slow
    def test_use_ability(self):
        for skill in self.bot.skills:
            self.bot.use_ability(skill)

    def test_filter_ability_cooldowns(self):
        ability_cooldowns = [
            (Ability(name='Проекция', keybind=['t'], type='skill', icon='', cooldown=15, duration=0.5, disabled=False), '2022-06-22 15:56:17.800236'),
            (Ability(name='Лавовое Озеро', keybind=['e'], type='skill', icon='', cooldown=15, duration=0.3, disabled=False), '2022-06-22 15:56:18.284364'),
            (Ability(name='Огненная Ярость', keybind=['w+', 'f'], type='skill', icon='', cooldown=6, duration=1.5, disabled=False), '2022-06-22 15:56:20.052835'),
            (Ability(name='Очаг Пожара', keybind=['space+', 'f'], type='skill', icon='', cooldown=6, duration=1, disabled=False), '2022-06-22 15:56:23.924626')]
        self.bot.ability_cooldowns = ability_cooldowns
        self.bot.filter_ability_cooldowns()
        self.bot.filter_ability_cooldowns()
        self.bot.filter_ability_cooldowns()
        self.bot.filter_ability_cooldowns()
        assert not self.bot.ability_cooldowns
