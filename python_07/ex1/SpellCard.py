from ex0.Card import Card
from enum import Enum


class EffectType(Enum):

    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:

        if not self.is_playable(game_state["available_mana"]):
            return {
                "card_played": self.name,
                "succes": False
            }
        game_state["available_mana"] -= self.cost

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Deal 3 damage to target"
        }

    def get_card_info(self):

        infos = super().get_card_info()

        infos["effect_type"] = self.effect_type

        return infos

    def resolve_effect(self, targets: list) -> dict:
        # in case the effect_type is damage
        if self.effect_type == EffectType.DAMAGE:
            for target in targets:
                target["hp"] -= 3
            return {"effect": "3 damage dealt"}
        # in this case the effect type is healing the target it add 3hp
        if self.effect_type == EffectType.HEAL:
            for target in targets:
                target["hp"] += 3
            return {"effect": "3 hp healed"}
        # in this case it gives the target +2 to his attack
        if self.effect == EffectType.BUFF:
            for target in targets:
                target["attack"] += 2
            return {"effect": "+2 attack buff applied"}
        # in this case of debuff it retrieve points from target attack
        if self.effect_type == EffectType.DEBUFF:
            for target in targets:
                target["attack"] -= 2
            return {"effect": "-2 attack buff applied"}

        return {"effect": "no effect"}

    def __str__(self):
        return f"{self.name} ({self.cost})"
