from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hands = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy):
        # Dependency Injection: inject factory and strategy from outside
        # This makes the engine flexible: change factory or strategy anytime!
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        # Simulate one turn of gameplay
        self.turns_simulated += 1

        # Step 1: Factory creates cards
        deck = self.factory.create_themed_deck(3)
        self.hand = deck["cards"]
        self.cards_created = len(self.hand)

        # Step 2: Strategy plays the cards
        result = self.strategy.execute_turn(self.hand, [])

        # Step 3: Track total damage
        self.total_damage += result["damage_dealt"]
        return result

    def get_engine_status(self) -> dict:

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
