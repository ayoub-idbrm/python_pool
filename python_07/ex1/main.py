from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")

    deck = Deck()

    deck.add_card(SpellCard("Lightning Bolt", 3, "common", EffectType.DAMAGE))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal",
            2,
            "rare",
            durability=3,
            effect="Permanent: +1 mana per turn"))
    deck.add_card(CreatureCard("Fire Dragon", 5, "epic", attack=7, health=10))

    stats = deck.get_deck_stats()
    stats["avg_cost"] = round(
        sum(c.cost for c in deck.cards) / len(deck.cards), 1)
    print("Building deck with different card types...")
    print(f"Deck stats: {stats}")

    print("Drawing and playing cards:")

    game_state = {
        "available_mana": 10,
        "hand": deck.cards.copy(),
        "artifact": [],
        "graveyard": [],
        "battlefield": []
    }

    while deck.cards:
        card = deck.draw_card()
        card_type = card.__class__.__name__
        print(f"Drew: {card.name} ({card_type})")

        result = card.play(game_state)
        print(f"Play result: {result}")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
