from enum import Enum
from dataclasses import dataclass, field


class AbilityType(Enum):
    BUFF = 'buff'
    FOOD = 'food'
    HEAL = 'heal'
    SKILL = 'skill'


@dataclass(frozen=True)
class Ability:
    name: str
    keybind: list[str]
    type: AbilityType
    icon: list[str, int] = field(default_factory=list)  # icon + threshold
    cooldown: int = 0
    duration: int = 0
    disabled: bool = False
