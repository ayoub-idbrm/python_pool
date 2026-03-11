from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state) -> dict:
        if not self.is_playable(game_state["available_mana"]):
            return {
                "name": self.name,
                "succes": False
            }
        game_state["available_mana"] -= self.cost
        game_state["hand"].remove(self)
        game_state["graveyard"].append(self)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def active_ability(self, game_state):
        if self.durability > 0:
            game_state["avaible_mana"] += 1
            self.durability -= 1
            if self.durability == 0:
                game_state["artifact"].remove(self)
                game_state["graveyard"].append(self)
                return {
                    "artifact": self.name,
                    "effect": self.effect,
                    "status": "destroyed"
                }
            return {
                "artifact": self.name,
                "effect": self.effect,
                "durability_left": self.durability
            }
        else:
            return {
                "artifact": self.name,
                "status": "already destroyed"
            }

    def __str__(self):
        return f"{self.name}"
