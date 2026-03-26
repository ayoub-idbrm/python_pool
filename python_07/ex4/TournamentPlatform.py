from typing import Dict, List, Optional
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform management system for tournament cards."""

    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0
        self.platform_status = "active"

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.id] = card
        return card.id

    def create_match(
        self, card1_id: str, card2_id: str
    ) -> Dict[str, Optional[object]]:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)
        if card1 is None or card2 is None:
            raise ValueError("One or both cards not registered on platform")

        if card1.attack_power > card2.attack_power:
            winner, loser = card1, card2
        elif card2.attack_power > card1.attack_power:
            winner, loser = card2, card1
        else:
            if card1.rating >= card2.rating:
                winner, loser = card1, card2
            else:
                winner, loser = card2, card1

        delta = 16
        winner.rating = winner.rating + delta
        loser.rating = loser.rating - delta

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[Dict[str, object]]:
        sorted_cards = sorted(
            self.cards.values(), key=lambda c: c.rating, reverse=True
        )
        leaderboard = []
        for idx, c in enumerate(sorted_cards):
            leaderboard.append({
                "position": idx + 1,
                "name": c.name,
                "id": c.id,
                "rating": c.rating,
                "record": f"{c.wins}-{c.losses}"
            })
        return leaderboard

    def generate_tournament_report(self) -> Dict[str, object]:
        total = len(self.cards)
        if total > 0:
            sum_ratings = sum(c.rating for c in self.cards.values())
            avg_rating = int(sum_ratings / total)
        else:
            avg_rating = 0
        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": self.platform_status,
        }
