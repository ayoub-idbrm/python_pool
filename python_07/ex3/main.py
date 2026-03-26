from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("Simulating aggressive turn...")

    result = engine.simulate_turn()

    print("Hand:", engine.hand)

    print("Turn execution:")
    print("Strategy:", result["strategy"])
    print("Actions:", {
        "cards_played": result["cards_played"],
        "mana_used": result["mana_used"],
        "targets_attacked": result["targets_attacked"],
        "damage_dealt": result["damage_dealt"]
    })

    print("Game Report:")
    print(engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
