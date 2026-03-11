from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__,  # Dynamic type name
        }

    # Before playing, we should always validate that cost <= available_mana
    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana

    def __repr__(self):
        return f"{self.name} ({self.cost})"
