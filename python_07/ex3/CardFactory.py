from abc import ABC, abstractmethod
from ex0 import Card


class CardFactory(ABC):

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        # Child decides: Dragon? Robot? Zombie?
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        # Child decides: Fireball? Laser? Curse?
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        # Child decides: Mana Ring? Shield? Sword?
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        # Child creates a complete deck with cards that fit together
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        # Child lists what types of cards it can create
        pass
