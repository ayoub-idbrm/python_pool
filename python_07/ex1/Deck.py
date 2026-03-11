from ex0.Card import Card
import random


class Deck:

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> Card:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        creatures = [
            1 for card in self.cards
            if card.__class__.__name__ == "CreatureCard"]
        spells = [
            1 for card in self.cards
            if card.__class__.__name__ == "SpellCard"]
        artifacts = [
            1 for card in self.cards
            if card.__class__.__name__ == "ArtifactCard"]
        return {
            "total_cards": len(self.cards),
            "creatures": len(creatures),
            "spells": len(spells),
            "artifacts": len(artifacts)
        }
