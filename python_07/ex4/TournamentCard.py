from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card with tournament capabilities combining Card, Combatable
    and Rankable."""

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int = 10,
        defense: int = 5,
        initial_rating: int = 1000,
    ):
        super().__init__(name, cost, rarity)
        self.id = card_id
        self.attack_power = attack_power
        self.defense = defense
        self.wins = 0
        self.losses = 0
        self.rating = initial_rating

    # Card abstract
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        if "played" not in game_state:
            game_state["played"] = []
        game_state["played"].append(self.get_card_info())
        return {
            "action": "played",
            "card": self.name,
            "game_state": game_state
        }

    # Combatable abstract
    def attack(self, target) -> Dict[str, Any]:
        if not hasattr(target, "defense"):
            raise TypeError("Target is not combatable")
        damage = self.attack_power - target.defense
        if damage < 1:
            damage = 1
        return {"attacker": self.id, "target": target.id, "damage": damage}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        net = incoming_damage - self.defense
        if net < 0:
            net = 0
        return {"defender": self.id, "incoming": incoming_damage, "net": net}

    def get_combat_stats(self) -> Dict[str, int]:
        return {"attack_power": self.attack_power, "defense": self.defense}

    # Rankable abstract
    def calculate_rating(self) -> int:
        return self.rating

    # this function modifies the wins by adding 1
    def update_wins(self, wins: int) -> None:
        self.wins += wins

    # this function modifies the losses by adding 1
    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    # get card tournament infos
    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
