from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []

        if "Enemy Player" in available_targets:
            prioritized.append("Enemy Player")

        for target in available_targets:
            if target != "Enemy Player":
                prioritized.append(target)

        return prioritized

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        available_mana = 5  # Start with 5 mana points

        # always target the enemy player (aggressive!)
        targets = self.prioritize_targets(["Enemy Player"])

        # helper function to get card cost
        def get_cost(card):
            return card.cost

        # sort cards by cost: play cheapest first to maximize cards
        sorted_hand = sorted(hand, key=get_cost)

        # Play as many cards
        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost

                # Calculate damage (creatures have attack, spells deal 6)
                if hasattr(card, "attack"):
                    damage_dealt += card.attack
                else:
                    damage_dealt += 6  # Default spell damage

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt
        }
