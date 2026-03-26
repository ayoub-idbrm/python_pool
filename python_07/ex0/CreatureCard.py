from ex0.Card import Card


class CreatureCard(Card):
    """
    CreatureCard is a specific type of card.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ):
        super().__init__(name, cost, rarity)
        # we should always validate the health and attack
        if attack < 0 or health < 0:
            raise ValueError("Attack and health should be positive")

        self.attack = attack
        self.health = health

    # Implementation of the play() function
    def play(self, game_state: dict) -> dict:
        # Mana represents the points required to play the card.
        # We check it using the is_playable() function.
        if not self.is_playable(game_state["available_mana"]):
            # Not enough mana: return failure
            return {
                "card_played": self.name,
                "effect": False,
            }

        # The mutable variable game_state is decremented by the cost
        # of the played card.
        # NOTE: This modifies the game_state dict in-place (mutation)
        game_state["available_mana"] -= self.cost

        # The result of playing the card is a dictionary containing
        # the used mana (cost) and the effect of the card.
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    # attack_target function
    # in subject we didn't have the target type so we use it as string
    def attack_target(self, target) -> dict:
        # This card can attack a target player or creature.
        # Attack represents the damage dealt to the target.
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    # Override the get_card_info() method
    def get_card_info(self) -> dict:
        # Call the parent function to get the basic card info
        # (name, cost, rarity, type)
        infos = super().get_card_info()

        # Add attack and health values specific to CreatureCard
        infos["attack"] = self.attack
        infos["health"] = self.health
        return infos

    def __str__(self):
        return f"{self.name} ({self.attack})"
