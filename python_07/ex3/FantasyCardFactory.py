from ex3.CardFactory import CardFactory
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        # Creates fantasy creatures based on the parameter type:
        if isinstance(name_or_power, str):
            # String = custom name creature
            return CreatureCard(name_or_power, 2, "rare", 5, 2)

        if isinstance(name_or_power, int):
            # Integer = Fire Dragon with custom power
            return CreatureCard(
                "Fire Dragon", 5, "legendary", name_or_power, 1)
        # None = default Goblin
        return CreatureCard("Goblin warrior", 2, "common", 2, 1)

    def create_spell(self, name_or_power=None) -> Card:
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, 3, "fire", 4)
        if isinstance(name_or_power, int):
            return SpellCard("lightning Bolt", 3, "lightning", name_or_power)
        return SpellCard("fireball", 3, "fire", 3)

    def create_artifact(self, name_or_power=None) -> Card:
        return ArtifactCard("Mana Ring", 1, "mana_boost")

    def create_themed_deck(self, size: int) -> dict:
        # Creates a fantasy themed deck with coordinated cards
        deck = []
        if size >= 1:
            deck.append(self.create_creature(5))  # Fire Dragon (power=5)
        if size >= 2:
            deck.append(self.create_creature("Goblin Warrior"))
        if size >= 3:
            deck.append(self.create_spell("Lightning Bolt"))
        return {
            "deck_size": len(deck),
            "cards": deck
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
