"""Demonstration script for the ex4 tournament platform."""
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    # Create two example tournament cards
    fire = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=7,
        rarity="legendary",
        attack_power=18,
        defense=6,
        initial_rating=1200,
    )

    ice = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=5,
        rarity="epic",
        attack_power=14,
        defense=7,
        initial_rating=1150,
    )

    for c in (fire, ice):
        platform.register_card(c)
        print(f"{c.name} (ID: {c.id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {c.rating}")
        print(f"- Record: {c.wins}-{c.losses}")

    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)

    print("Tournament Leaderboard:")
    lb = platform.get_leaderboard()
    for entry in lb:
        pos = entry['position']
        name = entry['name']
        rating = entry['rating']
        record = entry['record']
        print(f"{pos}. {name} - Rating: {rating} ({record})")

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()
