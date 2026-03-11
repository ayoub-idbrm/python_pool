from .Combatable import Combatable
from .Magical import Magical
from ex0 import Card


class EliteCard(Card, Combatable, Magical):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack_power: int,
            health: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.total_mana = 0

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["available_mana"]):
            return {
                "card_played": self.name,
                "success": False
            }
        game_state["available_mana"] -= self.cost
        return {
            "card_played": self.name,
            "used_mana": self.cost,
            "effect": "elite card effect"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        needed_mana = len(targets) * 2
        if needed_mana > self.total_mana:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": 0,
                "success": False
            }
        self.total_mana -= needed_mana
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": needed_mana,
            "success": True
        }

    def channel_mana(self, amount: int) -> dict:
        self.total_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.total_mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "total_mana": self.total_mana
        }
